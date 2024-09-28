from configparser import ConfigParser
import csv

def read_configuration(category, key):
    config = ConfigParser()
    config.read("configurations/config.ini")
    return config.get(category, key)

def read_data_from_csv(filename):
    # create an empty list
    datalist= []

    # open the csv file
    csvdata= open(filename,"r")

    # create CSV reader
    reader= csv.reader(csvdata)

    #skip header
    next(reader)
    # Add csv rows to the list
    for rows in reader:
        datalist.append(rows)
        print(datalist)
        return datalist