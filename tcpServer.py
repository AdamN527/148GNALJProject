import time 
import random

opening = ["hello","greetings","howdy"]
rebuttal = ["how are you","y'all","everybody"]

place = 0 #keep track of whether looking for initial input or rebuttal

previous_state = ""
rollbacknum = 0
run = 1
exp = ""

def listener(v):

    check = guesser(v)
    
    return check

def guesser(val):
	global place,previous_state,rollbacknum,exp
	previous_state = val
	if place == 0:
		a = random.randint(0,(len(opening)-1))
		exp = opening[a]
		if val == opening[a]:        
			place = 1
			return 1
		else:
			time.sleep(2) #will stall for 2 seconds if input is incorrect simulating a revert back then commiting to the action actually used
			rollbacknum += 1
			place = 1
			return 0
            


	if place == 1:
		a = random.randint(0,(len(rebuttal)-1))
		exp = rebuttal[a]
		if val == rebuttal[a]:
			place = 0
			return 1
		else:

			time.sleep(2) #will stall for 2 seconds if input is incorrect simulating a revert back then commiting to the action actually used

			rollbacknum += 1
			place = 0
			return 0



from socket import *
serverPort = 42069
serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', serverPort))
serverSock.listen(1)
print ("The server is ready to receive")
while True:
	while run:
		clientSock, addr = serverSock.accept()
		message = clientSock.recv(2048)
		recdMessage = message.decode()
	
		x = listener(recdMessage)

		if not place :
			if x:
				clientSock.send("No roll back required!\n".encode())
				clientSock.send("expected: ".encode())
				clientSock.send(exp.encode())
				clientSock.send("\nrecieved: ".encode())
				clientSock.send(message)
			else:
				clientSock.send("we must go back\n".encode())
				clientSock.send("expected: ".encode())
				clientSock.send(exp.encode())
				clientSock.send("\nrecieved: ".encode())
				clientSock.send(message)


		elif place :
			if x :
				clientSock.send("No roll back required!\n".encode())
				clientSock.send("expected: ".encode())
				clientSock.send(exp.encode())
				clientSock.send("\nrecieved: ".encode())
				clientSock.send(message)
			else:
				clientSock.send("we must go back\n".encode())
				clientSock.send("expected: ".encode())
				clientSock.send(exp.encode())
				clientSock.send("\nrecieved: ".encode())
				clientSock.send(message)
		z=str(place)
		clientSock.send("\nyou are in loop ".encode())
		clientSock.send(z.encode())
		clientSock.send("\nyou have reverted back ".encode())
		z=str(rollbacknum)
		clientSock.send(z.encode())
		clientSock.send(" amount of times\n ".encode())

	serverSock.close()
		
