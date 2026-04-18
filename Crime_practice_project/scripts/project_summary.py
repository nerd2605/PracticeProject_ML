project_summary = {"total_records": 57790,"highest_crime_month": "2025-10","lowest_crime_month": "2025-12","top_crime_type": "Violence and sexual offences","top_lsoa_area": "Cardiff 032H"}

project_summary

import json

with open("project_summary.json", "w") as f:json.dump(project_summary, f, indent=4)