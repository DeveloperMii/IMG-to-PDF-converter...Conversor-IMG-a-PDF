#Librerias
from pathlib import Path
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
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
Ancho : float = None
Alto : float = None
buffer = BytesIO()

Ruta = str(Path(__file__).parent)

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

print("Empezando conversion")

#Convertir Pdf
for i in Ordenados:
    i = Path(i)
    print(str(i.name) + " ha sido integrado")
    with Image.open(i) as img:
        buffer = BytesIO()
        img = img.convert("RGB")
        img.save(buffer, format="JPEG", quality=85, subsampling=2,optimize=True)
        buffer.seek(0)
        imagen = ImageReader(buffer)
        img_n : int = img.size[0]
        img_l : int = img.size[1]
        Ancho = img_n * 72 / 300
        Alto = img_l * 72 / 300
        x = 0
        y = 0
        Pdf.setPageSize((Ancho, Alto))
        Pdf.drawImage(imagen, x, y, width=Ancho, height=Alto, preserveAspectRatio=Escalado)
        Pdf.showPage()
        buffer.close()

Pdf.save()