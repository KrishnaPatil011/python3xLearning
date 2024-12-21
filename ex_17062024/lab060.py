# *arg-any number of arguments

def sum_three(a=1,b=1,c=1):
    return a+b+c
result1=sum_three()
result2=sum_three(2)
result3=sum_three(4,5)
result4=sum_three(c=7)
result5=sum_three(c=3,b=1,a=3)


print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
