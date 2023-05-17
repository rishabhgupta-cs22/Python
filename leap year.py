#leap year python program
year=int(input("year check kar"))

if(year%4==0 and year%100!=0 or year%400==0):
    print("this is a leap year")
else: print("not a leap year")    
