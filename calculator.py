def calculator(num_x,num_y,operation):
    if operation=="add":
        return num_x+num_y
        
    elif operation=="subtract":
        return num_x-num_y 

    elif operation=='multiply':
        return num_x*num_y

    else:
        return num_x/num_y

a=calculator(20,25,'add')
print('a',a)
b=calculator(40,3,'subtract')
print('b',b)
d=calculator(10, 4,'multiply')
print('d',d)
p=calculator(40, 4,'divide')
print('p',p)
print()
num1=calculator(24, 20, 'add')
print('num',num1)
num2=calculator(50, 60,'multiply')
print('num2',num2)
num3=calculator(80, 120,'divide')
print('num3',num3)
num4=calculator(90, 23,'subtract')
print('num4',num4)
print()
num_x=int(input("enter the number:"))
num_y=int(input("enter the number:"))
print()
add_result=calculator(num_x, num_y, 'add')
subtract_result=calculator(num_x, num_y, 'subtract')
multiply_result=calculator(num_x, num_y, 'multiply')
divide_result=calculator(num_x, num_y, 'divide')
print('add_result',add_result)
print('subtract_result',subtract_result)
print( 'multiply_result',multiply_result)
print( 'divide_result',divide_result)

def list_change():
    i=0
    while i<len(multiple_list):
        j=0
        while j<len(multiple_list[i]):
            multiply=calculator(multiple_list[0][j],multiple_list[1][j],'multiply')
            j=j+1
            print('multiply',[0],[j],'*',[1],[j],'=',multiply)
        i=i+1
        break
multiple_list =([5, 10, 50, 20], [2, 20, 3, 5])
list_change()

