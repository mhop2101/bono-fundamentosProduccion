
# Generador de PDF con Diseño Personalizado y Márgenes Específicos
Mateo Sierra – 202123722                                                                      

Miguel Gómez - 202122562  

Martin Castañeda - 202124068 

Juan Diego Lozano – 202122869 

Daniel Barbosa - 202110757
## Descripción

Este proyecto ofrece una solución eficiente para la inserción de imágenes en documentos PDF con márgenes y dimensiones personalizadas. Diseñado para optimizar el proceso de cambio de cirel en la empresa, este programa elimina la necesidad de métodos de prueba y error. Mediante la creación de un PDF personalizado, proporciona una guía clara y precisa que facilita y acelera este proceso.

## Objetivo

El objetivo principal de este programa es mejorar la eficiencia y precisión en la creación de documentos PDF personalizados. Al permitir a los usuarios especificar márgenes y dimensiones, se facilita la adaptación del documento a necesidades específicas, lo que resulta esencial en el proceso de cambio de cirel. Este enfoque dirigido ayuda a la empresa a ahorrar tiempo y recursos, asegurando al mismo tiempo la calidad y exactitud en la presentación de la información.

## Funcionalidades Clave

- **Inserción Personalizada de Imágenes:** Posibilidad de añadir cualquier imagen a un documento PDF que servira de guia en el cambio del cirel.
- **Configuración de Márgenes y Dimensiones:** Personalización completa de márgenes (izquierdo, derecho, superior, inferior) y dimensiones del documento.
- **Optimización de Procesos:** Diseñado específicamente para mejorar la eficiencia en el proceso de cambio de cirel, reduciendo la dependencia del método de prueba y error.

## Impacto en la Empresa

La implementación de este programa tiene un impacto directo y positivo en las operaciones de la empresa:
- **Reducción de Tiempo de Proceso:** Agiliza significativamente la creación de documentos personalizados.
- **Aumento de Precisión:** Elimina errores comunes asociados con el método de prueba y error.
- **Mejora en la Presentación de Información:** Garantiza una presentación clara y precisa de los datos.

---

## Requisitos

Para ejecutar este script, necesitarás Python instalado en tu sistema, así como las bibliotecas `Pillow` y `reportlab`. Puedes instalar estas dependencias utilizando el archivo `requirements.txt` incluido en este proyecto.

## Instalación


```
pip install -r requirements.txt
```

## Uso


```
python programa.py <margen_izquierdo> <margen_derecho> <margen_superior> <margen_inferior> <ruta_imagen> <ruta_salida_pdf> [--width <ancho>] [--height <alto>]
```

Donde:

- `<margen_izquierdo>` es el margen izquierdo en unidades.
- `<margen_derecho>` es el margen derecho.
- `<margen_superior>` es el margen superior.
- `<margen_inferior>` es el margen inferior.
- `<ruta_imagen>` es la ruta al archivo de imagen.
- `<ruta_salida_pdf>` es la ruta de salida para el archivo PDF generado.
- `--width` y `--height` son argumentos opcionales para especificar el ancho y alto del PDF (en unidades).

## Ejemplo

```
python programa.py 567 567 283 283 imagen.png salida.pdf --width 2835 --height 1984
```

Al ejecutar este comando, la imagen miimagen.png se integrará en un documento PDF titulado salida.pdf, configurado con márgenes uniformes de 567 y 283 unidades en cada lado que son 20cm y 10cm y dimensiones de 2835x1984 unidades que son 100cm x 70cm. Este archivo PDF servirá como una guía precisa en el cirel, proporcionando a los operarios instrucciones claras sobre la ubicación exacta para colocar el diseño. Esto elimina la necesidad de localizar la posición adecuada mediante métodos de prueba y error, facilitando así el proceso y aumentando la eficiencia operativa.


---

