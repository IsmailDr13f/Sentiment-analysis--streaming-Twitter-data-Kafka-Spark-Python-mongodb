
import json
import re

def convert_to_bytes(line):
    line = line.strip()
    columns = line.split(',')
    bytes_data = {
        'Tweet ID': columns[0],
        'Entity': columns[1],
        'sentiment': columns[2],
        'tweet_content': columns[3]
    }
    return bytes_data

def bytes_to_json(input_bytes):
    input_str = str(input_bytes)
    cleaned_string = input_str[2:-1]
    cleaned_string = cleaned_string.replace('\\', '\\\\')
    cleaned_string = cleaned_string.replace('\\\\"', ' ')
    cleaned_string = cleaned_string.replace('(', '')
    cleaned_string = cleaned_string.replace(')', '')
    cleaned_string = cleaned_string.replace(';', '')
    return json.loads(cleaned_string)

def clean_tweet_content(tweet: str) -> str:
    tweet = re.sub(r'http\S+', '', tweet)
    tweet = re.sub(r'bit.ly/\S+', '', tweet)
    tweet = tweet.strip('[link]')
    tweet = re.sub(r'(RT\s@[A-Za-z]+[A-Za-z0-9-_]+)', '', tweet)
    tweet = re.sub(r'(@[A-Za-z]+[A-Za-z0-9-_]+)', '', tweet)
    tweet = tweet.replace('\\\\', '')
    tweet = tweet.replace('\\',' ')
    my_punctuation = '!"$%&\'()*+,-./:;<=>?[\\]^_`{|}~•@â«»—'
    tweet = re.sub('[' + my_punctuation + ']+', ' ', tweet)
    tweet = re.sub(r'([0-9]+)', '', tweet)
    tweet = re.sub(r'(#[A-Za-z]+[A-Za-z0-9-_]+)', '', tweet)
    tweet = re.sub(r'\s+', ' ', tweet)
    tweet = tweet.lower()
    tweet = re.sub(r'\bim\b', '', tweet)
    return tweet.strip()
