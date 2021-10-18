def check_number_list(a,b):
    i=0
    while i<len(a):
        if a[i]%2==0 and b[i]%2==0:
            print('even',a[i],b[i])
        else:
            print('odd',a[i],b[i])
        i=i+1
a=[2, 6, 18, 10, 3, 75] 
b=[6, 19, 24, 12, 3, 87]
check_number_list(a, b)
