import pandas as pd
import sqlite3

# # Read sqlite query results into a pandas DataFrame
# con = sqlite3.connect("data.db")
# df = pd.read_sql_query("SELECT * from portfolios", con)

# # Verify that result of SQL query is stored in the dataframe
# print(df.head())

# con.close()

data = ["Test User", "WMT", "Portfolio One"]
df = pd.DataFrame(data, columns=["analyst", "ticker", "portfolio_name"])
print(df)
