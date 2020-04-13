#!/usr/bin/env python

import urllib2
import os.path
import time
import pandas as pd

dbfile = "user.csv"
outputfile = "Anytone.csv"
dburl = "https://www.radioid.net/static/user.csv"

print ("\nAnytoneCSVtool: A tool for downloading the current DMR database\nand converting for upload to Anytone DMR HTs by vk3dan\n")

# get the current database csv from radioid.net
if os.path.isfile(dbfile):
    print("user.csv found")
    creation_time = os.path.getctime(dbfile)
    if (current_time - creation_time) // (24 * 3600) >= 7:
        print("file over 7 days old, fetching current version (~9MB)")
        os.unlink(dbfile)
        response = urllib2.urlopen(dburl)
        with open(dbfile, 'w') as f: f.write(response.read ())
else:
    print("fetching DMR database file (~9MB)")
    response = urllib2.urlopen(dburl)
    with open(dbfile, 'w') as f: f.write (response.read ())

# manipulate DMR csv to suit Anytone HT
print("reformatting DMR database to suit Anytone...")
df = pd.read_csv(dbfile, dtype=object)
df.drop([0], axis=0, inplace=True)
df.insert(0,"No.",df.index.T)
df.insert(9,"Call Type","Private Call")
df.insert(10,"Call Alert","None")
df.drop(["LAST_NAME", "REMARKS"], axis=1, inplace=True)
df.insert(7,"Remarks","")
df = df.rename(columns={"RADIO_ID": "Radio ID", "CALLSIGN": "Callsign", "FIRST_NAME": "Name", "CITY": "City", "STATE": "State", "COUNTRY": "Country"})
df.to_csv(outputfile, index=False)
print (repr(df.index.size)+ " DMR IDs output to Anytone.csv")
