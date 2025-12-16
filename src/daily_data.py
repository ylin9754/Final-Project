import pandas as pd
import matplotlib.pyplot as plt
import os

path = r"E:\R\mayy\1214\final\data\processed\columbus_daily_merged.csv"
df = pd.read_csv(path)
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

HOT_F = 90
COLD_F = 32
RAIN_IN = 0.01

df["is_hot"]  = df["Maximum"] >= HOT_F
df["is_cold"] = df["Minimum"] <= COLD_F
df["is_rainy"] = df["Precipitation"] >= RAIN_IN
df["is_snow"]  = df["NewSnow"] > 0

monthly = df.groupby("Month").agg(
    avg_temp_mean=("Average","mean"),
    max_temp_max=("Maximum","max"),
    min_temp_min=("Minimum","min"),
    precip_sum=("Precipitation","sum"),
    rainy_days=("is_rainy","sum"),
    precip_trace_days=("Precipitation_trace","sum"),
    new_snow_sum=("NewSnow","sum"),
    snow_days=("is_snow","sum"),
    hdd_sum=("HDD","sum"),
    cdd_sum=("CDD","sum"),
    dep_mean=("Departure","mean"),
).reset_index()

print(monthly)


out_dir = "plots"
os.makedirs(out_dir, exist_ok=True)


x_date = df["Date"].to_numpy()

plt.figure()
plt.plot(x_date, df["Average"].to_numpy())
plt.title("Daily Average Temperature")
plt.xlabel("Date"); plt.ylabel("Temperature (F)")
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "01_daily_avg_temperature.png"), dpi=300)
plt.close()


plt.figure()
y_min = df["Minimum"].to_numpy()
y_max = df["Maximum"].to_numpy()
plt.fill_between(x_date, y_min, y_max, alpha=0.3)
plt.plot(x_date, y_max)
plt.plot(x_date, y_min)
plt.title("Daily Temperature Range (Min to Max)")
plt.xlabel("Date"); plt.ylabel("Temperature (F)")
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "02_daily_temp_range.png"), dpi=300)
plt.close()


plt.figure()
plt.bar(x_date, df["Precipitation"].to_numpy())
plt.title("Daily Precipitation")
plt.xlabel("Date"); plt.ylabel("Precipitation (in)")
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "03_daily_precipitation.png"), dpi=300)
plt.close()


nonzero = df.loc[df["Precipitation"] > 0, "Precipitation"].dropna().to_numpy()
if len(nonzero) > 0:
    plt.figure()
    plt.hist(nonzero)
    plt.title("Precipitation Distribution (Non-zero Days)")
    plt.xlabel("Precipitation (in)"); plt.ylabel("Days")
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "04_precip_hist_nonzero.png"), dpi=300)
    plt.close()


plt.figure()
plt.bar(monthly["Month"].astype(str).to_numpy(), monthly["hdd_sum"].to_numpy())
plt.title("Monthly HDD (Heating Degree Days)")
plt.xlabel("Month"); plt.ylabel("HDD")
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "05_monthly_hdd.png"), dpi=300)
plt.close()

plt.figure()
plt.bar(monthly["Month"].astype(str).to_numpy(), monthly["cdd_sum"].to_numpy())
plt.title("Monthly CDD (Cooling Degree Days)")
plt.xlabel("Month"); plt.ylabel("CDD")
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "06_monthly_cdd.png"), dpi=300)
plt.close()

print(f"Saved plots to: {os.path.abspath(out_dir)}")
