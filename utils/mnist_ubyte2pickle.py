import numpy as np
import pandas as pd
import pickle

# Train Iamge ---
with open('./datasets/mnist/orig/train-images.idx3-ubyte', 'rb') as f:
  data = np.frombuffer(f.read(), dtype=np.uint8, offset=16)
  data = data.reshape(-1, 28*28) / 255.0
  print('train-images.idx3-ubyte:', data.shape)

with open('./datasets/mnist/train-images-flatten.pkl', 'wb') as f:
  pickle.dump(data, f)

with open('./datasets/mnist/train-images-2d.pkl', 'wb') as f:
  pickle.dump(data.reshape(-1, 1, 28, 28), f)

# Train Label ---
with open('./datasets/mnist/orig/train-labels.idx1-ubyte', 'rb') as f:
  data = pd.get_dummies(np.frombuffer(f.read(), dtype=np.uint8, offset=8), dtype='float32').to_numpy()
  print('train-labels.idx1-ubyte:', data.shape)

with open('./datasets/mnist/train-labels.pkl', 'wb') as f:
  pickle.dump(data, f)

# Test Iamge ---
with open('./datasets/mnist/orig/t10k-images.idx3-ubyte', 'rb') as f:
  data = np.frombuffer(f.read(), dtype=np.uint8, offset=16)
  data = data.reshape(-1, 28*28) / 255.0
  print('t10k-images.idx3-ubyte:', data.shape)

with open('./datasets/mnist/test-images-flatten.pkl', 'wb') as f:
  pickle.dump(data, f)

with open('./datasets/mnist/test-images-2d.pkl', 'wb') as f:
  pickle.dump(data.reshape(-1, 1, 28, 28), f)

# Test Label ---
with open('./datasets/mnist/orig/t10k-labels.idx1-ubyte', 'rb') as f:
  data = pd.get_dummies(np.frombuffer(f.read(), dtype=np.uint8, offset=8), dtype='float32').to_numpy()
  print('t10k-labels.idx1-ubyte:', data.shape)

with open('./datasets/mnist/test-labels.pkl', 'wb') as f:
  pickle.dump(data, f)
