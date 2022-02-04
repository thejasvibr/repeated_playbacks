# Instructions to setup the repeated playbacks



## The Parameters file

* Start and stop times should be in 24 hr format HH:MM:SS
* The stop time is always assumed to be after the start time. ie. if the start time is 08:00:00 and stop time is 03:00:00
Then the stop time is assumed to be the *next* day's 03:00:00!
* Playback file: remember to double slash your paths if there is a colon in it
* Playback device: use the number from sounddevice.query_devices() 

## Getting the recurring task setup with Task Scheduler

The current instructions are for a Windows 10 system. 

1. Set the relevant parameters in the ```parameters.txt``` file (start and stop time, playback file, soundcard name)
1. Create a new batch file (a file ending with a .bat)
	1. The first line of your batch file should change working directories to the ```repeated_playback``` folder. The second line should
	call Python from the virtual environment of your choice along with the ```repeated_playback.py``` module
	```
	cd C:\YOURDIRECTORYHERE\repeated_playback
	BASEPATHHERE\anaconda3\envs\YOURENVHERE\pythonw.exe repeated_playback.py
	```
	
1. Open a 'Task Scheduler' instance (type it into the Windows search bar)
1. Click on 'Create Basic Task'
	1. Set the name, frequency ('Trigger' -> 'Daily'-> and then set the time),
	1. Set the Action ('Start a program') and specify more details (in 'Program/script' enter the batch file path)
1. Open the task again in Task Scheduler and check that there are no weird conditions. Make sure only the following are enabled.
	1. In the 'General' tab, check 'Run whether user is logged on or not' and 'Do not store password...'
	1. In the 'Conditions' tab, check 'Wake the computer to run this task'
	1. In the 'Settings' tab, check on 'Allow the task to be run on demand' (for testing) and 'If the running task does not end when requested...'
