# Créer une VM Linux avec Compute Engine et lancer apache

## Pré-requis 

* avoir accès à la console GCP avec son compte
* avoir créé un projet
* avoir activer compute engine sur le projet


## Créer la VM Linux     

* Accéder à la page Créer une instance
* Dans la section Disque de démarrage, cliquez sur Modifier pour commencer à configurer le disque de démarrage.
* Dans l'onglet Public images, sélectionnez Ubuntu dans la liste Système d'exploitation.
* Choisissez Ubuntu 20.04 LTS dans la liste Version.
* Cliquez sur Select (Sélectionner).
* Dans la section Pare-feu, sélectionnez Autoriser le trafic HTTP.
* Pour créer la VM, cliquez sur Créer.

Patientez un court instant le temps que l'instance démarre. Une fois l'instance prête, elle est répertoriée sur la page Instances de VM avec une icône d'état verte.

Compute Engine attribue le rôle roles/compute.instanceAdmin à l'utilisateur qui crée la VM. Compute Engine ajoute également cet utilisateur au groupe sudo.

## Se connecter à l'instance de VM

* Dans la console Google Cloud, accédez à la page Instances de VM.
* Dans la liste des instances de machine virtuelle, cliquez sur SSH sur la ligne de l'instance à laquelle vous souhaitez vous connecter.

[](https://cloud.google.com/static/docs/images/establish-ssh-connection-1.png?hl=fr)

## Installer Apache

Dans Google Cloud Console, accédez à la page Instances de VM.
* Accéder à la page "Instances de VM" 
* Pour vous connecter à la VM Linux que vous venez de créer, cliquez sur SSH sur la ligne de la VM.
* Pour mettre à jour les packages disponibles et installer le package apache2, utilisez le gestionnaire de packages de ce système d'exploitation. Pour mettre à jour une VM Ubuntu, exécutez la commande suivante :
```
sudo apt update && sudo apt -y install apache2
```
* Après l'installation d'Apache, le système d'exploitation lance automatiquement le serveur Apache.
* Vérifiez qu'Apache est en cours d'exécution :
```
sudo systemctl status apache2
```
Écrasez la page Web par défaut du serveur Web Apache :
```
echo '<!doctype html><html><body><h1>Hello World!</h1></body></html>' | sudo tee /var/www/html/index
```

## Ouverture du pare-feu
* Afin d'accéder à notre page web il est necéssaire d'ouvrir le port 80 du pare feu utilisé par notre VM

## Tester le serveur

* Vérifiez que votre VM envoie du trafic vers son adresse IP externe.
* Dans Google Cloud Console, accédez à la page Instances de VM.
* Accéder à la page "Instances de VM"
* Copiez l'adresse IP externe de votre VM sous la colonne Adresse IP externe.
* Dans un navigateur, accédez à http://[EXTERNAL_IP]. Ne vous connectez pas à l'aide de https, car cela renvoie une erreur Connection Refused au serveur.
* La page "Hello World!" doit s'afficher.

## Nettoyage

Pour éviter que les ressources utilisées sur cette page soient facturées sur votre compte Google Cloud, procédez comme suit :

* Dans Google Cloud Console, accédez à la page Instances de VM.
* Accéder à la page "Instances de VM"
* Cliquez sur le nom de l'instance que vous avez créée.
* En haut de la page de détails de l'instance, cliquez sur Delete (Supprimer).
