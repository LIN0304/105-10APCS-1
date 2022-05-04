list1=[]
a,b,c=map(int, input().split())
list1.append(a, b, c)
list1.sort
print(list1)
if a+b<=c:
    print('no')
    x=list1[2]*list1[2]
    y=list1[1]*list1[1]
    z=list1[0]*list1[0]
    p=y+z
    if x==p:
        print('right')
    elif x<p:
        print('acute')
    else:
        print('obtuse')
        
