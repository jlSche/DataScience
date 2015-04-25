import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from matplotlib.ticker import FuncFormatter

def formatFunction(tick_loc, tick_num):
  if tick_loc >= 1000:
    return '$' + str(tick_loc/1000) + 'M'
  else:
    return '$' + str(int(tick_loc)) + 'K'

df = pd.read_excel('../sourceData/twIncome2.xlsx', sheetname=1, index_col=None)
df.columns=['Country','Year','Top 10% avg income','Bottom 90% avg income']
df = df.drop(df.index[:1])

plt.scatter(df['Top 10% avg income'], df['Bottom 90% avg income'], marker='o', alpha=0.1)

for label, x, y in zip(df['Year'], df['Top 10% avg income'], df['Bottom 90% avg income']):
  plt.annotate(label, xy = (x, y), xytext = (0, 0), textcoords = 'offset points', ha = 'center', va = 'center', color='royalblue')

#plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%d K'))
plt.gca().xaxis.set_major_formatter(FuncFormatter(formatFunction))
plt.gca().yaxis.set_major_formatter(FuncFormatter(formatFunction))
plt.gca().tick_params(axis='x', colors='dimgray')
plt.gca().tick_params(axis='y', colors='dimgray')
plt.xlabel('Average Income for the Top 10 %', size=13, fontweight='bold')
plt.ylabel('Average Income for the Bottom 90%', size=13, fontweight='bold')
plt.show()
	

