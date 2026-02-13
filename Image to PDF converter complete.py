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
    Route = input("In which folder are the images located? \n(If it is the same folder as this file, just press Enter)\n:  ").strip()
    if Route in ["", "."]:
        Route = str(Path(__file__).parent)
    if Path(Route).exists():
        print("The chosen route is: " + Route)
        while True:
            match input("If you are unsure, press 1 \nIf you are sure, press 2 \n : ").strip():
                case "1":
                    option = False
                    break
                case "2":
                    option = True
                    break
                case _:
                    print("Enter a valid value")
    else:
        print("The route is invalid")
    if option:
        break

print("")

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
Format[0], Format[1] = A4

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

#Selecting the PDF size
while True:
    finished = False
    match input("If you want to select a base size for the PDF, press 1 \nIf you want a custom size for the PDF, press 2 \nIf you want the PDF size to be adapted for each image, press 3 \nIf you just press enter, the chosen option will be 1 \n : ").strip():
        case "" | "." | "1":
            match str(input("Select the paper size from (just type one of the following options): \n A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, B0, B1, B2, B3, B4, B5, B6, B7, B8, B9, B10, LETTER, LEGAL, TABLOID \nIf you just press Enter, A4 will be selected (as it is the most common) \n :")).strip().upper():
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
                    print("Enter a valid option \nReturning to the beginning")
        case "2":
            measures : list = ["", ""]
            type = input("Choose one of the following units (Write it as shown below): \n mm  cm  inch  pt \n (72 PT = 1 inch) \n : ").strip().lower()
            match type:
                case "mm" | "cm" | "inch" | "pt":
                    while True:
                        validated = True
                        measures[0] = input("Enter the horizontal measurement in the selected unit (value only): ").strip()
                        for i in measures[0]:
                            if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                validated = False
                                print("Enter a valid value")
                                break
                            if i == ",":
                                measures[0].replace(",", ".")
                        if validated:
                            break
                    while True:
                        validated = True
                        measures[1] = input("Enter the vertical measurement in the selected unit (value only): ").strip()
                        for i in measures[1]:
                            if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                validated = False
                                print("Enter a valid value")
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
                    print("Enter a valid unit \nReturning to the beginning")
        case "3":
            match input("If you are unsure, press 1 \nIf you are sure, press 2 \n : ").strip():
                case "1":
                    print("Back to the beginning")
                case "2":
                    Dynamic = True
                    finished = True
                case _:
                    print("Enter a valid unit \nReturning to the beginning")
        case _:
            print("Enter a valid option")
    if finished:
        break

print("")

#Choice of orientation
if not Dynamic:
    while True:
        match input("If you want all pages to be vertical, press 1 \nIf you want all pages to be horizontal, press 2 \nIf you want the program to decide the best orientation, press 3 \nIf you just press Enter, the default option will be 1 \n : ").strip():
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
                print("Enter a valid value")
    print("")

#Margin selection
while True:
    finished = False
    match input("If you want to select a default margin size, press 1 \nIf you want a custom margin size, press 2 \nIf you just press Enter, the first option will be selected. \n : ").strip():
        case "" | "." | "1":
            match input("Select the paper size from (just type the index number of one of the following options): \n 1. None  0mm  0cm  0inch  0PT \n 2. Very narrow  10mm  1cm  0.39inch  28.35PT \n 3. Narrow  15mm  1.5cm  0.59inch  42.52PT \n 4. Standard  25mm  2.5cm  1inch  72PT \n 5. Wide  30mm  3cm  1.18inch  85.04PT \n 6. Very Wide 40mm  4cm  1.57inch  113.39PT \n If you just press enter, 4. Standard will be selected (as it is the most common) \n :").strip():
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
                    print("Enter a valid unit \nReturning to the beginning")
        case "2":
            measures : list = ["", "", "", ""]
            type = input("Choose one of the following units (Write it as shown below): \n mm  cm  inch  pt \n (72 PT = 1 inch)\n : ").strip().lower()
            match type:
                case "mm" | "cm" | "inch" | "pt":
                    while True:
                        validated = True
                        measures[0] = input("Enter the top margin measurement in the selected unit (value only): ").strip()
                        for i in measures[0]:
                            if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                validated = False
                                print("Enter a valid value")
                                break
                            if i == ",":
                                measures[0].replace(",", ".")
                        if validated:
                            break
                    while True:
                        validated = True
                        measures[1] = input("Enter the bottom margin measurement in the selected unit (value only): ").strip()
                        for i in measures[1]:
                            if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                validated = False
                                print("Enter a valid value")
                                break
                            if i == ",":
                                measures[1].replace(",", ".")
                        if validated:
                            break
                    while True:
                        validated = True
                        measures[2] = input("Enter the left margin measurement in the selected unit (value only): ").strip()
                        for i in measures[2]:
                            if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                validated = False
                                print("Enter a valid value")
                                break
                            if i == ",":
                                measures[2].replace(",", ".")
                        if validated:
                            break
                    while True:
                        validated = True
                        measures[3] = input("Enter the right margin measurement in the selected unit (value only): ").strip()
                        for i in measures[3]:
                            if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                validated = False
                                print("Enter a valid value")
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
                    print("Enter a valid unit \nBack to the beginning")
        case _:
            print("Enter a valid option")
    if finished:
        break

print("")

#Image size selection
while True:
    finished = False
    match input("If you want the image to occupy as much space as possible, press 1 \nIf you want the image to have a custom size, press 2 (Please note that if this size is larger than the page, the image may be cropped) \nIf you just press Enter, option 1 will be selected \n : ").strip():
        case "" | "." | "1":
            SizeType = 1
            ImgSize[0] = 100
            ImgSize[1] = 100
            finished = True
        case "2":
            measures : list = ["", ""]
            type = input("Choose one of the following units (Write it as shown below): \n mm  cm  inch  pt  % \n (72 PT = 1 inch)\n : ").strip().lower()
            match type:
                case "mm" | "cm" | "inch" | "pt" | "%":
                    while True:
                        validated = True
                        measures[0] = input("Enter the horizontal size in the selected unit (value only): ").strip()
                        for i in measures[0]:
                            if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                validated = False
                                print("Enter a valid value")
                                break
                            if i == ",":
                                measures[0].replace(",", ".")
                        if validated:
                            break
                    while True:
                        validated = True
                        measures[1] = input("Enter the vertical size in the selected unit (value only): ").strip()
                        for i in measures[1]:
                            if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                validated = False
                                print("Enter a valid value")
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
                    print("Enter a valid unit \nBack to the beginning")
        case _:
            print("Enter a valid option")
    if finished:
        break

print("")

#Scaling type selection
while True:
    match input("If you want the images to be scaled using all available space but with distortion, press 1 \nIf you want the images to be scaled without distortion even if all available space is not used, press 2 \nIf you just press Enter, option 2 will be selected \n : ").strip():
        case "1":
            Scaling = False
            break
        case "" | "." | "2":
            Scaling = True
            break
        case _:
            print("Enter a valid value")

print("")

#Position selection
while True:
    finished = False
    match input("If you want a predefined position, press 1 \nIf you want a custom position, press 2 (if the values do not match the size of the sheet, the image may be cropped) \nIf you just press Enter, option 1 will be selected. \n : ").strip():
        case "" | "." | "1":
            match input("Select one of the following positions (just enter the index) \nIf you just press enter, option 5 center will be the default \n 1. Top Left 2. Top Cen 3. Top Rig \n 4. Bot Lef 5. Center  6. Bot Rig \n 7. Bot Lef 8. Bot Cen 9. Bot Rig \n:").strip():
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
                    print("Enter a valid unit \nReturning to the beginning")
        case "2":
            input("Before moving on to the measurements, I would like to explain that the reference point for taking them is the lower left corner of the image")
            measures : list = ["", ""]
            type = input("Choose one of the following units (Write it as shown below): \n mm  cm  inch  pt \n (72 PT = 1 inch) \n : ").strip().lower()
            match type:
                case "mm" | "cm" | "inch" | "pt":
                    while True:
                        validated = True
                        measures[0] = input("Enter the horizontal position in the selected unit (value only).: ").strip()
                        for i in measures[0]:
                            if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                validated = False
                                print("Enter a valid value")
                                break
                            if i == ",":
                                measures[0].replace(",", ".")
                        if validated:
                            break
                    while True:
                        validated = True
                        measures[1] = input("Enter the vertical position in the selected unit (value only).: ").strip()
                        for i in measures[1]:
                            if not i in ["0","1","2","3","4","5","6","7","8","9",".",","]:
                                validated = False
                                print("Enter a valid value")
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
                    print("Enter a valid unit \nBack to the beginning")
        case _:
            print("Enter a valid option")
    if finished:
        break

print("Starting conversion")

#Create the PDF
for i in Ordered:
    i = Path(i)
    print(str(i.name) + " has been integrated")
    with Image.open(i) as img:
        buffer = BytesIO()
        img = img.convert("RGB")
        img.save(buffer, format="JPEG", quality=85, subsampling=2,optimize=True)
        imagen = ImageReader(buffer)
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
                    print("unexpected error")
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
                print("unexpected error")
        if TPosition == 1:
            match PPosition[0]:
                case 1:
                    x = Margins["lef"]
                case 2:
                    x = ((Width - imgtx) / 2) - Margins["Rig"] + Margins["lef"]
                case 3:
                    x = Width - Margins["Rig"] - imgtx
                case _:
                    print("unexpected error")
            match PPosition[1]:
                case 1:
                    y = Margins["Bot"]
                case 2:
                    y = ((Height - imgty) / 2) - Margins["Top"] + Margins["Bot"]
                case 3:
                    y = Height - Margins["Top"] - imgty
                case _:
                    print("unexpected error")
        else:
            x = CPosition[0]
            y = CPosition[1]
        Pdf.setPageSize((Width, Height))
        Pdf.drawImage(imagen, x, y, width=imgtx, height=imgty, preserveAspectRatio=Scaling)
        Pdf.showPage()

Pdf.save()
if NameA != "":
    print("The PDF is in: " + str(Path(Route)) + "/" + str(Path(Route).name) + " (" + NameA + ")" + ".pdf")
else:
    print("The PDF is in: " + str(Path(Route)) + "/" + str(Path(Route).name) + ".pdf")
    
input("Press Enter to close the program")