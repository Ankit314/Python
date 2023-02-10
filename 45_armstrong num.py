lower=100
upeer=1000
for num in range(lower,upeer+1):
    sum=0
    temp=num
    while (temp>0):
        digit=temp%10
        sum+=digit**3
        temp=temp/10
        if (num==sum):
            print(num)