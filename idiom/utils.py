from idiom.models import Idiom

def get_next_idioms(input_idiom, max_results=3):
    if len(input_idiom) != 4:
        return []
    last_char = input_idiom[-1]
    return Idiom.objects.filter(text__startswith=last_char)[:max_results]
