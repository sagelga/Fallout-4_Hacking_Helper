
LOCAL
1/1
master
REMOTE
1/1
origin
master
PULL REQUESTS
0
TAGS
0/0
SUBMODULES
0
README.md
Ignore white space
@@ -1,42 +0,0 @@
# Fallout 4 Hacking Mini-game Solver
![Fallout 4 Hacker Perks](https://vignette2.wikia.nocookie.net/fallout/images/e/ec/Fo4_Hacker.png/revision/latest?cb=20170320162306)

Python script that helps you to hack Fallout 4 terminal fast and efficiently, using custom alorithms to find the true answer within 4 allocated attempts.

# Inspiration
What inspires me is that when I played Fallout 4 game, and the riddles just get harder than ever. <br>
So, I create python program to find the answer to the riddles

![Hacking Terminal from Fallout 4](http://cdn.gamer-network.net/2015/usgamer/f4_lock_01.jpg)

# How to use
Interface will tell you what you can do and what to do. Don't worry.
1. Start typing up all the possible answers (all the possible answer)
2. Press enter continue
3. Program will start finding relationships to the wording, and showing you the most possible answers
4. Choose one, and tell the program that you chose what word, and ends up with how much likeness
5. Repeat until you can find the answer

# How does it work
Program will count on how many characters relationships to others. That relationships that we have found helps you to find the answer swiftly by eliminating lone-wolf passwords and grouping passwords

Program does not store the previous results. Thus, you will need to start it over and do it again.

# Testing Environment
During test run of the program, sample size of the word is 4 characters long (Advanced level Terminal) is used. Algorithms can find true answer within 4 attempts, with most of the time with 3 attempts.

Testing continues, as they have been tested with a longer strings, like 8-length words. They are able to calculate the possibilities very efficiently and mostly, within 4 attempts.

# Future Developments
I have an idea on making this thing to be more user-friendly, but still based on Terminal like to let you feel more immersive with the game.

1. Edit your input words
2. Visualizing the relationships between words
3. Adaptive terminal size
4. Creating vocabulary cache into .txt file

I hoped you like the project!

![](https://vignette2.wikia.nocookie.net/fallout/images/1/13/RobCos_Worst_Nightmare_trophy.png/revision/latest?cb=20170618215901)

-- Crafted with love by [@sagelga](github.com/sagelga) and with help from [@ntsd](github.com/ntsd) 
