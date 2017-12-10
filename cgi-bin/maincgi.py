#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cgi, cgitb 

import sys
sys.path.insert(0, "./planetoplot/modules")
from ppclass import pp

# for debugging in web browser
cgitb.enable()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# RETRIEVE and PLOT DATA with PPCLASS
fifi = "./data/wrfout_d01_2024-10-04_06z00z00_zabg"
req = pp()
req.file = fifi
req.var = "HGT"
req.x = form.getvalue("x")
req.y = form.getvalue("y")
req.z = form.getvalue("z")
req.t = form.getvalue("t")
req.out = "agg" 
req.filename = "webapp"
req.getplot()


##### NOW WRITE THE HTML PAGE TO USER
print "Content-type:text/html;charset=utf-8\n"
print     #Apache needs a space after content-type
header="""<html><head><title>Mars Climate Database: The Web Interface</title></head><body>"""
print header
print "THIS IS A TEST!"
print "<img src='../webapp.png'><br />"
bottom = "</body></html>"
print bottom

