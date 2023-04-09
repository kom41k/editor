#создай тут фоторедактор Easy Editor!
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PIL import Image, ImageFilter, ImageEnhance
from PyQt5.QtGui import QPixmap
from PIL.ImageFilter import SHARPEN, CONTOUR

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Easy Editor')
main_win.resize(700,500)
papka = QPushButton('Папка')
left = QPushButton('Лево')
right = QPushButton('Право')
mirror = QPushButton('Зеркало')
rez = QPushButton('Резкость')
blawhi = QPushButton('Ч/Б')
con = QPushButton('Контур')
cont = QPushButton('Контраст')
photo = QLabel('Картинка')
listpapok = QListWidget()
h_main = QHBoxLayout()
v_1 = QVBoxLayout()
v_2 = QVBoxLayout()
h_1 = QHBoxLayout()
h_1.addWidget(left)
h_1.addWidget(right)
h_1.addWidget(mirror)
h_1.addWidget(rez)
h_1.addWidget(blawhi)
h_1.addWidget(con)
h_1.addWidget(cont)
v_1.addWidget(papka)
v_1.addWidget(listpapok)
h_main.addLayout(v_1, 20)
h_main.addLayout(v_2, 80)
v_2.addWidget(photo, 95)
v_2.addLayout(h_1)
papka.setStyleSheet('color: rgb(66, 255, 185);')
left.setStyleSheet('color: rgb(66, 100, 185);')
right.setStyleSheet('color: rgb(66, 100, 185);')
mirror.setStyleSheet('color: rgb(66, 100, 185);')
rez.setStyleSheet('color: rgb(66, 100, 185);')
blawhi.setStyleSheet('color: rgb(66, 100, 185);')
con.setStyleSheet('color: rgb(50,205,110);')

papka.setStyleSheet('background: rgb(239,0,255);')
left.setStyleSheet('background: rgb(0,0,255);')
right.setStyleSheet('background: rgb(0,255,255);')
mirror.setStyleSheet('background: rgb(255,205,0);')
blawhi.setStyleSheet('background: rgb(255,0,230);')
rez.setStyleSheet('background: rgb(34,255,0);')
con.setStyleSheet('background: rgb(100,200,150);')
main_win.setLayout(h_main)


workdir = ''

def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result

def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    
def showFilenamesList():
    extensions = ['.jpg','.jpeg','.png','.gif','.bmp']
    chooseWorkdir()
    filenames = filter(os.listdir(workdir), extensions)
    listpapok.clear()
    for filename in filenames:
        listpapok.addItem(filename)
    
class Imageprocessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"
    def loadimage(self, filename):
        self.filename = filename
        image_path = os.path.join(workdir, filename)
        self.image = Image.open(image_path)
    def showimage(self, path):
        photo.hide()
        pixmapimage = QPixmap(path)
        w, h = photo.width(), photo.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        photo.setPixmap(pixmapimage)
        photo.show()
    def saveimage(self):
        path = os.path.join(workdir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)
    def dolalala(self):
        self.image = self.image.convert('L')
        self.saveimage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showimage(image_path)
    def do_a_flip(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveimage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showimage(image_path)
    def do_a_flip_2(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveimage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showimage(image_path)
    def do_sharpen(self):
        self.image = self.image.filter(SHARPEN)
        self.saveimage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showimage(image_path)
    def do_a_flip_lf(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveimage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showimage(image_path)
    def do_a_con(self):
        self.image = self.image.filter(CONTOUR)
        self.saveimage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showimage(image_path)
    def do_a_cont(self):
        self.image = ImageEnhance.Contrast(self.image)
        self.image = self.image.enhance(3)
        self.saveimage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showimage(image_path) 
             

workimage = Imageprocessor()

def showchosenimage():
    if listpapok.currentRow() >= 0:
        filename = listpapok.currentItem().text()
        workimage.loadimage(filename)
        image_path = os.path.join(workdir, workimage.filename)
        workimage.showimage(image_path)

papka.clicked.connect(showFilenamesList)
listpapok.currentRowChanged.connect(showchosenimage)
blawhi.clicked.connect(workimage.dolalala)
mirror.clicked.connect(workimage.do_a_flip_lf)
left.clicked.connect(workimage.do_a_flip)
right.clicked.connect(workimage.do_a_flip_2)
rez.clicked.connect(workimage.do_sharpen)
con.clicked.connect(workimage.do_a_con)
cont.clicked.connect(workimage.do_a_cont)





 







main_win.show()
app.exec_()