# coding=utf-8
from datetime import datetime
import matplotlib.pyplot as plt

# def time_line():
#     xs = [datetime.strptime(d, '%Y/%m/%d').date() for d in l_time]
#     return xs

if __name__ == "__main__" :

    # show text
    plt.title( ' hello line ' )
    plt.xlabel(' Date Line ')
    plt.ylabel(' P line ')

    # 背景网格
    plt.grid(True)

    # names data
    x_names  = [  "4.14" ,"4.15"  , "4.16" , "4.17"   ]
    x_values = [  20     ,19      , 20     , 22      ]


    plt.plot( x_names , x_values , 'ro')
    plt.axis([0, 6, 0, 40  ])
    plt.show()