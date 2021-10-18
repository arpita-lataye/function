# without argument
def num():
    a=int(input('enter num:'))
    if a%2==0:
        print('even')
    else:
        print('odd')
num()


# with argument
def oddeven(a):
    if a%2==0:
        print('even')
    else:
        print('odd')
oddeven(6)

# with argument user input
def oddeven(a):
    if a%2==0:
        print('even')
    else:
        print('odd')
m=int(input('enter number:'))
oddeven(m)