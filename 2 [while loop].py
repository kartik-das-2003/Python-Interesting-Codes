print("GIVE ME YOUR PIN NO::")
n=int() #numbers of determination unit
x=9253 #passcode
while(x==9253):#while pass code is 9253 then..
    for i in range(1): #for loop configuration notice..
        n=int(n+1) #significant part
        x=input("Enter Passcode:")#passcode input to verify allow next candidate
        x=int(x) #follow this position
        if(x==9253):
            print("candidate",n,"come in")
            
        else:
            print("end of our day")
