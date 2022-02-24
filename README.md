# Inscripción UTDT

Un programa de inscripción automática en SiGEdu.

## Selenium y ChromeDriver

El programa requiere un package de Python llamada *Selenium* y un ejecutable llamado *chromedriver*. Selenium se puede instalar usando el package manager *pip*, con el comando `pip install selenium` o con *conda*, y el comando `conda install -c conda-forge selenium `. ChromeDriver se puede descargar de la [página oficial](https://chromedriver.chromium.org/downloads). Se puede ubicar en el mismo directorio que el programa, o en el PATH del sistema operativo.

## Instrucciones

1.   Obtener los URLs de las materias deseadas. Para obtener el url de una materia, alguien que ya tenga la inscripción habilitada (de un año mayor al tuyo o de otra carrera) debe hacer click derecho en el nombre de la materia y copiar el enlace.

     ![](https://user-images.githubusercontent.com/6855052/126911816-c3f600dd-3318-499a-9bca-33fd5642f174.png)

2.   Completar la información en `datos.py`.

3.   Ejecutar `generate.py`. Para hacer esto, abrir la Terminal (macOS) o Línea de Comando (Windows) y navegar al directorio dónde está el archivo, luego ejecutar el comando `python3 generate.py`.

4.   Ejecutar `run.sh`. Para hacer esto, ejecutar el comando `bash run.sh`.

___
###### Authors:  
###### Alfonso Gauna - alfonsogauna@hotmail.com  
###### Felipe Tappata - felipetappata@gmail.com