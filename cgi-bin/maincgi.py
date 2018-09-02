#!/usr/bin/env python
# -*- coding: UTF-8 -*-

##############################
##############################
fifi = "./data/wrfout_d01_2024-10-04_06z00z00_zabg"
fifi = "/home/aspiga/data/VENUS/Xave-24perVd_300_extract_last.nc"
title = "LMD Venus Climate Database"
##############################
##############################

import cgi, cgitb 
import numpy as np

import sys
sys.path.insert(0, "./planetoplot/modules")
from ppclass import pp,inspect

import datetime
import hashlib

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

# SET OUTPUT
req.xp = 10
req.yp = 10
req.svx = 3
req.svy = 3
req.title = title
req.out = "agg" 
req.nopickle = True
#req.quiet = False ; req.verbose = True # debug
req.quiet = True ; req.verbose = False # production

# INFER A NAME from CURRENT DATE
req.filename = hashlib.md5(str(datetime.datetime.today())).hexdigest()

##### NOW WRITE THE HTML PAGE TO USER -- HEADER
print "Content-type:text/html;charset=utf-8\n"
print     #Apache needs a space after content-type
header="""<html><head><title>LMD Venus Climate Database</title></head><body>"""
print header
print "THIS IS A TEST!"
print req.x,req.y,req.z,req.t

##### RUN PLANETOPLOT
req.getplot()

##### NOW WRITE THE HTML PAGE TO USER -- FIGURE and BOTTOM
print "<img src='../"+req.filename+".png'><br />"
bottom = "</body></html>"
print bottom
