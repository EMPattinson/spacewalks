# https://data.nasa.gov/resource/eva.json (with modifications)
import pathlib
import json
import csv
import datetime as dt

import matplotlib.pyplot as plt

input_file = open(pathlib.Path("EVA_data_NASA.json"), 'r', encoding="ascii")
output_file = open(pathlib.Path("EVA_data_NASA.csv"),'w', encoding="utf-8")
graph_file = pathlib.Path("EVA_time_by_year.png")

field_names = ("EVA #", "Country", "Crew    ", "Vehicle", "Date", "Duration", "Purpose")

data=[]


for i in range(375):
    line=input_file.readline()
    print(line)
    data.append(json.loads(line[1:-1]))
#data.pop(0)
## Comment out this bit if you don't want the spreadsheet


outfile_writer = csv.writer(output_file)



time = []
date =[]

j=0
for i in data:
    print(data[j])
    # and this bit
    outfile_writer.writerow(data[j].values())
    if 'duration' in data[j].keys():
        eva_duration=data[j]['duration']
        if eva_duration == '':
            pass
        else:
            eva_duration_datetime = dt.datetime.strptime(eva_duration,'%H:%M')
            eva_duration_hours = dt.timedelta(hours=eva_duration_datetime.hour, minutes=eva_duration_datetime.minute, seconds=eva_duration_datetime.second).total_seconds()/(60*60)
            print(eva_duration_datetime,eva_duration_hours)
            time.append(eva_duration_hours)
            if 'date' in data[j].keys():
                date.append(dt.datetime.strptime(data[j]['date'][0:10], '%Y-%m-%d'))
                #date.append(data[j]['date'][0:10])

            else:
                time.pop(0)
    j+=1

eva_duration_datetime=[0]
for i in time:
    eva_duration_datetime.append(eva_duration_datetime[-1]+i)

date,time = zip(*sorted(zip(date, time)))



plt.plot(date,eva_duration_datetime[1:], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()
