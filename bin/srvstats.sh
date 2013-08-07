#!/bin/sh
echo "Welcome to srvstats!"
echo "Script starts up web service"
echo "on ports:" 
echo "8880 (for top information in HTML-table)" 
echo "8888 (for application specific CPU information printed out per request as json -string)"

../src/pyWebSite.py 1>&2
