#---------------------------------------------
# Possible GET command:
# - /http_ping
# - /get_state_xxx
# - /get_image
#---------------------------------------------

from src.utils import param
from src.connection.HTTPS.client import https_client_fct
from src.utils import parser_json

import json


def send_https_get(ip, port, connected, command):
    data = None
    if(connected):
        try:
            client = http.client.HTTPConnection(ip, port, timeout=2)
            client.request("GET", command)
            response = client.getresponse()
            data = response.read()
            client.close()
        except:
            pass
    return data

def get_image(dest):
    ip = param.state_edge["hub"]["info"]["ip"]
    port = param.state_edge["hub"]["http"]["server_port"]
    connected = param.state_control["interface"]["edge"]["http_connected"]

    command = "/get_image"
    data = send_https_get(ip, port, connected, command)
    if(data != None):
        if(len(data) != 0):
            img = open(param.path_state_current + "image", "wb")
            img.write(data)
            img.close()
            return True
    return False
