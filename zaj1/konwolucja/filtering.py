import cv2
import tensorflow as tf
tf.compat.v1.disable_eager_execution()

kernel = tf.constant([
[
[[ -1., 0., 0.], [ 0., -1., 0.], [ 0., 0., -1.]],
[[ -1., 0., 0.], [ 0., -1., 0.], [ 0., 0., -1.]],
[[ -1., 0., 0.], [ 0., -1., 0.], [ 0., 0., -1.]]
],
[
[[ -1., 0., 0.], [ 0., -1., 0.], [ 0., 0., -1.]],
[[ 8., 0., 0.], [ 0., 8., 0.], [ 0., 0., 8.]],
[[ -1., 0., 0.], [ 0., -1., 0.], [ 0., 0., -1.]]
],
[
[[ -1., 0., 0.], [ 0., -1., 0.], [ 0., 0., -1.]],
[[ -1., 0., 0.], [ 0., -1., 0.], [ 0., 0., -1.]],
[[ -1., 0., 0.], [ 0., -1., 0.], [ 0., 0., -1.]]
]])

padding = "SAME"
stride = 1
image = cv2.imread("../data/person_2.png")


input  = tf.reshape(image, [1, 128, 170, 3],name='image')
input_2 = tf.cast(input,tf.float32)

print("input_2",input_2)

a = tf.nn.conv2d(input_2, kernel, [1, stride, stride, 1], padding=padding)
b = tf.minimum(tf.nn.relu(a),255)
result = tf.squeeze(b)

to_file = tf.cast(result, tf.uint8)
op = tf.image.encode_png(to_file)
wf = tf.io.write_file('../data/test_file.png',op)

with tf.compat.v1.Session() as sess:
    sess.run(wf)
