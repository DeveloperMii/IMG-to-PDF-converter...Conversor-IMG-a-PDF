#Librerias
from pathlib import Path
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, LETTER, LEGAL, TABLOID, B0, B1, B2, B3, B4, B5, B6, B7, B8, B9, B10, landscape, portrait
from reportlab.lib.utils import ImageReader
from io import BytesIO

#Variables
Ruta : str = ""
Imagenes : list = []
Max_caracter : int = 0
Archivos : list = []
Ordenados : list = []
Pdf : canvas.Canvas = None
Escalado : bool = True
Horientacion : int = 3
Margenes : dict = {"Sup" : 0.0, "Inf" : 0.0, "Izq" : 0.0, "Der" : 0.0}
Ancho : float = None
Alto : float = None
Formato : list = [0.0,0.0]
Dinamico : bool = False
Tamaño : list = [100.0,100.0]
TTam : int = 1
PosP : list = [2,2]
PosM : list = [0.0,0.0]
TPos : int = 1

#Confirmacion de ruta
while True:
    opcion = False
    Ruta = ""
    Ruta = input("En que ruta carpeta estan las imagenes \n(Si es la misma en la que esta este archivo solo pulse enter)\n:  ").strip()
    if Ruta in ["", "."]:
        Ruta = str(Path(__file__).parent)
    if Path(Ruta).exists():
        print("La ruta escogida es: " + Ruta)
        while True:
            match input("Si no esta seguro presione 1 en caso de estar seguro presione 2: ").strip():
                case "1":
                    opcion = False
                    break
                case "2":
                    opcion = True
                    break
                case _:
                    print("Ingrese un valor valido")
    else:
        print("La ruta es invalida")
    if opcion:
        break

print("")

#Proteccion de sobreescritura
NameA = ""
if Path(str(Path(Ruta)) + "/" + str(Path(Ruta).name) +".pdf").exists():
    NameA = "0"
    for i in Path(Ruta).iterdir():
        if i.stem[:len(Path(Ruta).name)] == str(Path(Ruta).name):
            NameA = str(int(NameA) + 1)
    Pdf : canvas.Canvas = canvas.Canvas(str(Path(Ruta)) + "/" + str(Path(Ruta).name) + " (" + NameA + ")" + ".pdf", pagesize=A4)
else:
    Pdf : canvas.Canvas = canvas.Canvas(str(Path(Ruta)) + "/" + str(Path(Ruta).name) + ".pdf", pagesize=A4)
Formato[0], Formato[1] = A4

#Seleccionado de imagenes
for i in Path(Ruta).iterdir():
    Nombre = ""
    chara = 0
    if i.suffix.lower() in [".png", ".jpg", ".jpeg", "webp", ".tiff", ".bmp", "ico"]:
        for j in i.stem:
            if j in ["0","1","2","3","4","5","6","7","8","9"]:
                chara = chara + 1
            else:
                break
        if chara > Max_caracter:
            Max_caracter = chara
        Imagenes.append(i)

#Ordenarlos
for i in Imagenes:
    i = Path(i)
    chara = 0
    for j in i.stem:
        if j in ["0","1","2","3","4","5","6","7","8","9"]:
            chara = chara + 1
        else:
            break
    Archivos.append(str(str(i.parent) + "/" + str(i.name[:chara]).zfill(Max_caracter) + str(i.name[chara:])))
Archivos.sort()

#Lista con las rutas ordenadas
for i in range(0, len(Archivos)):
    Nombre = ""
    for j in range(0, len(Path(Archivos[i]).stem)):
        if Path(str(Path(Archivos[i]).parent) + "/" + str(Path(Archivos[i]).stem[j:] + str(Path(Archivos[i]).suffix))).exists():
            Nombre = Path(Archivos[i]).stem[j:]
        if Path(Archivos[i]).stem[j] != "0":
            break
    Ordenados.append(str(str(Path(Imagenes[i]).parent) + "/" + Nombre + str(Path(Archivos[i]).suffix)))

#Eleccion del tamaño del pdf
while True:
    terminado = False
    match input("Si quiere seleccionar un tamaño base para el PDF pulse 1 \nSi quiere un tamaño personalizado para el PDF pulse 2 \nSi quiere que el tamaño del PDF sea adaptado para cada imagen pulse 3 \nSi solo se pulsa enter la opcion elegida sera la 1 \n: ").strip():
        case "" | "." | "1":
            match str(input("Selecione el tamaño del papel entre (solo escriba alguna de las siguientes opciones): \n A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, B0, B1, B2, B3, B4, B5, B6, B7, B8, B9, B10, LETTER, LEGAL, TABLOID \n Si solo preciona enter se eligira A4 (por ser el mas comun) \n:")).strip().upper():
                case "A0":
                    Formato = A0
                    terminado = True
                case "A1":
                    Formato = A1
                    terminado = True
                case "A2":
                    Formato = A2
                    terminado = True
                case "A3":
                    Formato = A3
                    terminado = True
                case "" | "." | "A4":
                    Formato = A4
                    terminado = True
                case "A5":
                    Formato = A5
                    terminado = True
                case "A6":
                    Formato = A6
                    terminado = True
                case "A7":
                    Formato = A7
                    terminado = True
                case "A8":
                    Formato = A8
                    terminado = True
                case "A9":
                    Formato = A9
                    terminado = True
                case "A10":
                    Formato = A10
                    terminado = True
                case "B0":
                    Formato = B0
                    terminado = True
                case "B1":
                    Formato = B1
                    terminado = True
                case "B2":
                    Formato = B2
                    terminado = True
                case "B3":
                    Formato = B3
                    terminado = True
                case "B4":
                    Formato = B4
                    terminado = True
                case "B5":
                    Formato = B5
                    terminado = True
                case "B6":
                    Formato = B6
                    terminado = True
                case "B7":
                    Formato = B7
                    terminado = True
                case "B8":
                    Formato = B8
                    terminado = True
                case "B9":
                    Formato = B9
                    terminado = True
                case "B10":
                    Formato = B10
                    terminado = True
                case "LETTER":
                    Formato = LETTER
                    terminado = True
                case "LEGAL":
                    Formato = LEGAL
                    terminado = True
                case "TABLOID":
                    Formato = TABLOID
                    terminado = True
                case _:
                    print("Ingrese una opcion valida \nVolviendo al inicio")
        case "2":
            match input("Si los valores los tiene en alguna medida fisica pulse 1 \nSi los valores los tiene en PT (72 PT = 1 inch) pulse 2 \n:").strip():
                case "1":
                    medidas : list = ["", ""]
                    tipo = input("Escoja una de las siguientes unidades (Escribala como vera acontinuacion): \n mm  cm  inch \n: ").strip().lower()
                    match tipo:
                        case "mm", "cm", "inch":
                            while True:
                                valido = True
                                medidas[0] = input("Ingrese la medida horizontal en unidad escogida (solo el valor): ").strip()
                                for i in medidas[0]:
                                    if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                        valido = False
                                        print("Ingrese un valor valido")
                                        break
                                    if i == ",":
                                        medidas[0].replace(",", ".")
                                if valido:
                                    break
                            while True:
                                valido = True
                                medidas[1] = input("Ingrese la medida vertical en unidad escogida (solo el valor): ").strip()
                                for i in medidas[1]:
                                    if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                        valido = False
                                        print("Ingrese un valor valido")
                                        break
                                    if i == ",":
                                        medidas[1].replace(",", ".")
                                if valido:
                                    break
                            if tipo == "mm":
                                Formato[0] = float(medidas[0]) * (72 / 25.4)
                                Formato[1] = float(medidas[1]) * (72 / 25.4)
                                terminado = True
                            elif tipo == "cm":
                                Formato[0] = float(medidas[0]) * (72 / 2.54)
                                Formato[1] = float(medidas[1]) * (72 / 2.54)
                                terminado = True
                            else:
                                Formato[0] = float(medidas[0]) * 72
                                Formato[1] = float(medidas[1]) * 72
                                terminado = True
                        case _:
                            print("ingrese una unidad valida \nVolviendo al inicio")
                case "2":
                    match input("Si no esta seguro presione 1 \nSi esta seguro presione 2: ").strip():
                        case "1":
                            print("Volviendo al inicio")
                        case "2":
                            medidas : list = ["", ""]
                            while True:
                                valido = True
                                medidas[0] = input("Ingrese el tamaño horizontal del PDF en PT (72 PT = 1 inch):  ").strip()
                                for i in medidas[0]:
                                    if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                        valido = False
                                        print("Ingrese un valor valido")
                                        break
                                    if i == ",":
                                        medidas[0].replace(",", ".")
                                if valido:
                                    break
                            while True:
                                valido = True
                                medidas[1] = input("Ingrese el tamaño vertical del PDF en PT (72 PT = 1 inch):  ").strip()
                                for i in medidas[1]:
                                    if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                        valido = False
                                        print("Ingrese un valor valido")
                                        break
                                    if i == ",":
                                        medidas[1].replace(",", ".")
                                if valido:
                                    break
                            Formato[0] = float(medidas[0])
                            Formato[1] = float(medidas[1])
                            terminado = True
                        case _:
                            print("Ingrese una opcion valida \nVolviendo al inicio")
        case "3":
            match input("Si no esta seguro presione 1 \nSi esta seguro presione 2 \n: ").strip():
                case "1":
                    print("Volviendo al inicio")
                case "2":
                    Dinamico = True
                    terminado = True
                case _:
                    print("Ingrese una opcion valida \nVolviendo al inicio")
        case _:
            print("Ingrese una opcion valida")
    if terminado:
        break

print("")

#Eleccion de horientacion
if not Dinamico:
    while True:
        match input("Si quiere que todas las paginas esten en vertical presione 1 \nSi quiere que todas las paginas esten en horizontal presione 2 \nSi quiere que el programa decida la mejor horientacion presione 3 \nSi solo se pulsa enter la opcion elegida sera la 1: ").strip():
            case ""|"."|"1":
                Horientacion = 1
                break
            case "2":
                Horientacion = 2
                break
            case "3":
                Horientacion = 3
                break
            case _:
                print("Ingrese un valor valido")
    print("")

#Eleccion de margenes
while True:
    terminado = False
    match input("Si quiere seleccionar un tamaño base para los margenes pulse 1 \nSi quiere un tamaño personalizado para los margenes pulse 2 \nSi solo se pulsa enter la opcion elegida sera la 1 \n: ").strip():
        case "" | "." | "1":
            match input("Selecione el tamaño del papel entre (solo escriba el numero indice de alguna de las siguientes opciones): \n 1. Ninguno  0mm  0cm  0inch  0PT \n 2. Muy estrecho  10mm  1cm  0.39inch  28.35PT \n 3. Estrecho  15mm  1.5cm  0.59inch  42.52PT \n 4. Estandar  25mm  2.5cm  1inch  72PT \n 5. Ancho  30mm  3cm  1.18inch  85.04PT \n 6. Muy Ancho 40mm  4cm  1.57inch  113.39PT \n Si solo preciona enter se eligira 4. Estandar (por ser el mas comun) \n:").strip():
                case "1":
                    Margenes["Sup"] = 0.0
                    Margenes["Inf"] = 0.0
                    Margenes["Izq"] = 0.0
                    Margenes["Der"] = 0.0
                    terminado = True
                case "2":
                    Margenes["Sup"] = 28.35
                    Margenes["Inf"] = 28.35
                    Margenes["Izq"] = 28.35
                    Margenes["Der"] = 28.35
                    terminado = True
                case "3":
                    Margenes["Sup"] = 42.52
                    Margenes["Inf"] = 42.52
                    Margenes["Izq"] = 42.52
                    Margenes["Der"] = 42.52
                    terminado = True
                case "." | "" | "4":
                    Margenes["Sup"] = 72.0
                    Margenes["Inf"] = 72.0
                    Margenes["Izq"] = 72.0
                    Margenes["Der"] = 72.0
                    terminado = True
                case "5":
                    Margenes["Sup"] = 85.04
                    Margenes["Inf"] = 85.04
                    Margenes["Izq"] = 85.04
                    Margenes["Der"] = 85.04
                    terminado = True
                case "6":
                    Margenes["Sup"] = 113.39
                    Margenes["Inf"] = 113.39
                    Margenes["Izq"] = 113.39
                    Margenes["Der"] = 113.39
                    terminado = True
                case _:
                    print("Ingrese una opcion valida \nVolviendo al inicio")
        case "2":
            match input("Si los valores los tiene en alguna medida fisica pulse 1 \nSi los valores los tiene en PT (72 PT = 1 inch) pulse 2").strip():
                case "1":
                    medidas : list = ["", "", "", ""]
                    tipo = input("Escoja una de las siguientes unidades (Escribala como vera acontinuacion): \n mm  cm  inch \n: ").strip().lower()
                    match tipo:
                        case "mm" | "cm" | "inch":
                            while True:
                                valido = True
                                medidas[0] = input("Ingrese la medida del margen superior en unidad escogida (solo el valor): ").strip()
                                for i in medidas[0]:
                                    if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                        valido = False
                                        print("Ingrese un valor valido")
                                        break
                                    if i == ",":
                                        medidas[0].replace(",", ".")
                                if valido:
                                    break
                            while True:
                                valido = True
                                medidas[1] = input("Ingrese la medida del margen inferior en unidad escogida (solo el valor): ").strip()
                                for i in medidas[1]:
                                    if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                        valido = False
                                        print("Ingrese un valor valido")
                                        break
                                    if i == ",":
                                        medidas[1].replace(",", ".")
                                if valido:
                                    break
                            while True:
                                valido = True
                                medidas[2] = input("Ingrese la medida margen izquierdo en unidad escogida (solo el valor): ").strip()
                                for i in medidas[2]:
                                    if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                        valido = False
                                        print("Ingrese un valor valido")
                                        break
                                    if i == ",":
                                        medidas[2].replace(",", ".")
                                if valido:
                                    break
                            while True:
                                valido = True
                                medidas[3] = input("Ingrese la medida del margen derecho en unidad escogida (solo el valor): ").strip()
                                for i in medidas[3]:
                                    if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                        valido = False
                                        print("Ingrese un valor valido")
                                        break
                                    if i == ",":
                                        medidas[1].replace(",", ".")
                                if valido:
                                    break
                            if tipo == "mm":
                                Margenes["Sup"] = float(medidas[0]) * (72 / 25.4)
                                Margenes["Inf"] = float(medidas[1]) * (72 / 25.4)
                                Margenes["Izq"] = float(medidas[2]) * (72 / 25.4)
                                Margenes["Der"] = float(medidas[3]) * (72 / 25.4)
                                terminado = True
                            elif tipo == "cm":
                                Margenes["Sup"] = float(medidas[0]) * (72 / 2.54)
                                Margenes["Inf"] = float(medidas[1]) * (72 / 2.54)
                                Margenes["Izq"] = float(medidas[2]) * (72 / 2.54)
                                Margenes["Der"] = float(medidas[3]) * (72 / 2.54)
                                terminado = True
                            else:
                                Margenes["Sup"] = float(medidas[0]) * 72
                                Margenes["Inf"] = float(medidas[1]) * 72
                                Margenes["Izq"] = float(medidas[2]) * 72
                                Margenes["Der"] = float(medidas[3]) * 72
                                terminado = True
                        case _:
                            print("ingrese una unidad valida \nVolviendo al inicio")
                case "2":
                    match input("Si no esta seguro presione 1 \nSi esta seguro presione 2: ").strip():
                        case "1":
                            print("Volviendo al inicio")
                        case "2":
                            medidas : list = ["", "", "", ""]
                            while True:
                                valido = True
                                medidas[0] = input("Ingrese la medida del margen superior en PT (72 PT = 1 inch): ").strip()
                                for i in medidas[0]:
                                    if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                        valido = False
                                        print("Ingrese un valor valido")
                                        break
                                    if i == ",":
                                        medidas[0].replace(",", ".")
                                if valido:
                                    break
                            while True:
                                valido = True
                                medidas[1] = input("Ingrese la medida del margen inferior en PT (72 PT = 1 inch): ").strip()
                                for i in medidas[1]:
                                    if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                        valido = False
                                        print("Ingrese un valor valido")
                                        break
                                    if i == ",":
                                        medidas[1].replace(",", ".")
                                if valido:
                                    break
                            while True:
                                valido = True
                                medidas[2] = input("Ingrese la medida margen izquierdo en PT (72 PT = 1 inch): ").strip()
                                for i in medidas[2]:
                                    if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                        valido = False
                                        print("Ingrese un valor valido")
                                        break
                                    if i == ",":
                                        medidas[2].replace(",", ".")
                                if valido:
                                    break
                            while True:
                                valido = True
                                medidas[3] = input("Ingrese la medida del margen derecho en PT (72 PT = 1 inch): ").strip()
                                for i in medidas[3]:
                                    if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                        valido = False
                                        print("Ingrese un valor valido")
                                        break
                                    if i == ",":
                                        medidas[1].replace(",", ".")
                                if valido:
                                    break
                            Margenes["Sup"] = float(medidas[0])
                            Margenes["Inf"] = float(medidas[1])
                            Margenes["Izq"] = float(medidas[2])
                            Margenes["Der"] = float(medidas[3])
                            terminado = True
                        case _:
                            print("Ingrese una opcion valida \nVolviendo al inicio")
        case _:
            print("Ingrese una opcion valida")
    if terminado:
        break

print("")

#Tamaño de imagen
while True:
    terminado = False
    match input("Si quiere que la imagen ocupe todo el espacio posible pulse 1 \nSi quiere que la imagen tenga un tamaño personalizado pulse 2 (Cabe resaltar que si ese tamaño es mayor al de la pagina la imagen puede cortarse) \nSi solo se pulsa enter la opcion elegida sera la 1 \n: ").strip():
        case "" | "." | "1":
            TTam = 1
            Tamaño[0] = 100
            Tamaño[1] = 100
            terminado = True
        case "2":
            match input("Si los valores los tiene en alguna medida fisica pulse 1 \nSi los valores los tiene en PT (72 PT = 1 inch) pulse 2 \nSi los valores los tiene en porcentage pulse 3 \n: ").strip():
                case "1":
                    medidas : list = ["", ""]
                    tipo = input("Escoja una de las siguientes unidades (Escribala como vera acontinuacion): \n mm  cm  inch \n: ").strip().lower()
                    match tipo:
                        case "mm", "cm", "inch":
                            while True:
                                valido = True
                                medidas[0] = input("Ingrese la tamaño horizontal en unidad escogida (solo el valor): ").strip()
                                for i in medidas[0]:
                                    if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                        valido = False
                                        print("Ingrese un valor valido")
                                        break
                                    if i == ",":
                                        medidas[0].replace(",", ".")
                                if valido:
                                    break
                            while True:
                                valido = True
                                medidas[1] = input("Ingrese la tamaño vertical en unidad escogida (solo el valor): ").strip()
                                for i in medidas[1]:
                                    if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                        valido = False
                                        print("Ingrese un valor valido")
                                        break
                                    if i == ",":
                                        medidas[1].replace(",", ".")
                                if valido:
                                    break
                            if tipo == "mm":
                                Tamaño[0] = float(medidas[0]) * (72 / 25.4)
                                Tamaño[1] = float(medidas[1]) * (72 / 25.4)
                                TTam = 2
                                terminado = True
                            elif tipo == "cm":
                                Tamaño[0] = float(medidas[0]) * (72 / 2.54)
                                Tamaño[1] = float(medidas[1]) * (72 / 2.54)
                                TTam = 2
                                terminado = True
                            else:
                                Tamaño[0] = float(medidas[0]) * 72
                                Tamaño[1] = float(medidas[1]) * 72
                                TTam = 2
                                terminado = True
                        case _:
                            print("ingrese una unidad valida \nVolviendo al inicio")
                case "2":
                    match input("Si no esta seguro presione 1 \nSi esta seguro presione 2: ").strip():
                        case "1":
                            print("Volviendo al inicio")
                        case "2":
                            medidas : list = ["", ""]
                            while True:
                                valido = True
                                medidas[0] = input("Ingrese el tamaño horizontal de la imagen en PT (72 PT = 1 inch):  ").strip()
                                for i in medidas[0]:
                                    if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                        valido = False
                                        print("Ingrese un valor valido")
                                        break
                                    if i == ",":
                                        medidas[0].replace(",", ".")
                                if valido:
                                    break
                            while True:
                                valido = True
                                medidas[1] = input("Ingrese el tamaño vertical de la imagen en PT (72 PT = 1 inch):  ").strip()
                                for i in medidas[1]:
                                    if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                        valido = False
                                        print("Ingrese un valor valido")
                                        break
                                    if i == ",":
                                        medidas[1].replace(",", ".")
                                if valido:
                                    break
                            Tamaño[0] = float(medidas[0])
                            Tamaño[1] = float(medidas[1])
                            TTam = 2
                            terminado = True
                        case _:
                            print("Ingrese una opcion valida \nVolviendo al inicio")
                case "3":
                    match input("Si no esta seguro presione 1 \nSi esta seguro presione 2: ").strip():
                        case "1":
                            print("Volviendo al inicio")
                        case "2":
                            medidas : list = ["", ""]
                            while True:
                                valido = True
                                medidas[0] = input("Ingrese el tamaño horizontal de la imagen en porcentaje:  ").strip()
                                for i in medidas[0]:
                                    if not i in ["0","1","2","3","4","5","6","7","8","9",".",",","%"]:
                                        valido = False
                                        print("Ingrese un valor valido")
                                        break
                                    if i == ",":
                                        medidas[0].replace(",", ".")
                                    if i == "%":
                                        medidas[0].replace("%", "")
                                if valido:
                                    break
                            while True:
                                valido = True
                                medidas[1] = input("Ingrese el tamaño vertical de la imagen en porcentaje:  ").strip()
                                for i in medidas[1]:
                                    if not i in ["0","1","2","3","4","5","6","7","8","9",".",",","%"]:
                                        valido = False
                                        print("Ingrese un valor valido")
                                        break
                                    if i == ",":
                                        medidas[1].replace(",", ".")
                                    if i == "%":
                                        medidas[1].replace("%", "")
                                if valido:
                                    break
                            Tamaño[0] = float(medidas[0])
                            Tamaño[1] = float(medidas[1])
                            TTam = 1
                            terminado = True
                        case _:
                            print("Ingrese una opcion valida \nVolviendo al inicio")
        case _:
            print("Ingrese una opcion valida")
    if terminado:
        break

print("")

#Tipo de escalado
while True:
    match input("Si quiere las imagenes se escalen usando todo el espacio disponible pero con deformacion presione 1 \nSi quiere que las imagenes se escalen sin deformacion aunque no se use todo el espacio disponible presione 2 \nSi solo se pulsa enter la opcion elegida sera la 2 \n: ").strip():
        case "1":
            Escalado = False
            break
        case "" | "." | "2":
            Escalado = True
            break
        case _:
            print("Ingrese un valor valido")

print("")

#Selector de posicion
while True:
    terminado = False
    match input("Si quiere una posicion predefinida pulse 1 \nSi quiere una posicion personalizada personalizado pulse 2 (Ante valores que no concuerden con el tamaño de la hoja pueden exister recortes en la imagen) \nSi solo se pulsa enter la opcion elegida sera la 1 \n: ").strip():
        case "" | "." | "1":
            match input("Elija una de las siguentes posiciones (solo ingrese el indice) (si solo presiona enter la opcion 5 centro sera la predeterminada) \n 1. Sup Izq 2. Sup Cen 3. Sup Der \n 4. Cen Izq 5. Centro  6. Cen Der \n 7. Inf Izq 8. Inf Cen 9. Inf Der \n:").strip():
                case "1":
                    PosP[0] = 1
                    PosP[1] = 1
                    TPos = 1
                    terminado = True
                case "2":
                    PosP[0] = 1
                    PosP[1] = 2
                    TPos = 1
                    terminado = True
                case "3":
                    PosP[0] = 1
                    PosP[1] = 3
                    TPos = 1
                    terminado = True
                case "4":
                    PosP[0] = 2
                    PosP[1] = 1
                    TPos = 1
                    terminado = True
                case "" | "." | "5":
                    PosP[0] = 2
                    PosP[1] = 2
                    TPos = 1
                    terminado = True
                case "6":
                    PosP[0] = 2
                    PosP[1] = 3
                    TPos = 1
                    terminado = True
                case "7":
                    PosP[0] = 3
                    PosP[1] = 1
                    TPos = 1
                    terminado = True
                case "8":
                    PosP[0] = 3
                    PosP[1] = 2
                    TPos = 1
                    terminado = True
                case "9":
                    PosP[0] = 3
                    PosP[1] = 3
                    TPos = 1
                    terminado = True
                case _:
                    print("Ingrese una opcion valida \nVolviendo al inicio")
        case "2":
            input("Antes de pasar con las medidas me gustaria explicar que el punto de referencia para tomarlas es la esquina inferior izquierda de la imagen")
            match input("Si los valores los tiene en alguna medida fisica pulse 1 \nSi los valores los tiene en PT (72 PT = 1 inch) pulse 2 \n: ").strip():
                case "1":
                    medidas : list = ["", ""]
                    tipo = input("Escoja una de las siguientes unidades (Escribala como vera acontinuacion): \n mm  cm  inch \n: ").strip().lower()
                    match tipo:
                        case "mm", "cm", "inch":
                            while True:
                                valido = True
                                medidas[0] = input("Ingrese la posicion horizontal en unidad escogida (solo el valor): ").strip()
                                for i in medidas[0]:
                                    if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                        valido = False
                                        print("Ingrese un valor valido")
                                        break
                                    if i == ",":
                                        medidas[0].replace(",", ".")
                                if valido:
                                    break
                            while True:
                                valido = True
                                medidas[1] = input("Ingrese la posicion vertical en unidad escogida (solo el valor): ").strip()
                                for i in medidas[1]:
                                    if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                        valido = False
                                        print("Ingrese un valor valido")
                                        break
                                    if i == ",":
                                        medidas[1].replace(",", ".")
                                if valido:
                                    break
                            if tipo == "mm":
                                PosM[0] = float(medidas[0]) * (72 / 25.4)
                                PosM[1] = float(medidas[1]) * (72 / 25.4)
                                TPos = 2
                                terminado = True
                            elif tipo == "cm":
                                PosM[0] = float(medidas[0]) * (72 / 2.54)
                                PosM[1] = float(medidas[1]) * (72 / 2.54)
                                TPos = 2
                                terminado = True
                            else:
                                PosM[0] = float(medidas[0]) * 72
                                PosM[1] = float(medidas[1]) * 72
                                TPos = 2
                                terminado = True
                        case _:
                            print("ingrese una unidad valida \nVolviendo al inicio")
                case "2":
                    match input("Si no esta seguro presione 1 \nSi esta seguro presione 2: ").strip():
                        case "1":
                            print("Volviendo al inicio")
                        case "2":
                            medidas : list = ["", ""]
                            while True:
                                valido = True
                                medidas[0] = input("Ingrese el posicion horizontal de la imagen en PT (72 PT = 1 inch):  ").strip()
                                for i in medidas[0]:
                                    if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                        valido = False
                                        print("Ingrese un valor valido")
                                        break
                                    if i == ",":
                                        medidas[0].replace(",", ".")
                                if valido:
                                    break
                            while True:
                                valido = True
                                medidas[1] = input("Ingrese el posicion vertical de la imagen en PT (72 PT = 1 inch):  ").strip()
                                for i in medidas[1]:
                                    if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                        valido = False
                                        print("Ingrese un valor valido")
                                        break
                                    if i == ",":
                                        medidas[1].replace(",", ".")
                                if valido:
                                    break
                            PosM[0] = float(medidas[0])
                            PosM[1] = float(medidas[1])
                            TPos = 2
                            terminado = True
                        case _:
                            print("Ingrese una opcion valida \nVolviendo al inicio")
        case _:
            print("Ingrese una opcion valida")
    if terminado:
        break

print("Empezando conversion")

#Convertir Pdf
for i in Ordenados:
    i = Path(i)
    print(str(i.name) + " ha sido integrado")
    with Image.open(i) as img:
        buffer = BytesIO()
        img = img.convert("RGB")
        img.save(buffer, format="JPEG", quality=85, subsampling=2,optimize=True)
        imagen = ImageReader(buffer)
        img_n : int = img.size[0]
        img_l : int = img.size[1]
        usablex = 0.0
        usabley = 0.0
        imgtx = 0.0
        imgty = 0.0
        x = 0.0
        y = 0.0
        if Dinamico:
            Ancho = img_n * 72 / 300
            Alto = img_l * 72 / 300
        else:
            match Horientacion:
                case 1:
                    Ancho, Alto = portrait(Formato)
                case 2:
                    Ancho, Alto = landscape(Formato)
                case 3:
                    if img_n > img_l:
                        Ancho, Alto = landscape(Formato)
                    else:
                        Ancho, Alto = portrait(Formato)
                case _:
                    print("Error inesperado")
                    break
        usablex = Ancho - Margenes["Izq"] - Margenes["Der"]
        usabley = Alto - Margenes["Sup"] - Margenes["Sup"]
        match TTam:
            case 1:
                imgtx = usablex * (Tamaño[0] / 100)
                imgty = usabley * (Tamaño[1] / 100)
            case 2:
                imgtx = Tamaño[0]
                imgty = Tamaño[1]
            case _:
                print("Error inesperado")
        if TPos == 1:
            match PosP[0]:
                case 1:
                    x = Margenes["Izq"]
                case 2:
                    x = ((Ancho - imgtx) / 2) - Margenes["Der"] + Margenes["Izq"]
                case 3:
                    x = Ancho - Margenes["Der"] - imgtx
                case _:
                    print("Error inesperado")
            match PosP[1]:
                case 1:
                    y = Margenes["Inf"]
                case 2:
                    y = ((Alto - imgty) / 2) - Margenes["Sup"] + Margenes["Inf"]
                case 3:
                    y = Alto - Margenes["Sup"] - imgty
                case _:
                    print("Error inesperado")
        else:
            x = PosM[0]
            y = PosM[1]
        Pdf.setPageSize((Ancho, Alto))
        Pdf.drawImage(imagen, x, y, width=imgtx, height=imgty, preserveAspectRatio=Escalado)
        Pdf.showPage()

Pdf.save()
if NameA != "":
    print("El pdf esta en: " + str(Path(Ruta)) + "/" + str(Path(Ruta).name) + " (" + NameA + ")" + ".pdf")
else:
    print("El pdf esta en: " + str(Path(Ruta)) + "/" + str(Path(Ruta).name) + ".pdf")
input("Pulse enter para cerrar el programa")