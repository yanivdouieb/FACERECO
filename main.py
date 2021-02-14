from __future__ import print_function
import cv2
import sys, time
print("FACERECO AI \n")
DrvLocDef = input("Dossier où se situe votre image : ")
DrvLoc = input("Dossier où sera exportée la photo : ")
imageExt = input("Extension de votre fichier de départ : ")
imagePath = DrvLocDef + "/" + input("Nom du fichier d'entrée : ") + "." + imageExt
imageOutput = DrvLoc + "/" + "FACERECO - " + input("Nom du fichier de sortie : FACERECO - ") + ".jpg";
CCP = "hcc.xml"
CC = cv2.CascadeClassifier(CCP)
image = cv2.imread(imagePath)
NBLoad = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
det_face = CC.detectMultiScale(NBLoad)

for(x,y,width,height) in det_face:
    cv2.rectangle(image, (x,y), (x+width, y+height), (0,255,0),5)

cv2.imwrite(imageOutput, image)

print("Loading", end='')
time.sleep(0.5)
print(7*'\b'+"Loading.", end='')
time.sleep(0.5)
print(8*'\b'+"Loading..", end='')
time.sleep(0.5)
print(9*'\b'+"Loading...", end='')
time.sleep(0.5)
print(10*'\b'+"Loading", end='')
time.sleep(0.5)
print(7*'\b'+"Loading.", end='')
time.sleep(0.5)
print(8*'\b'+"Loading..", end='')
time.sleep(0.5)
print(9*'\b'+"Loading...", end='')
time.sleep(0.5)
print(10*'\b'+"Votre fichier a bien été traiter... Merci d'avoir utilisé FACERECO \n \n")