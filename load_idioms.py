import json
from idiom.models import Idiom

def load_idioms():
    with open('idioms.json', 'r', encoding='utf-8') as f:
        idioms = json.load(f)
        for idiom in idioms:
            Idiom.objects.get_or_create(text=idiom['text'], meaning=idiom.get('meaning'))


