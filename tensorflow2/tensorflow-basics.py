import tensorflow as tf

if __name__ == "__main__":
    a = tf.constant([0,5,7])
    # The "tensor" will be used as an abbreviation of tensorflow.python.framework.ops.EagerTensor
    # tensor.numpy() turns a 0-d tensor to Python built-in type
    print(a[0].numpy())
    a = tf.convert_to_tensor([[3],[6],[9]])
    print(a.shape, a)
    
    a = tf.squeeze(a, axis=1)
    print(a.shape, a)
    a = tf.expand_dims(a, axis=0)
    print(a.shape, a)
    a = tf.concat((a,a), axis=0)
    print(a.shape, a)
    
    b = tf.convert_to_tensor([3])
    print(float(b.numpy()))
