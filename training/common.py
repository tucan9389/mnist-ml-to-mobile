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

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def show_mnist_img(dataset, index):
    test_img_vec = dataset[index]
    pixels = test_img_vec.reshape((28, 28))
    plt.title(f'{index} image')
    plt.imshow(pixels, cmap='gray')
    plt.show()

def show_training_result(history):
    # Retrieve a list of accuracy results on training and validation data
    # sets for each training epoch
    acc = history.history['acc']
    val_acc = history.history['val_acc']

    # Retrieve a list of list results on training and validation data
    # sets for each training epoch
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    # Get number of epochs
    epochs = range(len(acc))

    # Plot training and validation accuracy per epoch
    plt.plot(epochs, acc, label='training set acc')
    plt.plot(epochs, val_acc, label='validation set acc')
    plt.title('Accuracy')
    plt.legend(loc='best')

    plt.figure()

    # Plot training and validation loss per epoch
    plt.plot(epochs, loss, label='training set loss')
    plt.plot(epochs, val_loss, label='validation set loss')
    plt.title('Loss')
    plt.legend(loc='best')

    plt.show()

def mkdir_ifneeded(path):
    import os
    dirs = path.split('/')
    middle_path = dirs[0]
    for dir in dirs:
        if dir == dirs[0]:
            continue
        else:
            middle_path += f'/{dir}'
            if not os.path.exists(middle_path):
                os.mkdir(middle_path)

