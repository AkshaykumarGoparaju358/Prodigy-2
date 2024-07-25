import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = '/content/RTA Dataset.csv'
data = pd.read_csv(file_path)

print(data.head())

data['Time'] = pd.to_datetime(data['Time'], format='%H:%M:%S').dt.time

data['Hour'] = data['Time'].apply(lambda x: x.hour)

plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='Cause_of_accident', order=data['Cause_of_accident'].value_counts().index)
plt.title('Accident Distribution by Cause of Accident')
plt.xlabel('Cause of Accident')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()

if 'Weather' in data.columns:
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x='Weather', order=data['Weather'].value_counts().index)
    plt.title('Accident Distribution by Weather Condition')
    plt.xlabel('Weather')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()
else:
    print("Weather column is missing from the dataset.")

plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='Hour', order=range(24))
plt.title('Accident Distribution by Time of Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='Day_of_week', order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.title('Accident Distribution by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='Accident_severity', order=data['Accident_severity'].value_counts().index)
plt.title('Accident Distribution by Severity')
plt.xlabel('Accident Severity')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='Driving_experience', order=data['Driving_experience'].value_counts().index)
plt.title('Accident Distribution by Driving Experience')
plt.xlabel('Driving Experience')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

if 'Latitude' in data.columns and 'Longitude' in data.columns:
    import geopandas as gpd
    from shapely.geometry import Point
    gdf = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data.Longitude, data.Latitude))

    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    fig, ax = plt.subplots(figsize=(15, 10))
    world.boundary.plot(ax=ax)
    gdf.plot(ax=ax, markersize=1, color='red', alpha=0.5)
    plt.title('Accident Hotspots')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.show()
else:
    print("Latitude and Longitude columns are missing from the dataset. Hotspot visualization cannot be performed.")
