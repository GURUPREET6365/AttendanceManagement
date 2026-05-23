I was preparing for IIT JEE examination in class 11th and 12th.
And compulsorily, I had to go coaching and school both daily, so I struggles lot in time management.
So I decided to take leave from school, because school is not ready to give me leave based on my preparation.
I started taking leaves, and even without informing them, and the major problem is fine, they take fine from the absentees, and I don't know how many days I took leave.

So, I got the Idea that why don't write a program to manage my attendance for both coaching and school.

project starting date: 3 may 2026

version 1:
I built the minimal version of this, by integrating the sqlalchemy, alembic and postgresql, for easy data management.
Firstly, I built this in terminal.
Wrote a class having functions for marking the school and coaching attendance.

problem 1:
The problem I faced here that The function that I made having the problem that I mark attendance twice for coaching and school both and even for one attendance, two rows created.

solution 1:
I solved this problem by removing three function. I removed individual school and coaching attendance marking function and that's exisiting check, and created a date of attendance, where I am checking todays exisiting attendance and created another function which are taking both school and coaching status and marked together.


problem 2:
now it is working and I started running the program, but the problem is, I want to automate it by schedule the python program. I setup that, but the problem is, I was directly editing the file to run, now I want to make that terminal will ask about the status when I run the program.

solution 2:
I used task scheduler, where I automated It by running the windows task scheduler, and run the program using .bat file at the startup of the system.


problem 3:
I faced the problem that it runs also in sunday and the biggest problem is sometime, I forget to open the laptop, then that day attendance is missed.