# Copyright 2020 Doyoung Gwak (tucan.dev@gmail.com)
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ======================
# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np
import cv2
from skimage import color, io

saved_model_dir_path = '../outputs/saved_model'
saved_model_path = f'{saved_model_dir_path}/mnist_001'
model = tf.keras.models.load_model(saved_model_path)

print(f'모델 입력 shape: {model.input_shape}')

'''
params:
- filepath: 
    - 설명: 임시 이미지 파일이 저장된 경로
    - 타입: str
returns:
- pred_number:
    - 설명: 0~9 사이의 추론된 숫자
    - 타입: int
- pred_label:
    - 설명: 카테고리별 0.0~1.0 사이의 확률값 리스트
    - 타입: [float]
'''
def inference_werkzeug_image(filepath):
    img = color.rgb2gray(io.imread(filepath))
    img = np.array(img)
    img = cv2.resize(img, (28, 28))
    img = np.float32(img)
    img = img / 255.0

    if len(model.input_shape) == 4:
        input_shape = (1, 28, 28, 1)
    elif len(model.input_shape) == 3:
        input_shape = (1, 28, 28)
    else:
        assert False, f"len(model.input_shape)은 3 혹은 4 이어야합니다. {len(model.input_shape)} 길이는 지원하지 않습니다."

    img = np.reshape(img, input_shape)

    # import matplotlib.pyplot as plt
    # plt.imshow(np.reshape(img, (28, 28)), cmap='gray', interpolation='none')
    # plt.show()

    # 모델 추론
    pred_label = model.predict(img)

    pred_number = np.argmax(pred_label)
    return int(pred_number), pred_label.tolist()
