# coding=utf-8

# loop 迭代次数
# num

def base( loop , num , rat , count ):
    count += 1
    num += num * rat
    loop -= 1
    print( "Y:\t" , count , "\t = " , num )
    if  loop> 0  :
        base( loop , num , rat , count)
    return num

def fun1( loop , num , rat):
    return base( loop , num , rat  , 0 )

print("hello-------------")
num = fun1(10  , 10000 , 0.2 )

print( "Fin:" , num )