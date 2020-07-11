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

import tfcoreml
import tensorflow as tf
import os

saved_model_dir_path = '../../outputs/saved_model'
saved_model_path = f'{saved_model_dir_path}/mnist_001'
mlmodel_dir_path = '../../outputs/mlmodel'
mlmodel_path = f'{mlmodel_dir_path}/mnist_001.mlmodel'

model = tf.keras.models.load_model(saved_model_path)
model.summary()
last_layer = model.layers[-1]
print(last_layer)

if not os.path.exists(mlmodel_dir_path):
    os.mkdir(mlmodel_dir_path)

input_name_shape_dict = {
   model.input_names[0]: list(model.input_shape)
}
output_feature_names = model.output_names

# saved_model_path = f'{saved_model_path}/saved_model.pb'
mlmodel = tfcoreml.convert(tf_model_path=saved_model_path,
                           mlmodel_path=mlmodel_path,
                           input_name_shape_dict={'input_2': [1, 28, 28, 1]},
                           output_feature_names=['Identity'],#['dense_1/Identity'],
                           minimum_ios_deployment_target='13')
