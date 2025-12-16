import os
import pandas as pd


xlsx_path = r"E:\R\mayy\1214\final\data\raw\Columbus_ThreadEx_2025_Jul-Nov.xlsx"
sheet_names = ["2025-07", "2025-08", "2025-09", "2025-10", "2025-11"]

# 读取并合并所有月份的数据
dfs = [pd.read_excel(xlsx_path, sheet_name=sheet, engine="openpyxl") for sheet in sheet_names]
df = pd.concat(dfs, ignore_index=True)

out_dir = r"E:\R\mayy\1214\final\data\processed"
os.makedirs(out_dir, exist_ok=True)

out_csv = os.path.join(out_dir, "columbus_daily_merged.csv")

df.to_csv(out_csv, index=False, encoding="utf-8-sig")

print("Done.")
print("Saved:", out_csv)
print(df.head())
