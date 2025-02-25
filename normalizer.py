import unidecode

def normalize_word(word):
    word = word.split("/")[0]
    
    word = unidecode.unidecode(word)
    
    return word.lower().strip()

def process_file(input_file, output_file):
    normalized_words = set()
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            for line in f:
                word = normalize_word(line)
                if word:
                    normalized_words.add(word)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {input_file}")
        return
    except Exception as e:
        print(f"Error al leer el archivo: {str(e)}")
        return

    normalized_words = sorted(normalized_words)
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for word in normalized_words:
                f.write(word + '\n')
        print(f"Proceso completado. Se guardaron {len(normalized_words)} palabras únicas en {output_file}")
    except Exception as e:
        print(f"Error al escribir el archivo: {str(e)}")

if __name__ == "__main__":
    input_file = "listado-general.txt"
    output_file = "listado-normalizado.txt"
    process_file(input_file, output_file)