# MNIST 모바일 앱 예제

1. 모델 변환
2. 앱 실행

## 모델 변환

### 환경 세팅

- 아나콘다 설치 ([`training`](../training), [`app-server`](../app-server)와 동일한 방법)

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
- iOS 11+
- [Xcode 설치](https://apps.apple.com/app/id497799835)
- [Cocoapods 설치](https://guides.cocoapods.org/using/getting-started.html)

#### CocoaPods 의존성 라이브러리 설치

```shell
$ cd ~/mnist-ml-to-mobile/app-mobile/ios
$ pod install
```

#### 모델 탑재

`MNIST-TFLiteSwift.xcworkspace` 열어서 변환된 tflite 모델을 Xcode 프로젝트에 추가.

모델 이름이 `mnist.tflite`와 다르면, `MNISTImageClassifier.swift` 파일의 `modelName` 값을 추가된 모델 파일 이름과 동일하게 지정해주어야 합니다.

#### 빌드 & 실행

좌측 상단의 실행버튼 클릭 (혹은 ⌘ + R 단축키)

### 실행 화면

|                             gif                              |                         screenshot-1                         |                         screenshot-2                         |                         screenshot-3                         |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| ![mnist-ios-demo](https://user-images.githubusercontent.com/37643248/87229057-1b84cc80-c3e0-11ea-97ca-92fd23ac71b7.gif) | <img src="https://user-images.githubusercontent.com/37643248/87228939-65b97e00-c3df-11ea-8fcf-e1a959457212.png" width=180px> | <img src="https://user-images.githubusercontent.com/37643248/87228969-939ec280-c3df-11ea-82a7-77ac5a9037d6.png" width=180px> | <img src="https://user-images.githubusercontent.com/37643248/87228975-9bf6fd80-c3df-11ea-8c5a-082e82b6eec3.png" width=180px> |

### Android

> 준비중...