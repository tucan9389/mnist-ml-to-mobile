# Machine Learning into Mobile with MNIST

앱에서 손글씨로 숫자를 쓰면, 어떤 숫자(0~9)인지 맞춰줍니다. 

[MNIST 데이터셋](http://yann.lecun.com/exdb/mnist/), [TensorFlow 2](https://www.tensorflow.org), [Flask](https://flask.palletsprojects.com), [TensorFlow Lite](https://www.tensorflow.org/lite) 등을 사용하여 모델 학습, 서버 추론, 앱 추론을 실행해볼 수 있습니다.

## 예제 소개

- [training](training): TF2를 사용한 딥러닝 모델 학습을 위한 예제
- [app-server](app-server): Flask를 사용한 서버 추론을 위한 앱 예제
- [app-mobile](app-mobile): 모바일 앱에서 온디바이스 추론 및 서버 통신 추론을 위한 앱 예제

## 동작 방법

### A. 서버 추론

1. [training](training)를 수행하여 학습된 saved_model을 얻습니다.
2. saved_model을 [app-server](app-server)에 넣고, 서버를 실행합니다.
3. 모바일 앱([app-mobile](app-mobile)) 혹은 브라우저를 통해 mnist 추론 요청을 합니다.

### B. 온디바이스 추론

1. [training](training)를 실행하여 학습된 saved_model을 얻습니다.
2. saved_model을 tflite로 변환합니다.
3. tflite 모델을 앱 프로젝트에 탑재합니다.

## TODO

- [x] [TF2](https://www.tensorflow.org)를 사용한 딥러닝 모델 학습 예제
- [ ] [Flask](https://flask.palletsprojects.com)를 사용한 딥러닝 모델 서빙 예제
- [ ] [TensorFlowLiteSwift](https://www.tensorflow.org/lite/guide/ios)를 사용한 iOS 온디바이스 추론 예제
- [ ] [Alamofire](https://github.com/Alamofire/Alamofire)를 사용한 iOS 서버 통신 추론 예제
- [ ] 안드로이드 온디바이스 추론 예제
- [ ] 안드로이드 서버 통신 추론 예제

