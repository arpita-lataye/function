def perfect(num):               #perfect number is a positive integer that is equal to the half of the sum of its all positive divisors.
    sum=0                       #perfect number is a positive integer that is equal to the sum of its positive divisors excluding the number itself.
    i=1
    while i<=num:
        if (num%i)==0:
            sum=sum+i%num
        i=i+1
    if sum==num:
        print(num,'is perfect number')
    else:
        print(num,'is not a perfect number')
number=int(input('enter the number:'))
perfect(number)



# def function(number):
#     result=0
#     for i in range(1,number):
#         if number%i==0:
#             result=result+i
#     if result==number:
#         print('perfect')
#     else:
#         print('not')
# number=int(input('enter the number:'))
# function(number)

