#Libraries
from pathlib import Path
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape, portrait
from reportlab.lib.utils import ImageReader
from io import BytesIO

#Variables
Route : str = ""
Option = False
Img : list = []
Max_character : int = 0
Files : list = []
Ordered : list = []
Pdf : canvas.Canvas = None
Scaling : bool = False
Orientation : int = 3

#Route confirmation
while True:
    Route = ""
    Route = input("¿En que ruta carpeta estan las imagenes? \n(Si es la misma en la que esta este archivo, solo pulse enter) \n :  ")
    if Route in ["", "."]:
        Route = str(Path(__file__).parent)
    if Path(Route).exists():
        print("La ruta escogida es: " + Route)
        while True:
            match input("Si no esta seguro, presione 1 \nSi esta seguro, presione 2 \n : "):
                case "1":
                    Option = False
                    break
                case "2":
                    Option = True
                    break
                case _:
                    print("Ingrese un valor valido")
    else:
        print("La ruta es invalida")
    if Option:
        break

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

Width, Height = A4

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

#Choice of orientation
while True:
    match input("Si quiere que todas las paginas esten en vertical, presione 1 \nSi quiere que todas las paginas esten en horizontal, presione 2 \nSi quiere que el programa decida la mejor horientacion, presione 3 \nSi solo se pulsa enter, la opcion elegida sera la 1 \n : "):
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

#Type of scaling
while True:
    match input("Si quiere las imagenes se escalen usando todo el espacio disponible pero con deformacion, presione 1 \nSi quiere que las imagenes se escalen sin deformacion aunque no se use todo el espacio disponible, presione 2 \nSi solo se pulsa enter, la opcion elegida sera la 2 \n: "):
        case "1":
            Scaling = False
            break
        case "" | "." | "2":
            Scaling = True
            break
        case _:
            print("Ingrese un valor valido")

print("Empezando conversion")

#Create the PDF
for i in Ordered:
    scale : list = [0.0,0.0]
    i = Path(i)
    print(str(i.name) + " ha sido integrado")
    with Image.open(i) as img:
        buffer = BytesIO()
        img = img.convert("RGB")
        img.save(buffer, format="JPEG", quality=85, subsampling=2,optimize=True)
        image = ImageReader(buffer)
        img_n : int = img.size[0]
        img_l : int = img.size[1]
        match Orientation:
            case 1:
                Width, Height = portrait(A4)
            case 2:
                Width, Height = landscape(A4)
            case 3:
                if img_n > img_l:
                    Width, Height = landscape(A4)
                else:
                    Width, Height = portrait(A4)
            case _:
                print("error inesperado")
                break
        xsafespace = Width * (100 / 100)
        ysafespace = Height * (100 / 100)
        xsafespace = xsafespace - (20 * 2)
        ysafespace = ysafespace - (20 * 2)
        scale[0] = xsafespace / img_n
        scale[1] = ysafespace / img_l
        img_n : float = img_n * scale[0]
        img_l : float = img_l * scale[1]
        x : float = (Width - img_n) / 2
        y : float = (Height - img_l) / 2
        Pdf.setPageSize((Width, Height))
        Pdf.drawImage(image, x, y, width=xsafespace, height=ysafespace, preserveAspectRatio=Scaling)
        Pdf.showPage()

Pdf.save()
if NameA != "":
    print("El pdf esta en: " + str(Path(Route)) + "/" + str(Path(Route).name) + " (" + NameA + ")" + ".pdf")
else:
    print("El pdf esta en: " + str(Path(Route)) + "/" + str(Path(Route).name) + ".pdf")

input("Pulse enter para cerrar el programa")