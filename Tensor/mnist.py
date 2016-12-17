#Beginner program as directed by Tensor tutorial

#Importing MNIST data from Yann LeCun's website
from tensorflow.examples.tutorials.mnist import input_data

#creating a data set to hold the MNIST data - one hot enabled
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

import tensorflow as tf

#softmax variables: evidence = sum(wx+b), softmax exponentiates and normalizes evidence
#placeholder value that holds 784 dimensional arrays, 'None' means the dimensions can be of any length
x = tf.placeholder(tf.float32, [None, 784])
#creating a 10D variable of 784 weights - to be computed by the algorithm and applied to classes
W = tf.Variable(tf.zeros([784, 10]))
#creating a variable to hold the biases - to be computed by the algorithm
b = tf.Variable(tf.zeros([10]))

#implementing the softmax model function
y = tf.nn.softmax(tf.matmul(x, W) + b)
#placeholder that will hold the correct answers
y_ = tf.placeholder(tf.float32, [None, 10])
#cross entropy function measures inefficiency in the model output: H(y)=-sum(y'log(y)), where y' is true distr.
cross_entropy = -tf.reduce_sum(y_*tf.log(y))
#gradient descent algorithm is used to minimize cross entropy with a learning rate of .01
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

#initializing created variables
init = tf.initialize_all_variables()

#launching the model in a session, and running init
sess = tf.Session()
sess.run(init)

#training over 1000 steps - stochastic training
for i in range(1000):
    #take in batch of random hundred data points
    batch_xs, batch_ys = mnist.train.next_batch(100)
    #running train_step with x and y_ placeholders filled in from batch
    sess.run(train_step, feed_dict={x: batch_xs, y_:batch_ys})
    
#argmax provides highest entry in a tensor along an axis/dimension
#checking if prediction and actual are equal
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
#casting booleans to binary numbers and taking the mean
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))