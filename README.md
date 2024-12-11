
# Boston Bus Route 57 Designated Station Arrival Prediction
# Midterm Presentation Link
https://www.bilibili.com/video/BV1kJDMYfEeC/?vd_source=39b2f6be2c7ee5a7ce77b461cba09892

## Team Members

- Jiangjian Xie ([xjj2023@bu.edu](mailto:xjj2023@bu.edu))
- Zhekai Zhu ([zzk@bu.edu](mailto:zzk@bu.edu))
- Wenyuan Cui ([wycui@bu.edu](mailto:wycui@bu.edu))
- Mohan Guo ([gmh926@bu.edu](mailto:gmh926@bu.edu))

## Introduction
Public transportation is a vital aspect of urban life, providing a reliable and cost-effective means of mobility for residents and students alike. Among the many bus routes in Boston, Route 57 serves as a key transit option for Boston University students, connecting them to various stops across the city. However, the uncertainty of bus arrival times, influenced by factors such as weather conditions, traffic, and passenger load, often creates inconvenience for passengers.

This project seeks to address this issue by developing a predictive model for the arrival times of Route 57 buses at designated stations. By leveraging real-world data, including weather conditions, weekday patterns, and bus schedules, we aim to enhance the commuting experience for Boston University students. The insights from this project can potentially contribute to more efficient route planning and better time management for daily commuters.


## Project Overview

The Boston 57 bus passes through multiple stops at Boston University and serves as o
ne of the transportation options for Boston University students. This project aims to predict the arrival time of bus route 57 at designated stations based on factors such as weather conditions, weekday patterns, and passenger numbers.

## Run steps
- git clone https://github.com/FlipW0rld/CS506_Project.git
- cd CS506_Project
- make install
- make notebook
- jupyter notebook
- Then run each cell in test_3models.ipynb and test_diff_dataset.ipynb

## Methodology (方法)

### Data description and Collection:

Data was collected from October 7th to November 31st. The collected data includes:

- Date
- Weekday
- Bus arrival time
- Weather conditions (e.g., sunny, rainy, snowy)
  - Temperature at 2 meters
  - sensible temperature
  - Precipitation
  - Humidity
  - Wind speed
  - Cloud cover

Team members took turns recording bus arrival times either through on-site observation or using bus query applications such as Google Maps and MBTA Website.

### Data Processing 
#### test_3models
- Contains functions such as load_data and get_features_and_target for data processing.
load_data reads the dataset, drops unnecessary columns (Date, Week Day, Arrival Time), and handles missing values using forward and backward fill.
get_features_and_target separates the dataset into features (X) and the target variable (y), specifically targeting arrival_minutes_after_noon.
- Preprocessing includes data standardization through pipelines, which is essential for models like gradient-boosting frameworks.

#### test_diff_dataset
- Includes preprocess_old_data and preprocess_new_data for handling datasets with potentially different schemas:
- Converts time-based features (Arrival Time) into a numerical format (arrival_minutes_after_noon).
- Encodes categorical features like Weather into numerical codes.
- Uses forward and backward fill to handle missing values.
- Includes error handling to ensure critical columns (Arrival Time, Weather) exist in the dataset.


### Feature Engineering:
In this project, a series of feature engineering steps were implemented to enhance the model's performance and capture underlying patterns in the data. Below is a detailed explanation of these steps:

#### Data Preprocessing
After loading the raw data, several preprocessing steps were applied to ensure the dataset was ready for further analysis. The Date column was converted into a standard datetime format, and the Arrival Time column was converted into time format. The Week Day column was mapped to numeric values (e.g., Monday = 0, Sunday = 6), enabling easier handling by machine learning models. Additionally, the Weather column was transformed using one-hot encoding to generate binary indicator variables for different weather conditions, ensuring categorical variables did not introduce biases.

#### Adding Simple Features
To further enrich the dataset, features representing temporal patterns were added. A binary feature, IsPeakHour, was introduced to identify whether the arrival time fell within typical peak hours (7:00–9:00 in the morning and 17:00–19:00 in the evening). Another feature, TimePeriod, categorized the day into four distinct periods: Early Morning (0:00–6:00), Morning (7:00–11:00), Afternoon (12:00–17:00), and Evening (18:00–23:59). These features capture the behavioral differences in data associated with different times of the day.

#### Adding Weather Features
To incorporate weather effects, hourly weather data was fetched using the Open-Meteo API. For each unique date in the dataset, weather data was retrieved based on the latitude and longitude of the location. This data included key weather metrics such as temperature (temperature_2m), apparent temperature (apparent_temperature), precipitation rate (precipitation), wind speed (wind_speed_10m), relative humidity (relative_humidity_2m), and cloud cover (cloud_cover). The hourly data was aligned with the dataset based on the Date and Arrival Time to ensure temporal consistency. Temporary columns created during the merging process were removed, leaving a clean, enriched dataset.

#### Feature Engineering Outcomes
The final dataset, saved as a csv file, contains a robust set of features encompassing time, weather, and peak-hour patterns. These engineered features provide diverse and relevant information, enabling the model to make more accurate and insightful predictions.

### Model Training
#### test_3models
- Focuses on training multiple models, including:
Random Forest Regressor
LightGBM Regressor
XGBoost Regressor
- Employs techniques like:
Hyperparameter tuning using GridSearchCV for optimized model performance.
TimeSeriesSplit for validation, ensuring that time-order dependencies are maintained.
- Evaluation uses Mean Absolute Error (MAE) to assess model performance.

#### test_diff_dataset
- Includes preprocess_old_data and preprocess_new_data for handling datasets with potentially different schemas:
- Converts time-based features (Arrival Time) into a numerical format (arrival_minutes_after_noon).
- Encodes categorical features like Weather into numerical codes.
- Uses forward and backward fill to handle missing values.
- Includes error handling to ensure critical columns (Arrival Time, Weather) exist in the dataset.


_________________________`````

### Evaluation and Visualization:
To assess the performance of the models and the impact of feature engineering, we compared the Mean Absolute Error (MAE) across different models trained with both the original dataset and the enriched dataset, which included weather-related features. The results are summarized below:

#### Model Comparison
Random Forest achieved an MAE of 13.40 with key hyperparameters such as n_estimators=300, min_samples_leaf=5, and random_state=42.
LightGBM reported an MAE of 13.65, with parameters including learning_rate=0.01, n_estimators=300, and default tree structure settings (num_leaves=31).
XGBoost demonstrated the best performance, achieving an MAE of 13.25, using a depth-limited configuration (max_depth=3), learning_rate=0.05, and n_estimators=100.
These results highlight that the XGBoost model slightly outperformed the others in terms of error minimization.
![image](https://github.com/user-attachments/assets/51b38637-fb67-4c3f-905d-868bbc651a1e)


#### impact of Feature Engineering
To evaluate the effect of introducing weather-related features, we compared the MAE of models trained on the original dataset (without weather features) and the enriched dataset (with weather features). As shown in the chart, the MAE decreased from 13.40 to 12.70, indicating that the additional features significantly improved model accuracy. This reduction demonstrates the importance of integrating external contextual data, such as weather conditions, in capturing real-world patterns and variability.
![image](https://github.com/user-attachments/assets/85a214d6-3be9-43d2-bf68-c91bfc4602e7)


### 为达到目标而采取的方法的有效性 









## 中期报告以来的进展情况



## Result and Conclusion(总体结果和结论（+支持这些结论的证据）)
Conclusion The predictive models developed in this project demonstrate the potential to accurately forecast the arrival times of Route 57 buses at designated stations. Among the tested algorithms, the LightGBM Regressor showed the best overall performance, making it a suitable choice for real-world deployment. The integration of weather and temporal data played a pivotal role in improving prediction accuracy, emphasizing the importance of feature engineering in machine learning projects.

These findings validate the feasibility of utilizing machine learning techniques for enhancing public transportation efficiency. With further refinement, such as integrating real-time traffic data and expanding the dataset, this model can serve as a reliable tool for improving the commuting experience of Boston University students and the broader community. This project underscores the transformative potential of data-driven solutions in addressing urban transportation challenges.

