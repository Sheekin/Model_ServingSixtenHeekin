# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 15:52:11 2021

@author: 943655
"""
import json
import requests


if __name__ == "__main__":
    # Construct the URL and message to send to the microservice
    url = 'http://localhost:5000'
    json_message = {
        'instances' : [1, 5, 8, 9]
    }

    # Using the requests library, send a POST request with the following
    # message to the URL.
    response = requests.post(url=url,
                             data=json.dumps(json_message))
    #json.dumps serializes (converts to string) the message
    # Extract the status code and returned text
    status_code = response.status_code
    response_body = response.text
    

    # Print out the responses
    print(f"status code: {status_code}")
    print(f"response: {response_body}")
    print(f"")