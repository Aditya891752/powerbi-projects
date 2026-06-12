"""PERSONAL HABIT & PRODUCTIVITY DASHBOARD - 6 Month Dataset
Senior Engineer Setup - Production Ready"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)
random.seed(42)

# Generate 6-month daily dataset (Jan 1 - Jun 30, 2024)
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 6, 30)
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

data = {
    'Date': [], 'Day_of_Week': [], 'Week_Number': [], 'Month': [],
    'Sleep_Hours': [], 'Sleep_Quality': [], 'Study_Hours': [], 'Study_Focus_Score': [],
    'Gym_Duration_Minutes': [], 'Gym_Intensity': [], 'Water_Intake_Liters': [],
    'Screen_Time_Hours': [], 'Mood_Score': [], 'Productivity_Score': [],
    'Calories_Burned': [], 'Steps': []
}

for date in date_range:
    day_of_week = date.strftime('%A')
    week_number = date.isocalendar()[1]
    month = date.strftime('%B')
    
    # Sleep: Higher on weekends, trend improvement
    base_sleep = 6.5 + (0.5 * (date - start_date).days / 181)
    if day_of_week in ['Saturday', 'Sunday']:
        sleep_hours = np.clip(np.random.normal(base_sleep + 1.5, 0.6), 4, 10)
    else:
        sleep_hours = np.clip(np.random.normal(base_sleep, 0.7), 4, 9)
    sleep_quality = int(np.clip(np.random.normal(sleep_hours * 1.3, 1.2), 2, 10))
    
    # Study: Lower weekends, higher mid-week
    if day_of_week in ['Saturday', 'Sunday']:
        study_hours = np.clip(np.random.normal(2, 1), 0, 6)
    else:
        study_hours = np.clip(np.random.normal(4.5, 1.2), 0, 9)
    study_focus = int(np.clip(np.random.normal(6 + (study_hours * 0.5), 1.5), 1, 10))
    
    # Gym: Less weekends, varies
    if day_of_week in ['Saturday', 'Sunday']:
        gym_duration = np.random.choice([0, 30, 45, 60, 75], p=[0.4, 0.2, 0.2, 0.15, 0.05])
    else:
        gym_duration = np.random.choice([0, 45, 60, 75, 90], p=[0.25, 0.3, 0.25, 0.15, 0.05])
    
    if gym_duration == 0:
        gym_intensity = 'Rest'
    elif gym_duration < 45:
        gym_intensity = 'Light'
    elif gym_duration < 75:
        gym_intensity = 'Medium'
    else:
        gym_intensity = 'High'
    
    # Water & Screen
    water_intake = np.clip(np.random.normal(2.5, 0.6), 1, 4)
    if day_of_week in ['Saturday', 'Sunday']:
        screen_time = np.clip(np.random.normal(7, 1.5), 3, 12)
    else:
        screen_time = np.clip(np.random.normal(5, 1.2), 2, 10)
    
    # Scores
    mood_score = int(np.clip((sleep_quality * 0.3 + (10 - screen_time) * 0.3 + (gym_intensity != 'Rest') * 4 + np.random.normal(0, 1)) / 1.0, 1, 10))
    productivity_score = int(np.clip((study_focus * 0.4 + sleep_quality * 0.3 + mood_score * 0.3) / 1.0, 1, 10))
    calories_burned = 300 + (gym_duration * 3) + np.random.normal(0, 100)
    steps = int(6000 + (gym_duration * 2) + (10 - screen_time) * 1000 + np.random.normal(0, 2000))
    
    data['Date'].append(date)
    data['Day_of_Week'].append(day_of_week)
    data['Week_Number'].append(week_number)
    data['Month'].append(month)
    data['Sleep_Hours'].append(round(sleep_hours, 2))
    data['Sleep_Quality'].append(sleep_quality)
    data['Study_Hours'].append(round(study_hours, 2))
    data['Study_Focus_Score'].append(study_focus)
    data['Gym_Duration_Minutes'].append(int(gym_duration))
    data['Gym_Intensity'].append(gym_intensity)
    data['Water_Intake_Liters'].append(round(water_intake, 2))
    data['Screen_Time_Hours'].append(round(screen_time, 2))
    data['Mood_Score'].append(mood_score)
    data['Productivity_Score'].append(productivity_score)
    data['Calories_Burned'].append(int(calories_burned))
    data['Steps'].append(steps)

df = pd.DataFrame(data)
df.to_csv('personal_habit_tracking_6months.csv', index=False)
print(f"✅ Dataset Generated: {len(df)} records | {df['Date'].min().date()} to {df['Date'].max().date()}")