import tensorflow as tf

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
file = tf.io.read_file('../data/frederick.png')
image = tf.image.decode_png(file)

input  = tf.reshape(image, [1, 128, 171, 3],name='image')
input_2 = tf.cast(input,tf.float32)

a = tf.nn.conv2d(input_2, kernel, [1, stride, stride, 1], padding=padding)
b = tf.minimum(tf.nn.relu(a),255)
result = tf.squeeze(b)

to_file = tf.cast(result, tf.uint8)
op = tf.image.encode_png(to_file)
wf = tf.io.write_file('../data/test_file.png',op)

with tf.Session() as sess:
    sess.run(wf)
