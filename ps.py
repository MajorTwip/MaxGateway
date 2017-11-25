#!/usr/bin/env python

import cgi
import cgitb
import requests
import json

cgitb.enable()

ip_powerswitch1 = "192.168.33.7"

# print header
print "Content-type: text/plain\n"

form = cgi.FieldStorage()

if form.has_key("tool"):
    tool = form.getvalue('tool') 
    if tool == "PS":
        if form.has_key("cmd"):
            cmd = form.getvalue("cmd")
            if cmd == "get":
                r = requests.get("http://" + ip_powerswitch1 + "/?cmd=511")
                #print r.json()
                print r.json()['data']['watt'][0]
                print r.json()['data']['watt'][1]
                print r.json()['data']['watt'][2]
                print r.json()['data']['watt'][3]
                print r.json()['data']['watt'][4]
                print r.json()['data']['watt'][5]
                print r.json()['data']['switch'][0]
                print r.json()['data']['switch'][1]
                print r.json()['data']['switch'][2]
                print r.json()['data']['switch'][3]
                print r.json()['data']['switch'][4]
                print r.json()['data']['switch'][5]
            elif cmd == "set":
                if form.has_key("port"):
                    port = form.getvalue("port")
                    r = requests.get('http://' + ip_powerswitch1 + '/?cmd=200&json={"port":' + port + ',"state":1}')
                    print "OK"
                else:
                    print "NO PORT DEFINED"                
            elif cmd == "reset":
                if form.has_key("port"):
                    port = form.getvalue("port")
                    r = requests.get('http://' + ip_powerswitch1 + '/?cmd=200&json={"port":' + port + ',"state":0}')
                    print "OK"
                else:
                    print "NO PORT DEFINED" 
            else:
                print "ILLEGAL CMD"
    else:
        print "ILLEGAL TOOL"
else:
    print "NO TOOL DEFINED"
#print "END"
