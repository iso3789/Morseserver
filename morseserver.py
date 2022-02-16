#!/usr/bin/env python3
import socketserver
import sys

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST = "0.0.0.0"
    #Error handling
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + "<port>")
        exit (1)
    port = int(sys.argv[1])

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, port), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
