# Créer et utiliser un bucket de stockage

## Pré-requis

* Avoir accès à un projet GCP 

## Créer un bucket

Les buckets sont les conteneurs de base dans lesquels sont stockées vos données dans Cloud Storage.

* Pour créer un bucket :

  *  Dans la console Google Cloud, accédez à la page du Navigateur Cloud Storage.
  *  Accéder à la page "Buckets"
  *  Cliquez sur Create a bucket (Créer un bucket) pour ouvrir le formulaire de création de bucket.
  *  Formulaire de création d'un bucket.
  *  Saisissez les informations relatives à votre bucket et cliquez sur Continuer à chaque étape :
    * Saisissez un nom unique pour le bucket: N'incluez aucune information sensible dans le nom des buckets, car leur espace de noms est global et visible par tous.
    * Choisissez Région pour le champ Type d'emplacement et us-east1 (Caroline du Sud) pour le champ Emplacement.
    * Choisissez Standard comme classe de stockage par défaut.
    * Choisissez Uniforme pour le champ Contrôle des accès.
    * Décochez la case Appliquer la protection contre l'accès public sur ce bucket, ce qui vous permettra de partager l'objet ultérieurement.
    * Choisissez Aucun pour les outils de protection.
  * Cliquez sur Create (Créer).

* Voilà ! Vous venez de créer un bucket Cloud Storage.

## Importer un objet dans le bucket

![](https://cloud.google.com/static/storage/images/kitten.png?hl=fr)

* Pour transférer l'image ci-dessus dans votre nouveau bucket :
  * Cliquez avec le bouton droit sur l'image ci-dessus et téléchargez-la sur votre ordinateur.
  * Sur la page du bucket Cloud Storage, cliquez sur le nom du bucket que vous avez créé.
  * Dans l'onglet Objets, cliquez sur Importer des fichiers.
  * Dans la boîte de dialogue de sélection de fichier, accédez au fichier que vous avez téléchargé et sélectionnez-le.
* Une fois le transfert terminé, vous devez voir le nom du fichier et des informations le concernant, telles que sa taille et son type.

## Télécharger l'objet

* Pour télécharger l'image depuis votre bucket, cliquez sur Télécharger file_download.

## Partager l'objet

* Pour autoriser l'accès public au bucket et créer une URL accessible au public pour l'image :
  * Cliquez sur l'onglet Autorisations au-dessus de la liste des fichiers.
  * Cliquez sur le bouton Accorder l'accès pour ajouter un compte principal.
  * Le volet Ajouter des comptes principaux s'affiche.
  * Dans le champ Nouveaux comptes principaux, saisissez allUsers.
  * Dans la liste déroulante Sélectionner un rôle, sélectionnez Cloud Storage > Lecteur des objets de l'espace de stockage.
  * Cliquez sur Enregistrer.
  * Dans la fenêtre Voulez-vous vraiment rendre cette ressource publique ?, cliquez sur Autoriser l'accès public.
* Pour vérifier, cliquez sur l'onglet Objets pour revenir à la liste des objets. La colonne Accès public de votre objet doit indiquer Public sur Internet. Le bouton Copier l'URL fournit une URL partageable semblable à la suivante : https://storage.googleapis.com/YOUR_BUCKET_NAME/kitten.png
* Pour supprimer l'accès public du bucket et cesser de partager l'image publiquement :
  * Cliquez sur l'onglet Autorisations au-dessus de la liste des objets.
  * Cochez la case associée à l'entrée contenant allUsers dans la colonne Compte principal.
  * Cliquez sur le bouton Supprimer l'accès.
  * Dans la boîte de dialogue qui s'affiche, cliquez sur Confirmer.

* Dans l'onglet Objets, vous devriez constater que l'image ne dispose plus d'un bouton Copier l'URL.

Remarque : Une fois que vous avez supprimé l'accès public à l'image, vous pouvez toujours accéder à une version mise en cache de celle-ci pendant un certain temps.

## Créer des dossiers

* Dans l'onglet Objets, cliquez sur Créer un dossier.
* Saisissez folder1 dans le champ Nom et cliquez sur Créer.
* Le dossier s'affiche alors dans le bucket avec une icône de dossier pour le distinguer des objets.
* Créez un sous-dossier et importez un fichier dans celui-ci :
  * Cliquez sur folder1.
  * Cliquez sur Créer un dossier.
  * Saisissez folder2 dans le champ Nom et cliquez sur Créer.
  * Cliquez sur folder2.
  * Cliquez sur Importer des fichiers.
  * Dans la fenêtre de sélection de fichier, accédez à la capture d'écran que vous avez téléchargée et sélectionnez-la.
* Une fois le transfert terminé, vous devriez voir le nom du fichier et des informations le concernant, telles que sa taille et son type.

## Supprimer les objets

* Cliquez sur la flèche à côté de Détails du bucket pour revenir au niveau des buckets.
* Sélectionnez le bucket.
* Cochez la case à côté de folder1.
* Cliquez sur le bouton Supprimer.
* Dans la fenêtre qui s'ouvre, saisissez le nom du dossier à supprimer.
* Cliquez sur Supprimer pour supprimer définitivement le dossier, ainsi que tous les objets et sous-dossiers qu'il contient.

## Nettoyage

* Ouvrez la page "Buckets Cloud Storage" dans la console Google Cloud.
* Ouvrir la page "Buckets"
* Cochez la case à côté du bucket que vous avez créé.
* Cliquez sur Supprimer.
* Dans la fenêtre qui s'affiche, confirmez que vous souhaitez supprimer le bucket.
* Cliquez sur Supprimer.

## Pour aller plus loin :
* Pour découvrir plus de fonctionnalité vous pouvez par exemple héberger un site statique sur Compute storage : https://cloud.google.com/storage/docs/hosting-static-website?hl=fr  
