from socket import *
#key words#
#1st opening = ["hello","greetings","howdy"]
#2nd rebuttal = ["how are you","y'all","everybody"]

serverName = "localhost"
serverPort = 42069
message = ""
done = 0
reset = 0

while not done:
    
    clientSock = socket(AF_INET, SOCK_STREAM)
    
    print ("Establishing connection with server")
    clientSock.connect((serverName, serverPort))

    message = input("Enter one of the key words:\n")


    while 1:


        print("Sending message ", message, " to server")
        clientSock.send(message.encode())
        rcvdMessage, serverAddress = clientSock.recvfrom(2048)
        print (rcvdMessage.decode())

        reset = input("enter 0 to keep inputing or 1 to quit\n")
        reset = int(reset)
        if not reset:
            break
        else:
            done = 1
            break

    clientSock.close()
