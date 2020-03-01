#!/usr/bin/env python3
import os

def check_reboot():
  """Returns True if the computer has a pending reboot"""
  return os.path.exists("/run/reboot-required")

def print_str(text):
  print(text)

def print_str2(text):
  print(text)

def print_str3(text):
  print(text)

# main funtion
def main():
  if check_reboot():
    print("Pending Reboot.")
    sys.exit(1)
  if disk_full_check():
    print("Disk full")
    sys.exit(1)
  print("Everything is ok.")
  exit(0)
main()
