import json
import logging
from idiom.models import Idiom, Pinyin

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_idioms():
    try:
        with open('transformed_idioms.json', 'r', encoding='utf-8') as f:
            idioms = json.load(f)
            logging.info("Successfully loaded idioms from transformed_idioms.json.")
            
            for idiom in idioms:
                # First, create or get the Idiom instance
                idiom_obj, idiom_created = Idiom.objects.get_or_create(
                    text=idiom['text'],
                    defaults={
                        'meaning': idiom.get('meaning'),
                        'example': idiom.get('example'),
                        'derivation': idiom.get('derivation'),
                        'weight': idiom.get('weight', 1),  # Default weight if not provided
                        'notes': idiom.get('notes', ''),  # Default empty string if not provided
                    }
                )

                # Now create or get the Pinyin instance, linking it to the Idiom instance
                pinyin_obj, pinyin_created = Pinyin.objects.get_or_create(
                    idiom=idiom_obj,  # This must be set since it's a OneToOneField
                    defaults={
                        'pinyin_text': idiom.get('pinyin'),
                        'tone_marks': idiom.get('tone_marks'),
                    }
                )

                if idiom_created:
                    logging.info(f"Created new idiom: {idiom['text']}")
                else:
                    logging.info(f"Idiom already exists: {idiom['text']}")

                if pinyin_created:
                    logging.info(f"Created new pinyin: {idiom.get('pinyin')}")
                else:
                    logging.info(f"Pinyin already exists: {idiom.get('pinyin')}")

    except FileNotFoundError:
        logging.error("The file transformed_idioms.json was not found.")
    except json.JSONDecodeError:
        logging.error("Error decoding JSON from the file.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

# Call the function (if needed)
# load_idioms()



import json

# Define the input and output file paths
input_file_path = r'C:\Users\recur\Desktop\WORK\chengyu_game\idiom.json'
output_file_path = r'C:\Users\recur\Desktop\WORK\chengyu_game\transformed_idioms.json'

# Read the original JSON data
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    idioms = json.load(input_file)

# Transform the data
transformed_idioms = []
for idiom in idioms:
    transformed_idiom = {
        'text': idiom['word'],  # Rename 'word' to 'text'
        'pinyin': idiom['pinyin'],
        'meaning': idiom['explanation'],  # Rename 'explanation' to 'meaning'
        'example': idiom['example'],
        'derivation': idiom['derivation']
    }
    transformed_idioms.append(transformed_idiom)

# Save the transformed data to a new JSON file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(transformed_idioms, output_file, ensure_ascii=False, indent=4)

print(f'Transformed JSON data has been saved to {output_file_path}')
