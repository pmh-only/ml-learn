## Machine Learning

> [!IMPORTANT]
> 데이터셋은 [개인 Git LFS 서버](https://src.pmh.codes/pmh_only/ml-learn)에 저장되어 있으며\
> 데이터셋을 받기 위해 Clone전 [Git LFS를 설치](https://docs.github.com/repositories/working-with-files/managing-large-files/installing-git-large-file-storage)하여야 합니다.

## Fetch Dependancies
```
pip install torch torchvision torchaudio \
  --index-url https://download.pytorch.org/whl/cpu
  
pip install -r requirements.txt
```

## Contents Overview
* PyTorch - ANN
  * [PyTorch - 붓꽃 분류](./ann_pytorch_iris.ipynb)
  * [PyTorch - 붓꽃(확장) 분류](./ann_pytorch_iris_extended.ipynb)
  * [PyTorch - 보스턴 집값 예측 회귀](./ann_pytorch_housing.ipynb)
  * [PyTorch - MNIST 손글씨 분류 (ANN)](./ann_pytorch_mnist.ipynb)

* PyTorch - CNN
  * [PyTorch - MNIST 손글씨 분류 (CNN)](./cnn_pytorch_mnist.ipynb)
  * [PyTorch - Pizza/Not Pizza 분류](./cnn_pytorch_pizza.ipynb)

* PyTorch - RNN
  * [PyTorch - MNIST 손글씨 분류 (RNN)](./rnn_pytorch_mnist.ipynb)
  * [PyTorch - 뉴욕 증시 예측 회귀](./rnn_pytorch_nystock.ipynb)

* Scikit Learn - Linear Algorithms
  * [Scikit Learn - 당뇨병 분류](./linear_class_sklearn_diabetes.ipynb)
  * [Scikit Learn - 당뇨병 회귀](./linear_regs_sklearn_diabetes.ipynb)

* Scikit Learn - Decision Tree
  * [Scikit Learn - 와인 퀄리티 분류/회귀](./tree_sklearn_wine.ipynb)

* SageMaker - XGBoost
  * [XGBoost - 보스턴 집값 예측 회귀](./xgboost_sagemaker_housing.ipynb)
  * [XGBoost - 붓꽃(확장) 분류](./xgboost_sagemaker_iris_extended.ipynb)
