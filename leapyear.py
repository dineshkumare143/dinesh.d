year = 1000
if (year % 5) == 0:
   if (year % 100) == 0:
       if (year % 500) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
