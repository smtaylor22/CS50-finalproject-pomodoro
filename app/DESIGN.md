I created this application as a flask web app. The main reason for this was
so I could run a timer on the front end but then record data on the backend on 
my server. 

I took the same source code that was given form pset8 from when we learned about
about flask webapps. I removed and changed features that of course were not necessary
to my webapp. All the backend logic is run through python. 

I built several html pages to display the timer and the dashboard or overview of 
the users logged entries. The framework I used to build these webpages was 
bootstrap. 

For index.html I wanted to display a simple countdown timer. To display the 
countdown timer I created a separate file for my javascript called
countdown.js. It is stored in the folder named static I did this because the javascript was long enough that it looked
cleaner to have it in a separate file. All the logic and functionality for the countdown timer is 
in there. I created one main function called function timer(). This function
starts the timer and triggers other functions necessary for the countdown. 

I used the javascript timer function called setInterval to run the timer and then
did some math calculations the countdown. The time the user entered is minutes
so I turn that time into seconds to work with set interval. 

I wanted the timer to display with two digits in each column. I created
Conver_time to do this. I first converted time into minutes and seconds and
then concatinated those two variables. I also wanted there to be a zero 
in front of the digit if it was a single digit. 

When the countdown is done it sounds an alarm and tells you its time for a break.
It also then resets the timer. 

I created a function to change the start button to say paused after its clicked. 
This keeps things clean and simple. The Reset button I designed to return 
the timer to default values with out reloading the webpage. 

I created a database with two tables. One to store users and their passwords and
another to store logged timer data. 
When an timer is started I have the data submitted via post to my server. 
I then record the timer data into the history1 database. I have not created any alerts 
to enforce the user to input data into the Title and Description fields. If not data is entered it 
is simply left blank. It isn't necessary to use the timer feature. 

I created Dashboard to display the most important data for users. I used Django
to loop through the dictionary I passed from my server to display the info 
in the table. When using the pomodoro technique many people like to keep track of how many pomodoros 
they have completed so I have displayed that as well then as how much time the add up 
to. I display when the user started working and how long their interval was.
I also created a function in helpers.py that converted the start time from 
24 hour time to 12 hour time. 




