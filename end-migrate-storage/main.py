# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import io
from datetime import datetime

from flask import (Flask, abort, redirect, render_template,
            request, send_file, url_for)
from werkzeug.utils import secure_filename

from google.cloud import exceptions, datastore, storage

app = Flask(__name__)
ds_client = datastore.Client()
gcs_client = storage.Client()
PROJECT_ID = 'cursusm2i-2023'
BUCKET = PROJECT_ID+'.appspot.com'

def store_visit(remote_addr, user_agent, upload_key):
    entity = datastore.Entity(key=ds_client.key('Visit'))
    entity.update({
        'timestamp': datetime.now(),
        'visitor': '{}: {}'.format(remote_addr, user_agent),
        'file_blob': upload_key
    })
    ds_client.put(entity)

def fetch_visits(limit):
    query = ds_client.query(kind='Visit')
    query.order = ['-timestamp']
    return query.fetch(limit=limit)


@app.route('/', methods=['GET', 'POST'])
def root():
    'main application (GET/POST) handler'
    context = {}
    if request.method == 'GET':
        context['upload_url'] = url_for('upload')
    else:
        context['visits'] = fetch_visits(10)
    return render_template('index.html', **context)
    

@app.route('/upload', methods=['POST'])
def upload():
    'Upload blob (POST) handler'
    fname = None
    upload = request.files.get('file', None)
    if upload:
        fname = secure_filename(upload.filename)
        blob = gcs_client.bucket(BUCKET).blob(fname)
        blob.upload_from_file(upload, content_type=upload.content_type)
    store_visit(request.remote_addr, request.user_agent, fname)
    return redirect(url_for('root'), code=307)

@app.route('/view/<path:fname>')
def view(fname):
    'view uploaded blob (GET) handler'
    blob = gcs_client.bucket(BUCKET).blob(fname)
    try:
        media = blob.download_as_bytes()
    except exceptions.NotFound:
        abort(404)
    return send_file(io.BytesIO(media), mimetype=blob.content_type)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
