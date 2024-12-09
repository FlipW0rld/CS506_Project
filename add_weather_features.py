import pandas as pd
import requests

def load_and_preprocess_data(file_path):
    """
    Load and preprocess the input data.
    :param file_path: Path to the CSV file.
    :return: Preprocessed DataFrame.
    """
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d')
    df['Arrival Time'] = pd.to_datetime(df['Arrival Time'], format='%H:%M').dt.time
    df['arrival_hour'] = df['Arrival Time'].apply(lambda x: x.hour)
    df['arrival_minute'] = df['Arrival Time'].apply(lambda x: x.minute)
    df['arrival_minutes_after_noon'] = df['arrival_hour'] * 60 + df['arrival_minute'] - (12 * 60)
    weekday_map = {
        'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3,
        'Friday': 4, 'Saturday': 5, 'Sunday': 6
    }
    df['day_of_week'] = df['Week Day'].map(weekday_map)
    df = pd.get_dummies(df, columns=['Weather'], drop_first=True)
    return df

def add_simple_features(df):
    """
    Add simple features such as peak hour and time period.
    :param df: Input DataFrame.
    :return: DataFrame with added features.
    """
    # Mark peak hours
    df['IsPeakHour'] = df['arrival_hour'].apply(lambda x: 1 if 7 <= x <= 9 or 17 <= x <= 19 else 0)

    # Define time periods of the day
    def time_period(hour):
        if 0 <= hour <= 6:
            return 'Early Morning'
        elif 7 <= hour <= 11:
            return 'Morning'
        elif 12 <= hour <= 17:
            return 'Afternoon'
        else:
            return 'Evening'

    df['TimePeriod'] = df['arrival_hour'].apply(time_period)
    return df

def fetch_weather_data(date, latitude=42.3601, longitude=-71.0589):
    """
    Fetch hourly weather data from Open-Meteo API for a specific date.
    :param date: Date string (YYYY-MM-DD).
    :param latitude: Latitude of the location.
    :param longitude: Longitude of the location.
    :return: Dictionary containing hourly weather data.
    """
    api_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": date,
        "end_date": date,
        "hourly": (
            "temperature_2m,apparent_temperature,precipitation,"
            "wind_speed_10m,relative_humidity_2m,cloud_cover"
        ),
        "timezone": "auto"
    }
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        return response.json().get("hourly", {})
    else:
        print(f"API request failed (status code: {response.status_code})")
        return {}

def add_weather_features(df, latitude=42.3601, longitude=-71.0589):
    """
    Add weather features to the DataFrame.
    :param df: Input DataFrame.
    :param latitude: Latitude of the location.
    :param longitude: Longitude of the location.
    :return: DataFrame with added weather features.
    """
    weather_data_list = []

    # Loop through each unique date and fetch weather data
    for date in df['Date'].dt.strftime('%Y-%m-%d').unique():
        hourly_weather = fetch_weather_data(date, latitude, longitude)
        if hourly_weather:
            for i, hour in enumerate(hourly_weather['time']):
                weather_data_list.append({
                    "date": date,
                    "hour": int(hour.split("T")[1][:2]),  # Extract hour
                    "temperature_2m": hourly_weather['temperature_2m'][i],
                    "apparent_temperature": hourly_weather['apparent_temperature'][i],
                    "precipitation": hourly_weather['precipitation'][i],
                    "wind_speed_10m": hourly_weather['wind_speed_10m'][i],
                    "relative_humidity_2m": hourly_weather['relative_humidity_2m'][i],
                    "cloud_cover": hourly_weather['cloud_cover'][i]
                })

    # Convert to DataFrame
    weather_df = pd.DataFrame(weather_data_list)

    # Convert date column to datetime type
    weather_df['date'] = pd.to_datetime(weather_df['date'])

    # Merge weather data with the original DataFrame
    df = pd.merge(df, weather_df, left_on=['Date', 'arrival_hour'], right_on=['date', 'hour'], how='left')
    df.drop(columns=['date', 'hour'], inplace=True)  # Drop temporary columns
    return df

def enrich_data_with_features(file_path):
    """
    Enrich data by adding simple and weather-related features.
    :param file_path: Path to the input CSV file.
    """
    df = load_and_preprocess_data(file_path)
    df = add_simple_features(df)
    df = add_weather_features(df)
    df.to_csv('enriched_bus_schedule.csv', index=False)
    print("Data processing completed. Saved as 'enriched_bus_schedule.csv'.")

if __name__ == "__main__":
    # Load and preprocess data
    file_path = 'bus_arrival_schedule.csv'
    print("Loading and preprocessing data...")
    df = load_and_preprocess_data(file_path)

    # Add weather features
    print("Adding weather features...")
    try:
        df = add_weather_features(df)
    except Exception as e:
        print(f"Failed to add weather features: {e}")

    # Save final data
    output_file = 'bus_arrival_schedule_with_weather.csv'
    df.to_csv(output_file, index=False)
    print(f"Data processing completed. Saved as '{output_file}'.")
