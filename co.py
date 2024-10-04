from elasticsearch import Elasticsearch

# Connexion à ElasticSearch (remplace les valeurs selon ton cas)
es = Elasticsearch(["https://localhost:9200"], basic_auth=('elastic', 'changeme'), verify_certs=False)

# Requête pour récupérer les documents d'un index
result = es.search(index="adresses_geo", body={"query": {"match_all": {}}})

# Parcourir les résultats
for doc in result['hits']['hits']:
    data = doc['_source']
    print(f"Ville: {data['city']}")
    print(f"Rue: {data['street']}, Numéro: {data['num']}")
    print(f"Code Postal: {data['postal_code']}")
    print(f"Coordonnées: Latitude {data['location']['lat']}, Longitude {data['location']['lon']}")
    print(f"Source: {data['source']}")
    print("="*30)