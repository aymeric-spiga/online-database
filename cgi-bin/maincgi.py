#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cgi, cgitb 
import numpy as np

import sys
sys.path.insert(0, "./planetoplot/modules")
from ppclass import pp,inspect

##################################
def getform(source,isfloat=False):
  output = form.getvalue(source)
  if isfloat:
    if output is not None:
      output = np.float(output)
  return output
##################################

# for debugging in web browser
cgitb.enable()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# RETRIEVE and PLOT DATA with PPCLASS
fifi = "./data/wrfout_d01_2024-10-04_06z00z00_zabg"
req = pp()
##
req.file = fifi
req.var = form.getvalue("var")
req.vargoal = form.getvalue("vargoal")
##
req.x = getform("x")
req.y = getform("y")
req.z = getform("z")
req.t = getform("t")
##
req.xmin = getform("xmin",isfloat=True)
req.xmax = getform("xmax",isfloat=True)
req.ymin = getform("ymin",isfloat=True)
req.ymax = getform("ymax",isfloat=True)
##
if form.getvalue("logy") == "True": req.logy = True
##
req.colorbar = getform("colorbar")
req.vmin = getform("vmin",isfloat=True)
req.vmax = getform("vmax",isfloat=True)
##
req.back = getform("back") # marche pas
req.proj = getform("proj")

# SET OUTPUT and RUN !
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
print inspect(fifi)
bottom = "</body></html>"
print bottom

