import json
from kafka import KafkaProducer
import time

# Configuration du producteur Kafka
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Fonction pour lire et publier les données en continu
def publish_data():
    #with open('twitter_training.csv','r',errors='ignore') as file:
    with open('twitter_validation.csv','r',errors='ignore') as file:
        for line in file:
            # Ignorer les lignes vides
            if not line.strip():
                continue
            
            # Convertir la ligne CSV en objet JSON
            json_data = convert_to_json(line)
            if json_data:
                # Envoyer l'objet JSON au topic Kafka
                producer.send('tweets', json.dumps(json_data).encode('UTF-8'))
            
                # Ajoutez un délai entre chaque envoi de message (1 seconde ici)
                time.sleep(0.5)
            
                # Assurez-vous que les messages sont envoyés immédiatement
                producer.flush()  

# Fonction pour convertir une ligne CSV en objet JSON
def convert_to_json(line):
    # Supprimer les caractères de fin de ligne
    line = line.strip()
    
    # Diviser la ligne en colonnes en utilisant la virgule comme délimiteur
    columns = line.split(',')
    
    # Vérifier s'il y a exactement 4 colonnes
    if len(columns) == 4:
        # Créer un dictionnaire JSON à partir des colonnes
        json_data = {
            'Tweet_ID': columns[0], 
            'Entity': columns[1],
            'sentiment': columns[2],  
            'tweet_content': columns[3]
        }
        return json_data
    else:
        return None  # Retourner None si la ligne ne contient pas les 4 éléments requis

# Publier les données en continu
publish_data()
