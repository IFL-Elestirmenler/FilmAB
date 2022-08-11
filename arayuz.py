from tkinter import *
#from tkinter import ttk
from PIL import Image, ImageTk


pencere = Tk()

def IcerigeGoreFilmBul(icerik: Text, sonuc: StringVar):
    ic = icerik.get("1.0", "end-1c")
    liste = ["Recep İvedik 1", "Recep İvedik 2", "Recep İvedik 3", "Recep İvedik 4", "Recep İvedik 5", "Recep İvedik 6", "Recep İvedik 7"]
    #sonuçları sonuçyazı ya koy
    sonuc.set(liste)

def ozetEkran():
    global pencere
    pencere.destroy()
    pencere = Tk()
    pencere.title("Özete Göre Film Bul")
    pencere.geometry("700x500")
    pencere.resizable(False, False)
    Label(pencere, text="Nasıl Bir Film İzlemek İstersiniz?", font=("Arial", 12)).place(x=240, y=5)
    #yazı kutusu
    girdi = Text(pencere, font=("Arial", 12))
    girdi.place(x=50, y=35, width=600, height=200)

    Label(pencere, text="Sonuç:", font=("Arial", 12)).place(x=50, y=350)
    # sonuç listbox
    lV = StringVar(value=[])
    
    sonuc = Listbox(pencere, listvariable=lV)
    kaydirmaCubugu = Scrollbar(sonuc, command=sonuc.yview)
    sonuc.config(yscrollcommand=kaydirmaCubugu.set)
    sonuc.place(x=50, y=375,width=600, height=100)
    
    kaydirmaCubugu.place(x=570, y=0, width=30, height=100)
    #buton
    Button(pencere, text="İçeriğe göre film ara",command=lambda: IcerigeGoreFilmBul(girdi, lV), padx=35, pady=10, font=("Arial", 12)).place(x=50, y=250)
    Button(pencere, text="Geri Dön",command=anaEkran, padx=50, pady=10, font=("Arial", 12)).place(x=475, y=250)
    pencere.mainloop()

def VerilenlereGoreFilmBulAra(tur: str, tarih: str, isim: str, sonuc: StringVar):
    liste = ["Recep İvedik 1", "Recep İvedik 2", "Recep İvedik 3", "Recep İvedik 4", "Recep İvedik 5", "Recep İvedik 6", "Recep İvedik 7"]
    sonuc.set(value=liste)

def VerilenlereGoreFilmBulEkle(eklenecek: str, listboxVar: StringVar, valList: list):
    valList.append(eklenecek)
    listboxVar.set(value=valList)

def VerilenlereGoreFilmBulKaldir(verilenlerListBox: Listbox, listboxVar: StringVar, valList: list):
    try:
        valList.pop(verilenlerListBox.curselection()[0])
    except:
        return
    listboxVar.set(value=valList)

def VerilenlerEkran():
    global pencere
    pencere.destroy()
    pencere = Tk()
    pencere.title("Seçilen Filmlere Göre Film Bul")
    pencere.geometry("700x575")
    #Tür Seçeneği
    Label(pencere, text="Tür:", font=("Arial", 12)).place(x=130, y=5)
    tiklananTur = StringVar()
    tiklananTur.set("[Seçilmedi]")
    turListesi = ["[Seçilmedi]", "bilinmeyen", "dram", "komedi", "korku", "aksiyon", "gerilim", "romantik", "batı", "suç", "macera", "müzikal", "bilim kurgu", "kara film", "gizem", "savaş", "animasyon", "aile", "fantastik", "biyografi", "anime", "sosyal", "tarih"]
    OM1 = OptionMenu(pencere, tiklananTur, *turListesi)
    OM1.config(font=("Arial", 12))
    OM1.place(x=70, y=40, width=150, height=50)
    #Tarih Seçeneği
    Label(pencere, text="Yıl:", font=("Arial", 12)).place(x=335, y=5)
    tiklananTarih = StringVar()
    tiklananTarih.set("[Seçilmedi]")
    tarihListesi = ["[Seçilmedi]", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]
    OM2 = OptionMenu(pencere, tiklananTarih, *tarihListesi)
    OM2.config(font=("Arial", 12))
    OM2.place(x=275, y=40, width=150, height=50)
    #İsim Seçeneği
    Label(pencere, text="İsim:", font=("Arial", 12)).place(x=530, y=5)
    tiklananIsim = StringVar()
    tiklananIsim.set("[Seçilmedi]")
    isimListesi = ["[Seçilmedi]", "Recep İvedik 1", "Recep İvedik 2", "Recep İvedik 3", "Recep İvedik 4", "Recep İvedik 5", "Recep İvedik 6", "Recep İvedik 7"]
    OM3 = OptionMenu(pencere, tiklananIsim, *isimListesi)
    OM3.config(font=("Arial", 12))
    OM3.place(x=475, y=40, width=150, height=50)

    #Verilen 10 film listbox
    Label(text="Film Listesi:", font=("Arial", 12)).place(x=50, y=180)
    valueList1 = []
    lV1 = StringVar(value=valueList1)
    
    verilenler = Listbox(pencere, listvariable=lV1)
    kaydirmaCubugu1 = Scrollbar(verilenler, command=verilenler.yview)
    verilenler.config(yscrollcommand=kaydirmaCubugu1.set)
    verilenler.place(x=50, y=215,width=600, height=100)
    
    kaydirmaCubugu1.place(x=570, y=0, width=30, height=100)

    #sonuç listbox
    Label(text="Sonuç:", font=("Arial", 12)).place(x=50, y=390)
    lV2 = StringVar(value=[])
    
    sonuc = Listbox(pencere, listvariable=lV2)
    kaydirmaCubugu2 = Scrollbar(sonuc, command=sonuc.yview)
    sonuc.config(yscrollcommand=kaydirmaCubugu2.set)
    sonuc.place(x=50, y=425,width=600, height=100)
    
    kaydirmaCubugu2.place(x=570, y=0, width=30, height=100)
    #Ekle butonu
    Button(pencere, text="Ekle", padx=50, pady=10, font=("Arial", 12), command= lambda: VerilenlereGoreFilmBulEkle(tiklananIsim.get(), lV1, valueList1)).place(x=120, y=110)
    #Kaldır butonu
    Button(pencere, text="Kaldır", padx=50, pady=10, font=("Arial", 12), command= lambda: VerilenlereGoreFilmBulKaldir(verilenler, lV1, valueList1)).place(x=420, y=110)
    #arama butonu
    Button(pencere, text="Ara", padx=50, pady=10, font=("Arial", 12), command=lambda: VerilenlereGoreFilmBulAra(tiklananIsim.get(), tiklananTarih.get(), tiklananIsim.get(), lV2)).place(x=120, y=330)
    # geri butonu
    Button(pencere, text="Geri Dön", padx=50, pady=10, font=("Arial", 12), command=anaEkran).place(x=410, y=330)

    pencere.mainloop()



def anaEkran():
    global pencere
    pencere.destroy()
    pencere = Tk()
    pencere.title("FilmAB")
    pencere.geometry("800x600")
    pencere.resizable(False, False)
    #logo
    img = ImageTk.PhotoImage(Image.open("logo.png"))#.resize((640,320)))
    Label(pencere, image=img).place(x=127, y=80)
    #ilk buton
    Button(pencere, text="Özete Göre Film Bul", command=ozetEkran, padx=35, pady=17, bg='#074aa3', fg='#ffffff', font=("Arial", 12)).place(x=127, y=400)
    #ikinci buton
    Button(pencere, text="Seçilen Filmlere Göre Film Bul", command=VerilenlerEkran, padx=10, pady=17, bg='#a12732', fg='#ffffff', font=("Arial", 12)).place(x=430, y=400)
    pencere.mainloop()



def main():
    anaEkran()
    

main()