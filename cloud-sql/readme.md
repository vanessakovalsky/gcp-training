## Créer l'instance

```
gcloud sql instances create flights --tier=db-n1-standard-1 --activation-policy=ALWAYS
```

## Définir le mot de passe :

```
gcloud sql users set-password root --host % --instance flights --password Passw0rd
```

## créez une variable d'environnement avec l'adresse IP de Cloud Shell :
```
export ADDRESS=$(wget -qO - http://ipecho.net/plain)/32
```

## Ajoutez l'instance Cloud Shell à la liste blanche pour l'autoriser à gérer votre instance SQL.

```
gcloud sql instances patch flights --authorized-networks $ADDRESS
```

## Adresse IP de l'instance SQL

```
MYSQLIP=$(gcloud sql instances describe flights --format="value(ipAddresses.ipAddress)")
```

## Créer la BDD

```
gcloud sql databases create bts --instance=flights
```

## Créer la structure de la table 

* On récupère le fichier sql 
```
curl https://raw.githubusercontent.com/vanessakovalsky/gcp-training/main/cloud-sql/create-table.sql --output create_table.sql
```

* Puis on lance la création de la table :=
```
mysql --host=$MYSQLIP --user=root  --password --verbose bts < create_table.sql
```

## Pour importer les données 

* On récupère le fichier 
```
 curl https://raw.githubusercontent.com/vanessakovalsky/gcp-training/main/cloud-sql/csv/flights_raw_201501.csv  --output flights_raw.csv
```

* On se connecte a mysql avec la bonne option pour pouvoir importer le fichier 
```
mysql --host=$MYSQLIP --user=root  --password --local-infile
```

* Puis dans l'invite de commande de mysql on utilise les requêtes suivantes :
```
USE bts;
LOAD DATA LOCAL INFILE '/home/vanessakovalsky/flights_raw.csv' 
INTO TABLE flights 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
```


