# timezone_api_automation
 Developed an API automation framework using request library to cover the timezone API. Please refer to readme.md for detailed information

--What needs to be installed to execute the script?

Below are the dependencies which needs to be installed:
Script Dependency:
	# Programming Language: Python Version 3.8
	# pip list:
			requests
			json
			xmltodict
			pprint
			openpyxl
			time

Note: The entire automation script is written in python 3.8 but has compatibility with python 2.7 version as well.

--How to execute?

The script can be executed with the below command from the command line:
	python test_List_Time_Zone.py
	python test_Get_Time_Zone.py
	python test_Convert_Time_Zone.py

Note: The prior installation needs to be done.


--What if the code doesn't work?

*	Ensure that all the dependencies as mentioned in the first point are installed correctly.
*	If any code issue arises, please revert back with the logs displayed at the command line.
*	You can also refer to the attached recording of the script execution.
*	The code may fail at test_Convert_Time_Zone_TC4() due to below reason:

	Your request is temporarily denied as you have exceeded the rate limit.
	To remain the stability of free TimeZoneDB service, each IP only allowed to make <strong>one</strong> request per second.
	Please consider an <a href="https://timezonedb.com/premium" to premium service with no limits and faster response.

	****Temporary fix added time.sleep(1) after each testcase is executed.

	Each test case in this file executes successfully if ran individually


--How the code works?

GlobalUtilities contains:
	# getExcelInDictionary: Reads excel data and creates a dictionary
generic_api:
	# This is generic code which handles all types of requests (GET, POST, PUT, DELETE)
BaseClass:
	# Contains the main code flow and also handles the interaction between GlobalUtilities and generic_api

--Framework Used:
	I have created a basic framework which runs simply with Python. I tried using Pytest but there were some import issues which are taking time to resolve.
	Basically, this framework has 3 folders:
		- ExternalDependency -- currently no external dependency is needed
		- PythonLibrary -- contains all the global utils file and also the main test run code
		- TestData -- contains the excel file

--What are the added testcases?

Currently, 10 testcases for each API have be added.
Each testcase has been assigned specific tag and the testcase description is also added in each execution scenario
More testcases can be added.

--Execution logs?
	I have also attached the logs in Execution_logs folder.

-- OS support?

As far as all the required dependencies are installed correctly, the script will run on Windows, Linux and Mac seamlessly.

Please revert back if any point seems unclear.
Thank You :)