from datetime import date

# Calculate dates
d = date.today()
m = d.month()
y = d.year()
four_m = d.replace(month=(m-4))
one_y = d.replace(year=(y-1))

# Set earliest_date & latest_date in builds
config["builds"]["wa_4m"]["latest_date"] = d.strftime('%Y-%m-%d')
config["builds"]["wa_4m"]["earliest_date"]= four_m.strftime('%Y-%m-%d')
config["builds"]["wa_1y"]["earliest_date"]= one_y.strftime('%Y-%m-%d')
