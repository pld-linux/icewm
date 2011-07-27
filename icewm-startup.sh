#!/bin/sh

if [ ! -d ~/.icewm ] ; then
	mkdir -p ~/.icewm
	install -m 644 /etc/X11/icewm/* ~/.icewm/
fi
