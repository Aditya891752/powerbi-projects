# 🚀 QUICK START - 5 Minutes to Your First Dashboard

## Choose Your Path:

### Path A: Personal Habit Dashboard (Faster ⚡)

**Step 1:** Generate Data (1 min)
```bash
cd 01_Personal_Habit_Dashboard
python 01_Data_Generation.py
```
✅ Creates: `personal_habit_tracking_6months.csv`

**Step 2:** Open Power BI Desktop & Import (2 min)
- File → New
- Get Data → Text/CSV
- Select `personal_habit_tracking_6months.csv`
- Load

**Step 3:** Follow the Setup Guide (2 hours)
- Open: `03_Power_BI_Setup_Guide.md`
- Build visuals exactly as described
- Copy-paste DAX from `02_DAX_Measures.txt`

---

### Path B: IPL Cricket Dashboard (Impressive 🏏)

**Step 1:** Generate Data (1 min)
```bash
cd 02_IPL_Cricket_Dashboard
python 01_IPL_Data_Generation.py
```
✅ Creates: 3 CSV files (Matches, Deliveries, PlayerStats)

**Step 2:** Open Power BI Desktop & Import (3 min)
- File → New
- Get Data → Text/CSV (repeat 3 times)
- Import all CSVs in this order:
  1. `ipl_matches.csv`
  2. `ipl_deliveries.csv`
  3. `ipl_player_stats.csv`

**Step 3:** Create Relationships (5 min)
- Model tab → Manage Relationships
- Connect Matches(Match_ID) ↔ Deliveries(Match_ID)
- Connect PlayerStats(Player_Name) ↔ Deliveries(Batsman)
- Connect PlayerStats(Player_Name) ↔ Deliveries(Bowler)

**Step 4:** Follow the Setup Guide (3+ hours)
- Open: `03_Power_BI_Setup_Guide.md`
- Build 5 pages as described
- Copy-paste DAX from `02_DAX_Measures.txt`

---

## ✨ Pro Tips:

✅ **Keep guides open in second monitor** while building  
✅ **Copy-paste DAX exactly** first time to save debugging  
✅ **Test each visual** before moving to next  
✅ **Screenshot each page** for your portfolio  
✅ **Save PBIX file** with version numbers  

---

## 🎯 Expected Timeline:

**Project 1:** 4-5 hours total  
**Project 2:** 6-8 hours total  
**Both Projects:** 10-13 hours (includes breaks)  

---

## 📱 Your Next Move:

1. **Choose one project** ⬆️
2. **Run data generation**
3. **Follow the step-by-step guide**
4. **Build your dashboard**
5. **Screenshot for portfolio**
6. **Upload to GitHub**
7. **Post on LinkedIn**
8. **Use in interviews!** 🎉

---

## ❓ Stuck?

Check:
- The detailed setup guide for your project
- DAX measures file for copy-paste code
- Sample CSVs to see data structure
- README.md for additional context

---

**Ready? Pick a project above and start now!** ⚡
