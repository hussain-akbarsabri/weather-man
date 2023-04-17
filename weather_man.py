import re
import os
import sys

def get_output_flag(params):
    try:
        return params.split()[2]
    except ValueError:
        print("wrong params entered")
    except IndexError:
        print("flag not found")

def get_date(params):
    try:
        month_names = {"1": "Jan", "2": "Feb", "3": "Mar", "4": "Apr", "5": "May", "6": "Jun", "7": "Jul", "8": "Aug", "9": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"}
        date = params.split()[3].replace('/', '_')
        if "_" in date:
            split_date = date.split('_')
            split_date[-1] = month_names[date.split('_')[-1]]
            return '_'.join(split_date)
        return date
    except ValueError:
        print("wrong params entered")
    except IndexError:
        print("date not found")
    except KeyError:
        print("month not found")

def get_path(params):
    try:
        return params.split()[4]
    except ValueError:
        print("wrong params entered")
    except IndexError:
        print("path not found")

def get_filtered_files(date, path):
    files = os.listdir(path)
    matching_files = [f for f in files if date in f]
    return matching_files

def calculate_temperature(path, files):
    max_temp = -sys.maxsize
    min_temp = sys.maxsize
    try:
        for file in files:
            with open((path + '/' + file), 'r') as f:
                for row in f:
                    line = row.split(',')
                    if re.match(r'^\d{4}-\d{1,2}-\d{1,2}$', line[0]):
                        if line[1] != '' and int(line[1]) > max_temp:
                            max_temp = int(line[1])
                        if line[3] != '' and int(line[3]) < min_temp:
                            min_temp = int(line[3])
    except FileNotFoundError:
        print('file not found')
    return max_temp, min_temp

params = 'python weather_man.ipynb -c 2004/8 Dubai_weather'
output_flag = get_output_flag(params)
date = get_date(params)
path = get_path(params)
files = get_filtered_files(date, path)
if output_flag == '-e':
    'abc'
elif output_flag == '-a':
    'abc'
elif output_flag == '-c':
    'abc'
temperature = calculate_temperature(path, files)
print(temperature)
