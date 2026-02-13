#Libraries
from pathlib import Path
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
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
Width : float = None
Height : float = None

Route = str(Path(__file__).parent)

#Overwrite protection
NameA = ""
if Path(str(Path(Route)) + "/" + str(Path(Route).name) +".pdf").exists():
    NameA = "0"
    for i in Path(Route).iterdir():
        if i.stem[:len(Path(Route).name)] == str(Path(Route).name):
            NameA = str(int(NameA) + 1)
    Pdf : canvas.Canvas = canvas.Canvas(str(Path(Route)) + "/" + str(Path(Route).name) + " (" + NameA + ")" + ".pdf", pagesize=A4)
else:
    Pdf : canvas.Canvas = canvas.Canvas(str(Path(Route)) + "/" + str(Path(Route).name) + ".pdf", pagesize=A4)

#Image selection
for i in Path(Route).iterdir():
    chara = 0
    if i.suffix.lower() in [".png", ".jpg", ".jpeg", "webp", ".tiff", ".bmp", "ico"]:
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

print("Starting conversion")

#Convertir Pdf
for i in Ordered:
    i = Path(i)
    print(str(i.name) + " has been integrated")
    with Image.open(i) as img:
        buffer = BytesIO()
        img = img.convert("RGB")
        img.save(buffer, format="JPEG", quality=85, subsampling=2,optimize=True)
        buffer.seek(0)
        img = ImageReader(buffer)
        img_n : int = img.size[0]
        img_l : int = img.size[1]
        Width = img_n * 72 / 300
        Height = img_l * 72 / 300
        x = 0
        y = 0
        Pdf.setPageSize((Width, Height))
        Pdf.drawImage(img, x, y, width=Width, height=Height, preserveAspectRatio=Scaling)
        Pdf.showPage()
        buffer.close()

Pdf.save()