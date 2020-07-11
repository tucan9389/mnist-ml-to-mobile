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

from flask import Flask, request, flash, redirect, Response
from werkzeug.utils import secure_filename
import json, os
from inference import inference_werkzeug_image

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
TMP_FOLDER = 'tmp'

if not os.path.exists(TMP_FOLDER):
    os.mkdir(TMP_FOLDER)

app = Flask(__name__)
# app.secret_key = "super secret key"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/mnist', methods=['GET'])
def mnist_upload():
    return '''
            <!doctype html>
            <title>Upload new File</title>
            <h1>Upload new File</h1>
            <form method=post enctype=multipart/form-data>
              <input type=file name=mnist_image>
              <input type=submit value=Upload>
            </form>
            '''

@app.route('/mnist', methods=['POST'])
def mnist_prediction():
    # check if the post request has the file part
    if 'mnist_image' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['mnist_image']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)  # 업로드된 파일이 없으면 새로고침
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(TMP_FOLDER, filename)
        file.save(filepath)
        pred_number, pred_label = inference_werkzeug_image(filepath)
        result = {
            'filename': filename,
            'pred_number': pred_number,
            'pred_label': pred_label
        }
        if os.path.exists(filepath):
            os.remove(filepath)

        return Response(response=json.dumps(result),
                        status=200,
                        mimetype="application/json")



if __name__ == '__main__':
    app.debug = True
    app.run()
