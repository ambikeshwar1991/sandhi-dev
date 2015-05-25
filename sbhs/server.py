import argparse
import json
import operator
import SocketServer
import traceback
import threading
import yaml
 
from time import strftime, localtime
 
class MyTCPServer(SocketServer.ThreadingTCPServer):
    allow_reuse_address = True
 
class MyTCPServerHandler(SocketServer.BaseRequestHandler):
    def handle(self):
 
        response_template = '''HTTP/1.1 200 OK
Content-Type: text/plain
Access-Control-Allow-Origin: *\r\n\r\n%s
        '''
 
        try:
            # Handle HTTP Requests
            data = self.request.recv(2048).strip()
            print "Data_json", data
            # Extract content
            json_data = json.loads(data.split('\r\n\r\n')[-1])
            # Get response
            print "json data\n",json_data
            key = str(json_data).strip("u")
            key = key.strip("}")
            key = key.strip("{")
            key = key.split(",")
            key1 = key[0].split(":")
            heat = key1[1]
            key2 = key[1].split(":")
            fan = key2[1]
            print "Heat value\n",heat
            sm = int(heat) + int(fan)

            print "value of fan\n",fan
            #Myclass.val(self)
            response = str(sm)
 
        except Exception, e:
            print "Exception while receiving message: ",e
            traceback.print_exc()
            response = {"err": "invalid message format"}
# 
        finally:
            # send back response
            response = response_template%(str(response))
            print "Response ", response
 
            '''
            # For checking Performance
            self.server.c.prnt(("Performance output "),'r')
            self.server.c.prnt((self.server.h.heap()),'g')
            '''
            self.request.sendall(response)
 
 
if __name__ == "__main__":
 
    # Init Variables
    server = MyTCPServer(('127.0.0.1', 13333), MyTCPServerHandler)
 
    print "server running"
    server.serve_forever()
 
    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
 
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    server.shutdown()
