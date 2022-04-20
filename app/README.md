Documentation for Pomodoro Time Tracker 

Video Walkthrough (watch the second one first)
https://www.youtube.com/watch?v=aro7Crs4MUY&list=PLLYHI6pusiAzBQUkP1Cgq9qcq3iejT21q
I created this as Flask web app. It exists in the CS50 IDE. The application is
enlosed in a folder name "app". Navigate to the directory that you store the folder "app" in. Execute
flask run and open the link given. 

If you are not an existing user, you must click register in the top right hand
corner and create an account and password. You will be navigated to homepage
of the webapp where the timer exists.

If you are an existing user just log in with your password and username. You will be navigated to homepage
of the webapp where the timer exists.

How to Use Pomodoro Time Tracker
The Pomodoro technique is based off of setting an interval and working during
that set time usually about 25min. It's a technique used to help beat procrastination.
You can tell yourself that you will work for 25 min and then take a break.
After the end of your set timer, take a short break of 5-10 min.
After the short break start the next session of 25 min. Repeat as necessary. 

After logging in you will be presented with several fields to enter data.
This is where the tracking capabilities come into play. Here you can keep 
track of what you were working on during your pomodoro session. Enter the 
title of the project your working on and a specefic description of what you are 
doing. This is optional. It is not required to enter names for these. They can be 
left blank.

There are also several buttons to start or reset the timer. After you have inputed
your desired session length (i.e. 25min) click start. If you would like to pause
your session click the pause button. If you would like to totally stop and reset
your interval click the reset button. 

Work until the timer ends. After it ends take the break. Enter a time of 5 or 10 min.
After the break enter your session length and click start to begin your timer again. 

You can also view a log of your past Pomodoro sessions. Click on "Dashboard" next to 
"Timer" in the top left in the header. You can view the total number
of sessions you have done as well as the the total number of minutes you 
have worked there. Each row gives you info on each session.

The each row in the table underneath represents the data for each pomodoro session.
You can see the Project Title, the Description, the time you started the interval,
and the length of the iterval you did. 

One thing to note, I ran into an issue with sending the data from the for with Post. The way I have
it designed it would need to reload the page. I don't want it to reload the page. My TF told me to look 
into Ajax but I was not able to figure it out. Right now I have it to only work with the countdown timer and 
it doesn't send the info. If I add <form action="/" method="post"> it will send the data. but not the info
