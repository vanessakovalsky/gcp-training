## Créer la BDD

```
gcloud sql databases create bts --instance=flights

```

## Importer les données 

mysql --host=$MYSQLIP --user=root  --password --verbose bts < create_table.sql


