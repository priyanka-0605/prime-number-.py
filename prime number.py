x=int(input("entr the number:"))
count=0
for i in range(1,x+1):
    if(x%i==0):
        count+=1
if(count==2):
    print("prime number")
else:
    print("not prime number")
                