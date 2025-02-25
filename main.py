import itertools
import time
import json
from typing import List, Set, Dict
from tqdm import tqdm

def leer_diccionario(nombre_archivo: str) -> List[str]:
    """
    Lee el archivo de diccionario y devuelve una lista de palabras
    """
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            return [linea.strip() for linea in f.readlines() if linea.strip()]
    except FileNotFoundError:
        print(f"Error: No se encontro el archivo '{nombre_archivo}'")
        exit(1)
    except Exception as e:
        print(f"Error al leer el archivo: {str(e)}")
        exit(1)

def crear_diccionario_numeros_letras() -> Dict[str, str]:
    """
    Crea un diccionario de mapeo de numeros a letras posibles
    """
    return {
        "0": "O",
        "1": "I",
        "2": "Z",
        "3": "E",
        "4": "A",
        "5": "S",
        "6": "G",
        "7": "T",
        "8": "B",
        "9": "P"
    }

def obtener_palabras_siete_letras(palabras: List[str]) -> Set[str]:
    """
    Filtra palabras de exactamente 7 letras del diccionario
    """
    palabras_siete = set()
    print("Filtrando palabras de 7 letras...")
    for palabra in tqdm(palabras):
        palabra = palabra.strip().lower()
        if palabra.isalpha() and len(palabra) == 7:
            palabras_siete.add(palabra)
    return palabras_siete

def patron_a_palabra(patron: str, num_a_letra: Dict[str, str]) -> str:
    """
    Convierte un patrón tipo "AB 123 CD" a una palabra potencial
    Ejemplo: "AB 064 DO" -> "abogado"
    """
    patron = patron.lower()
    palabra = ""
    for char in patron:
        if char.isdigit():
            palabra += num_a_letra[char].lower()
        elif char != " ":
            palabra += char
    return palabra

def calcular_total_combinaciones() -> int:
    """
    Calcula el numero total de combinaciones posibles para la barra de progreso
    """
    letras = 26  # A-Z
    numeros = 10  # 0-9
    return letras * (numeros ** 3) * (letras ** 2)

def generar_y_verificar_patrones(diccionario_palabras: Set[str]) -> Dict[str, str]:
    """
    Genera y verifica todas las combinaciones posibles del patrón "AX NNN XX"
    Devuelve un diccionario con el formato {patron: palabra}
    """
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"
    num_a_letra = crear_diccionario_numeros_letras()
    palabras_encontradas = {}
    
    total_combinaciones = calcular_total_combinaciones()
    print(f"\nGenerando y verificando {total_combinaciones:,} combinaciones posibles...")
    
    with tqdm(total=total_combinaciones) as pbar:
        for segunda_letra in letras:
            for n1 in numeros:
                for n2 in numeros:
                    for n3 in numeros:
                        for ultima_letra1 in letras:
                            for ultima_letra2 in letras:
                                patron = f"A{segunda_letra} {n1}{n2}{n3} {ultima_letra1}{ultima_letra2}"
                                palabra_potencial = patron_a_palabra(patron, num_a_letra)
                                if palabra_potencial in diccionario_palabras:
                                    palabras_encontradas[patron] = palabra_potencial.upper()
                                pbar.update(1)
    
    return palabras_encontradas

def guardar_resultados_json(resultados: Dict[str, str], tiempo_ejecucion: float):
    """
    Guarda los resultados en un archivo JSON y muestra un resumen
    """
    nombre_archivo = "resultados_patrones.json"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(resultados, f, indent=2, ensure_ascii=False)
    
    print("\nResultados:")
    print("-" * 50)
    for patron, palabra in resultados.items():
        print(f"Patrón: {patron} -> Palabra: {palabra}")
    print("-" * 50)
    print(f"Se encontraron {len(resultados)} coincidencias")
    print(f"Tiempo total de ejecución: {tiempo_ejecucion:.2f} segundos")
    print(f"Resultados guardados en '{nombre_archivo}'")

if __name__ == "__main__":
    tiempo_inicio = time.time()
    
    print("Leyendo archivo de diccionario...")
    palabras = leer_diccionario("listado-normalizado.txt")
    print(f"Se leyeron {len(palabras):,} palabras del archivo")
    
    palabras_siete = obtener_palabras_siete_letras(palabras)
    print(f"Se encontraron {len(palabras_siete):,} palabras de 7 letras")
    
    resultados = generar_y_verificar_patrones(palabras_siete)
    
    tiempo_total = time.time() - tiempo_inicio
    guardar_resultados_json(resultados, tiempo_total)