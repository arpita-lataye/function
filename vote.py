def eligible_for_vote(a):
    if a<18:
        print('you are not eligible for vote')
    else:
        print('you are eligible for vote')
a=int(input('enter age:'))
eligible_for_vote(a)