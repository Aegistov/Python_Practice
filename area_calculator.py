#This will calculate the area of a Circle or Triangle
#With the magic of code
from math import pi
from time import sleep
from datetime import datetime
now = datetime.now()
print "CALCULATOR INITIATED"
print "%s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute)
sleep(1)
hint = "Don't forget to include the correct units!\n"
option = input("Enter C for Circle or T for Triangle\n").upper()
if option == "C":
  radius = float(input("Input the radius of the circle as a number\n"))
  area = pi*radius**2
  print "The pie is baking...\n"
  sleep(1)
  print "%.2f\n%s\n" % (area, hint)
elif option == "T":
  base = float(input("Input the base of the triangle as a number\n"))
  height = float(input("Input the height of the triangle as a number\n"))
  area = (base * height) / 2
  print "Uni Bi Tri...\n"
  sleep(1)
  print "%.2f\n%s\n" % (area, hint)
else:
  print "GARBAGE INPUT. CALCULATOR FAILING"
  sleep(1)
  print "CALCULATOR SHUTTING DOWN"
  sleep(2)