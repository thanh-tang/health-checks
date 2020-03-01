#!/usr/bin/env python3

import re
import csv
import operator

def error_search(log_file):
  error_messages = {} # "Error", "Count"
  error_statistics = {} # "Username", "INFO", "ERROR"
  error_pattern = r"(INFO|ERROR) (.*) \((.*)\)$"

  # with open(log_file, mode="r",encoding="UTF-8") as file:
  with open(log_file) as file:
    for log in  file.readlines():
      result = re.search(error_pattern, log)
      if result is None:
        continue

      # initialize value
      if result.group(1) == "ERROR" and result.group(2) not in error_messages:
        error_messages[result.group(2)] = 0
      if result.group(3) not in error_statistics:
        error_statistics[result.group(3)]={"INFO":0,"ERROR":0}

      # set value for error and user
      if result.group(1) == "ERROR":
        error_messages[result.group(2)] += 1
      error_statistics[result.group(3)][result.group(1)] += 1

  # sort result
  error_messages = sorted(error_messages.items(), key=operator.itemgetter(1), reverse=True)
  error_statistics = sorted(error_statistics.items())
  return error_messages, error_statistics

def file_output_message(dictionary, file_name):
  with open(file_name, "w") as file:
    file.write("ERROR,Count\n")
    for key in dictionary:
      file.write(key[0] + "," + str(key[1]) + "\n")
    file.close()

def file_output_statistics(dictionary, file_name):
  with open(file_name, "w") as file:
    file.write("Username,INFO,ERROR\n")
    for values in dictionary:
      tmp = values[0] + "," + str(values[1]["INFO"]) + "," + str(values[1]["ERROR"]) + "\n"
      file.write(tmp)
    file.close()

error_messages, error_statistics = error_search("syslog.log")
file_output_message(error_messages, "error_message.csv")
file_output_statistics(error_statistics, "user_statistics.csv")
