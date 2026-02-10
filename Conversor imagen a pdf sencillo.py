#Librerias
from pathlib import Path
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape, portrait
from reportlab.lib.utils import ImageReader
from io import BytesIO

#Variables
Ruta : str = ""
Opcion = False
Imagenes : list = []
Max_caracter : int = 0
Archivos : list = []
Ordenados : list = []
Pdf : canvas.Canvas = None
Escalado : bool = False
Horientacion : int = 3
Margenes_y : float = 0
Margenes_x : float = 0
Porcentage_x : float = 0
Porcentage_y : float = 0

#Confirmacion de ruta
while True:
    Ruta = ""
    Ruta = input("En que ruta carpeta estan las imagenes \n(Si es la misma en la que esta este archivo solo pulse enter)\n:  ")
    if Ruta in ["", "."]:
        Ruta = str(Path(__file__).parent)
    if Path(Ruta).exists():
        print("La ruta escogida es: " + Ruta)
        while True:
            match input("Si no esta seguro presione 1 en caso de estar seguro presione 2: "):
                case "1":
                    Opcion = False
                    break
                case "2":
                    Opcion = True
                    break
                case _:
                    print("Ingrese un valor valido")
    else:
        print("La ruta es invalida")
    if Opcion:
        break

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
Ancho, Alto = A4

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

#Eleccion de horientacion
while True:
    match input("Si quiere que todas las paginas esten en vertical presione 1 \nSi quiere que todas las paginas esten en horizontal presione 2 \nSi quiere que el programa decida la mejor horientacion presione 3 \n: "):
        case "1":
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

#Tipo de escalado
while True:
    match input("Si quiere las imagenes se escalen con deformacion presione 1 \nSi quiere que las imagenes se escalen sin deformacion aunque queden espacios en blanco presione 2 \n: "):
        case "1":
            Escalado = False
            break
        case "2":
            Escalado = True
            break
        case _:
            print("Ingrese un valor valido")

print("Empezando conversion")

#Convertir Pdf
for i in Ordenados:
    escalax = 0
    escalay = 0
    i = Path(i)
    print(str(i.name) + " ha sido integrado")
    with Image.open(i) as img:
        buffer = BytesIO()
        img = img.convert("RGB")
        img.save(buffer, format="JPEG", quality=85, subsampling=2,optimize=True)
        imagen = ImageReader(buffer)
        img_n : int = img.size[0]
        img_l : int = img.size[1]
        match Horientacion:
            case 1:
                Ancho, Alto = portrait(A4)
            case 2:
                Ancho, Alto = landscape(A4)
            case 3:
                if img_n > img_l:
                    Ancho, Alto = landscape(A4)
                else:
                    Ancho, Alto = portrait(A4)
            case _:
                print("error inesperado")
                break
        usablex = Ancho * (100 / 100)
        usabley = Alto * (100 / 100)
        usablex = usablex - (20 * 2)
        usabley = usabley - (20 * 2)
        escalax : float = usablex / img_n
        escalay : float = usabley / img_l
        img_n : float = img_n * escalax
        img_l : float = img_l * escalay
        x : float = (Ancho - img_n) / 2
        y : float = (Alto - img_l) / 2
        Pdf.setPageSize((Ancho, Alto))
        Pdf.drawImage(imagen, x, y, width=usablex, height=usabley, preserveAspectRatio=Escalado)
        Pdf.showPage()

Pdf.save()
if NameA != "":
    print("El pdf esta en: " + str(Path(Ruta)) + "/" + str(Path(Ruta).name) + " (" + NameA + ")" + ".pdf")
else:
    print("El pdf esta en: " + str(Path(Ruta)) + "/" + str(Path(Ruta).name) + ".pdf")
input("Pulse enter para cerrar el programa")