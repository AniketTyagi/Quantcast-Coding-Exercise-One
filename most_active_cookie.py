#!/usr/bin/env python
import sys
from cookie_functions import mostActiveCookies
# Main file to find most active cookies in a given file log

if __name__ == "__main__":
  # Check if the command line arguments are valid
  if(len(sys.argv) != 4 or sys.argv[2] != "-d"):
    sys.exit("Usage: <input file> -d <date>");

  # Associate command line fields for readability
  input_file = sys.argv[1]
  input_date = sys.argv[3]
  for cookie in mostActiveCookies(input_file, input_date):
    print(cookie)
