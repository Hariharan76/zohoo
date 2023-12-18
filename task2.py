def func(n):
    answer=[]
    if n==0:
        return[""]
    else:
        for i in range(n):
            for h in func(i):
                for a in func(n-i-1):
                    answer.append("({}){}".format(h,a))
        # print(len(answer))
        return answer
    
n=int(input("enter the numper:"))
final=func(n)
print(final)