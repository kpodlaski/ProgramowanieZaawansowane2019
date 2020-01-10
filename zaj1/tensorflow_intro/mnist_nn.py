import tensorflow as tf


modelA = tf.keras.models.Sequential(
    [
        tf.keras.layers.Flatten(input_shape=(28,28)),
        tf.keras.layers.Dense(20, activation=tf.nn.sigmoid),#tf.nn.relu
        tf.keras.layers.Dense(10, activation=tf.nn.sigmoid),  # tf.nn.relu
        tf.keras.layers.Dense(10,activation=tf.nn.softmax)
    ]
)

model = tf.keras.models.Sequential(
    [   #LENET5 https://engmrk.com/lenet-5-a-classic-cnn-architecture/
        #tf.keras.layers.Flatten(input_shape=(28,28)),
        tf.keras.layers.Conv2D(6, kernel_size=(5,5), strides=(1,1),
                               input_shape=(28,28,1)),
        tf.keras.layers.AvgPool2D(pool_size=(2,2),strides=(2,2)),
        tf.keras.layers.Conv2D(16, kernel_size=(5, 5), strides=(1, 1)),
        tf.keras.layers.AvgPool2D(pool_size=(2, 2), strides=(2, 2)),
        tf.keras.layers.Conv2D(120, kernel_size=(2, 2), strides=(1, 1)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(86, activation=tf.nn.sigmoid),  # tf.nn.relu
        tf.keras.layers.Dense(10,activation=tf.nn.softmax)
    ]
)

model.compile(optimizer=tf.keras.optimizers.SGD(0.5),#GradientDescentOptimizer
              loss = tf.keras.losses.sparse_categorical_crossentropy, #tf.kearas.losses.mean_absolute_error
              metrics=['accuracy']
              )

mnist =tf.keras.datasets.mnist
#mnist = tf.keras.datasets.cifar10

(train_inputs, train_labels) , (test_inputs, test_labels)  =mnist.load_data()
train_inputs, test_inputs = train_inputs/255, test_inputs/255

model.summary()

train_inputs=train_inputs.reshape(60000,28,28,1)
test_inputs=test_inputs.reshape(10000,28,28,1)
print('train labels:',train_labels.shape)
print('train inputs:',train_inputs.shape)

print('test labels:',test_labels.shape)
print('test inputs:',test_inputs.shape)

model.fit(train_inputs, train_labels,epochs=10, batch_size=100)


test_loss, test_acc = model.evaluate(test_inputs, test_labels)
print('Test acc:',test_acc)
print('Test loss:', test_loss)
