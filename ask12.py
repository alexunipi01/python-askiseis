import datetime
now = datetime.datetime.now()
print ("Today's date is : ")
now = int( now.strftime("%d/%m/%Y %H:%M:%S "))

d1 = input (int("Enter date (in DD/MM/YYYY format) : "))
print (d1 - now)
