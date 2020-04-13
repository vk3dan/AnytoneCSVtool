# AnytoneCSVtool
A tool for fetching and converting the DMR ID database for upload to an Anytone HT (and possibly B-Tech 6x2)

If the DMR database file exists and is under 7 days old, it will be used, otherwise it will be downloaded again.

This tool is written in python and requires pandas.

Windows users can click on 'Releases' above and there is an exe file provided there.

Usage:
```
$ ./AnytoneCSVTool.py

AnytoneCSVtool: A tool for downloading the current DMR database
and converting for upload to Anytone DMR HTs by vk3dan

fetching DMR database file (~9MB)

reformatting DMR database to suit Anytone...
159124 DMR IDs output to Anytone.csv

$
```
