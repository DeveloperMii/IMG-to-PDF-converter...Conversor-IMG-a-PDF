#Libraries
from pathlib import Path
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, LETTER, LEGAL, TABLOID, B0, B1, B2, B3, B4, B5, B6, B7, B8, B9, B10, landscape, portrait
from reportlab.lib.utils import ImageReader
from io import BytesIO

#Variables
Route : str = ""
Img : list = []
Max_character : int = 0
Files : list = []
Ordered : list = []
Pdf : canvas.Canvas = None
Scaling : bool = True
Orientation : int = 3
Margins : dict = {"Top" : 0.0, "Bot" : 0.0, "lef" : 0.0, "Rig" : 0.0}
Width : float = None
Height : float = None
Format : list = [0.0,0.0]
Dynamic : bool = False
ImgSize : list = [100.0,100.0]
SizeType : int = 1
PPosition : list = [2,2]
CPosition : list = [0.0,0.0]
TPosition : int = 1

#Route confirmation
while True:
    option = False
    Route = ""
    Route = input("¿En que ruta carpeta estan las imagenes? \n(Si es la misma en la que esta este archivo, solo pulse enter) \n :  ").strip()
    if Route in ["", "."]:
        Route = str(Path(__file__).parent)
    if Path(Route).exists():
        print("La ruta escogida es: " + Route)
        while True:
            match input("Si no esta seguro, presione 1 \nSi esta seguro, presione 2 \n : ").strip():
                case "1":
                    option = False
                    break
                case "2":
                    option = True
                    break
                case _:
                    print("Ingrese un valor valido")
    else:
        print("La ruta es invalida")
    if option:
        break

print("")

#Overwrite protection
NameA = ""
if Path(str(Path(Route)) + "/" + str(Path(Route).name) + ".pdf").exists():
    NameA = "1"
    for i in Path(Route).iterdir():
        if i.stem[:len(Path(Route).name)] == str(Path(Route).name):
            if Path(str(Path(Route)) + "/" + str(Path(Route).name) + " (" + NameA + ")" + ".pdf").exists():
                NameA = str(int(NameA) + 1)
            else:
                break
    Pdf : canvas.Canvas = canvas.Canvas(str(Path(Route)) + "/" + str(Path(Route).name) + " (" + NameA + ")" + ".pdf", pagesize=A4)
else:
    Pdf : canvas.Canvas = canvas.Canvas(str(Path(Route)) + "/" + str(Path(Route).name) + ".pdf", pagesize=A4)

Format[0], Format[1] = A4

#Image selection
for i in Path(Route).iterdir():
    chara = 0
    if i.suffix.lower() in [".png", ".jpg", ".jpeg", ".webp", ".tiff", ".bmp", "ico"]:
        for j in i.stem:
            if j in ["0","1","2","3","4","5","6","7","8","9"]:
                chara = chara + 1
            else:
                break
        if chara > Max_character:
            Max_character = chara
        Img.append(i)

#Sort them
for i in Img:
    i = Path(i)
    chara = 0
    for j in i.stem:
        if j in ["0","1","2","3","4","5","6","7","8","9"]:
            chara = chara + 1
        else:
            break
    Files.append(str(str(i.parent) + "/" + str(i.name[:chara]).zfill(Max_character) + str(i.name[chara:])))
Files.sort()

#List with the routes sorted
for i in range(0, len(Files)):
    name = ""
    for j in range(0, len(Path(Files[i]).stem)):
        if Path(str(Path(Files[i]).parent) + "/" + str(Path(Files[i]).stem[j:] + str(Path(Files[i]).suffix))).exists():
            name = Path(Files[i]).stem[j:]
        if Path(Files[i]).stem[j] != "0":
            break
    Ordered.append(str(str(Path(Img[i]).parent) + "/" + name + str(Path(Files[i]).suffix)))

#Selecting the PDF size
while True:
    finished = False
    match input("Si quiere seleccionar un tamaño base para el PDF, pulse 1 \nSi quiere un tamaño personalizado para el PDF, pulse 2 \nSi quiere que el tamaño del PDF sea adaptado para cada imagen, pulse 3 \nSi solo se pulsa enter, la opcion elegida sera la 1 \n : ").strip():
        case "" | "." | "1":
            match str(input("Selecione el tamaño del papel entre (solo escriba alguna de las siguientes opciones): \n A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, B0, B1, B2, B3, B4, B5, B6, B7, B8, B9, B10, LETTER, LEGAL, TABLOID \nSi solo preciona enter, se eligira A4 (por ser el mas comun) \n :")).strip().upper():
                case "A0":
                    Format = A0
                    finished = True
                case "A1":
                    Format = A1
                    finished = True
                case "A2":
                    Format = A2
                    finished = True
                case "A3":
                    Format = A3
                    finished = True
                case "" | "." | "A4":
                    Format = A4
                    finished = True
                case "A5":
                    Format = A5
                    finished = True
                case "A6":
                    Format = A6
                    finished = True
                case "A7":
                    Format = A7
                    finished = True
                case "A8":
                    Format = A8
                    finished = True
                case "A9":
                    Format = A9
                    finished = True
                case "A10":
                    Format = A10
                    finished = True
                case "B0":
                    Format = B0
                    finished = True
                case "B1":
                    Format = B1
                    finished = True
                case "B2":
                    Format = B2
                    finished = True
                case "B3":
                    Format = B3
                    finished = True
                case "B4":
                    Format = B4
                    finished = True
                case "B5":
                    Format = B5
                    finished = True
                case "B6":
                    Format = B6
                    finished = True
                case "B7":
                    Format = B7
                    finished = True
                case "B8":
                    Format = B8
                    finished = True
                case "B9":
                    Format = B9
                    finished = True
                case "B10":
                    Format = B10
                    finished = True
                case "LETTER":
                    Format = LETTER
                    finished = True
                case "LEGAL":
                    Format = LEGAL
                    finished = True
                case "TABLOID":
                    Format = TABLOID
                    finished = True
                case _:
                    print("Ingrese una opcion valida \nVolviendo al inicio")
        case "2":
            measures : list = ["", ""]
            type = input("Escoja una de las siguientes unidades (Escribala como vera acontinuacion): \n mm  cm  inch  pt \n (72 PT = 1 inch)\n : ").strip().lower()
            match type:
                case "mm" | "cm" | "inch" | "pt":
                    while True:
                        validated = True
                        measures[0] = input("Ingrese la medida horizontal en unidad escogida (solo el valor): ").strip()
                        for i in measures[0]:
                            if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                validated = False
                                print("Ingrese un valor valido")
                                break
                            if i == ",":
                                measures[0].replace(",", ".")
                        if validated:
                            break
                    while True:
                        validated = True
                        measures[1] = input("Ingrese la medida vertical en unidad escogida (solo el valor): ").strip()
                        for i in measures[1]:
                            if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                validated = False
                                print("Ingrese un valor valido")
                                break
                            if i == ",":
                                measures[1].replace(",", ".")
                        if validated:
                            break
                    if type == "mm":
                        Format[0] = float(measures[0]) * (72 / 25.4)
                        Format[1] = float(measures[1]) * (72 / 25.4)
                        finished = True
                    elif type == "cm":
                        Format[0] = float(measures[0]) * (72 / 2.54)
                        Format[1] = float(measures[1]) * (72 / 2.54)
                        finished = True
                    elif type == "inch":
                        Format[0] = float(measures[0]) * 72
                        Format[1] = float(measures[1]) * 72
                        finished = True
                    else:
                        Format[0] = float(measures[0])
                        Format[1] = float(measures[1])
                        finished = True
                case _:
                    print("ingrese una unidad valida \nVolviendo al inicio")
        case "3":
            match input("Si no esta seguro, presione 1 \nSi esta seguro, presione 2 \n : ").strip():
                case "1":
                    print("Volviendo al inicio")
                case "2":
                    Dynamic = True
                    finished = True
                case _:
                    print("Ingrese una opcion valida \nVolviendo al inicio")
        case _:
            print("Ingrese una opcion valida")
    if finished:
        break

print("")

#Choice of orientation
if not Dynamic:
    while True:
        match input("Si quiere que todas las paginas esten en vertical, presione 1 \nSi quiere que todas las paginas esten en horizontal, presione 2 \nSi quiere que el programa decida la mejor horientacion, presione 3 \nSi solo se pulsa enter, la opcion elegida sera la 1 \n : ").strip():
            case "" | "." | "1":
                Orientation = 1
                break
            case "2":
                Orientation = 2
                break
            case "3":
                Orientation = 3
                break
            case _:
                print("Ingrese un valor valido")
    print("")

#Margin selection
while True:
    finished = False
    match input("Si quiere seleccionar un tamaño base para los margenes, pulse 1 \nSi quiere un tamaño personalizado para los margenes, pulse 2 \nSi solo se pulsa enter, la opcion elegida sera la 1 \n: ").strip():
        case "" | "." | "1":
            match input("Selecione el tamaño del papel entre (solo escriba el numero indice de alguna de las siguientes opciones): \n 1. Ninguno  0mm  0cm  0inch  0PT \n 2. Muy estrecho  10mm  1cm  0.39inch  28.35PT \n 3. Estrecho  15mm  1.5cm  0.59inch  42.52PT \n 4. Estandar  25mm  2.5cm  1inch  72PT \n 5. Ancho  30mm  3cm  1.18inch  85.04PT \n 6. Muy Ancho 40mm  4cm  1.57inch  113.39PT \n Si solo preciona enter se eligira 4. Estandar (por ser el mas comun) \n:").strip():
                case "1":
                    Margins["Top"] = 0.0
                    Margins["Bot"] = 0.0
                    Margins["lef"] = 0.0
                    Margins["Rig"] = 0.0
                    finished = True
                case "2":
                    Margins["Top"] = 28.35
                    Margins["Bot"] = 28.35
                    Margins["lef"] = 28.35
                    Margins["Rig"] = 28.35
                    finished = True
                case "3":
                    Margins["Top"] = 42.52
                    Margins["Bot"] = 42.52
                    Margins["lef"] = 42.52
                    Margins["Rig"] = 42.52
                    finished = True
                case "." | "" | "4":
                    Margins["Top"] = 72.0
                    Margins["Bot"] = 72.0
                    Margins["lef"] = 72.0
                    Margins["Rig"] = 72.0
                    finished = True
                case "5":
                    Margins["Top"] = 85.04
                    Margins["Bot"] = 85.04
                    Margins["lef"] = 85.04
                    Margins["Rig"] = 85.04
                    finished = True
                case "6":
                    Margins["Top"] = 113.39
                    Margins["Bot"] = 113.39
                    Margins["lef"] = 113.39
                    Margins["Rig"] = 113.39
                    finished = True
                case _:
                    print("Ingrese una opcion valida \nVolviendo al inicio")
        case "2":
            measures : list = ["", "", "", ""]
            type = input("Escoja una de las siguientes unidades (Escribala como vera acontinuacion): \n mm  cm  inch  pt \n (72 PT = 1 inch)\n : ").strip().lower()
            match type:
                case "mm" | "cm" | "inch" | "pt":
                    while True:
                        validated = True
                        measures[0] = input("Ingrese la medida del margen superior en unidad escogida (solo el valor): ").strip()
                        for i in measures[0]:
                            if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                validated = False
                                print("Ingrese un valor valido")
                                break
                            if i == ",":
                                measures[0].replace(",", ".")
                        if validated:
                            break
                    while True:
                        validated = True
                        measures[1] = input("Ingrese la medida del margen inferior en unidad escogida (solo el valor): ").strip()
                        for i in measures[1]:
                            if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                validated = False
                                print("Ingrese un valor valido")
                                break
                            if i == ",":
                                measures[1].replace(",", ".")
                        if validated:
                            break
                    while True:
                        validated = True
                        measures[2] = input("Ingrese la medida margen izquierdo en unidad escogida (solo el valor): ").strip()
                        for i in measures[2]:
                            if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                validated = False
                                print("Ingrese un valor valido")
                                break
                            if i == ",":
                                measures[2].replace(",", ".")
                        if validated:
                            break
                    while True:
                        validated = True
                        measures[3] = input("Ingrese la medida del margen derecho en unidad escogida (solo el valor): ").strip()
                        for i in measures[3]:
                            if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                validated = False
                                print("Ingrese un valor valido")
                                break
                            if i == ",":
                                measures[1].replace(",", ".")
                        if validated:
                            break
                    if type == "mm":
                        Margins["Top"] = float(measures[0]) * (72 / 25.4)
                        Margins["Bot"] = float(measures[1]) * (72 / 25.4)
                        Margins["lef"] = float(measures[2]) * (72 / 25.4)
                        Margins["Rig"] = float(measures[3]) * (72 / 25.4)
                        finished = True
                    elif type == "cm":
                        Margins["Top"] = float(measures[0]) * (72 / 2.54)
                        Margins["Bot"] = float(measures[1]) * (72 / 2.54)
                        Margins["lef"] = float(measures[2]) * (72 / 2.54)
                        Margins["Rig"] = float(measures[3]) * (72 / 2.54)
                        finished = True
                    elif type == "inch":
                        Margins["Top"] = float(measures[0]) * 72
                        Margins["Bot"] = float(measures[1]) * 72
                        Margins["lef"] = float(measures[2]) * 72
                        Margins["Rig"] = float(measures[3]) * 72
                        finished = True
                    else:
                        Margins["Top"] = float(measures[0])
                        Margins["Bot"] = float(measures[1])
                        Margins["lef"] = float(measures[2])
                        Margins["Rig"] = float(measures[3])
                        finished = True
                case _:
                    print("ingrese una unidad valida \nVolviendo al inicio")
        case _:
            print("Ingrese una opcion valida")
    if finished:
        break

print("")

#Image size selection
while True:
    finished = False
    match input("Si quiere que la imagen ocupe todo el espacio posible pulse 1 \nSi quiere que la imagen tenga un tamaño personalizado pulse 2 (Cabe resaltar que si ese tamaño es mayor al de la pagina la imagen puede cortarse) \nSi solo se pulsa enter la opcion elegida sera la 1 \n : ").strip():
        case "" | "." | "1":
            SizeType = 1
            ImgSize[0] = 100
            ImgSize[1] = 100
            finished = True
        case "2":
            measures : list = ["", ""]
            type = input("Escoja una de las siguientes unidades (Escribala como vera acontinuacion): \n mm  cm  inch  pt  % \n (72 PT = 1 inch)\n : ").strip().lower()
            match type:
                case "mm" | "cm" | "inch" | "pt" | "%":
                    while True:
                        validated = True
                        measures[0] = input("Ingrese la tamaño horizontal en unidad escogida (solo el valor): ").strip()
                        for i in measures[0]:
                            if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                validated = False
                                print("Ingrese un valor valido")
                                break
                            if i == ",":
                                measures[0].replace(",", ".")
                        if validated:
                            break
                    while True:
                        validated = True
                        measures[1] = input("Ingrese la tamaño vertical en unidad escogida (solo el valor): ").strip()
                        for i in measures[1]:
                            if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                validated = False
                                print("Ingrese un valor valido")
                                break
                            if i == ",":
                                measures[1].replace(",", ".")
                        if validated:
                            break
                    if type == "mm":
                        ImgSize[0] = float(measures[0]) * (72 / 25.4)
                        ImgSize[1] = float(measures[1]) * (72 / 25.4)
                        SizeType = 2
                        finished = True
                    elif type == "cm":
                        ImgSize[0] = float(measures[0]) * (72 / 2.54)
                        ImgSize[1] = float(measures[1]) * (72 / 2.54)
                        SizeType = 2
                        finished = True
                    elif type == "inch":
                        ImgSize[0] = float(measures[0]) * 72
                        ImgSize[1] = float(measures[1]) * 72
                        SizeType = 2
                        finished = True
                    elif type == "pt":
                        ImgSize[0] = float(measures[0])
                        ImgSize[1] = float(measures[1])
                        SizeType = 2
                        finished = True
                    else:
                        ImgSize[0] = float(measures[0])
                        ImgSize[1] = float(measures[1])
                        SizeType = 1
                        finished = True
                case _:
                    print("ingrese una unidad valida \nVolviendo al inicio")
        case _:
            print("Ingrese una opcion valida")
    if finished:
        break

print("")

#Scaling type selection
while True:
    match input("Si quiere las imagenes se escalen usando todo el espacio disponible pero con deformacion, presione 1 \nSi quiere que las imagenes se escalen sin deformacion aunque no se use todo el espacio disponible, presione 2 \nSi solo se pulsa enter, la opcion elegida sera la 2 \n: ").strip():
        case "1":
            Scaling = False
            break
        case "" | "." | "2":
            Scaling = True
            break
        case _:
            print("Ingrese un valor valido")

print("")

#Position selection
while True:
    finished = False
    match input("Si quiere una posicion predefinida pulse 1 \nSi quiere una posicion personalizada personalizado pulse 2 (Ante valores que no concuerden con el tamaño de la hoja pueden exister recortes en la imagen) \nSi solo se pulsa enter la opcion elegida sera la 1 \n: ").strip():
        case "" | "." | "1":
            match input("Elija una de las siguentes posiciones (solo ingrese el indice) \nSi solo presiona enter, la opcion 5 centro sera la predeterminada \n 1. Sup Izq 2. Sup Cen 3. Sup Der \n 4. Cen Izq 5. Centro  6. Cen Der \n 7. Inf Izq 8. Inf Cen 9. Inf Der \n:").strip():
                case "1":
                    PPosition[0] = 1
                    PPosition[1] = 1
                    TPosition = 1
                    finished = True
                case "2":
                    PPosition[0] = 1
                    PPosition[1] = 2
                    TPosition = 1
                    finished = True
                case "3":
                    PPosition[0] = 1
                    PPosition[1] = 3
                    TPosition = 1
                    finished = True
                case "4":
                    PPosition[0] = 2
                    PPosition[1] = 1
                    TPosition = 1
                    finished = True
                case "" | "." | "5":
                    PPosition[0] = 2
                    PPosition[1] = 2
                    TPosition = 1
                    finished = True
                case "6":
                    PPosition[0] = 2
                    PPosition[1] = 3
                    TPosition = 1
                    finished = True
                case "7":
                    PPosition[0] = 3
                    PPosition[1] = 1
                    TPosition = 1
                    finished = True
                case "8":
                    PPosition[0] = 3
                    PPosition[1] = 2
                    TPosition = 1
                    finished = True
                case "9":
                    PPosition[0] = 3
                    PPosition[1] = 3
                    TPosition = 1
                    finished = True
                case _:
                    print("Ingrese una opcion valida \nVolviendo al inicio")
        case "2":
            input("Antes de pasar con las medidas me gustaria explicar que el punto de referencia para tomarlas es la esquina inferior izquierda de la imagen")
            measures : list = ["", ""]
            type = input("Escoja una de las siguientes unidades (Escribala como vera acontinuacion): \n mm  cm  inch  pt \n (72 PT = 1 inch)\n : ").strip().lower()
            match type:
                case "mm" | "cm" | "inch":
                    while True:
                        validated = True
                        measures[0] = input("Ingrese la posicion horizontal en unidad escogida (solo el valor): ").strip()
                        for i in measures[0]:
                            if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                validated = False
                                print("Ingrese un valor valido")
                                break
                            if i == ",":
                                measures[0].replace(",", ".")
                        if validated:
                            break
                    while True:
                        validated = True
                        measures[1] = input("Ingrese la posicion vertical en unidad escogida (solo el valor): ").strip()
                        for i in measures[1]:
                            if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                validated = False
                                print("Ingrese un valor valido")
                                break
                            if i == ",":
                                measures[1].replace(",", ".")
                        if validated:
                            break
                    if type == "mm":
                        CPosition[0] = float(measures[0]) * (72 / 25.4)
                        CPosition[1] = float(measures[1]) * (72 / 25.4)
                        TPosition = 2
                        finished = True
                    elif type == "cm":
                        CPosition[0] = float(measures[0]) * (72 / 2.54)
                        CPosition[1] = float(measures[1]) * (72 / 2.54)
                        TPosition = 2
                        finished = True
                    elif type == "inch":
                        CPosition[0] = float(measures[0]) * 72
                        CPosition[1] = float(measures[1]) * 72
                        TPosition = 2
                        finished = True
                    else:
                        CPosition[0] = float(measures[0])
                        CPosition[1] = float(measures[1])
                        TPosition = 2
                        finished = True
                case _:
                    print("ingrese una unidad valida \nVolviendo al inicio")
        case _:
            print("Ingrese una opcion valida")
    if finished:
        break

print("Empezando conversion")

#Create the PDF
for i in Ordered:
    i = Path(i)
    print(str(i.name) + " ha sido integrado")
    with Image.open(i) as img:
        buffer = BytesIO()
        img = img.convert("RGB")
        img.save(buffer, format="JPEG", quality=85, subsampling=2,optimize=True)
        image = ImageReader(buffer)
        img_n : int = img.size[0]
        img_l : int = img.size[1]
        xsafespace = 0.0
        ysafespace = 0.0
        imgtx = 0.0
        imgty = 0.0
        x = 0.0
        y = 0.0
        if Dynamic:
            Width = img_n * 72 / 300
            Height = img_l * 72 / 300
        else:
            match Orientation:
                case 1:
                    Width, Height = portrait(Format)
                case 2:
                    Width, Height = landscape(Format)
                case 3:
                    if img_n > img_l:
                        Width, Height = landscape(Format)
                    else:
                        Width, Height = portrait(Format)
                case _:
                    print("Error inesperado")
                    break
        xsafespace = Width - Margins["lef"] - Margins["Rig"]
        ysafespace = Height - Margins["Top"] - Margins["Top"]
        match SizeType:
            case 1:
                imgtx =  xsafespace * (ImgSize[0] / 100)
                imgty = ysafespace * (ImgSize[1] / 100)
            case 2:
                imgtx = ImgSize[0]
                imgty = ImgSize[1]
            case _:
                print("Error inesperado")
        if TPosition == 1:
            match PPosition[0]:
                case 1:
                    x = Margins["lef"]
                case 2:
                    x = ((Width - imgtx) / 2) - Margins["Rig"] + Margins["lef"]
                case 3:
                    x = Width - Margins["Rig"] - imgtx
                case _:
                    print("Error inesperado")
            match PPosition[1]:
                case 1:
                    y = Margins["Bot"]
                case 2:
                    y = ((Height - imgty) / 2) - Margins["Top"] + Margins["Bot"]
                case 3:
                    y = Height - Margins["Top"] - imgty
                case _:
                    print("Error inesperado")
        else:
            x = CPosition[0]
            y = CPosition[1]
        Pdf.setPageSize((Width, Height))
        Pdf.drawImage(image, x, y, width=imgtx, height=imgty, preserveAspectRatio=Scaling)
        Pdf.showPage()

Pdf.save()
if NameA != "":
    print("El pdf esta en: " + str(Path(Route)) + "/" + str(Path(Route).name) + " (" + NameA + ")" + ".pdf")
else:
    print("El pdf esta en: " + str(Path(Route)) + "/" + str(Path(Route).name) + ".pdf")
input("Pulse enter para cerrar el programa")