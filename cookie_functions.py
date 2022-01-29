import sys, os, re
# Module containing cookie analysis functions

# Function which returns a list of the most active cookies on a given date
# param1: file to read cookies from
# param2: cookie date to keep track of
# return: array containing most active cookies [cookie_one, cookie_two, ... cookie_n]
def mostActiveCookies(current_file, current_date):
  # Array to keep track of most active cookies
  active_cookies = []
  # Dictionary to act as a hashtable to keep track of cookies
  cookie_dict = {}
  # Variable to keep track of most cookie occurences
  max_occurences = 0;
  # Open given input file for reading
  filepath = open(os.path.join(sys.path[0], current_file), "r")
  # Loop through file to keep track of cookies
  Lines = filepath.readlines()
  for line in Lines:
    # Split current line data fields
    cookie_data_one = line.split(",")
    cookie_data_two = cookie_data_one[1].split("T")
    # Associate cookie_data fields with appropriate variable for readbility
    cookie_name = cookie_data_one[0]
    cookie_date = cookie_data_two[0]
    # Make sure the cookie is of the specified input date
    if(cookie_date == current_date):
    # Increase the cookie's occurence in our dictionary
      if(cookie_name not in cookie_dict):
        cookie_dict[cookie_name] = 1;
      else:
        cookie_dict[cookie_name] += 1;
    # If the cookie's occurence is greater than our current maximum occurences, update the maxmimum occurences
      if(cookie_dict[cookie_name] > max_occurences):
        max_occurences = cookie_dict[cookie_name];
  # Loop through our dictionary and find cookies that match our maximum occurence value and print those out
  for cookie_name in cookie_dict:
    if(cookie_dict[cookie_name] == max_occurences):
      active_cookies.append(cookie_name)
  # Close file after done reading
  filepath.close();
  # Return the active cookies array
  return active_cookies
