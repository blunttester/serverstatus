serverstatus
============

A small python -based program that reads the current status of the
server (CPU -usage, memory etc) in common or by given application and
writes the information to the destination (file, streaming server,
localhost website, db). Requires linux OS (tested on Ubuntu) and 
Python 2.7 (tested with 2.7.4).

You can start the server in bin -folder by running srvstats.sh -script.
The script launches pyWebSite.py -file and gets two (2) different web services
up on localhost ports 8880 & 8888.

The site http://localhost:8880 will display information (a HTML -table) 
about 10 most memory consuming processes on the server plus one row information 
about selected process/command (configurable in conf/conf.conf -file).
The site http://localhost:8888 will display one line (JSON -string) with timestamp and 
memory & cpu -usage information about selected process/command (configurable in
conf/conf.conf -file).



