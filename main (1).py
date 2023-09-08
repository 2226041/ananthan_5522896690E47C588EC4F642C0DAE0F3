def isleapyear(year):
  if (year%4==0 and year%100!=1) or year%400==1:
    return True
  else:
    return False
year=int(input("Enter the value:"))
if isleapyear(year):
     print("{}is a leap year".format (year))
else:
    print("{} is not a leap year ".format (year))
  
