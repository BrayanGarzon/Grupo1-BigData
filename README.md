> ⚠️ **ADVERTENCIA — USO DE INTELIGENCIA ARTIFICIAL**
>
> Durante el desarrollo del parcial está **prohibido el uso de herramientas de Inteligencia Artificial generativa o sistemas de autocompletado de código**, incluyendo, entre otros, **ChatGPT, GitHub Copilot, Gemini, Claude o herramientas similares**.  
>
> Si se identifica el uso de alguna de estas herramientas durante el examen, el trabajo será considerado **copia/fraude académico y el parcial será anulado**, independientemente del porcentaje de avance o de los resultados obtenidos.


---

# PARCIAL — ANÁLISIS Y PROCESAMIENTO DE DATOS CON PANDAS

## Contexto

Una empresa dedicada al comercio electrónico almacena información sobre las ventas realizadas durante el año en un archivo llamado `ventas.csv`.

La empresa contrató a un equipo de desarrollo para construir un pequeño sistema que permita **preparar, procesar y analizar esta información**.

El equipo anterior dejó una primera versión del sistema. Sin embargo, antes de ponerlo en producción se detectó que **los resultados obtenidos no son confiables y algunas funcionalidades todavía no han sido implementadas**.

Usted ha sido asignado para revisar y finalizar el proyecto.

---

## Situación

En el repositorio encontrará un Notebook de Python llamado:

```text
main.ipynb
```

junto con el archivo:

```text
datos/ventas.csv
```

El Notebook contiene una primera versión del sistema de análisis.

### Su trabajo consiste en:

**Analizar el código existente, identificar y corregir los problemas que encuentre y completar el requerimiento pendiente de la empresa.**

No se indica directamente dónde se encuentran los problemas ni qué instrucciones debe utilizar para solucionarlos.

---

## Resultado esperado

El sistema final debe permitir:

- Preparar correctamente los datos para su análisis.
- Calcular el valor total de cada venta.
- Obtener el valor total de las ventas.
- Identificar el producto con mayor valor de ventas.
- Identificar la ciudad con mayor valor de ventas.
- Incorporar el nuevo análisis solicitado por la empresa: **valor total de ventas por categoría**.

El resultado final debe presentarse de manera clara en el Notebook. Por ejemplo:

```text
====================================
       INFORME DE VENTAS
====================================

Registros iniciales: XXXX
Registros después de limpieza: XXXX

Total vendido: $XXXXXXXX

Producto con mayores ventas: XXXXX
Ciudad con mayores ventas: XXXXX

Ventas por categoría:
Categoría 1: $XXXXXXXX
Categoría 2: $XXXXXXXX
Categoría 3: $XXXXXXXX

====================================
          FIN DEL INFORME
====================================
```

> **Nota:** Los valores mostrados son únicamente un ejemplo del formato esperado. Los resultados reales deben ser obtenidos a partir del archivo `ventas.csv`.

---

## Condiciones

- Se permite consultar apuntes, talleres, ejercicios realizados en clase y documentación "CUANDO EL DOCENTE LO INFORME"
- Se permite modificar el código existente.
- Se permite agregar nuevas celdas y código cuando sea necesario.
- No se debe modificar el archivo `ventas.csv`.
- Los resultados deben ser calculados mediante Python y Pandas.
- No se deben ingresar manualmente los resultados.
- El Notebook debe ejecutarse correctamente.

> **Importante:** Una línea de código puede ejecutarse sin producir un error y aun así estar haciendo algo incorrecto. Verifique los resultados obtenidos.

---

## Entrega

El archivo principal de entrega será:

```text
main.ipynb
```

El Notebook debe contener el **código corregido, la solución al nuevo requerimiento y los resultados obtenidos**.

---

## Criterios de evaluación

| Criterio | Porcentaje |
|---|---:|
| Identificación y corrección de problemas en el código | **35%** |
| Limpieza y preparación de los datos | **20%** |
| Análisis y obtención de resultados | **25%** |
| Implementación del nuevo requerimiento | **15%** |
| Ejecución y presentación del resultado | **5%** |
| **Total** | **100%** |