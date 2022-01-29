# Cookie Log Library
## About: 
This repository contains modules and executables to operate on cookie log text/csv files, with an assortment of functions to get valuable data from these formatted cookie log files of the format: (cookie,timestamp). Also contains unit tests for the cookie log modules.
## Files: 
### **cookie_functions.py**: 
Module containing functions which can parse through cookie log text files and retrieve valuable information regarding them. <br /> <br />
### **most_active_cookie.py**: 
Executable file containing function to get the most recurring cookie(s) of a certain date stamp within a cookie log file. Make sure to run to have cookie_functions.py within the same directory and to run **chmod +x most_active_cookie.py** to make it an executable and that the input csv file is readable. It is executed through the following command: <br />**./most_active_cookie.py (cookie_log file) -d (date)**<br /> <br />
### **test_most_active_cookie_unittest.py**: 
Executable file containing unit tests to test the most_active_cookie function within the cookie_functions module. Is executed through the following command: <br />**./test_most_active_cookie_unittest.py**<br /> <br />
### **test_file.csv**: 
Test cookie log CSV file to be utilized for the unit testing module
