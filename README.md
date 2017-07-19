<h1 align="center"> Fallout 4 Hacking Mini-game Solver </h1>
<img src="https://vignette2.wikia.nocookie.net/fallout/images/e/ec/Fo4_Hacker.png/revision/latest?cb=20170320162306" alt="Fallout Hack Perks" align="middle">

<p align="center"> Pure Python script that helps you to hack Fallout 4 terminal fast and efficiently, <br>by using custom algorithms to find the true answer within 4 allocated attempts. </p>

---

<h1 align="center"> Inspiration </h1>
What inspires me is that when I played Fallout 4 game, and the riddles just get harder than my brain to hack a terminal. <br>
So, I create python program to find the answer to the riddles and gets the loots behind the locked door.

![Hacking Terminal from Fallout 4](http://cdn.gamer-network.net/2015/usgamer/f4_lock_01.jpg)

---
<h1 align="center">Basic Requirements</h1>
<h3 align="center">Python 3 and above (work best with <a href="https://www.python.org/downloads/">Python 3.6</a>)</h3>
You can check if your computer has Python or not by using `python3` or `py -3` on your Terminal (UNIX-based OS), Command Prompt, Windows PowerShell (Windows OS)

<h3 align="center">(Optional) Latest version of this program (Requires Git)</h3>
You can check if your computer has the latest version of program by editing `configurations.py` and toggle `auto_update` to "True"

---

<h1 align="center">  How to use </h1>
Interface will tell you what you can do and what to do. Don't worry.

Start the program with `python3 core.py` for UNIX based OS or `py -3 core.py` for Windows OS
1. Start typing up all the possible answers (all the possible answer) one-by-one.
2. Program will shows all the vocabulary that you have typed in Vocabulary List.
3. If you want to edit the vocabulary, type `/edit <word that you want to change> <word that you want to be>` ie. `/edit test desk`
4. After you  input all the possible word, press ENTER to continue
5. Program will start finding relationships to the wording, and showing you the most possible answers in Recommended
6. Choose one from recommend or vocabulary list, and tell the program that you chose what word, and ends up with how much likeness
7. Program will eliminate the word that does not follow the rule, and show the one that does.
8. Repeat until you have solved the answer. If you have the answer correctly, press ENTER while the program asks for next word selection.

If you have any issues or troubleshoot, please check out the wiki

---

<h1 align="center">  How does it work </h1>
Program will count on how many characters relationships to others. That relationships that we have found helps you to find the answer swiftly by eliminating lone-wolf passwords and grouping passwords

<h3 align="center">Test run on how it works </h3>
If the answer is "SENT", this is how the program will eliminate the word list. And use the word "SHOT" as a first guess.

|Initial Input|Recommend<br>before tries #1|Recommend<br>before tries #2|Recommend<br>before tries #3|
|:-----------------:|:------------:|:------------:|:------------:|
|**s**hot <br> hurt <br> **s**ell <br> give <br> **s**ure <br> gear <br> **s**ent <br> fire <br> glow <br> week <br> ones <br> sick|**s**hot <br> **s**ell <br> **s**ure <br> **s**ent <br> **s**ick <br> |**s**en**t**|-|

Program will change recommended words everytime it finds a significant changes (like finding 0 likeness answer)

---

<h1 align="center">Testing Environment </h1>
During test run of the program, maximum word sample size is 11 characters long (Expert level Terminal) is used. Algorithms can find true answer within 4 attempts, with most of the time with 2 and 3 attempts.

Testing continues, as they have been tested with a varieties of strings length, like 8-length words. They are able to calculate the possibilities very efficiently and mostly, within 4 attempts.

---

<h1 align="center">Future Developments </h1>
I have an idea on making this thing to be more user-friendly, but still based on Terminal like to let you feel more immersive with the game.

1. Visualizing the relationships between words
2. Adaptive terminal size

---

<h1 align="center"> Project Checker </h1>
This is an automatic program checker. <br>Please take a look before cloning or doing something else, just for the program build strength.

|<img src="https://travis-ci.com/images/logos/TravisCI-Mascot-1.png" height="75px"> <br> TravisCI<br>Build Issues|<img src="https://pbs.twimg.com/profile_images/796423844663853056/WsR0OEAZ.jpg" height="75px">  <br> Codacy<br>Build Quality|
|:--------------------:|:--------------------:|
|Master branch<br>[![TravisCI](https://travis-ci.org/sagelga/Fallout-4_Hacking_Helper.svg?branch=master)](https://travis-ci.org/sagelga/Fallout-4_Hacking_Helper)|Master branch<br>[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f771095c4b29457abd2395d0a29d164f)](https://www.codacy.com/app/sagelga/Fallout-4_Hacking_Helper?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sagelga/Fallout-4_Hacking_Helper&amp;utm_campaign=Badge_Grade)|

---

### I hoped you like the project!

![](https://vignette2.wikia.nocookie.net/fallout/images/1/13/RobCos_Worst_Nightmare_trophy.png/revision/latest?cb=20170618215901)

-- Crafted with love by [@sagelga](github.com/sagelga) and with help from [@ntsd](github.com/ntsd) and [@kinisan](github.com/kinisan)

---

<p align="center">Fallout 4, Vault Boy and Fallout Franchise is a part of Bethesda Software LLC. <br>This software does not related or created for commercial use or a part of Fallout Franchise.<br><br>All photos and related pictures from Internet is copyright by its publishers. <br>Please see legal terms for more information.<p>
