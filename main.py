# Import the required module for text  
# to speech conversion 
from gtts import gTTS 
import json
import os

data = {}
words = []


def get_keys_json(file_name):
    with open(file_name,  encoding='utf-8') as f:
        data = json.load(f)

    for key in data.keys():
        words.append(key)

    return words, data

words, data = get_keys_json('eslestirme.json')
# print(data[words[0]][0]['ar'])


def save_tts(text, file_name, format='wav', language='ar', output_dir='output', ):
    myobj = gTTS(text=text, lang=language, slow=False) 
    # Create a directory in current working directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    myobj.save(f"{output_dir}/{file_name}.{format}")



for word in words:
    for i in range(len(data[word])):
        save_tts(data[word][i]['ar'], file_name=str(i+1), output_dir=f"output/{word}")
    