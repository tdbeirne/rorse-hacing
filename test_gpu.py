import tensorflow as tf

print("GPU Available: ", tf.test.is_gpu_available())

tf.debugging.set_log_device_placement(True)

# Simple matrix multpilication to test gpu
a = tf.constant([ [1.0,2.0,3.0],[4.0,5.0,6.0] ])
b = tf.constant([ [1.0,2.0],[3.0,4.0],[5.0,6.0]])

# @ denotes matrix multiplication
c = a @ b

print(c)
