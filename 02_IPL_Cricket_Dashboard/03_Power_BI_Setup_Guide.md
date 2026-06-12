# IPL Cricket Performance Dashboard - Complete Power BI Guide

## 🏆 PROJECT OVERVIEW

**Objective:** Build a professional multi-page sports analytics dashboard using real IPL data.  
**Dataset:** 234 IPL matches, 2800+ deliveries, 500+ player statistics.  
**Target Audience:** Recruiters + Cricket Analytics Portfolio.  
**Complexity:** Advanced (multi-page drill-throughs, custom sorting, dynamic filters)

---

## 📊 STEP 1: DATA IMPORT & RELATIONSHIPS

### Import 3 CSV Files:
1. **ipl_matches.csv** → Table: 'Matches'
2. **ipl_deliveries.csv** → Table: 'Deliveries'
3. **ipl_player_stats.csv** → Table: 'PlayerStats'

### Create Relationships:
- **Matches** (Match_ID) ←→ **Deliveries** (Match_ID) [1:Many]
- **PlayerStats** (Player_Name) ←→ **Deliveries** (Batsman) [1:Many]
- **PlayerStats** (Player_Name) ←→ **Deliveries** (Bowler) [1:Many]

### Data Type Setup:
- Dates: `Date` type
- Runs/Wickets: `Whole Number`
- Rates (Strike/Economy): `Decimal`
- Team/Role: `Text`

---

## 🎨 PAGE 1: MATCH OVERVIEW (6 Visuals)

### Visual 1: Wins by Team (Top-Left)
- **Chart Type:** Horizontal Bar Chart
- **X-Axis:** Winner (Team)
- **Y-Axis:** Count of matches won
- **Color:** Gradient from dark blue to light blue
- **Sort:** Descending by wins
- **Title:** "IPL Teams - Total Wins"
- **Data Labels:** ON, values

### Visual 2: Home vs Away Advantage (Top-Center)
- **Chart Type:** Clustered Column Chart
- **X-Axis:** Home_Team
- **Y-Axis 1:** Home wins (blue)
- **Y-Axis 2:** Away wins (orange)
- **Title:** "Home Court Advantage Analysis"
- **Tooltip:** Show win % for each

### Visual 3: Toss Decision Impact (Top-Right)
- **Chart Type:** Donut Chart
- **Values:** Count of Toss_Decision
- **Categories:** "bat" vs "field"
- **Color:** Bat=Green (#2ECC71), Field=Orange (#E74C3C)
- **Title:** "Toss Decision Distribution"
- **Center Label:** Toss Win %

### Visual 4: Win Margin Distribution (Bottom-Left)
- **Chart Type:** Histogram/Column Chart
- **X-Axis:** Winning_Margin (bins: 0-20, 20-50, 50+)
- **Y-Axis:** Count
- **Color:** #3498DB (Professional Blue)
- **Title:** "Match Outcomes - Winning Margins"

### Visual 5: Season Trend (Bottom-Center)
- **Chart Type:** Line Chart
- **X-Axis:** Season (2008-2016)
- **Y-Axis:** Count of matches
- **Multiple Lines:** By team (8 colors)
- **Title:** "IPL Growth - Matches Per Season"
- **Legend:** Positioned bottom

### Visual 6: Top 10 Venues (Bottom-Right)
- **Chart Type:** Bar Chart
- **X-Axis:** Venue
- **Y-Axis:** Match Count
- **Color:** #9B59B6 (Purple)
- **Top 10 Filter:** Only show top venues
- **Title:** "Most Frequently Used Venues"

---

## 👥 PAGE 2: PLAYER PERFORMANCE (5 Visuals + Drill-Through)

### Visual 1: Top 10 Batsmen (Left Side, Large)
- **Chart Type:** Bar Chart
- **X-Axis:** Player_Name
- **Y-Axis:** Sum of Runs
- **Color:** #27AE60 (Batting Green)
- **Data Labels:** ON, show run totals
- **Top 10 Filter:** Automatic
- **Title:** "Leading Run Scorers"
- **Interactivity:** Enable drill-through to player detail page

### Visual 2: Top 10 Bowlers (Left Side, Below)
- **Chart Type:** Bar Chart
- **X-Axis:** Player_Name
- **Y-Axis:** Sum of Wickets
- **Color:** #C0392B (Bowling Red)
- **Data Labels:** ON
- **Top 10 Filter:** Only wickets > 20
- **Title:** "Leading Wicket Takers"
- **Drill-Through:** Enabled

### Visual 3: Strike Rate Leaderboard (Right Side, Top)
- **Chart Type:** Table
- **Columns:** Player | Team | Matches | Strike Rate | Avg Runs/Match
- **Sort:** Strike Rate (Descending)
- **Conditional Formatting:** Bars for Strike Rate (Green=High, Red=Low)
- **Filter:** Only players with 20+ matches
- **Title:** "Best Strike Rates (Min 20 Matches)"

### Visual 4: Economy Rate Leaders (Right Side, Middle)
- **Chart Type:** Table
- **Columns:** Bowler | Team | Matches | Economy | Wickets
- **Sort:** Economy Rate (Ascending - lower is better)
- **Conditional Formatting:** Color scale (Green=Economical, Red=Expensive)
- **Filter:** Only bowlers with 15+ matches
- **Title:** "Most Economical Bowlers"

### Visual 5: Centuries & Fifties (Right Side, Bottom)
- **Chart Type:** Scatter Chart
- **X-Axis:** Centuries
- **Y-Axis:** Fifties
- **Size:** Total Runs
- **Color:** Team (8 colors, one per team)
- **Title:** "Achievement Matrix - Centuries vs Fifties"
- **Legend:** Team colors

---

## 🔍 PAGE 3: DETAILED PLAYER DRILL-THROUGH

**Triggered from:** Page 2 player clicks  
**Drill-Through Fields:** Player_Name, Team, Role

### Visual 1: Player KPIs (Top - 4 Cards)
1. **Total Runs** → Large number display
2. **Total Wickets** → Large number display (0 if batsman)
3. **Strike Rate / Economy** → KPI card (conditional formatting)
4. **Centuries / Best Bowling** → Text card

### Visual 2: Season Performance Trend
- **Chart Type:** Line Chart
- **X-Axis:** Season
- **Y-Axis:** Runs (if batsman) or Wickets (if bowler)
- **Color:** Team color
- **Title:** "Performance Across Seasons"

### Visual 3: Recent Form (Last 10 Matches)
- **Chart Type:** Column Chart
- **X-Axis:** Match Date (recent 10)
- **Y-Axis:** Runs/Wickets in each match
- **Color:** #E74C3C (Red for recent)
- **Title:** "Recent Performance"

### Visual 4: Head-to-Head Stats
- **Chart Type:** Table
- **Columns:** vs_Team | Matches | Runs/Wickets | Avg
- **Sort:** Matches (desc)
- **Title:** "Performance vs Each Team"

### Visual 5: Achievement Badges
- **Visual Type:** KPI Card with icons
- **Displays:**
  - 🥇 Centuries badge (if > 0)
  - 🥈 Fifties badge (if > 20)
  - ⚡ High SR badge (if > 140)
  - 🎯 Best Bowling badge

---

## 📈 PAGE 4: TEAM ANALYTICS (4 Visuals)

### Slicer: Team Selection (Dropdown)
- **Options:** All 8 IPL teams
- **Multi-select:** OFF (one team at a time)
- **Position:** Top of page

### Visual 1: Team Win % by Venue
- **Chart Type:** Bar Chart
- **X-Axis:** Venue
- **Y-Axis:** Win % (calculated measure)
- **Color:** Team color (selected team)
- **Title:** "Team Performance - Home Grounds"

### Visual 2: Squad Composition
- **Chart Type:** Pie Chart
- **Categories:** Role (Batsman, Bowler, All-rounder)
- **Values:** Count of players
- **Colors:** Batsman=#27AE60, Bowler=#C0392B, All-rounder=#F39C12
- **Title:** "Squad Composition"

### Visual 3: Toss Decision Impact
- **Chart Type:** Column Chart
- **X-Axis:** Toss_Decision (Bat vs Field)
- **Y-Axis:** Win % (calculated)
- **Color:** Bat=Green, Field=Orange
- **Title:** "Toss Strategy - Win Rate"

### Visual 4: Season-by-Season Performance
- **Chart Type:** Line Chart
- **X-Axis:** Season
- **Y-Axis:** Win %
- **Color:** Team color
- **Title:** "Team Performance Trend"

---

## 🎯 PAGE 5: MATCH INSIGHTS (3 Visuals)

### Visual 1: Runs Distribution by Over
- **Chart Type:** Column Chart
- **X-Axis:** Over (1-20)
- **Y-Axis:** Sum of Total_Runs (Inning 1 vs 2, stacked)
- **Colors:** Inning 1 = Dark Blue, Inning 2 = Light Blue
- **Title:** "Run Distribution Across Overs"
- **Insight:** Shows batting aggression timing

### Visual 2: Wicket Types Distribution
- **Chart Type:** Pie Chart
- **Values:** Count of Wicket_Type
- **Categories:** bowled, caught, lbw, run out
- **Colors:** Custom palette
- **Title:** "How Do Batsmen Get Out?"

### Visual 3: Best Bowling Performances
- **Chart Type:** Table
- **Columns:** Bowler | Team | Best_Bowling | Matches | Avg Economy
- **Conditional Formatting:** Best_Bowling column (color-coded)
- **Sort:** Wickets (descending)
- **Title:** "Notable Bowling Performances"

---

## 🎨 COLOR SCHEME (Sports Analytics)

### Primary Colors:
- **Team 1 (MI):** #004687 (Dark Blue)
- **Team 2 (CSK):** #FFCC00 (Gold)
- **Team 3 (RCB):** #EC1C24 (Red)
- **Team 4 (KKR):** #3366BB (Purple-Blue)
- **Team 5 (DC):** #00539B (Navy)
- **Team 6 (KXIP):** #A4161A (Maroon)
- **Team 7 (RR):** #E31937 (Pink-Red)
- **Team 8 (SRH):** #FF6D00 (Orange)

### Accent Colors:
- **Positive (Wins/Runs):** #27AE60 (Green)
- **Negative (Losses/Wickets):** #C0392B (Red)
- **Neutral (Data):** #3498DB (Blue)
- **Highlight:** #F39C12 (Orange)
- **Background:** #ECF0F1 (Light Gray)

### Typography:
- **Titles:** Segoe UI, 20pt, Bold, Dark Gray (#2C3E50)
- **Subtitles:** Segoe UI, 14pt, Regular
- **Data Labels:** Segoe UI, 10pt, Regular

---

## 🔗 INTERACTIVITY SETUP

### Slicers (Page 1):
1. **Season** - Horizontal buttons (2008-2016)
2. **Team** - Horizontal buttons (all 8 teams)
3. **Venue** - Dropdown (filter all pages)

### Drill-Throughs:
- **From:** Page 2 player bars
- **To:** Page 3 player detail
- **Back Button:** Positioned top-left
- **Pass Field:** Player_Name

### Cross-Filtering:
- **Page 1:** Clicking team bar filters all other visuals on that page
- **Page 4:** Team slicer updates all team analytics
- **Page 5:** Season slicer updates match insights

---

## 📱 RESPONSIVE DESIGN

- **Desktop:** 1920x1080
- **Tablet:** 1024x768
- **Margins:** 20px all sides
- **Grid spacing:** 5px
- **Visual borders:** 1px light gray

---

## 🚀 PUBLISHING STRATEGY

1. **Add Footer:** "IPL Analytics | Power BI Sports Dashboard | 234 Matches | Advanced DAX"
2. **Export PNGs:** Screenshot all 5 pages
3. **LinkedIn Post:** 
   - "Built a multi-page sports analytics dashboard analyzing 8 years of IPL data"
   - "Features: Player performance rankings, team analytics, drill-through details, advanced DAX measures"
   - "8 team-specific color schemes + dynamic filtering for complete interactivity"
4. **GitHub Upload:** PBIX + CSVs + DAX script
5. **Medium Article:** "Building Sports Analytics Dashboards with Power BI" (step-by-step)

---

## 💡 ADVANCED FEATURES TO IMPRESS

✅ **Team-specific color schemes** (recruiter will notice design thinking)  
✅ **Drill-through with context** (shows technical depth)  
✅ **Multi-measure comparisons** (advanced analytics)  
✅ **Season-over-season trends** (business insight)  
✅ **Custom DAX calculations** (hard to build, impressive to see)  
✅ **Conditional formatting** (polish & attention to detail)  

---

## 📊 EXPECTED RECRUITER REACTION

✅ "This is production-quality work"  
✅ "Shows understanding of sports analytics"  
✅ "Design is professional and intuitive"  
✅ "DAX measures indicate Power BI mastery"  
✅ Most likely follow-up: "Can you build this for our sales/marketing data?"  

---

**Estimated Build Time:** 6-8 hours  
**Difficulty:** Advanced  
**Portfolio Impact:** 10/10