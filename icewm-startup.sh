#!/bin/sh

if [ ! -d ~/.icewm ] ; then
	mkdir -p ~/.icewm
	install -m 644 /etc/X11/icewm/{keys,menu,preferences,programs,restart,toolbar,winoptions} ~/.icewm/
	echo "`which icewmbg` &" > ~/.icewm/startup
	chmod +x ~/.icewm/startup
fi
