import base64
import json
from google.cloud import bigquery

def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
        event (dict): Event payload.
        context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)
    load = [json.loads(pubsub_message)]
    tweet = load[0]['text']
    wordcount = len(tweet.split()) 
    load[0]['word_count'] = wordcount
    client = bigquery.Client()
    dataset_ref = client.dataset('twitter')
    table_ref = dataset_ref.table('twitter_data')
    table = client.get_table(table_ref)
    client.insert_rows(table,load)