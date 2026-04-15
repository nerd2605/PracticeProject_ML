class CrimeFilter:
    def __init__(self,df):
        self.df = df
    def filter_by_month(self,month):
        filtered_df = self.df[self.df["Month"] == month]
        return filtered_df 
    def filter_by_outcome(self,outcome):
        filtered_df = self.df[self.df["Last outcome category"] == outcome]
        return filtered_df
    def filter_by_crime(self, crime_type):
        filtered_df = self.df[self.df["Crime type"] == crime_type]
        return filtered_df
    def filter_by_location(self,location):
        filtered_df = self.df[self.df["Location"] == location]
        return filtered_df
    def filter_by_lsoa(self,lsoa):
        filtered_df = self.df[self.df["LSOA name"] == lsoa]
        return filtered_df

crime_filter = CrimeFilter(combined_df)
crime_filter.filter_by_month("2025-10").head()
crime_filter.filter_by_outcome("Unable to prosecute suspect").head()
crime_filter.filter_by_crime("Robbery").head()
crime_filter.filter_by_location("On or near Supermarket").head()
crime_filter.filter_by_lsoa("Vale of Glamorgan 003B").head()