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
git clone https://github.com/FlipW0rld/CS506_Project.git
cd CS506_Project
make install
make notebook
jupyter notebook
Then run each cell in test_3models.ipynb and test_diff_dataset.ipynb

## Project Overview

The Boston 57 bus passes through multiple stops at Boston University and serves as one of the transportation options for Boston University students. This project aims to predict the arrival time of bus route 57 at designated stations based on factors such as weather conditions, weekday patterns, and passenger numbers.

## Methodology (方法)

### Data Collection:

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

### Data Processing:

数据采集、处理、清理等







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





### Model Evaluation
- Metrics:
Mean Absolute Error (MAE)
Root Mean Squared Error (RMSE)
R² Score
- Cross-Validation: Used cross-validation techniques to evaluate model robustness and prevent overfitting.





## Experiments and Results
可视化、解释和权利要求






### Current Data Modeling Methods



### 中期报告以来的进展情况



## Result and Conclusion

