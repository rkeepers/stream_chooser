# Stream Chooser

I created this for use on the Raspberry Pi as there doesn't seem to be a lightweight 
stream player for the Pi that will sit in the tray or background. 

This requires VLC media player to be installed.

Once run, this will kill any running instances of VLC and allow you to select from 
stream source urls that are currently coded in the app. 
It should them begin playing and disappear into the background. 

On the Pi, the stream will continue to play even after the user logs out. 
Resource usage is low and I've left it playing for even a month or more.

TODO: 	find a lighter command line stream player than VLC
	have a separate file to contain the stream URLs
	have stream start playing on keypress
	loop back to selection so that other streams could be selected before exiting.

	
