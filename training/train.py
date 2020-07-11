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

from common import show_mnist_img, show_training_result, mkdir_ifneeded

# =============================================
# ================= 데이터셋 로드 =================
# =============================================
mnist = tf.keras.datasets.mnist

# download and load mnist dataset
(x_train, y_train), (x_valid, y_valid) = mnist.load_data()

# normalize
x_train = x_train / 255.0
x_valid = x_valid / 255.0

x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_valid = x_valid.reshape(x_valid.shape[0], 28, 28, 1)

# 데이터셋 확인
for i in range(4):
    show_mnist_img(x_train, i)

# =============================================
# ================== 모델 구성 ==================
# =============================================
model = tf.keras.models.Sequential([
    tf.keras.layers.InputLayer(input_shape=(28, 28, 1)),
    tf.keras.layers.Conv2D(64, kernel_size=(3, 3)),
    tf.keras.layers.ReLU(),
    tf.keras.layers.Conv2D(64, kernel_size=(3, 3)),
    tf.keras.layers.ReLU(),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128),
    tf.keras.layers.ReLU(),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.summary()

# =============================================
# ================== 학습 준비 ==================
# =============================================
model.compile(optimizer=tf.keras.optimizers.RMSprop(),
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['acc'])

# =============================================
# ==================== 학습 ====================
# =============================================
history = model.fit(x_train, y_train,
                    epochs=5,
                    validation_data=(x_valid, y_valid))

# =============================================
# ================= 결과 확인 ===================
# =============================================

show_training_result(history)

for i in range(10):
    show_mnist_img(x_valid, i)

    valid_img_vec = x_valid[i]
    valid_img_vec = np.expand_dims(valid_img_vec, axis=0)
    pred_label = model(valid_img_vec, training=False)
    pred_number = np.argmax(pred_label)
    gt_number = y_valid[i]
    print(f"실제 숫자: {gt_number}, 예측된 숫자: {pred_number}")

# =============================================
# ================= 모델 저장 ===================
# =============================================
saved_model_dir_path = '../outputs/saved_model'
mkdir_ifneeded(saved_model_dir_path)
saved_model_path = f'{saved_model_dir_path}/mnist_001'

model.save(saved_model_path)
