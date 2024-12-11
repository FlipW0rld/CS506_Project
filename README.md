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

The Boston 57 bus passes through multiple stops at Boston University and serves as one of the transportation options for Boston University students. This project aims to predict the arrival time of bus route 57 at designated stations based on factors such as weather conditions, weekday patterns, and passenger numbers.

## Methodology

### Data Collection

Data was collected from October 7th to October 31st. The collected data includes:

- Date
- Weekday
- Weather conditions (e.g., sunny, rainy, snowy)
- Precipitation
- Humidity
- Wind speed
- Cloud cover
- Bus arrival time

Team members took turns recording bus arrival times either through on-site observation or using bus query applications such as Google Maps.

### Preliminary Data Processing

#### Data Cleaning

- We ensured proper data types for each column:
  - "Date" was converted to datetime format for easier manipulation.
  - "Arrival Time" was processed to ensure accurate extraction of hour and minute values.
- For any missing values, we used linear interpolation to ensure the dataset remained complete.

#### Outlier Detection
- Identified and removed anomalous data points, such as arrival times outside normal operating hours, to enhance model reliability.

### Feature Engineering

#### Time Transformation
- Converted "Arrival Time" into "Arrival Time (Minutes)", representing the total minutes since midnight. This facilitates numerical analysis and simplifies model input.
#### Weather Encoding
- Categorical weather conditions (e.g., sunny, rainy, snowy) were transformed into numerical values for compatibility with machine learning models.
#### Derived Features
- Created new features such as "Day of the Week" and "Is Weekday" to capture potential weekday-specific patterns in bus arrival times.

### Exploratory Data Analysis (EDA)
#### Visualizations
- Created bar charts to examine the distribution of bus arrivals across different weekdays.
- Generated histograms to understand the overall distribution of arrival times during the day and identify peak hours.
#### Insights
- Observed clear weekday patterns and clustering of arrival times during specific hours, indicating predictable bus frequency during peak periods.

### Model Development
#### Linear Regression
- Goal: Establish a baseline for predicting bus arrival times.
- Features Used: Weekday, weather conditions, and other derived variables.
- Evaluation Metrics:
Coefficient of Determination (R²): 0.45
Mean Absolute Error (MAE): 5.2 minutes
- Preliminary Findings: Demonstrated moderate correlation, with room for improvement in capturing non-linear relationships.
- 
#### Decision Trees and Random Forests (In Progress)
- Objective: Improve predictive accuracy by capturing complex, non-linear relationships among features.
- Hyperparameter Tuning:
Experimented with parameters such as maximum tree depth and the number of trees to enhance performance.
- Expected Outcomes: Improved generalization and better handling of feature interactions, especially for weather and weekday influences.

### Model Evaluation
- Metrics:
Mean Absolute Error (MAE)
Root Mean Squared Error (RMSE)
R² Score
- Cross-Validation: Used cross-validation techniques to evaluate model robustness and prevent overfitting.





## Experiments and Results
### LightGBM
#### Daily arrival time distribution line chart

![9b6b1b8a22d6d64eed08db95caa25e7](https://github.com/user-attachments/assets/c1c8a4a5-2b3f-47a1-94e1-a9ba9cd9c641)




#### Boxplot of weather effects on arrival time

![8b70a7976faad9dfc72da609872c3c1](https://github.com/user-attachments/assets/86380964-22e7-46ad-bca3-51dce256fe1a)




#### Weekday vs. weekend bar chart
![510129b2ec307c3fb838122d3b72b5f](https://github.com/user-attachments/assets/97509fa3-5885-4707-b057-a1ab0b2f6b13)

### XGBoost
#### Daily arrival time distribution line chart
![7679502cbf04ad9d572c52038b7d5eb](https://github.com/user-attachments/assets/4621b0bd-f6d4-4280-9e27-40241dca1ef3)


#### Boxplot of weather effects on arrival time
![327e0923abd9cb55d82d3d265ec48cd](https://github.com/user-attachments/assets/c412785e-8215-4705-aabe-1993e1ca3d9d)


#### Weekday vs. weekend bar chart
![671e729608fa836adf6b368f2d7c5e7](https://github.com/user-attachments/assets/b6677aa0-45da-47b8-af77-485ceb67ba06)







### Current Data Modeling Methods

### Linear Regression

We implemented a linear regression model as an initial approach to predict bus arrival times based on features like weekday and weather conditions. We used data from October for training, and the model's performance showed moderate correlation upon initial evaluation. Linear regression established a baseline for model performance.

- **Model Evaluation Metrics**: The initial model had an R² value of 0.45 and a Mean Absolute Error (MAE) of 5.2 minutes, indicating a moderate predictive capability for the relationship between weekday, weather, and arrival time.

### Decision Trees and Random Forests (Upcoming)

We plan to implement decision tree-based models, such as Random Forests, to account for complex, non-linear relationships between features. These models will better capture the influence of factors such as traffic, weather, and weekday type on bus arrival times.

- **Hyperparameter Tuning**: We will use cross-validation to tune hyperparameters, such as tree depth and the number of trees, to improve model generalization.

### Results

- We successfully processed the dataset to create a clean version suitable for modeling.
- Initial visualizations indicate distinct weekday patterns in bus arrival frequency and a notable clustering of arrival times during peak hours.
- The linear regression model is currently being trained, and preliminary results show promising trends, suggesting a moderate correlation between weekday and arrival time.

## Conclusion

