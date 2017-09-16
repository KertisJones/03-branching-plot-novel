#!/Library/Frameworks/Python.framework/Versions/3.6/bin

import sys
import random

assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'



whoCount = 0
whoRequired = 5
whoAsk = False
whoName = False

userInput = ""

actors = {
		"My name is 'Sir Lancelot of Camelot'" : "John Cleese",
		"'Sir Robin of Camelot'" : "Eric Idle",
		"'Sir Galahad of Camelot'" : "Michael Palin",
		"It is 'Arthur', King of the Britons." : "Graham Chapman",
	}

print ("""


/////////////////////////////////
/////////////////////////////////
INSERTTOKENINSERTTOKENINSERTTOKEN
/////////////////////////////////
/////////////////////////////////
""")

while (not ("y" in userInput)):
    userInput = input("INSERT TOKEN? ")


print ("")
print ("    ----------LOADING----------    ")
print ("")

def startWhosOnFirst():
        global whoCount
        global whoAsk
        global whoName
        global whosOnSecond
        whoCount = 0
        whoAsk = False
        whoName = False
        whosOnSecond = False
        print("""

Strange as it may seem, they give ball players nowadays very peculiar names.

[1] Funny names?
[2] Give them names?
        
        """)
        
        userInput = input("~ ")
        if (userInput != "1" and userInput != "2"):
                startWhosOnFirst()
        else:
                print("""

Nicknames, nicknames. Now, on the St. Louis team we have Who's on first,
What's on second, I Don't Know is on third--
                
[1] That's what I want to find out. I want you to tell me the names of the
        fellows on the St. Louis team.

                """)
                userInput = input("~ ")
                if (userInput != "1"):
                        startWhosOnFirst()
                else:
                        print("""

I'm telling you. Who's on first, What's on second, I Don't Know is on
third--

[1] You know the fellows' names?
[2] Well then who's playing on first?
[3] I mean the fellow's name on first base.
[4] The fellow playin' first base.

                        """)
                        userInput = input("~ ")
                        if (userInput == "1" or userInput == "2"):
                                print("""

                                Yes.

                                """)
                                who()
                        elif (userInput == "3" or userInput == "4"):
                                print("""

                                Who.

                                """)
                                who()
                        else:
                                startWhosOnFirst()

def who():
        global whoCount
        global whoAsk
        global whoName
        
        whoCount += 1
        print("""
[1] You know the fellows' names?
[2] Well then who's playing on first?
[3] I mean the fellow's name on first base.
[4] The fellow playin' first base.
[5] The guy on first base.""")
        if (whoCount >= whoRequired):
                print("[6] Well, what are you askin' me for?")
        if (whoAsk):
                print("[7] I'm asking you--who's on first?")
        if (whoName):
                print("[8] That's who's name?")
                
        print("")
        userInput = input("~ ")
        if (userInput == "1" or userInput == "2"):
                print("""

Yes.

                """)
                who()
        elif (userInput == "3" or userInput == "4"):
                print("""

Who.

                """)
                who()
        elif (userInput == "5"):
                print("""

Who is on first.

                """)
                who()
        elif (userInput == "6" and whoCount >= whoRequired):
                print("""

I'm not asking you--I'm telling you. Who is on first.

                """)
                whoAsk = True
                who()
        elif (userInput == "7" and whoAsk):
                print("""

That's the man's name.

                """)
                whoName = True
                who()
        elif (userInput == "8" and whoName):
                print("""

Yes.


[1] When you pay off the first baseman every month, who gets the money?

                """)
                userInput = input("~ ")
                if (userInput != "1"):
                        who()
                        print("""


                        """)
                else:
                        print("""

Every dollar of it. And why not, the man's entitled to it.

                        """)
                        whoPay()
        else:
                whoCount -= 1
                who()

whosOnSecond = False
def whoPay():
        global whosOnSecond
        print("""
[1] Who is?
[2] So who gets it?
[3] Who does?
[4] Well, all I'm trying to find out is what's the guy's name on first base?""")
        if (whosOnSecond):
                print("[5] I'm not asking you who's on second.")
                
        print("")
        userInput = input("~ ")
        if (userInput == "1"):
                print("""

Yes.

                """)
                whoPay()
        elif (userInput == "2"):
                print("""

Why shouldn't he? Sometimes his wife comes down and collects it.

                """)
                whoPay()
        elif (userInput == "3"):
                print("""

Yes. After all, the man earns it.

                """)
                whoPay()
        elif (userInput == "4"):
                print("""

Oh, no, no. What is on second base.

                """)
                whosOnSecond = True
                whoPay()
        elif (userInput == "5" and whosOnSecond):
                print("""

Who's on first!

                """)
                #whoPay()
        else:
                whoPay()
#--------------------------------------------------------------

def startBridgekeeper():
        print("""

Stop! He who approacheth the Bridge of Death must answer me these questions
        three, ere the other side he see.

[1] Ask me the questions, bridgekeeper. I am not afraid.
[2] Ask me the questions, bridgekeeper. I'm... not afraid.
[3] I am prepared for your questions, bridgekeeper.
[4] I am King of the Britons, I shall face your trial.

""")
        userInput = input ("~ ")
        if (userInput == "1"):
                question1("My name is 'Sir Lancelot of Camelot'")
        elif (userInput == "2"):
                question1("'Sir Robin of Camelot'")
        elif (userInput == "3"):
                question1("'Sir Galahad of Camelot'")
        elif (userInput == "4"):
                question1("It is 'Arthur', King of the Britons.")
        else:
                startBridgekeeper()
 
def question1(name):
        print ("")
        print ("")
        print ("What... is your name?")
        print ("")
        print ("[1] " + name)
        print ("[2] My name is " + actors.get(name))
        print ("")

        userInput = input ("~ ")
        if (userInput == "1"):
                question2()
        elif (userInput == "2"):
                actor()
        else:
                question1(name)
        
def actor():
        print ("""

Is that so? Have you heard of Abbott and Costello?

[1] I'm a fan.
[2] Can't say I have.

        """)
        userInput = input ("~ ")
        if (userInput == "1"):
                print ("""

Fantastic! Boy do I have something for you. Look at this!

---------------------------------------------------------------------

                """)
                startWhosOnFirst()
        elif (userInput == "2"):
                print ("""

HOW DARE YOU! INTO THE GORGE OF ETERNAL PERIL WITH YOU!

                """)
        else:
                actor()

def question2():
        print ("""

What is your quest?

[1] To seek the Holy Grail.
[2] I seek the Grail.
[3] I quest for Camelot!
[4] I search for... a shrubbery!

        """)
        userInput = input ("~ ")
        if (userInput == "1" or userInput == "2"):
                question3()
        elif (userInput == "3"):
                print("")
                print("You shall not go to Camelot, tis a silly place.")
                print("Instead, you shall enter the Gorge of Eternal Peril. Goodbye.")
                print("")
        elif (userInput == "4"):
                print("")
                print("Ni!")
                print("")
        else:
                question2()

def question3():
        ranNum = random.randint(1, 3)
        if (ranNum == 1):
                color()
        elif (ranNum == 2):
                assyria()
        elif (ranNum == 3):
                swallow()
        else:
                color()
                    
def color():
        print ("""

What... is your favorite color?!?

[1] Blue.
[2] Red.
[3] Green.
[4] Blue. No, yellow!

        """)
        userInput = input ("~ ")
        if (userInput == "1" or userInput == "2" or userInput == "3"):
                print("")
                print("Congratulations, you may pass.")
                print("")
        elif (userInput == "4"):
                print("")
                print("'Blue. No, yel-- AUUUUUUUUUUGH!")
                print("")
        else:
                color()

def assyria():
        print ("""

What... is is the capital of Assyria?

[1] I don't know that!
[2] Aššur.
[3] Nineveh.
[4] Miletus.
[5] Syracuse?
[6] Abydos?
[7] Plovdiv!
[8] I got it... Kentucky!

        """)
        userInput = input ("~ ")
        if (userInput == "2" or userInput == "3"): #both Aššur and Nineveh have been capitals.
                print("")
                print("Congratulations, you may pass.")
                print("")
        else:
                print("")
                print("'AUUUUUUUUUUGH!")
                print("")
                      
def swallow():
        print ("""

What... is the air-speed velocity of an unladen swallow?

[1] What do you mean? An African or European swallow?
[2] I haven't a clue.
[3] 461 miles an hour!
[4] Coconuts.

        """)
        userInput = input ("~ ")
        if (userInput == "1"):
                print("")
                print("Huh? I-- I don't know that. Auuuuuuuugh!")
                print("Congratulations, you may pass.")
                print("")
        else:
                print("")
                print("Death to those who fail my test!")
                print("")
                

playGame = True

while playGame:
        whoCount = 0
        whoAsk = False
        whoName = False
        whosOnSecond = False
        
        startBridgekeeper()
        print("""

        --------------------------------------------------
                                 FIN
        --------------------------------------------------

Would you like to play again?

        """)
        userInput = input("~ ")
        if (not ("y" in userInput)):
                playGame = False



"""
def decode_response(user_input):
	return user_input


exit_game = False


while not exit_game:
	print('It was a dark and stormy night…')
	print("[1] Interrupt Snoopy's writing session")
	print('[2] Ask Mrs. Who what a tesseract means')
	print('[3] Research the life of Edward Bulwer-Lytton')
	user_input = decode_response(input('What do you choose (q to quit)? '))
	if user_input == 'q':
		exit_game = True
"""
