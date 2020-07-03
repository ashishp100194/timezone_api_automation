import requests
import json
import xmltodict
from pprint import pprint as pp
class generic_api():

    def __init__(self):
        pass

    def execute_api_call(self, method, endpoint, response_code, response_type=None, payload=None, header=None):

        response=''
        if method == 'POST':
            print ("Method Type: "+method)
            print(json.dumps(payload))
            print (payload)
            response = requests.post(endpoint, data=payload, headers=header)
        elif method == 'PUT':
            print("Method Type: "+method)
            print(json.dumps(payload))
            response = requests.put(endpoint, data=json.dumps(payload), headers=header)
        elif method == 'GET':
            print("Method Type: "+method)
            if header==None:
                response = requests.get(endpoint)
            else:
                response = requests.get(endpoint, headers=header)
        elif method == 'DELETE':
            print("Method Type: "+method)
            response = requests.delete(endpoint, headers=header)
        else:
            print("Method Type: "+method+" is invalid!")

        if response_type=='json':
            api_response=response.json()
        elif response_type=='xml':
            print("The response is in XML. This response will be converted into dict to parse easily!\nXML: {}".format(response.content))
            api_response=json.loads(json.dumps(xmltodict.parse(response.content)))
        pp(api_response)

        assert response.status_code == int(response_code), \
            "Validation of Expected response code failed.\nExpected : " + str(response_code) + "\nActual: " + str(response.status_code)  + "\n Actual Response Body: " + str(response.text)
        print('Response Code {} validated successfully'.format(response.status_code))

        return api_response