#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cgi, cgitb 

import sys
sys.path.insert(0, "./planetoplot/modules")
import ppplot
from ppclass import pp

# for debugging in web browser
cgitb.enable()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get parameters from form
ux = form.getvalue("x")
uy = form.getvalue("y")
uz = form.getvalue("z")
ut = form.getvalue("t")

########################################

fig = ppplot.figuref(x=8,y=6)



# RETRIEVE DATA
fifi = "./data/wrfout_d01_2024-10-04_06z00z00_zabg"
req = pp()
req.file = fifi
req.var = "HGT"
req.x = ux
req.y = uy
req.z = uz
req.t = ut

ff,xx,yy,zz,tt = req.getfd()

#ff,xx,yy,zz,tt = pp(file=fifi,var="HGT",z=0,t=0).getfd()
#xx = pp(file=fifi,var="XLONG",z=0,t=0).getf()
#yy = pp(file=fifi,var="XLAT",z=0,t=0).getf()
#uu = pp(file=fifi,var="Um",z=0,t=0).getf()
#vv = pp(file=fifi,var="Vm",z=0,t=0).getf()

# PLOT
pl = ppplot.plot2d()
pl.fig = fig # have to send to figure
pl.f = ff
pl.x = xx
pl.y = yy
#pl.vx = uu
#pl.vy = vv
pl.legend = "yorgl"
pl.marker = None
pl.nyticks = 20
pl.ylabel = "YAARGL"
#pl.proj = "laea"
pl.make()
########################################

# create figure
ppplot.sendagg(fig,filename='webapp.png', dpi=150)




##### NOW WRITE THE HTML PAGE TO USER
print "Content-type:text/html;charset=utf-8\n"
print     #Apache needs a space after content-type
header="""<html><head><title>Mars Climate Database: The Web Interface</title></head><body>"""
print header
print "THIS IS A TEST!",ux,uy,uz,ut
print "<img src='../webapp.png'><br />"
bottom = "</body></html>"
print bottom

