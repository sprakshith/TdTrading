# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# sns.set_style("darkgrid")
#
# df = pd.read_csv("Data/^NSEI/MorningStar/ProfitAndLoss.csv")
#
# df["DATE"] = pd.to_datetime(df["DATE"])
# df["PROFIT"] = df["P&L"] > 0
#
# for COL in ['VOLUME', "MACD", "MACDS", "RSI14"]:
#     fig, axes = plt.subplots(ncols=2, nrows=2)
#     fig.set_size_inches(20, 12)
#
#     DAYS_LIST = [5, 10, 15, 20]
#
#     index = 0
#     for i in range(2):
#         for j in range(2):
#             profit_count = len(df[df["DAYS"] == DAYS_LIST[index]][df["PROFIT"] == True])
#             loss_count = len(df[df["DAYS"] == DAYS_LIST[index]][df["PROFIT"] == False])
#             sns.scatterplot(x=COL, y="P&L", data=df[df["DAYS"] == DAYS_LIST[index]], hue="PROFIT", ax=axes[i][j])
#             axes[i][j].set_title(f"{DAYS_LIST[index]} Days: {profit_count} VS {loss_count}")
#             index += 1
#
#     plt.savefig("Data/^NSEI/MorningStar/Images/" + f"P&L VS {COL}.png", dpi=300)
