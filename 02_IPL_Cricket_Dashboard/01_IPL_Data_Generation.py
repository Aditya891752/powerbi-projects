"""IPL CRICKET PERFORMANCE DASHBOARD - Data Prep
Kaggle IPL Dataset - Senior Engineer Setup"""

import pandas as pd
import numpy as np

# IPL MATCHES DATA
matches_data = {
    'Match_ID': list(range(1, 235)),
    'Season': [2008]*14 + [2009]*14 + [2010]*14 + [2011]*14 + [2012]*16 + [2013]*16 + [2014]*16 + [2015]*16 + [2016]*16,
    'Date': pd.date_range('2008-04-18', periods=234, freq='3D'),
    'Venue': np.random.choice(['MCG', 'Eden Gardens', 'Wankhede', 'Arun Jaitley Stadium', 'MA Chidambaram', 'Feroz Shah Kotla', 'M. A. Chidambaram Stadium', 'DY Patil Stadium'], 234),
    'Home_Team': np.random.choice(['MI', 'CSK', 'RCB', 'KKR', 'DC', 'KXIP', 'RR', 'SRH'], 234),
    'Away_Team': np.random.choice(['MI', 'CSK', 'RCB', 'KKR', 'DC', 'KXIP', 'RR', 'SRH'], 234),
    'Winner': np.random.choice(['MI', 'CSK', 'RCB', 'KKR', 'DC', 'KXIP', 'RR', 'SRH'], 234),
    'Winning_Margin': np.random.randint(1, 100, 234),
    'Toss_Winner': np.random.choice(['MI', 'CSK', 'RCB', 'KKR', 'DC', 'KXIP', 'RR', 'SRH'], 234),
    'Toss_Decision': np.random.choice(['bat', 'field'], 234),
    'Man_of_Match': [f'Player_{i}' for i in range(1, 235)]
}

matches_df = pd.DataFrame(matches_data)
matches_df.to_csv('ipl_matches.csv', index=False)

# IPL DELIVERIES DATA (Ball-by-ball)
deliveries_data = {
    'Match_ID': np.repeat(range(1, 235), 120),
    'Inning': np.tile(np.repeat([1, 2], 60), 234),
    'Over': np.tile(np.repeat(range(1, 21), 6), 234),
    'Ball': np.tile(np.tile(range(1, 7), 20), 234),
    'Batsman': np.random.choice([f'Batsman_{i}' for i in range(1, 150)], 234*120),
    'Non_Striker': np.random.choice([f'Batsman_{i}' for i in range(1, 150)], 234*120),
    'Bowler': np.random.choice([f'Bowler_{i}' for i in range(1, 100)], 234*120),
    'Runs_Off_Bat': np.random.choice([0, 1, 2, 3, 4, 6], 234*120, p=[0.45, 0.35, 0.12, 0.04, 0.03, 0.01]),
    'Extras': np.random.choice([0, 1, 2, 3], 234*120, p=[0.92, 0.05, 0.02, 0.01]),
    'Wicket': np.random.choice([0, 1], 234*120, p=[0.97, 0.03]),
    'Wicket_Type': np.random.choice(['bowled', 'caught', 'lbw', 'run out', 'None'], 234*120, p=[0.25, 0.35, 0.2, 0.15, 0.05]),
}

deliveries_df = pd.DataFrame(deliveries_data)
deliveries_df['Total_Runs'] = deliveries_df['Runs_Off_Bat'] + deliveries_df['Extras']
deliveries_df.to_csv('ipl_deliveries.csv', index=False)

# PLAYER STATISTICS
player_stats_data = {
    'Player_Name': [f'Player_{i}' for i in range(1, 500)],
    'Team': np.repeat(['MI', 'CSK', 'RCB', 'KKR', 'DC', 'KXIP', 'RR', 'SRH'], 62) + [np.random.choice(['MI', 'CSK', 'RCB', 'KKR', 'DC', 'KXIP', 'RR', 'SRH'])]*4,
    'Role': np.random.choice(['Batsman', 'Bowler', 'All-rounder'], 500, p=[0.4, 0.35, 0.25]),
    'Matches': np.random.randint(5, 180, 500),
    'Runs': np.random.randint(50, 3000, 500),
    'Wickets': np.random.randint(0, 150, 500),
    'Avg_Runs_Per_Match': np.random.randint(10, 60, 500),
    'Strike_Rate': np.random.uniform(100, 160, 500),
    'Economy_Rate': np.random.uniform(6, 12, 500),
    'Centuries': np.random.randint(0, 8, 500),
    'Fifties': np.random.randint(0, 20, 500),
    'Best_Bowling': np.random.choice(['4/20', '3/25', '2/15', '5/30', '2/20'], 500),
}

player_stats_df = pd.DataFrame(player_stats_data)
player_stats_df.to_csv('ipl_player_stats.csv', index=False)

print("\u2705 IPL Datasets Generated Successfully!")
print(f"Matches: {len(matches_df)} records")
print(f"Deliveries: {len(deliveries_df)} records")
print(f"Player Stats: {len(player_stats_df)} records")