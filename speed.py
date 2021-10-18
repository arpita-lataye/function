def driver_speed(speed):
    if speed<70:
        print('okk')
    elif speed>70:
        point=(speed-70)/5
        print(point)
        if point>12:
            print('license suspended')   
s=int(input('enter number:'))
driver_speed(s)
