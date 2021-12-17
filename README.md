# 148GNALJProject

CMPE-148 Project:

Offline simulation

For the offline simulation, the user must be able to run programs from python. When running the program, the console will wait to accept any response. 
It will randomly pick a greeting from the list of greetings. If the user matches the expected greeting, the client will not roll back. Otherwise, it would go back to the
previous state and take the input as was provided (also show what was expected to be input). 

Server simulation

This simulation works similar (you start up ther server and client), the server is expecting an output, the user types in their response (in the client line) 
which if it is contained in the key words and is selected; therewill be no rollback. Otherwise, if the server was not expecting 
the response it would go back to the previous state and take the actual input
( in a game this would be perceived lag and would cause a delay for the next input due to correcting for the previous input).

* There is no end case so a kill signal will need to be sent. In some cases such as Linux distributions this can be done using CNTRL + C *
