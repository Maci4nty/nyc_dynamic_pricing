import pandas as pd


data_path = r'data\processed\nyc_pricing_final.csv.gz'

dataFrame = pd.read_csv(data_path)

baseline_revenue = dataFrame['price'].sum().round(0)

dynamic_revenue = dataFrame['dynamic_price'].sum().round(0)

ROI = (((dynamic_revenue - baseline_revenue) / baseline_revenue) * 100).round(2)

print(f"Revenue with old prices: {baseline_revenue}\n"
      f"Revenue with new prices: {dynamic_revenue}\n"
      f"ROI of the change: {ROI}")
