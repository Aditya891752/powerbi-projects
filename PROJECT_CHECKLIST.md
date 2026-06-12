# 📋 Project Checklist - Track Your Progress

## Project 1: Personal Habit & Productivity Dashboard

### Phase 1: Data Preparation
- [ ] Run Python script (`01_Data_Generation.py`)
- [ ] Verify CSV was created
- [ ] Open CSV in Excel to check data quality
- [ ] Look for 181 rows (6 months)
- [ ] Confirm all columns present

### Phase 2: Power BI Setup
- [ ] Create new Power BI file
- [ ] Import CSV data
- [ ] Change data types:
  - [ ] Date → Date type
  - [ ] Sleep_Hours → Decimal
  - [ ] Study_Hours → Decimal
  - [ ] Scores → Whole Number
  - [ ] Intensity → Text

### Phase 3: Page 1 - Dashboard Overview
**Visual 1: Sleep Hours Trend**
- [ ] Create Area Chart
- [ ] X-Axis: Date (continuous)
- [ ] Y-Axis: Sleep_Hours
- [ ] Color: #2E75B6
- [ ] Add 7-hour reference line
- [ ] Title: "Sleep Pattern (6 Month Trend)"

**Visual 2: Productivity vs Mood Scatter**
- [ ] Create Scatter Chart
- [ ] X-Axis: Mood_Score
- [ ] Y-Axis: Productivity_Score
- [ ] Size: Gym_Duration_Minutes
- [ ] Color: Gym_Intensity

**Visual 3: KPI Cards**
- [ ] Card 1: Avg_Sleep_CurrentMonth
- [ ] Card 2: Avg_Productivity
- [ ] Card 3: Avg_Mood
- [ ] Card 4: Gym_Consistency_Pct

**Visual 4: Study Hours by Day**
- [ ] Column Chart
- [ ] Day_of_Week on X-axis
- [ ] Sum Study_Hours on Y-axis
- [ ] Color: #70AD47
- [ ] Data labels: ON

**Visual 5: Water vs Screen Time**
- [ ] Combo Chart
- [ ] Line: Screen_Time (Avg)
- [ ] Column: Water_Intake (Avg)
- [ ] X-axis: Week_Number

**Visual 6: Gym Heatmap**
- [ ] Matrix visual
- [ ] Rows: Week_Number
- [ ] Columns: Day_of_Week
- [ ] Values: Gym_Intensity (color-coded)

### Phase 4: Page 2 - Detailed Analysis
- [ ] Create new page
- [ ] Add daily performance line chart
- [ ] Add correlation heatmap
- [ ] Add monthly performance card
- [ ] Enable drill-through

### Phase 5: Page 3 - Goal Tracking
- [ ] Create 4 gauge visuals
  - [ ] Sleep Quality Goal
  - [ ] Study Goal
  - [ ] Gym Consistency
  - [ ] Water Intake
- [ ] Create habits summary table
- [ ] Add conditional icons

### Phase 6: DAX Measures
- [ ] Copy Avg_Sleep_CurrentMonth
- [ ] Copy Avg_Productivity
- [ ] Copy Avg_Mood
- [ ] Copy Total_Study_Hours
- [ ] Copy Total_Gym_Sessions
- [ ] Copy Gym_Consistency_Pct
- [ ] Copy Sleep_7Day_Avg
- [ ] Copy Productivity_vs_PrevMonth
- [ ] Copy Goal Achievement measures
- [ ] Copy Correlation measures

### Phase 7: Design & Formatting
- [ ] Apply color scheme
- [ ] Set fonts (Segoe UI)
- [ ] Add page backgrounds
- [ ] Add borders to visuals
- [ ] Set margins (20px)
- [ ] Add footer text

### Phase 8: Interactivity
- [ ] Add Month slicer
- [ ] Add Gym_Intensity slicer
- [ ] Configure drill-through
- [ ] Add custom tooltips
- [ ] Test all interactions

### Phase 9: Polish & Export
- [ ] Review all pages
- [ ] Fix any visual issues
- [ ] Screenshot all 3 pages
- [ ] Save PBIX file
- [ ] Upload to GitHub

**Status: ☐ Not Started  ☐ In Progress  ☐ Complete**

---

## Project 2: IPL Cricket Performance Dashboard

### Phase 1: Data Preparation
- [ ] Run Python script (`01_IPL_Data_Generation.py`)
- [ ] Verify 3 CSVs created:
  - [ ] ipl_matches.csv
  - [ ] ipl_deliveries.csv
  - [ ] ipl_player_stats.csv
- [ ] Check data quality for each
- [ ] Verify row counts

### Phase 2: Power BI Setup
- [ ] Create new Power BI file
- [ ] Import ipl_matches.csv
- [ ] Import ipl_deliveries.csv
- [ ] Import ipl_player_stats.csv
- [ ] Set correct data types

### Phase 3: Relationships
- [ ] Model tab → Manage Relationships
- [ ] Create: Matches(Match_ID) → Deliveries(Match_ID)
- [ ] Create: PlayerStats(Player_Name) → Deliveries(Batsman)
- [ ] Create: PlayerStats(Player_Name) → Deliveries(Bowler)
- [ ] Verify relationships in Model view

### Phase 4: Page 1 - Match Overview
- [ ] Visual 1: Wins by Team (Bar Chart)
- [ ] Visual 2: Home vs Away (Clustered Columns)
- [ ] Visual 3: Toss Decision (Donut)
- [ ] Visual 4: Win Margin (Histogram)
- [ ] Visual 5: Season Trend (Line Chart)
- [ ] Visual 6: Top 10 Venues (Bar Chart)
- [ ] Add slicers: Season, Team

### Phase 5: Page 2 - Player Performance
- [ ] Visual 1: Top 10 Batsmen (Bar)
- [ ] Visual 2: Top 10 Bowlers (Bar)
- [ ] Visual 3: Strike Rate Leaderboard (Table)
- [ ] Visual 4: Economy Rate Leaders (Table)
- [ ] Visual 5: Centuries vs Fifties (Scatter)
- [ ] Enable drill-through on player bars

### Phase 6: Page 3 - Player Drill-Through
- [ ] Create detail page
- [ ] Add 4 KPI cards
- [ ] Add season performance line
- [ ] Add recent form columns
- [ ] Add head-to-head table
- [ ] Add achievement badges
- [ ] Add back button

### Phase 7: Page 4 - Team Analytics
- [ ] Add Team slicer (dropdown)
- [ ] Visual 1: Win % by Venue
- [ ] Visual 2: Squad Composition (Pie)
- [ ] Visual 3: Toss Strategy (Columns)
- [ ] Visual 4: Season Trend (Line)

### Phase 8: Page 5 - Match Insights
- [ ] Visual 1: Runs by Over (Stacked Columns)
- [ ] Visual 2: Wicket Types (Pie)
- [ ] Visual 3: Best Bowling Performances (Table)
- [ ] Add Season slicer

### Phase 9: DAX Measures
- [ ] Copy all Team Performance measures
- [ ] Copy all Batting metrics
- [ ] Copy all Bowling metrics
- [ ] Copy all Player Rankings
- [ ] Copy all Match Insights
- [ ] Copy Advanced Analytics measures
- [ ] Test each measure

### Phase 10: Color Scheme & Design
- [ ] Apply team color scheme:
  - [ ] MI: #004687
  - [ ] CSK: #FFCC00
  - [ ] RCB: #EC1C24
  - [ ] KKR: #3366BB
  - [ ] DC: #00539B
  - [ ] KXIP: #A4161A
  - [ ] RR: #E31937
  - [ ] SRH: #FF6D00
- [ ] Set accent colors
- [ ] Apply typography
- [ ] Add page backgrounds
- [ ] Set margins & spacing

### Phase 11: Interactivity
- [ ] Configure slicers (Season, Team, Venue)
- [ ] Set up drill-through flow
- [ ] Test all cross-filtering
- [ ] Add custom tooltips
- [ ] Configure back button
- [ ] Test navigation on all pages

### Phase 12: Polish & Export
- [ ] Review all 5 pages
- [ ] Check visual consistency
- [ ] Verify all interactivity works
- [ ] Fix any data issues
- [ ] Screenshot all pages
- [ ] Add footer text
- [ ] Save PBIX file
- [ ] Upload to GitHub

**Status: ☐ Not Started  ☐ In Progress  ☐ Complete**

---

## Portfolio Finalization

### GitHub
- [ ] Create repository
- [ ] Upload both PBIX files
- [ ] Upload all CSV data
- [ ] Upload Python scripts
- [ ] Upload setup guides
- [ ] Create comprehensive README
- [ ] Add links in bio

### LinkedIn
- [ ] Post about Project 1
  - [ ] Screenshot dashboard
  - [ ] Write compelling caption
  - [ ] Tag #PowerBI #DataAnalytics
  - [ ] Link to GitHub
- [ ] Post about Project 2
  - [ ] Screenshot dashboard
  - [ ] Write compelling caption
  - [ ] Tag #PowerBI #SportsAnalytics
  - [ ] Link to GitHub

### Resume Updates
- [ ] Add Power BI section
- [ ] List both projects
- [ ] Mention DAX complexity
- [ ] Link to GitHub portfolio
- [ ] Mention visualization types used

### Interview Preparation
- [ ] Write 2-minute pitch for each project
- [ ] Prepare 3 technical questions you could answer
- [ ] Practice explaining DAX measures
- [ ] Think of how to adapt these to business scenarios
- [ ] Record 5-minute demo video (optional)

### Portfolio Website (Optional)
- [ ] Create case study for Project 1
- [ ] Create case study for Project 2
- [ ] Write lessons learned
- [ ] Include screenshots
- [ ] Add demo videos
- [ ] Link from resume

---

## Final Verification

**Before claiming "Complete":**

- [ ] Both dashboards build without errors
- [ ] All DAX measures work correctly
- [ ] All visuals display data properly
- [ ] All interactions function as designed
- [ ] Dashboards look professional (design passes inspection)
- [ ] Data is accurate and clean
- [ ] Files are organized on GitHub
- [ ] Portfolio materials are published
- [ ] You can explain every part in an interview
- [ ] You feel confident showing these to a recruiter

---

## Estimated Timeline

| Phase | Time | Total |
|-------|------|-------|
| Project 1: Data | 15 min | 15 min |
| Project 1: Visuals | 2.5 hrs | 2 hrs 45 min |
| Project 1: DAX & Design | 1.5 hrs | 4 hrs 15 min |
| **Project 1 Total** | - | **4-5 hours** |
| | | |
| Project 2: Data | 20 min | 20 min |
| Project 2: Setup & Relationships | 2.5 hrs | 3 hrs 10 min |
| Project 2: Visuals (5 pages) | 2.5 hrs | 5 hrs 40 min |
| Project 2: DAX & Design | 1.5 hrs | 7 hrs 10 min |
| **Project 2 Total** | - | **6-8 hours** |
| | | |
| **Both Projects** | - | **10-13 hours** |
| **With breaks & polish** | - | **14-16 hours** |

---

**Good luck! Check off these boxes as you complete them.** ✅
