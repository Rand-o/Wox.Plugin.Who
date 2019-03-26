# -*- coding: utf-8 -*-

from wox import Wox, WoxAPI
from netaddr import valid_ipv4
import pyperclip
import socket
import os

def json_wox(title, subtitle, icon, action=None, action_params=None, action_keep=None):
    json = {
        'Title': title,
        'SubTitle': subtitle,
        'IcoPath': icon
    }
    if action and action_params and action_keep:
        json.update({
            'JsonRPCAction': {
                'method': action,
                'parameters': action_params,
                'dontHideAfterAction': action_keep
            }
        })
    return json

def copy_to_clipboard(text):
    pyperclip.copy(text.strip())

def WhoIs(query):
    try:
    	if not valid_ipv4(query):
    		host = socket.gethostbyname(query)
    	else:
    		host = socket.gethostbyaddr(query)[0]
    except Exception as e:
        host = e
    results = []
    results.append(json_wox(host,
                            'Query: {}'.format(query),
                            'Images/app.icog',
                            'copy_clip',
                            [str(host)],
                            True))
    return results

class Who_Is(Wox):

    def query(self, query):
        return WhoIs(query)

    def copy_clip(self, query):
        #copy to clipboard after pressing enter
        copy_to_clipboard(query)
        WoxAPI.hide_app()
        

if __name__ == "__main__":
    Who_Is()