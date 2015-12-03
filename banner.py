import os

import time
from termcolor import colored, cprint

#the width of the display
WIDTH = 80

#the message to print
message = "hotline bling".upper()
#the printed banner version of the message
#this is a 7-line display, stored as 7 strings
#initially, these are empty.
printedMessage = [ "","","","","","","" ]

#a dictionary mapping letters to their 7-line
#banner display equivalents. each letter in the dictionary
#maps to 7 strings, one for each line of the display.
characters = { " " : [ " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " " ],
               "E" : [ "******",
                       "*     ",
                       "*     ",
                       "******",
                       "*     ",
                       "*     ",
                       "******" ],

               "O" : [ "******",
                       "*    *",
                       "*    *",
                       "*    *",
                       "*    *",
                       "*    *",
                       "******" ],

               "H" : [ "*    *",
                       "*    *",
                       "*    *",
                       "******",
                       "*    *",
                       "*    *",
                       "*    *" ],

               "T" : [ "******",
                       "   *  ",
                       "   *  ",
                       "   *  ",
                       "   *  ",
                       "   *  ",
                       "   *  " ],

               "L" : [ "*     ",
                       "*     ",
                       "*     ",
                       "*     ",
                       "*     ",
                       "*     ",
                       "******" ],

               "N" : [ "* *    *",
                       "*  *   *",
                       "*   *  *",
                       "*   *  *",
                       "*   *  *",
                       "*    * *",
                       "*      *" ],

                "B" : [ "***** ",
                        "*    *",
                        "*    *",
                        "****  ",
                        "*    *",
                        "*    *",
                        "***** " ],

                "G" : [ "******",
                        "*     ",
                        "*     ",
                        "*     ",
                        "*  ***",
                        "*    *",
                        "******" ],

                   "I" : [ "******",
                           "   *  ",
                           "   *  ",
                           "   *  ",
                           "   *  ",
                           "   *  ",
                           "******" ]

               }

#build up the printed banner. to do this, the 1st row of the
#display is created for each character in the message, followed by
#the second line, etc..
for row in range(7):
    for char in message:
        printedMessage[row] += (str(characters[char][row]) + "  ")

#the offset is how far to the right we want to print the message.
#initially, we want to print the message just off the display.
offset = WIDTH
while True:
    os.system("clear")
    #print each line of the message, including the offset.
    for row in range(7):
        cprint(" " * offset + printedMessage[row][max(0,offset*-1):WIDTH - offset], 'white', 'on_magenta', attrs=['bold'])
    #move the message a little to the left.
    offset -=1
    #if the entire message has moved 'through' the display then
    #clear and quit
    if offset <= ((len(message)+5)*6) * -1:
        #offset = WIDTH     #UNCOMMENT THIS LINE AND REMOVE THE TWO BELOW TO KEEP SCROLLING/RESTART 
        os.system("clear")
        quit()
    #take out or change this line to speed up / slow down the display
    time.sleep(.05)
