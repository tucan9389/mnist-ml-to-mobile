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
import os

model_name = 'mnist_001'
saved_model_dir_path = '../../outputs/saved_model'
saved_model_path = f'{saved_model_dir_path}/{model_name}'
tflite_dir_path = '../../outputs/tflite'
tflite_model_path = f'{tflite_dir_path}/{model_name}.tflite'

if not os.path.exists(tflite_dir_path):
    os.mkdir(tflite_dir_path)

# Convert the model.
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_path)
tflite_model = converter.convert()

# Save the TF Lite model.
with tf.io.gfile.GFile(tflite_model_path, 'wb') as f:
  f.write(tflite_model)
