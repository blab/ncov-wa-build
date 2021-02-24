from dateutil import relativedelta

# Calculate dates
d = date.today()
four_m = d - relativedelta.relativedelta(months=4)
one_y = d - relativedelta.relativedelta(years=1)

# Set earliest_date & latest_date in builds
if "wa_4m" in config["builds"]:
    config["builds"]["wa_4m"]["latest_date"] = d.strftime('%Y-%m-%d')
    config["builds"]["wa_4m"]["earliest_date"]= four_m.strftime('%Y-%m-%d')

if "wa_1y" in config["builds"]:
    config["builds"]["wa_1y"]["earliest_date"]= one_y.strftime('%Y-%m-%d')

# Add # of sequences per subsampling group
for build in config["builds"]:
    if "n_sequences" in config["builds"][build]:
        n = config["builds"][build]["n_sequences"]
        config["builds"][build]['n_usa'] = int(n*2/5)
        config["builds"][build]['n_global'] = int(n/5)
        config["builds"][build]['n_early'] = int(n/4)
        config["builds"][build]['n_global_early'] = int(n*3/20)
