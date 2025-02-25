# Palabras Ocultas en Patentes Argentinas

¡Mirá qué picardía! Las patentes Argentinas esconden palabras.

## Descripción

Este proyecto detecta y genera todas las posibles patentes argentinas (formato "AX NNN XX") que esconden palabras reales cuando reemplazás los números por letras. Por ejemplo, la patente "AB 064 DO" se puede leer como "ABOGADO" si reemplazás el 0 por O, el 6 por G y el 4 por A.

## Características

- Busca palabras de 7 letras en un diccionario de español
- Genera todas las combinaciones posibles de patentes que comienzan con A
- Convierte números a letras usando este mapeo:
  - 0 → O
  - 1 → I
  - 2 → Z
  - 3 → E
  - 4 → A
  - 5 → S
  - 6 → G
  - 7 → T
  - 8 → B
  - 9 → P
- Muestra barra de progreso durante la ejecución
- Guarda los resultados en formato JSON
- Calcula el tiempo total de ejecución

## Requisitos

- Python 3.6 o superior
- Biblioteca tqdm (`pip install tqdm`)

## Instalación

1. Cloná este repositorio:
```bash
git clone https://github.com/totoacee/patentes-argentinas.git
cd patentes-palabras-argentinas
```

2. Instalá las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

1. Coloca tu archivo de diccionario (listado-general.txt) en el directorio raíz o usa el que ya incluí.

2. Ejecuta el script:
```bash
python patentes_palabras.py
```

3. Los resultados se guardarán en `resultados_patrones.json`.

## Estructura de los resultados

El archivo JSON resultante tiene el siguiente formato:
```json
{
  "AB 064 DO": "ABOGADO",
  "AC 353 RO": "ACESERO",
  "...": "..."
}
```

## Cómo funciona

1. Lee un diccionario de palabras en español
2. Filtra sólo las palabras de 7 letras
3. Genera sistemáticamente todas las combinaciones posibles del patrón "AX NNN XX"
4. Para cada combinación, convierte los números a letras
5. Verifica si la palabra resultante existe en el diccionario
6. Guarda las coincidencias en un archivo JSON

## Licencia

Este proyecto está licenciado bajo [MIT License](LICENSE).

---

### Sobre mí

Este proyecto fue desarrollado por HIGHER®, mi emprendimiento personal especializado en desarrollo web.

¡Ayudame a seguir creando estas herramientas siguiéndome en Instagram!
[https://www.instagram.com/higherdesarrollo](https://www.instagram.com/higherdesarrollo)