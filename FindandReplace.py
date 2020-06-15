# IMPORT JSON FROM URL AND WRITE TO FILE -------------------------------------------------------------------
import urllib.request, json, os, time

## Access and read input file
datain = urllib.request.urlopen(url)
data = json.loads(datain.read())

## Create a New File and Write Input Data To It
timestr = time.strftime("%Y%m%d")
with open ("ActivityLocationNames_Updated_" + timestr + ".json", "wt") as dataout:
	dataout.write(json.dumps(data))
	datain.close()
	dataout.close()

# FIND AND REPLACE STRINGS -------------------------------------------------------------------
datain = open("ActivityLocationNames_Updated_" + timestr + ".json", "r+")
data = datain.read()
data = data.replace(Old Value, New Value) # Insert old values and new values and repeat line for all value pairs.


datain.close()

datain = open("ActivityLocationNames_Updated_" + timestr + ".json", "w+")
datain.write(data)
datain.close()