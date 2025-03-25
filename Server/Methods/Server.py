import socket


class Server:

    def __init__(self, port):

        #Gets the IP address for later usage and sets the port variable.
        self.port = port
        self.hostname = socket.gethostname()
        self.ipaddress = socket.gethostbyname(self.hostname)

        #Initializes Socket to use TCP
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        
        self.server.bind((self.ipaddress, self.port))

        self.server.listen(100)

        #Inits a string for the latest message for usage when the clients grab the latest message.
        self.NewestMessage = ""

    def clientthread(self):
        pass

        