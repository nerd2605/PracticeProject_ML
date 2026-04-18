# Features 
# Feature 1 
crimes_per_location = combined_df.groupby("Location").size().reset_index(name = "Crime_Count")
# print(crimes_per_location.head())
# print(crimes_per_location["Crime_Count"].max())
# print(crimes_per_location["Crime_Count"].min())
# print(len(crimes_per_location))

#Feature 2 

crimes_per_type = combined_df.groupby("Crime type").size().reset_index(name = "Crime_Type")
print(crimes_per_type)
# print(crimes_per_type["Crime Type"].max())
# print(crimes_per_type["Crime Type"].min())
# print(crimes_per_type["Crime Type"].mean())
# print(crimes_per_type["Crime Type"].median())
# print(len(crimes_per_type))
# crimes_per_type.sort_values(by="Crime Type",ascending=False)

# Feature 3 
crimes_per_month = combined_df.groupby("Month").size().reset_index(name = "Crime_Count")
# print(crimes_per_month)
print(crimes_per_month.sort_values(by="Crime_Count", ascending=False).head(1))
print(crimes_per_month.sort_values(by="Crime_Count", ascending=True).head(1))
crimes_per_month["Monthly change"] = crimes_per_month["Crime_Count"].diff()
# print(crimes_per_month)
crimes_per_month["Absolute Change"] = crimes_per_month["Monthly change"].abs()
print(crimes_per_month)

# Feature 4

crimes_by_lsoa = combined_df.groupby("LSOA name").size().reset_index(name = "Crime_Count")
# print(len(crimes_by_lsoa))
# print(crimes_by_lsoa.sort_values(by="Crime_Count", ascending = False))
# print(crimes_by_lsoa.sort_values(by="Crime_Count", ascending = True))

def classify_risk(count):
    if count < 50:
        return "Low"
    elif count < 200:
        return "Medium"
    else:
        return "High"
crimes_by_lsoa["Risk Level"] = (crimes_by_lsoa["Crime_Count"].apply(classify_risk))

risk_counts = crimes_by_lsoa["Risk Level"].value_counts()
# print(risk_counts)
risk_count_percentage = risk_counts/risk_counts.sum() * 100 
# print(risk_count_percentage)


crimes_by_risk = crimes_by_lsoa.groupby("Risk Level")["Crime_Count"].sum().reset_index()
# print(crimes_by_risk)

total_crimes_by_risk = crimes_by_risk["Crime_Count"].sum()
crimes_by_risk["Percentage"] = (crimes_by_risk["Crime_Count"] / total_crimes_by_risk * 100)
# print(crimes_by_risk)

crimes_by_risk = (crimes_by_lsoa.groupby("Risk Level")["Crime_Count"].sum().reset_index())

print(crimes_by_risk)