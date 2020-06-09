import tensorflow as tf

x = tf.zeros([2,3])

print(x)

x1= tf.Variable(x)

print(x1)


op = x1[0 , 1].assign(1)

print(op)

op = x1[1 , 2].assign(99)

print(op)

