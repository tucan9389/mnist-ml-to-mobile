# Machine Learning into Mobile with MNIST

앱에서 손글씨로 숫자를 쓰면, 0~9 숫자 중 하나를 추론합니다. [MNIST 데이터셋](http://yann.lecun.com/exdb/mnist/), [TensorFlow 2](https://www.tensorflow.org), [Flask](https://flask.palletsprojects.com), [TensorFlow Lite](https://www.tensorflow.org/lite) 등을 사용하여 모델 학습부터 응용까지 가볍게 모델 추론 앱을 만들어 볼 수 있습니다.

|                    온디바이스 추론 플로우                    |
| :----------------------------------------------------------: |
| <img width="1029" alt="diagram-ondevice-inference" src="https://user-images.githubusercontent.com/37643248/87227935-ede85500-c3d8-11ea-849c-bfb57595d0c7.png"> |

|                       서버 추론 플로우                       |
| :----------------------------------------------------------: |
| <img width="1043" alt="diagram-server-inference" src="https://user-images.githubusercontent.com/37643248/87227936-f04aaf00-c3d8-11ea-987c-6dfaf7caf2a8.png"> |

## 폴더 구조

```
~/mnist-ml-to-mobile
  ├── training		: TF2를 사용한 딥러닝 모델 학습을 위한 예제
  ├── app-server	: Flask를 사용한 서버 추론을 위한 앱 예제
  ├── app-mobile	: 모바일 앱에서 온디바이스 추론 및 서버 통신 추론을 위한 앱 예제
  |	├── convert	: tflite 변환을 위한 예제
  |	├── ios		: iOS 예제 프로젝트 (https://github.com/tucan9389/MNIST-TFLiteSwift)
  |	└── android     : 현재 미지원 (PR은 환영입니다🎉)
  ├── outputs		: 학습된 모델, 변환된 모델이 저장되는 위치
  ├── LICENSE
  └── README.md
```

## 동작 방법

### A. 서버 추론

1. 학습([training](training))을 통해 학습된 모델(saved_model)을 얻습니다.
2. saved_model을 서버 앱 폴더에([app-server](app-server))에 넣고, 서버를 실행합니다.
3. 모바일 앱([app-mobile](app-mobile)) 혹은 브라우저를 통해 mnist 추론 요청을 합니다.

### B. 온디바이스 추론

1. 학습([training](training))을 통해 학습된 모델(saved_model)을 얻습니다.
2. saved_model을 tflite로 변환합니다.
3. tflite 모델을 앱 프로젝트에 탑재합니다.
4. 모바일 앱([app-mobile](app-mobile))을 통해 mnist 온디바이스 추론을 합니다.

## TODO

- [x] [TF2](https://www.tensorflow.org)를 사용한 딥러닝 모델 학습 예제 추가
- [x] [Flask](https://flask.palletsprojects.com)를 사용한 딥러닝 모델 서빙 예제 추가
- [ ] [TensorFlowLiteSwift](https://www.tensorflow.org/lite/guide/ios)를 사용한 iOS 온디바이스 추론 예제 추가
- [ ] [Alamofire](https://github.com/Alamofire/Alamofire)를 사용한 iOS 서버 통신 추론 예제 추가
- [ ] 안드로이드 온디바이스 추론 예제 추가
- [ ] 안드로이드 서버 통신 추론 예제 추가

