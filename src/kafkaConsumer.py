from kafka import KafkaConsumer
from json import dumps, loads
import json
from s3fs import S3FileSystem
from dotenv import load_dotenv
from time import sleep
import os

load_dotenv('.env')

consumer = KafkaConsumer(
                'NYA-stock-data',
                bootstrap_servers=[os.getenv('VM_IP')],
                value_deserializer=lambda x: loads(x.decode('utf-8'))
                )
