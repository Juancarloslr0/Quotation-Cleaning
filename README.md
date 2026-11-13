# Normalizador de cotizaciones

**English summary:** A Jupyter-based workflow for cleaning supplier quotations, classifying rows, assigning sections, grouping duplicate line items, and preparing a four-column table for Airtable.

## Qué problema resuelve

Las cotizaciones de proveedores en Excel pueden mezclar partidas, encabezados de apartados, filas incompletas, importes especiales y resúmenes. Este proyecto organiza esas filas para preparar una tabla de carga en Airtable, conservando el orden de origen para facilitar la revisión.

## Flujo del pipeline

1. Lee la hoja de cotización usando la segunda fila como encabezado.
2. Normaliza campos de texto y elimina filas totalmente vacías y filas de resumen.
3. Trata el marcador `"$-"` como precio vacío y clasifica las filas según su estructura.
4. Asigna a las partidas el contexto del apartado precedente.
5. Distingue las descripciones que aparecen en apartados distintos.
6. Agrupa las partidas completas con la misma descripción final, precio y unidad, sumando sus cantidades.
7. Prepara y valida una tabla final de cuatro columnas para Airtable.

## Entradas y salidas

- **Entrada:** archivo Excel con una fila de título y, a continuación, una fila de encabezados. El notebook espera las columnas `Unnamed: 0`, `CSI`, `Labor Code`, `Scope Description`, `Bid Form QTY`, `Bid Form UOM`, `QTY`, `UOM`, `Unit Rate`, `Total`, `Comments/ Notes` y `GS`.
- **Salida:** tabla Excel con las columnas `Scope Description`, `QTY`, `Unit Rate` y `UOM`.
- Se incluye `data/sample_input.xlsx` como entrada de ejemplo sintética.

## Cómo ejecutarlo

Desde la raíz del repositorio:

1. Crea y activa un entorno virtual:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

2. Instala las dependencias:

   ```powershell
   pip install -r requirements.txt
   ```

3. Genera los datos de ejemplo:

   ```powershell
   python scripts/generate_sample_data.py
   ```

4. Abre `notebooks/quotation_cleaning.ipynb` en Jupyter o VS Code. El notebook usa `data/sample_input.xlsx` como entrada y guarda el resultado en `output/sample_output.xlsx`.

## Estructura del repositorio

```text
.
├── data/
│   ├── private/                  # Archivos reales, ignorados por Git
│   └── sample_input.xlsx         # Datos sintéticos de ejemplo
├── notebooks/
│   └── quotation_cleaning.ipynb
├── output/                       # Salidas locales, ignoradas por Git
├── scripts/
│   └── generate_sample_data.py
├── .gitignore
├── README.md
└── requirements.txt
```

Los datos de ejemplo son sintéticos; los archivos reales van en data/private/ (ignorada por Git)
