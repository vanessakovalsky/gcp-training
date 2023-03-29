# Ajout de stockage Cloud Storage à notre application

## Configuration de base

* Récupérer le code du dossier : end-migrate-datastore 
* Déployer votre application avec gcloud

## Ajout des dépendances

* Ajouter dans le fichier `requirements.txt` la ligne suivante :
```
google-cloud-storage
```
* Lancer l'installation des dépendances en local : `pip install -r requirements.txt`

## Ajout des imports et création des clients

* Dans le fichier `main.py` :
    * Remplacer les imports par les lignes suivantes :
    ```
    import io
    from datetime import datetime

    from flask import (Flask, abort, redirect, render_template,
            request, send_file, url_for)
    from werkzeug.utils import secure_filename

    import google.auth
    from google.cloud import exceptions, datastore, storage
    ```
    * Ajouter après la création du client de Datastore (en changeant l'id du projet poru mettre le votre) :
    ```
    gcs_client = storage.Client()
    PROJECT_ID = 'idprojet'
    BUCKET = PROJECT_ID+'.appspot.com'
    ```

## Ajouter la fonction d'envoi de fichier

* Dans le fichier main.py nous définissions une nouvelle fonction avec une route qui permet d'envoyer dans cloud storage les fichiers.
* Ajouter la fonction suivante après celle qui définit la route \ :
```
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
```
* Cette fonction permet de récupérer un fichier et de l'envoyer sur Cloud Storage.
* On ajoute l'enregistrement de l'adresse à la base de données, remplacer la fonction store_visit par le code suivant :
```
def store_visit(remote_addr, user_agent, upload_key):
    entity = datastore.Entity(key=ds_client.key('Visit'))
    entity.update({
        'timestamp': datetime.now(),
        'visitor': '{}: {}'.format(remote_addr, user_agent),
        'file_blob': upload_key
    })
    ds_client.put(entity)
```


## Ajout du formulaire d'envoi

* Commençons par modifier la route pour permettre l'envoi de fichier.
* Pour cela remplacer le code suivant 
```
@app.route('/')
def root():
    store_visit(request.remote_addr, request.user_agent)
    visits = fetch_visits(10)
    return render_template('index.html', visits=visits)
```
* Par :
```
@app.route('/', methods=['GET', 'POST'])
def root():
    'main application (GET/POST) handler'
    context = {}
    if request.method == 'GET':
        context['upload_url'] = url_for('upload')
    else:
        context['visits'] = fetch_visits(10)
    return render_template('index.html', **context)
```
* Ensuite nous allons modifier le fichier index.html du dossier template pour ajouter le formulaire, remplacer son contenu par :
```
<!doctype html>
<html>
<head>
<title>VisitMe Example</title>
</head>
<body>

<h1>VisitMe example</h1>
{% if upload_url %}

<h3>Welcome... upload a file? (optional)</h3>
<form action="{{ upload_url }}" method="POST" enctype="multipart/form-data">
    <input type="file" name="file"><p></p>
    <input type="submit"> <input type="submit" value="Skip">
</form>

{% else %}

<h3>Last 10 visits</h3>
<ul>
{% for visit in visits %}
<li>{{ visit.timestamp.ctime() }}
    <i><code>
    {% if visit.file_blob %}
        (<a href="/view/{{ visit.file_blob }}" target="_blank">view</a>)
    {% else %}
        (none)
    {% endif %}
    </code></i>
    from {{ visit.visitor }}
</li>
{% endfor %}
</ul>

{% endif %}

</body>
</html>
```
* A ce stade, le formulaire et le téléchargement fonctionne, il ne reste qu'à ajouter l'affichage de l'image.

## Ajout de l'affichage de l'image

* Dans le fichier main.py on ajoute une route pour afficher le fichier envoyer en ajoutant la route suivante :

```
@app.route('/view/<path:fname>')
def view(fname):
    'view uploaded blob (GET) handler'
    blob = gcs_client.bucket(BUCKET).blob(fname)
    try:
        media = blob.download_as_bytes()
    except exceptions.NotFound:
        abort(404)
    return send_file(io.BytesIO(media), mimetype=blob.content_type)
```
* Tout le code est à jour il ne reste qu'à redeployer notre application et la tester

## Déployer
* Déployer l'application avec gcloud :
```
gcloud app deploy
```
* Ouvrir l'application et envoyer un fichier.
* Une fois l'envoi terminé vous devriez arriver sur une page blanche, recharger la page, vous revenez sur le formulaire
* Pour afficher la liste, vous pouvez cliquer sur le bouton Skip et voir la liste avec un lien view pour les visites contenant un fichier.
* En cliquant sur le lien view vous accèder à votre fichier.
* Vous pouvez vérifier dans la console GCP dans Cloud Storage vous devriez avoir un bucket qui se nomme avec l'identifiant de votre projet, et à l'intérieur retrouver votre fichier.