import os
import pandas as pd  # We need Pandas for the timezone fix
from datetime import date, timedelta

# --- PERMANENT FIX FOR JUGAAD-DATA BUG ---
# This overrides the default os.makedirs to always use exist_ok=True,
# preventing the multithreading crash.
original_makedirs = os.makedirs
def safe_makedirs(name, mode=0o777, exist_ok=False):
    return original_makedirs(name, mode, exist_ok=True)
os.makedirs = safe_makedirs
# -----------------------------------------

# Now import the library AFTER applying the fix
from jugaad_data.nse import stock_df

symbol = input("Enter stock symbol: ")

# Set your timeframe
end_date = date.today()
start_date = end_date - timedelta(days=15)

# Fetch historical data directly from the NSE
df = stock_df(symbol=symbol, from_date=start_date, to_date=end_date, series="EQ")

# --- FIX 1: Correct the timezone shift so your dates match ---
df['DATE'] = pd.to_datetime(df['DATE']) - pd.Timedelta(days=-1)

# --- FIX 2: Only request the columns that actually exist ---
# (Remember: stock_df cannot fetch Delivery data)
working_data = df[["DATE", "VOLUME", "NO OF TRADES", "DELIVERY QTY", "DELIVERY %"]]

# print(working_data.head(10))

print(list(df.columns))
