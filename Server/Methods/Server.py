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

        #Inits a list of clients to broadcast messages to.
        self.client_list = []

        """
        Main Loop
        """
        while True: 
 
            """Accepts a connection request and stores two parameters, 
            conn which is a socket object for that user, and addr 
            which contains the IP address of the client that just 
            connected"""
            conn, addr = self.server.accept() 
        
            """Maintains a list of clients for ease of broadcasting 
            a message to all available people in the chatroom"""
            self.client_list.append(conn) 
        
            # prints the address of the user that just connected 
            print (addr[0] + " connected")
        
            # creates and individual thread for every user 
            # that connects 
            self.start_new_thread(self.clientthread,(conn,addr))    

    def clientthread(self, conn, addr):
            
        # sends a message to the client whose user object is conn 
        conn.send("Welcome to this chatroom!") 
 
        while True: 
                try: 
                    message = conn.recv(2048) 
                    if message: 
    
                        """prints the message and address of the 
                        user who just sent the message on the server 
                        terminal"""
                        print ("<" + addr[0] + "> " + message) 
    
                        # Calls broadcast function to send message to all 
                        message_to_send = "<" + addr[0] + "> " + message 
                        broadcast(message_to_send, conn) 
    
                    else: 
                        """message may have no content if the connection 
                        is broken, in this case we remove the connection"""
                        remove(conn) 
    
                except: 
                    continue

    def broadcast(self, message, connection):
            for self.clients in self.client_list:
               if self.clients != connection:
                    try: 
                       self.clients.send(message)
                    except:
                        self.clients.close()
                        remove(self.clients)

    def remove(self, connection):
         if connection in self.client_list:
              self.client_list.remove(connection)


        