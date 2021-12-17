import random
import time

opening = ["hello","greetings","howdy"]
rebuttal = ["how are you","y'all","everybody"]

place = 0 #keep track of whether looking for initial input or rebuttal

previous_state = ""
rollbacknum = 0


def listener():
    if place == 0: v = input("enter a greeting: \n")

    if place == 1: v = input("enter a rebuttal: \n")

    guesser(v)
    print("you have reverted back ",rollbacknum," amount of times\n")

    return 0

def guesser(val):
    global place,previous_state,rollbacknum
    previous_state = val
    if place == 0:
        a = random.randint(0,(len(opening)-1))
        if val == opening[a]:
            
            print("No roll back required!\n")
            print("expected: ",opening[a])
            print("\nrecieved: ", val)
            place = 1
            return
        else:
            print("we must go back\n")
            print("expected: ",opening[a])
            time.sleep(2) #will stall for 2 seconds if input is incorrect simulating a revert back then commiting to the action actually used
            print("\nrecieved: ", val)
            rollbacknum += 1
            place = 1
            return
            


    if place == 1:
        a = random.randint(0,(len(rebuttal)-1))
        if val == rebuttal[a]:
            print("No roll back required!\n")#guessed correctly continue on without reverting back
            print("expected: ",rebuttal[a])
            print("\nrecieved: ", val)
            place = 0
            return
        else:
            print("we must go back\n")#revert back to previous state and run normally (would revert back to previous state and run original command)
            print("expected: ",rebuttal[a])
            time.sleep(2) #will stall for 2 seconds if input is incorrect simulating a revert back then commiting to the action actually used
            print("\nrecieved: ", val)
            rollbacknum += 1
            place = 0
            return


while 1:
    listener()
