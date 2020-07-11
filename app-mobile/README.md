# MNIST 모바일 앱 예제

1. 모델 변환
2. 앱 실행

## 모델 변환

### 환경 세팅

아나콘다 설치 (training, app-server와 동일)

### 변환

```
# TensorFlow Lite 모델로 변환
(tf2_mnist_mobile_env) $ python convert_tf2_to_tflite.py

# Core ML 모델로 변환 (문제가 있습니다..)
# (tf2_mnist_mobile_env) $ python convert_tf2_to_mlmodel.py
```

## 앱 실행

### iOS

#### 환경 세팅

- macOS 필요

- Xcode 설치
- Cocoapods 설치
- 의존성 라이브러리 설치

#### 모델 탑재



#### 빌드 & 실행



### Android

> 준비중...