from idiom.models import Idiom

def get_next_idioms(input_idiom, max_results=3):
    if len(input_idiom) != 4:
        return []

    last_char = input_idiom[-1]
    
    # Attempt to find idioms starting with the last character
    idioms_by_last_char = Idiom.objects.filter(text__startswith=last_char)[:max_results]
    
    if idioms_by_last_char.exists():
        return idioms_by_last_char

    # If no idioms were found, try to get the Pinyin for the last character
    last_idiom = Idiom.objects.filter(text=input_idiom).first()
    if last_idiom and last_idiom.pinyin:
        last_pinyin = last_idiom.pinyin.pinyin_text
        # Fetch the last syllable from the Pinyin
        # Split the Pinyin string and get the last syllable
        last_pinyin_syllable = last_pinyin.split()[-1]  # Get the last Pinyin syllable
        
        # Attempt to find idioms starting with the last syllable of the Pinyin
        idioms_by_last_pinyin = Idiom.objects.filter(pinyin__pinyin_text__startswith=last_pinyin_syllable)[:max_results]
        return idioms_by_last_pinyin

    # If still no idioms found, return an empty list
    return []
