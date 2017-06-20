import keras_rcnn.backend
import numpy
import numpy.testing
import keras
import keras.backend

def test_anchor():
    x = keras.backend.variable(numpy.array(
      [[ -84.,  -40.,  99.,  55.],
       [-176.,  -88., 191., 103.],
       [-360., -184., 375., 199.],
       [ -56.,  -56.,  71.,  71.],
       [-120., -120., 135., 135.],
       [-248., -248., 263., 263.],
       [ -36.,  -80.,  51.,  95.],
       [ -80., -168.,  95., 183.],
       [-168., -344., 183., 359.]]
    ))
    y = keras_rcnn.backend.anchor()
    assert keras.backend.eval(keras.backend.all(keras.backend.equal(keras.backend.eval(x), keras.backend.eval(y))))

def test_clip():
    pass


def bbox_transform():
    pass




