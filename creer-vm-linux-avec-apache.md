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
