# MNIST 모델링 예제

아래 방법으로 수행하면 학습 및 모델 저장(saved_model)을 수행합니다.

## 목차

- [환경 세팅](#환경-세팅)
- [실행 방법](#실행-방법)
- [결과 확인](#결과-확인)
- [참고](#참고)

## 환경 세팅

1. Adaconda 설치
2. conda로 가상환경 접속
3. 필요 python 라이브러리 설치

### 1. Anaconda 설치

- macOS - [Installing on macOS](https://docs.anaconda.com/anaconda/install/mac-os/)
- Ubuntu 18.04 - [How To Install Anaconda on Ubuntu 18.04 [Quickstart]](https://www.digitalocean.com/community/tutorials/how-to-install-anaconda-on-ubuntu-18-04-quickstart)

### 2. conda로 가상환경 생성 및 접속

```shell
# 가상환경 생성
$ conda create -n {가상환경_이름} python=3.6
# conda create -n tf2_mnist_training_env python=3.6

# 가상환경 접속
$ conda activate {가상환경_이름}
# or
$ source activate {가상환경_이름}
# conda activate tf2_mnist_training_env
```

### 3. 필요 python 라이브러리 설치

```shell
(tf2_mnist_training_env) $ cd ~/MNIST-ml-to-mobile/training
(tf2_mnist_training_env) $ pip install -r requirements.txt
```

## 실행 방법

### 1. conda로 가상환경 접속

```shell
$ conda activate {가상환경_이름}
# conda activate tf2_mnist_training_env
```

### 2. 학습 스크립트 실행

```shell
(tf2_mnist_training_env) $ python train.py
```

## 결과 확인



## 참고

