# Data Project Practice
# by Joe Fraser

import os
import csv 
import statistics

# Data variables
spring = []
fall = []

def output_stats(list):
    print(f"Mean: {round(statistics.mean(list), 2)}")
    print(f"Median: {statistics.median(list)}")
    print(f"STD: {round(statistics.stdev(list), 2)}")
    print()

def display_csv_reader():

    # Create a file in directory 
    """ 
    filepath = os.path.join('c:/your/full/path', 'filename')
    if not os.path.exists('c:/your/full/path'):
        os.makedirs('c:/your/full/path')
    f = open(filepath, "a") 
    """

    # Read in the fie
    csv = 'Day 14/sample_grades.csv'

    with open(csv) as data_file:
        for line in data_file:
            list = line.rstrip().rsplit(',')
            if list[1] == 'Spring 2016':
                spring.append(eval(list[2]))
            else:
                fall.append(eval(list[2]))


if __name__ == '__main__':
    display_csv_reader()
    print('Fall 2016')
    output_stats(fall)
    
    print('Spring 2016')
    output_stats(spring)
    
    