import pandas as pd
import numpy as np
import os

indexlist1 = []
indexlist2 = []
def createIndexNeeded(size, freq):
  for idx in range(0, size):
    if idx % freq != 0:
      indexlist2.append(idx)
    if idx % freq != (freq-1):
      indexlist1.append(idx)

def convertDateFormat(date):
  return pd.to_datetime(str(date)) 

def categorizeDiff(value):
	if value < -20:
		return 1
	elif value < -10:
		return 2
	elif value < -5:
		return 3
	elif value < 5:
		return 4
	elif value < 10:
		return 5
	elif value < 20:
		return 6
	else:
		return 7

# read files in ../sourceData/youbike
youbike_file_path = './sourceData/youbike/'
youbike_data = [f for f in os.listdir(youbike_file_path) if os.path.isfile(os.path.join(youbike_file_path, f))]

# read all data
df = pd.read_csv(youbike_file_path+youbike_data[1])
for idx in range(2, len(youbike_data)):
	temp_df = pd.read_csv(youbike_file_path+youbike_data[idx])
	df = df.append(temp_df, ignore_index=True)
print len(df)

df = df.ix[:, ['mday','lat','lng','sbi']].sort(['lat','lng','mday']).reset_index(drop=True)

createIndexNeeded(len(df), 12)
newdf2 = df.ix[indexlist2].reset_index(drop=True)
newdf1 = df.ix[indexlist1].reset_index(drop=True)
print len(newdf1)
print len(newdf2)


diffdf = newdf1.merge(newdf2, right_index=True, left_index=True, how='outer')
diffdf['diff'] = diffdf['sbi_x'] - diffdf['sbi_y']
diffdf = diffdf[diffdf['diff']!=0]
diffdf.dropna(inplace=True)
diffdf = diffdf.ix[:, ['mday_x', 'lat_x','lng_x', 'diff']]
diffdf.columns = ['date','lat','lng','diff']
diffdf['date'] = diffdf['date'].apply(convertDateFormat)
diffdf['diff'] = diffdf['diff'].apply(categorizeDiff)

diffdf.to_csv('./ttemp.csv', index=False)



