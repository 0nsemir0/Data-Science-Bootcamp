import pandas as pd
import matplotlib.pyplot as plt
import ssl
import seaborn as sns
#1

# Disable SSL verification
ssl._create_default_https_context = ssl._create_unverified_context
# Read the dataset
url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)

df['hour_beginning'] = pd.to_datetime(df['hour_beginning'], format='%m/%d/%Y %I:%M:%S %p')
df['DAY_OF_WEEK'] = df['hour_beginning'].dt.dayofweek

weekdays = df[df['DAY_OF_WEEK'] < 5]

daily_counts = weekdays.groupby('DAY_OF_WEEK')['Pedestrians'].sum()

plt.figure(figsize=(10, 5))
daily_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
daily_counts.plot(kind='line', marker='o')
plt.title('Pedestrian Counts by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Total Pedestrian Count')
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#done with 1.


#2 
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'], format='%m/%d/%Y %I:%M:%S %p')
df = df[(df['hour_beginning'].dt.year == 2019) & (df['location'] == 'Brooklyn Bridge')]

weather_encoded = pd.get_dummies(df['weather_summary'])

analysis_data = pd.concat([df['Pedestrians'], weather_encoded], axis=1)

correlation_matrix = analysis_data.corr()


plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', square=True)
plt.title('Correlation Matrix between Pedestrian Counts and Weather Conditions (2019)')
plt.show()

#3 
def categorize_time_of_day(hour):
    if hour < 6:
        return 'Night'
    elif hour < 12:
        return 'Morning'
    elif hour < 18:
        return 'Afternoon'
    else:
        return 'Evening'

df['time_of_day'] = df['hour_beginning'].dt.hour.apply(categorize_time_of_day)

activity_counts = df.groupby('time_of_day')['Pedestrians'].sum().reset_index()

plt.figure(figsize=(10, 5))
sns.barplot(data=activity_counts, x='time_of_day', y='Pedestrians', palette='viridis')
plt.title('Total Pedestrian Counts by Time of Day')
plt.xlabel('Time of Day')
plt.ylabel('Total Pedestrian Count')
plt.grid()
plt.show()