from generic_api import generic_api
from GlobalUtilities import GlobalUtilities
from Variables import Variables
import time

class BaseClass():

    def __init__(self):
        #generic_api.__init__(self)
        #GlobalUtilities.__init__(self)
        self.GA=generic_api()
        self.GU=GlobalUtilities()

    def update_endpoint(self, endpoint, BaseURL, Key=None):
        if 'YOUR_API_KEY' in endpoint:
            endpoint = str(endpoint).replace('YOUR_API_KEY', str(Key))
        endpoint=BaseURL+endpoint
        print(endpoint)
        return endpoint

    def append_endpoint(self, endpoint, append_value):
        return endpoint+append_value

    def Timezone(self, sheetName, TestCaseName, BaseURL=Variables["api_base_url"], key=Variables["Key_1"]):

        testdata=self.GU.getExcelInDictionary(Variables["workBookpath"], sheetName, TestCaseName)
        print("\n\nExecuting testcase: {}\n{}".format(TestCaseName, testdata["Description"]))
        testdata["Endpoint"]=self.update_endpoint(testdata["Endpoint"], BaseURL, key)
        if testdata["Response_type"]=="json":
            testdata["Endpoint"]=self.append_endpoint(testdata["Endpoint"],"&format=json")
        response=self.GA.execute_api_call(testdata["Method"], testdata["Endpoint"], testdata["Response_code"],testdata["Response_type"])
        self.validate_Timezone_response(response,testdata)
        time.sleep(1)

    def validate_Timezone_response(self, actual_response, testdata):

        if testdata["Response_type"]=="json":
            response_message = actual_response['message']
            response_status = actual_response['status']
            if response_message=='':
                response_message='None'
        else:
            response_message=actual_response['result']['message']
            response_status = actual_response['result']['status']

        assert(str(response_message)==str(testdata['Message'])),\
            "The API response contains incorrect message: {}, the expected message is {}".format(response_message,testdata['Message'])
        assert (response_status == testdata['Status']),\
            "The API response contains incorrect status: {}, the expected status is {}".format(response_message, testdata['Status'])
        print("Response contains valid Status: {} and valid Message: {}".format(response_status,response_message))
