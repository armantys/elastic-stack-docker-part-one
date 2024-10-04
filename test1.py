from elasticsearch import Elasticsearch

# Initialiser le client Elasticsearch
es = Elasticsearch(["https://localhost:9200"], basic_auth=('elastic', 'changeme'), verify_certs=False)

# Supprimer l'index s'il existe déjà
if es.indices.exists(index="adresses_geo"):
    es.indices.delete(index="adresses_geo")
    print("Index 'adresses_geo' supprimé.")

# Créer un nouvel index avec 'location' en tant que geo_point
mapping = {
    "mappings": {
        "properties": {
            "num": { "type": "text" },
            "street": { "type": "text" },
            "postal_code": { "type": "long" },
            "city": { "type": "text" },
            "source": { "type": "text" },
            "location": { "type": "geo_point" }  # Définir le champ location en tant que geo_point
        }
    }
}

es.indices.create(index="adresses_geo", body=mapping)
print("Index 'adresses_geo' créé avec le mapping geo_point.")