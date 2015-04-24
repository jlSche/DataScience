import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('../sourceData/twIncome2.xlsx', sheetname=1, index_col=None)
df.columns=['Country','Year','Top 10% avg income','Bottom 90% avg income']
df = df.drop(df.index[:1])

plt.scatter(df['Top 10% avg income'], df['Bottom 90% avg income'], marker='o', alpha=0.1)

for label, x, y in zip(df['Year'], df['Top 10% avg income'], df['Bottom 90% avg income']):
    plt.annotate(label, xy = (x, y), xytext = (0, 0), textcoords = 'offset points', ha = 'center', va = 'center', color='royalblue')

plt.xlabel('Top 10% Avg. Income (thousand TWD)', size=15)
plt.ylabel('Bottom 90% Avg. Income (thousand TWD)', size=15)
plt.show()
	


