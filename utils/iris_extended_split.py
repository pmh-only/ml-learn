import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split

original = pd.read_csv('./datasets/iris_extended.csv')
train, test = train_test_split(original, train_size=0.3, test_size=0.7)

train.to_csv('./datasets/iris_extended_train.csv', index=False)
test.to_csv('./datasets/iris_extended_test.csv', index=False)
