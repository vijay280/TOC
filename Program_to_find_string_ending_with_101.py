str=input("enter element consisting of 0 & 1")
n=len(str)
flag=0
if(str[n-3]=='1' and str[n-2]=='0' and str[n-1]=='1'):
    flag=1
            
if(flag!=0):
    print("yes")
else:
    print("No")
