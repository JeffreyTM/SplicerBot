# SplicerBot
Discord bot coded to add videos to a collection of the best splices to a single location using a command. Prefix is '-'.

Coded in python using replit, a website that hosts public coding projects. Bot is kept on 24/7 by using the web_server class to run whenever the page is pinged, and UptimeRobot to ping the page every 5 minutes.

# What is Splicing
Splicing involves taking a muted video and combining it with audio from an unrelated song and playing them simultaneously to see how they line up.

# Note
This bot will not work when installing from Github, as some commands are tied to my personal Discord ID. This is intended only for personal use. If you have any questions on implementation, feel free to message me.

# Commands
Some stuff here is a WIP. I'm still trying to figure out how best to store the message id so it doesn't have to be included in commands, and I want to replace -reset with -delete.

-setup: Sets up the initial message, introducing the Splicing Hall of Fame.

-id (message id): Creates a message that displays the format for adding splices and gives the user the message id, which is also used for adding splices.

-add (message id, video link, audio link): Edits the previous message created and adds the splice with the video and audio links. 

-reset (message id, arg): Resets the entire list of splices, used when someone creates a faulty add. The parameter 'arg' can be used to edit the message to include everything except the faulty add.


