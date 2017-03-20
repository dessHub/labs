def binary_converter(n):
    if(n==0):
        return "0"
    elif(n<0):
        return "Invalid input"
    elif(n>255):
        return "Invalid input"
    else:
        ans=""
        while(n>0):
            temp=n%2
            ans=str(temp)+ans
            n=n/2
        return ans  
