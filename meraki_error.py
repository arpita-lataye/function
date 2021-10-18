def calculate_sum(a,b):
    sum = a+b
    print('sum',sum)
calculate_sum(4,5)

def function_multi(a,b):
    multiply=a*b
    return multiply
d=function_multi(3, 4)
print('multiplication',d)


def avg(number1,number2,number3):
    sum=number1+number2+number3
    avg=number1+number2+number3/3
    print(' of numbers',sum)
    print('avg of numbers',avg)
avg(1,3,2)


def voter(age):
    if age < 18:
        print("eligible")
    else:
        print("not eligible")
voter(20)

def distance(kms):
    if kms < 20:
        print("close")
    elif kms < 50:
        print('median')
    else:
        print('far')
distance(10)
distance(30)
distance(66)