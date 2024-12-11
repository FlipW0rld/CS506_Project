
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

## Run steps
- git clone https://github.com/FlipW0rld/CS506_Project.git
- cd CS506_Project
- make install
- make notebook
- jupyter notebook
- Then run each cell in test_3models.ipynb and test_diff_dataset.ipynb

## Project Overview

The Boston 57 bus passes through multiple stops at Boston University and serves as o
ne of the transportation options for Boston University students. This project aims to predict the arrival time of bus route 57 at designated stations based on factors such as weather conditions, weekday patterns, and passenger numbers.

## Methodology (方法)

### Data Decirption and Collection:

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

### Data Processing (数据处理、清理，数据预处理等):


### Feature Engineering (特征工程):
In this project, a series of feature engineering steps were implemented to enhance the model's performance and capture underlying patterns in the data. Below is a detailed explanation of these steps:

#### Data Preprocessing
After loading the raw data, several preprocessing steps were applied:

#####  Date and Time Formatting:
The Date column was converted into a standard datetime format.
The Arrival Time column was converted into time format, and new features were derived to represent ground truth time.
##### Derived Time Features:
arrival_minutes_after_noon: This feature calculates the number of minutes between the arrival time and noon (12:00). It is derived directly from the Arrival Time column without explicitly creating arrival_hour or arrival_minute.
##### Weekday Mapping:
The Week Day column was mapped to numeric values (e.g., Monday = 0, Sunday = 6) to facilitate machine learning tasks.
##### Weather Encoding:
The Weather column was transformed using one-hot encoding, generating binary indicator variables for different weather conditions. This avoids bias associated with categorical variables.
Adding Simple Features

To capture additional temporal patterns, the following features were introduced:

##### Peak Hour Indicator (IsPeakHour):
A binary feature that identifies whether the arrival time falls within peak hours: 7:00–9:00 (morning peak) or 17:00–19:00 (evening peak).
##### Time Period Classification (TimePeriod):
The day was divided into four periods:
Early Morning: 0:00–6:00
Morning: 7:00–11:00
Afternoon: 12:00–17:00
Evening: 18:00–23:59
This feature helps capture time-of-day trends and variations in data patterns.
#### Adding Weather Features
To incorporate the influence of weather conditions on the data, hourly weather data was fetched from the Open-Meteo API. The following steps were performed:

##### API Integration:
For each unique date in the dataset, hourly weather data was fetched using latitude and longitude parameters.
The weather data includes key variables: temperature, precipitation, wind speed, humidity, and cloud cover.
##### Feature Generation:
The hourly weather data was processed to extract relevant metrics for each hour, including:
temperature_2m: Temperature at 2 meters above ground.
apparent_temperature: Feels-like temperature.
precipitation: Precipitation rate.
wind_speed_10m: Wind speed at 10 meters above ground.
relative_humidity_2m: Relative humidity at 2 meters.
cloud_cover: Cloud coverage as a percentage.
##### Data Merging:
The weather data was merged with the original dataset based on the Date and Arrival Time. Temporary columns used during the merging process, such as intermediate timestamps, were removed to keep the dataset clean.
Feature Engineering Outcomes
The final enriched dataset includes a comprehensive set of features that capture temporal, weather-related, and peak-hour effects. This enhanced dataset provides the model with diverse dimensions of information, enabling more robust predictions.

### Model Training (模型构建和训练):


_________________________`````

### Evaluation and Visualization (评价和可视化，可视化，解释和主张):

### 为达到目标而采取的方法的有效性 









## 中期报告以来的进展情况



## Result and Conclusion(总体结果和结论（+支持这些结论的证据）)

