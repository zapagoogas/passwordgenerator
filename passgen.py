#-----------------------------------------------------------------------------------------------------------------------
# Author: Nick McGee                                                                                                   |
# Purpose: To generate a random password using lists of predefined words                                               |
# Date: 7/26/2022                                                                                                      |
# Contact: ndmcgee2004@gmail.com                                                                                       |
#-----------------------------------------------------------------------------------------------------------------------

import random

# Index of the words used in the password
wordOneIndex = ['Arrogant', 'Bewildered','Complicated','Defamation','Eclectic','Fanatic','Grandious','Hornswoggled','Introverted','Jetlagged','Keystone','Lampoon','Marvelous','Engineered'  ]
wordTwoIndex = ['Beaver','Seashell','Carrot','Weasel','Beaches','Interface','Novel','Script','Spray','Design','Field','Hippo','Martyr','Misnomer' ]
# index of numbers and symbols used in the password
numIndex = list(range(1024))
symIndex = ['!','@','#','$','%','^','&','*','(',')']

#asking user for confirmation on password generation, if no program exits
q = input("Would you like to generate a password? Y/N\n")
if q == 'Y' or 'y':
    # shuffles the data in the lists so the passwords are randomly generated
    random.shuffle(wordOneIndex)
    random.shuffle(wordTwoIndex)
    random.shuffle(numIndex)
    random.shuffle(symIndex)
    # choosing which specific items in the list to use, choosing every prime because it makes me look smarter than i am
    passOut = wordOneIndex[0], wordTwoIndex[3],numIndex[5],symIndex[7]
    # this was confusing at first, but using the splat operator displays what was the list in a string form. sep is the seperation between the printed values
    print( "Your password is: ", *passOut, sep="")

else:
    quit




