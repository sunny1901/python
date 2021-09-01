
# 收益 = （本金 + 利率）^ 年数
# 公式 = （1 + 1 / n ）^ n
import math

"""
base 本金
rate 利率
count 频率
"""
def profit1( arr ):
    base = arr[0]
    rate = arr[1]
    count = arr[2]
    a = base + rate
    profit = a ** count
    return profit

"""
base 本金
rate 利率
count 频率
"""
def profit2( arr ):
    base = arr[0]
    rate = arr[1]
    count = arr[2]
    a = base + rate
    profit = math.pow( a , count )
    return profit



# 1 假设银行存款，年利率 100% （记作1）
o = ( 1 , 1 , 1 )
print( "按年结" ,profit1( o ) )
print( "按年结" ,profit2( o ) )

# 2 银行将利率，改为【半年】,一年2次
o = ( 1 , 0.5 , 2 )
print( "半年结" , profit1( o ) )
print( "半年结" ,  profit2( o ) )

# 3 银行将利率，改为【季度】，一年4 次
o = ( 1 , 0.25 , 4 )
print( "季度结" ,profit1( o ) )
print( "季度结" , profit2( o ) )

# 4 银行将利率，改为【月度】，一年12次
o = ( 1 , (1/12) , 12 )
print( "月度结" , profit1( o ) )
print( "月度结" , profit2( o ) )

# 5 银行将利率，改为【日结】，一年365次
count = 365
o = ( 1 , (1/365) , 365 )
print( "按日结" , profit1( o ) )
print( "按日结" , profit2( o ) )


# 6 银行将利率，改为【小时结】，一年 8760 次
count = 365 * 24
o = ( 1 , (1/count) , count )
print( "按时结" , profit1( o ) )
print( "按时结" , profit2( o ) )


# 6 银行将利率，改为【分钟结算】，一年 525600 次
count = 365 * 24 * 60
o = ( 1 , (1/count) , count )
print( "分钟结" , profit1( o ) )
print( "分钟结" , profit2( o ) )

# 6 银行将利率，改为【秒结算】，一年 22896000 次
count = 365 * 24 * 60 * 60
o = ( 1 , (1/count) , count )
print( "秒结" , profit1( o ) )
print( "秒结" , profit2( o ) )

print( "自然数e" , 2.71828)


