# def add_numbers(num1,num2):
#     print(num1+num2)
# num1=56
# num2=12
# add_numbers(num1,num2)

def add_number_list(a,b):
    i=0
    sum=0
    while i<len(a):
        if a[i] in a:
            sum=a[i]+b[i]
            print('sum of',i,'position:',sum)
        i=i+1
a=[23,45,12]
b=[45,65,22]
add_number_list(a,b)