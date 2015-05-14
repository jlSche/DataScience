import urllib
import datetime
import time
import os

currenttime = datetime.datetime.now()
filename = str(currenttime.hour)+str(currenttime.minute)+'.csv'
filepath = os.path.join('~/Documents/DataScience/sourceData/youbike/', filename)
content = urllib.urlretrieve('http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=ddb80380-f1b3-4f8e-8016-7ed9cba571d5&format=csv', filename)



