from dateutil import relativedelta

# Calculate dates
d = date.today()
two_m = d - relativedelta.relativedelta(months=2)
four_m = d - relativedelta.relativedelta(months=4)
one_y = d - relativedelta.relativedelta(years=1)

# Set earliest_date & latest_date in builds
if "wa_2m" in config["builds"]:
    config["builds"]["wa_2m"]["earliest_date"]= two_m.strftime('%Y-%m-%d')
    config["builds"]["wa_2m"]["background_date"] = four_m.strftime('%Y-%m-%d')

if "wa_4m" in config["builds"]:
    config["builds"]["wa_4m"]["earliest_date"]= four_m.strftime('%Y-%m-%d')

if "wa_1y" in config["builds"]:
    config["builds"]["wa_1y"]["earliest_date"]= one_y.strftime('%Y-%m-%d')
