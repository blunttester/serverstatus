serverstatus
============

A small python -based program that reads the current status of the
server (CPU -usage, memory etc) in common or by given application and
writes the information to the destination (file, streaming server,
localhost website, db). Requires OSX or linux OS (tested on OSX Mountain Lion and Ubuntu) and 
Python 2.7 (tested with 2.7.4). NOTE: on linux you'll need to modify pySrvStats.py -file
in order to get the data fetched properly from the system.

You can start the server in bin -folder by running srvstats.sh -script.
The script launches pyWebSite.py -file and gets 3 different web services
up on localhost ports 8780, 8788 & 8789.

The site http://localhost:8780 will display information (a HTML -table) 
about 10 most memory consuming processes on the server plus one row information 
about selected process/command (configurable in conf/conf.conf -file).

The site http://localhost:8788 will display one line (JSON -string) with timestamp and 
memory & cpu -usage information about selected process/command (configurable in
conf/conf.conf -file).

The site http://localhost:8789 will display one line with application name and 
memory, cpu & thread -usage information about selected process/command (configurable in
conf/conf.conf -file).


