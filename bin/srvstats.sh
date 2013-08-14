#!/bin/sh
echo "Welcome to srvstats!"
echo "Script starts up web service"
echo "on ports:" 
echo "8780 (for top information in HTML-table)"
echo "8788 (for application specific CPU information printed out per request as json -string)"
echo "8789 (for application specific CPU,MEM & Threads -information printed out per request)"

../src/pyWebSite.py 1>&2
