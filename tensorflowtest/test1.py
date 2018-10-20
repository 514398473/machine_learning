#coding=utf-8
import tensorflow as tf

a = tf.constant(5.0)
b = tf.constant(5.0)
sum1 = tf.add(a,b)
with tf.Session() as sess:
    print(sess.run(sum1))