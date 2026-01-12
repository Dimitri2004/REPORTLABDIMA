# Proyecto de Aprendizaje con ReportLab

Este repositorio contiene una serie de scripts en Python como parte de un proyecto de repaso y aprendizaje para generar archivos PDF utilizando la biblioteca `reportlab`.

## Descripción

El objetivo principal de este proyecto es explorar las capacidades de `reportlab` para la creación y manipulación de documentos PDF de forma programática. Cada script se enfoca en una funcionalidad diferente de la biblioteca.

## Scripts del Proyecto

A continuación se detalla el propósito de cada script:

### `ExemplosReportLab.py`

Este script introduce los conceptos básicos del módulo `reportlab.pdfgen.canvas`.

- **Funcionalidad:**
  - Crea un documento PDF (`1ºprimeiroDocumento.pdf`).
  - Dibuja cadenas de texto en coordenadas específicas (`drawString`).
  - Inserta imágenes (PNG y JPG) en el documento (`drawImage`).
- **Resultado:** Genera el archivo `1ºprimeiroDocumento.pdf`.

### `ExemplosReportLab2.py`

Este script explora el uso de objetos `Drawing` del módulo `reportlab.graphics`.

- **Funcionalidad:**
  - Crea un "lienzo" (`Drawing`) donde se pueden añadir formas.
  - Añade objetos de imagen (`Image`) al lienzo.
  - Demuestra transformaciones de objetos como traslación (`translate`), rotación (`rotate`) y escalado (`scale`).
- **Resultado:** Genera el archivo `2ºexemploDrawing.pdf`.

### `ExemplosReportLab3.py`

Este script se centra en la manipulación avanzada de texto con `canvas`.

- **Funcionalidad:**
  - Utiliza un objeto `beginText` para un control más preciso del texto.
  - Establece el punto de origen (`setTextOrigin`), la fuente (`setFont`) y el color del texto (`setFillGray`).
  - Escribe bloques de texto y líneas individuales (`textLine`, `textLines`).
  - Itera sobre las fuentes disponibles en `reportlab` y muestra un ejemplo de cada una.
- **Resultado:** Genera el archivo `3ºtextoCanvas.pdf`.

## Archivos

### Scripts
- `ExemplosReportLab.py`
- `ExemplosReportLab2.py`
- `ExemplosReportLab3.py`

### PDFs Generados
- `1ºprimeiroDocumento.pdf`
- `2ºexemploDrawing.pdf`
- `3ºtextoCanvas.pdf`

### Recursos
- `box-pixilart.png` (Imagen utilizada en los ejemplos)
- `equis16x216.jpg` (Imagen utilizada en los ejemplos)

## Cómo Empezar

Para ejecutar los scripts y generar los archivos PDF, sigue estos pasos:

### Prerrequisitos

- Tener Python instalado.
- Instalar la biblioteca `reportlab`.

### Instalación

Abre una terminal y ejecuta el siguiente comando para instalar `reportlab`:

```bash
pip install reportlab
```

### Ejecución

Navega al directorio del proyecto y ejecuta los scripts individualmente:

```bash
python ExemplosReportLab.py
python ExemplosReportLab2.py
python ExemplosReportLab3.py
```

Cada script generará su correspondiente archivo PDF en el directorio raíz del proyecto.
