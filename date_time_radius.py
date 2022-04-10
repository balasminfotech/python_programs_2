import datetime
now=datetime.datetime.now()
print("The current date time is:",now.strftime("%Y-%m-%d %H:%M:%S"))


from math import pi
r=float(input("Enter radius of a circle : "))
print("The radius of a circle is "+str(r)+ "is " +str(pi * r**2))


fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)

exam_st_date = (11, 12, 2014)
print("The exam  date  is %i/%i/%i:" % exam_st_date)
