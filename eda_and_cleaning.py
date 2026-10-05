import pandas as pd

# --- 1. CONFIGURATION & DATA INGESTION ---
calendar_path=r"data\raw\calendar.csv.gz"
listings_path=r"data\raw\listings.csv.gz"

df_calendar=pd.read_csv(calendar_path)
df_listings=pd.read_csv(listings_path)

# --- 2. DATA SANITIZATION & TYPE CASTING
# Removing listings without base prices - lack of a reference point makes impossible to calculate ROI
df_listings = df_listings.dropna(subset=["price"])

# Conversion currency from string type to numeric type for later operations
df_listings["price"] = df_listings["price"].str.replace("$", "")
df_listings["price"] = df_listings["price"].str.replace(",", "")
df_listings["price"] = df_listings["price"].astype(float)

# Standardization date format for future seasonality and weekend premium analysis
df_calendar["date"] = pd.to_datetime(df_calendar["date"])

# --- 3. DATA INTEGRATION ---
# Isolation only essential columns before merge to optimize memory usage
ids_and_price = df_listings[["id", "price"]]

# Enriching the calendar with static base prices (creating a baseline for the dynamic model)
merged_tables = df_calendar.merge(ids_and_price, how="inner", left_on="listing_id", right_on="id")
merged_tables = merged_tables.drop(columns=["id"])

# --- 4. EXPORT PIPELINE ---
# Exporting to a compressed .csv.gz format to comply with GitHub file size limits
merged_tables.to_csv(r"data\processed\nyc_pricing_base.csv.gz", index=False, compression="gzip")