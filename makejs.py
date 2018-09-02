#!/usr/bin/env python
# -*- coding: UTF-8 -*-

##########################
## create an JS scripts for HTML list from dimensions in netCDF file
fifi = "/home/aspiga/data/VENUS/Xave-24perVd_300_extract_last.nc"
##########################

import netCDF4

### load netCDF file
netcdfobj = netCDF4.Dataset(fifi)

### loop on dimensions to create JS files
for c in netcdfobj.dimensions.keys():

    ### open a dedicated JS file
    name = netcdfobj.dimensions[c].name
    asciifile = open("list_"+name+".js", "w")

    ### write the list
    asciifile.write("document.write('\\\n")
 
    ### first the mean case (with good bounds)
    valfirst = netcdfobj.variables[c][0]
    vallast = netcdfobj.variables[c][-1]
    if valfirst > vallast: zemin,zemax = vallast,valfirst
    else: zemax,zemin = vallast,valfirst   
    if "pres" in c: zemax,zemin = vallast,valfirst
    asciifile.write('<option value="'+str(zemin)+","+str(zemax)+'">'+"mean</option>\\\n")

    ### then individual values
    for v in netcdfobj.variables[c][:]:
       asciifile.write('<option value="'+str(v)+'">'+str(v)+"</option>\\\n")
    asciifile.write("');")

asciifile.close()

### JS file with variables in it
asciifile = open("list_var.js", "w")
asciifile.write("document.write('\\\n")
for vvv in netcdfobj.variables.keys():
    if netcdfobj.variables[vvv].ndim > 1:
        asciifile.write('<option value="'+vvv+'">'+vvv+"</option>\\\n")
asciifile.write("');")
asciifile.close()

