import requests
from random import randint 
import datetime

def simple_request(code):
    responce = requests.get(f'https://httpstat.us/{code}')
    message = responce.text[4:] # убираю код из начала сообщения
    status_code = responce.status_code

    print(datetime.datetime.now(), ' - httpRequests.py - Request Code: ', code, '\n\tResponce code: ', status_code, '\n\tResponce message: ', message, sep='')
    if (code >= 400):
        error_message = "HTTP Error from httpRequests.py: code: " + str(status_code) + ", message: " + str(message)
        raise Exception(error_message)

for i in range(5):
    try:
        simple_request(randint(200,599)) # можно сделать при помощи хардкода пула описанных на сайте кодов
    except Exception as e:
        print(e)
