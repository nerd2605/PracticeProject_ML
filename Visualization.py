# Visualization 
import matplotlib.pyplot as plt
plt.figure()
plt.bar(crimes_by_risk["Risk Level"],crimes_by_risk["Crime_Count"])
plt.title("Crime Count by Risk Level")
plt.xlabel("Risk Level")
plt.ylabel("Crime Count")
plt.show()

# 2 
plt.figure(figsize = (8,5))
plt.plot(crimes_per_month["Month"], crimes_per_month["Crime_Count"])
plt.title("Crime count by Month")
plt.xlabel("Month")
plt.xticks(rotation = 45)
plt.ylabel("Crime_Count")
plt.show()

# #3 
plt.figure(figsize = (10,6))
plt.bar(crimes_per_type["Crime type"], crimes_per_type["Crime_Type"])
plt.title("Crime by type")
plt.xlabel("Crime type")
plt.xticks(rotation = 55)
plt.ylabel("Crime_Type")
plt.show()

#4 

crimes_per_lsoa_sorted = crimes_by_lsoa.sort_values(by = "Crime_Count", ascending =False).head(10)
plt.figure(figsize = (10,6))
plt.bar(crimes_per_lsoa_sorted["LSOA name"], crimes_per_lsoa_sorted["Crime_Count"])
plt.title("Crimes by LSOA")
plt.xlabel("LSOA name")
plt.ylabel("Crime Count")
plt.xticks(rotation = 60)
plt.show()

# 5 

plt.figure(figsize = (10,5))
plt.bar(crimes_per_month["Month"], crimes_per_month["Absolute Change"])
plt.title("Crimes by month")
plt.xlabel("Month")
plt.ylabel("Absolute Change")
plt.xticks(rotation = 60)
plt.show()

#6 

