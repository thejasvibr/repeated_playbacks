# Instructions to setup the repeated playbacks

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
	1. In the 'Conditions' tab, 'Wake the computer to run this task'
	1. In the 'Setting' tab, check on 'Allow the task to be run on demand' (for testing) and 'If the running task does not end when requested...'
	1. 