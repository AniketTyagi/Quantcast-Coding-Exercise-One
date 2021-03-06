# Cookie Log Library
## About: 
This repository contains modules and executables to operate on cookie log text/csv files, with an assortment of functions to get valuable data from these formatted cookie log files of the format: (cookie,timestamp). Also contains unit tests for the cookie log modules.
## Files: 
### InterviewQuestion(4).zip
File containing the executables for the main file and the unit testing file.<br /> <br />
### **cookie_functions.py**: 
Module containing functions which can parse through cookie log text files and retrieve valuable information regarding them. <br /> <br />
### **most_active_cookie.py**: 
Source file containing function to get the most recurring cookie(s) of a certain date stamp within a cookie log file. The executable can be found within the zip file and it is executed through the following command: <br />**./most_active_cookie (cookie_log file) -d (date)**<br /> <br />
### **test_most_active_cookie_unittest.py**: 
Source file containing unit tests to test the most_active_cookie function within the cookie_functions module. The executable can be found within the zip file and it executed through the following command, and make sure the test_file.csv is within the same folder for reading: <br />**./test_most_active_cookie_unittest**<br /> <br />
### **test_file.csv**: 
Test cookie log CSV file to be utilized for the unit testing module
## How to run
Make sure to download the interview question zip file, as it contains every source file along with the main and unit test executables, and the test csv file for unit testing
