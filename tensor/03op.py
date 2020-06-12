# tensorfflow 2.0
import tensorflow as tf

# demo1

function demo1():
    tf.disable_v2_behavior()

    a1 = tf.constant( 1 )
    b1 = tf.constant( 2 )

    value = tf.add( a , b )

    # with tf.Session() as sess:
    #     print( sess.run( value ) )

    sess = tf.compat.v1.Session()
    print( sess.run( value ) )
    sess.close()

    ai = ses