# IMG to PDF converter / Conversor de IMG a PDF

![Version](https://img.shields.io/badge/version-1.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.10%2B-yellow)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20Mac-lightgrey)

## Table of content / Tabla de contenido

- [English](#english)
    - [Description](#description)
    - [Features](#features)
    - [How to run it?](#how-to-run-it)
    - [How does the program work?](#how-does-the-program-work)
    - [Editions](#editions)
    - [Requirements](#requirements)
    - [Recommendations](#recommendations)
    - [Limitations](#limitations)
    - [License](#license)
    - [Contributions](#contributions)
    - [Version](#version)

- [Español](#español)
    - [Descripcion](#descripcion)
    - [Caracteristicas](#caracteristicas)
    - [¿Como ejecutarlo?](#como-ejecutarlo)
    - [¿Como funciona el programa?](#como-funciona-el-programa)
    - [Ediciones](#ediciones)
    - [Requisitos](#requisitos)
    - [Recomendaciones](#recomendaciones)
    - [Limitaciones](#limitaciones)
    - [Licencia](#licencia)
    - [Contribuciones](#contribuciones)
    - [Versión](#versión)

## English

> Note: English is not my first language, so there may be minor translations errors

### Description

This Python script converts a set of images in the same folder into a .pdf file created in the folder where the images are located.
You don't need to enter the data into the terminal, since it doesn't support it; instead, it asks for the information bit by bit, and depending on the version, it requests more or less data.
In addition, there are three versions of the file, each designed for a specific use/user. I will describe the differences between the editions later on.
These three versions have a .py (Python file) or .exe (Windows executable) version in case you want to review the code or run it without installing anything.

### Features

- Allows you to create a PDF with thousands of images (the only limitation is that a single image cannot exceed the computer's RAM).
- Automatic sorting by file name (alphabetical).
- Support for multiple formats.
- Step-by-step interface.

### How to run it?

#### Python file (.py) option

1. Download the chosen version from the release section.
2. Install Python 3.10 or higher.
3. Install the libraries by running `pip install -r Requirements.txt` or `pip install pillow==12.1.0 reportlab==4.4.9`
4. You can run the file from the terminal or by double-clicking on it.
5. Enter the requested data and press Enter to continue.

#### Windows Executable Option (.exe)

1. Download the version of your choice from the release section.
2. You can run the file from the terminal or by double-clicking on it.
3. Enter the requested data and press Enter to continue.

### How does the program work?

The program runs in a terminal and requests data step by step:
> The program does not work if arguments are passed to it via the terminal.
1. It asks the user for the folder where the images are located.
2. It sorts the files alphabetically.
> The order of the pages will be determined by the file names.
3. It asks for data about the PDF configuration.
> The main change between versions lies in the PDF configuration.
4. It creates the PDF by inserting each image into a page and shows you where the file is located and what it is called.

### Editions

#### Simple

This edition is designed for the average user and allows you to:

1. Specify the path to the PDF or select the path where the file is located.
2. Choose the orientation of each page or let the program decide the best one.
3. Choose how you want the image to be scaled.
> This version is limited to using only A4 paper size.

#### Complete

This edition is designed for more experienced/professional PDF users and allows you to:

1. Specify the path to the PDF or select the path where the file is located.
2. Choose the sheet size from a preset option (A4, B5, Legal, etc.), a custom size with measurements in mm, cm, inches, and pt, or a size adjusted to each image.
> pt is the PDF's own measurement and is equivalent to 72 PT = 1 inch.
3. Choose the orientation of each page or let the program decide the best one (as long as the size does not fit each image).
4. Choose the margins for the sheet from preset options or customize them with measurements in mm, cm, inches, and pt (works even with dynamic pages).
> Dynamic pages refer to when the pages adapt to the images.
5. Choose the size of the image so that it fills the entire page (excluding margins) or give it a custom size with measurements in mm, cm, inches, pt, and % (the entire page minus the margins is taken as 100%).
6. Choose how you want the image to be scaled.
7. Choose where you want the image to be placed from preset options or customize it with measurements in mm, cm, inches, and pt.

#### Fast

This edition is designed for automation and does the following:

1. Takes the path where the file is located.
2. Creates a perfect page for each image.

### Requirements

#### Python File (.py) Option

- Python 3.10 or higher
- pip
- Libraries
    - pillow==12.1.0
    - reportlab==4.4.9
- Operating system
    - Windows 10 or higher / Linux (compatible with Python 3.10 or higher) / Mac (compatible with Python 3.10 or higher)

#### Windows Executable (.exe) Option

- Windows 10 or 11

### Recommendations

1. Images should be named so that if you sort them alphabetically, they are in the desired order (if the order does not matter, this point can be disregarded).
2. The name of the PDF will be the same as the folder, so naming it with the final name is more practical.

### Limitations

1. The program will only recognize png, jpg, jpeg, webp, tiff, bmp, and ico files. If the file is not in one of these formats, it will not be converted into pages.
2. The program may slightly reduce the image quality within the PDF due to the compression used to manage the final file size.
3. If the image size is larger than the page, it may skip the margins or even cut the image.

### License

This project is licensed under MIT.

### Contributions

Pull requests are not currently accepted.
If you find a bug or want to suggest an improvement, open an issue explaining the case.
The project can be freely modified by forking it, but such versions will not be associated with the official version.

### Version

Current version: 1.0

## Español

> Esta es la versión original del README

### Descripcion

Este script de python convierte un conjunto de imágenes que estén en una misma carpeta a un archivo .pdf creado en la carpeta donde están las imágenes.
No es necesario pasarle los datos por la terminal ya que no los soporta el los va pidendo poco a poco y dependiendo de la edicion pide mas o menos datos.
Además de que existen 3 versiones del archivo cada una pensada para un uso/usuario concreto, describire las diferencias entre las ediciones mas adelante.
Estas 3 versiones tienen una versión en .py (Archivo de Python) o .exe (Ejecutable de Windows) por si quieres revisar el codigo o ejecutarlo sin instalar nada.

### Caracteristicas

- Permite crear un PDF con miles de imágenes (El unico limite es que una sola imagen supere la Ram del equipo).
- Orden automatico por el nombre de los archivos (Alfabetico).
- Soporte de multiples formatos.
- Interfaz paso a paso.

### ¿Como ejecutarlo?

#### Opcion Archivo de Python (.py)

1. Descargar la version elegida en el apartado de release.
2. Instalar Python 3.10 o superior.
3. Instalar las librerias ejecutando `pip install -r Requirements.txt` o `pip install pillow==12.1.0 reportlab==4.4.9`
4. Puedes ejecutar el archivo desde la terminal o dandole doble click.
5. Escribir los datos que pida y pulsar enter para continuar.

#### Opcion Ejecutable de Windows (.exe)

1. Descargar la version elegida en el apartado de release.
2. Puedes ejecutar el archivo desde la terminal o dandole doble click.
3. Escribir los datos que pida y pulsar enter para continuar.

### ¿Como funciona el programa?

El programa se ejecuta en terminal y pide datos poco a poco:
> El programa no funciona si se le pasan argumentos por terminal.
1. Pide al usuario la carpeta donde están las imágenes.
2. Ordena los archivos por orden alfabetico.
> El orden de las paginas estara dictaminado por el nombre de los archivos.
3. Pide datos sobre la configuracion del PDF.
> El principal cambio entre versiones radica en la configuracion del PDF.
4. Crea el PDF insertando cada imagen en una pagina y te muestra donde quedo el archivo y como se llama.

### Ediciones

#### Sencilla

Esta edicion esta pensada para el usuario comun y permite:

1. Dar la ruta al PDF o toma la ruta donde esta el archivo.
2. Elegir la Orientacion de cada pagina o que el programa decida la mejor.
3. Elegir como quieres que se escale la imagen.
> Esta version esta limitada a solo usar tamaño de hoja A4.

#### Completa

Esta edicion esta pensada para un usuario mas experimentado / profesional en los PDF y permite:

1. Dar la ruta al PDF o toma la ruta donde esta el archivo.
2. Elegir el tamaño de hoja sea una opcion prestablecida (A4, B5, Legal, etc), un tamaño personalizado con medidas de mm, cm, inch y pt o un tamaño ajustado a cada imagen.
> pt es la medida propia de los PDF y equivale a 72 PT = 1 inch.
3. Elegir la orientacion de cada pagina o que el programa decida la mejor (Siempre y cuando el tamaño no se ajuste a cada imagen).
4. Elegir los margenes que tendra la hoja en unas opciones preestablecidas o personalizados con medidas de mm, cm, inch y pt (funciona incluso con paginas dinamicas).
> Paginas dinamicas se refiere a cuando las paginas se adaptan a las imágenes.
5. Elegir el tamaño de la imagen para que ocupe toda la pagina (Descontando los margenes) o darle un tamaño personalizado con medidas de mm, cm, inch, pt y % (Se toma como 100% toda la pagina descontado los margenes).
6. Elegir como quieres que se escale la imagen.
7. Elegir donde quieres que este la imagen en una opciones preestablecidas o personalizada con medidas de mm, cm, inch y pt.

#### Rapida

Esta edicion esta pensada para automatizacion y hace:

1. toma la ruta donde esta el archivo.
2. Crea una pagina perfecta para cada imagen.

### Requisitos

#### Opcion Archivo de Python (.py)

- Python 3.10 o superior
- pip
- Librerias
    - pillow==12.1.0
    - reportlab==4.4.9
- Sistema operativo
    - Windows 10 o superior / Linux (compatible con Python 3.10 o superior) / Mac (compatible con Python 3.10 o superior)

#### Opcion Ejecutable de Windows (.exe)

- Windows 10 o 11

### Recomendaciones

1. Las imágenes deberian que estar nombrada de tal manera que si las ordenas alfabeticamente tengan el orden deseado (Si no importa el orden este punto es descartable).
2. El nombre del pdf sera el mismo que la carpeta por lo que nombrar esta con el nombre final es mas practico.

### Limitaciones

1. El programa solo reconocera archivos png, jpg, jpeg, webp, tiff, bmp y ico si no esta en ninguno de estos no los volvera paginas.
2. El programa puede bajar un poco la calidad de la imagen dentro del pdf debido a la compresion usada para manejar el peso final del archivo.
3. En caso de que el tamaño de la imagen sea superior a la pagina puede saltarse los margenes o incluso cortar la imagen.

### Licencia

Este proyecto esta bajo licencia MIT.

### Contribuciones

Actualmente no se aceptan Pull Requests.
Si encuentras un error o deseas sugerir una mejora, abre un issue explicando el caso.
El proyecto puede ser modificado libremente mediante un fork, pero dichas versiones no estarán asociadas a la version oficial

### Versión

Versión actual: 1.0