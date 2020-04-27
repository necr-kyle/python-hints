import tensorflow as tf

if __name__ == "__main__":
    a = tf.constant([0,5,7])
    # The "tensor" will be used as an abbreviation of tensorflow.python.framework.ops.EagerTensor
    # tensor.numpy() turns a 0-d tensor to Python built-in type
    print(a[0].numpy())
