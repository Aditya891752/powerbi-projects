# Personal Habit & Productivity Dashboard - Power BI Setup Guide

## 📊 PROJECT OVERVIEW
**Objective:** Build a visually striking personal analytics dashboard tracking 6 months of daily habits.  
**Target Audience:** Recruiters - shows data literacy & self-optimization mindset.  
**Complexity:** Senior-level (advanced DAX, drill-throughs, custom formatting)

---

## 📥 STEP 1: DATA IMPORT

1. **Open Power BI Desktop**
2. **Get Data → Text/CSV**
3. **Load:** `personal_habit_tracking_6months.csv`
4. **Transform Data:**
   - Date column: Set to `Date` data type
   - All score columns: Change to `Whole Number`
   - Sleep/Study/Water/Screen: Change to `Decimal Number`
   - Gym_Intensity: Set to `Text`

---

## 🎨 STEP 2: PAGE 1 - DASHBOARD OVERVIEW (3x2 Grid)

### Visual 1: Sleep Hours Trend (Top-Left)
- **Chart Type:** Area Chart
- **X-Axis:** Date (continuous)
- **Y-Axis:** Sleep_Hours
- **Color:** #2E75B6 (Professional Blue)
- **Title:** "Sleep Pattern (6 Month Trend)"
- **Goal Line:** Add reference line at 7 hours (healthy benchmark)

### Visual 2: Productivity vs Mood Scatter (Top-Center)
- **Chart Type:** Scatter Chart
- **X-Axis:** Mood_Score
- **Y-Axis:** Productivity_Score
- **Size:** Gym_Duration_Minutes
- **Legend:** Gym_Intensity (color coding)
- **Colors:** Rest=Gray, Light=Yellow, Medium=Orange, High=Red
- **Title:** "Mood-Productivity Relationship"

### Visual 3: Key KPIs (Top-Right, 4 Cards)
- Card 1: Avg_Sleep_CurrentMonth → "7.2 hrs"
- Card 2: Avg_Productivity → "7.8/10"
- Card 3: Avg_Mood → "7.3/10"
- Card 4: Gym_Consistency_Pct → "68%"

### Visual 4: Study Hours by Day of Week (Bottom-Left)
- **Chart Type:** Column Chart
- **X-Axis:** Day_of_Week (Mon-Sun)
- **Y-Axis:** Sum of Study_Hours
- **Color:** #70AD47 (Study Green)
- **Data Labels:** ON

### Visual 5: Water Intake vs Screen Time (Bottom-Center)
- **Chart Type:** Combo Chart
- **Line:** Screen_Time_Hours (Avg) → Color: #FF6B6B (Red)
- **Column:** Water_Intake_Liters (Avg) → Color: #4ECDC4 (Cyan)
- **X-Axis:** Week_Number
- **Title:** "Inverse Health Indicator"

### Visual 6: Gym Consistency Heatmap (Bottom-Right)
- **Chart Type:** Matrix/Table
- **Rows:** Week_Number
- **Columns:** Day_of_Week
- **Values:** Gym_Intensity (color-coded background)
- **Conditional Formatting:** High=Dark Green, Medium=Orange, Light=Yellow, Rest=Gray

---

## 📈 STEP 3: PAGE 2 - DETAILED ANALYSIS (Drill-Through)

### Visual 1: Daily Performance Breakdown (Line Chart)
- **X-Axis:** Date
- **Y-Axis:** Mood_Score, Productivity_Score, Sleep_Quality
- **Multi-line:** 3 lines overlaid
- **Colors:** Mood=Blue, Productivity=Green, Sleep=Orange
- **Enable Drill-Through** on Day_of_Week

### Visual 2: Correlation Heatmap
- **Chart Type:** Table with conditional formatting
- **Metrics:** Sleep_Hours, Study_Hours, Gym_Duration, Mood_Score, Productivity_Score
- **Show:** Correlation coefficients (calculate using DAX)
- **Heat Colors:** Green (positive) → White → Red (negative)

### Visual 3: Monthly Performance Card
- **Slicer:** Month selection (dropdown)
- **Displays:** 
  - Avg Sleep, Avg Study, Total Gym Hours
  - Consistency metrics (% target achievement)
  - Trend indicator (↑/↓ vs previous month)

---

## 🎯 STEP 4: PAGE 3 - GOAL TRACKING

### Visual 1: Goal Progress Gauges (4 Gauges in 2x2 grid)
1. **Sleep Quality Goal** (Target: 7+ hrs) → Gauge 0-100%
2. **Study Goal** (Target: 4+ hrs) → Gauge 0-100%
3. **Gym Consistency** (Target: 65%+) → Gauge 0-100%
4. **Water Intake Goal** (Target: 2.5+ L) → Gauge 0-100%

**Formatting:**
- Green (90-100%), Yellow (70-89%), Red (Below 70%)
- Use DAX formulas for each goal measure

### Visual 2: Habits Summary Table
- **Columns:** Metric | Target | Actual | Achievement % | Trend
- **Rows:** Sleep, Study, Gym, Water, Mood, Productivity
- **Conditional Icons:** ✅ (Met), ⚠️ (Close), ❌ (Missed)

---

## 🎨 STEP 5: FORMATTING & DESIGN

### Color Scheme (Professional Data Analytics)
- **Primary:** #1F77B4 (Dark Blue) - Titles, KPIs
- **Secondary:** #2E75B6 (Professional Blue) - Charts
- **Accent 1:** #70AD47 (Green) - Positive metrics
- **Accent 2:** #FF6B6B (Red) - Warning metrics
- **Accent 3:** #4ECDC4 (Cyan) - Health metrics
- **Background:** #F5F5F5 (Light Gray)
- **Text:** #333333 (Dark Gray)

### Typography
- **Titles:** Segoe UI, 18pt, Bold, Dark Blue
- **Subtitles:** Segoe UI, 12pt, Regular
- **Data Labels:** Segoe UI, 10pt, Regular

### Page Layout
- **Margins:** 20px all sides
- **Grid Spacing:** 5px
- **Visual Borders:** Light gray, 1px
- **Background:** Apply theme color

---

## 🔗 STEP 6: INTERACTIVITY

### Slicers (Top of Page 1)
1. **Month Slicer** - Horizontal button style
2. **Gym_Intensity Slicer** - Horizontal button style

### Drill-Through Setup
- **From:** Overview charts (Sleep, Productivity)
- **To:** Detail pages with date-specific breakdown
- **Back Button:** Enabled on all detail pages

### Tooltips
- **Hover on trend lines:** Show 7-day average
- **Hover on mood:** Show sleep + screen time correlation

---

## 📊 STEP 7: PUBLISHING TIPS FOR RECRUITERS

1. **Add Footer:** "Personal Analytics Dashboard | 6-Month Self-Tracking | Built with Power BI"
2. **Screenshot:** Capture all 3 pages for portfolio
3. **LinkedIn:** Post with caption: "Built a personal analytics dashboard to track habits & correlate productivity with lifestyle factors. SQL queries + DAX measures + interactive drill-throughs."
4. **GitHub:** Upload PBIX file + Data CSV + DAX script

---

## ⚙️ ADVANCED DAX (Optional Enhancement)

```DAX
// Correlation: Sleep Impact on Productivity (coefficient)
Sleep_Productivity_Correlation = 
VAR HighSleepAvgProd = CALCULATE(
    AVERAGE('HabitTracking'[Productivity_Score]),
    FILTER('HabitTracking', 'HabitTracking'[Sleep_Hours] >= 8)
)
VAR LowSleepAvgProd = CALCULATE(
    AVERAGE('HabitTracking'[Productivity_Score]),
    FILTER('HabitTracking', 'HabitTracking'[Sleep_Hours] < 6.5)
)
RETURN
ROUNDUP((HighSleepAvgProd - LowSleepAvgProd) / LowSleepAvgProd * 100, 1)
```

**Result:** Shows % productivity improvement with better sleep → Impressive insight!

---

## 🎯 EXPECTED RECRUITER REACTION
✅ "This shows SQL + data modeling skills"  
✅ "DAX measures indicate Power BI expertise"  
✅ "Personal optimization mindset = professional growth"  
✅ "Multi-page design = UX awareness"  
✅ Likely to ask: "Can you build this for our sales data?"  

---

**Estimated Build Time:** 4-5 hours  
**Difficulty:** Senior  
**Portfolio Impact:** 9/10