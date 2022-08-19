# FilmAB
Projemiz bir film öneri robotudur. Arayüzümüz açıldığında size iki seçenek sunar:
1. Özet girerek: Nasıl bir film izlemek istediğinizi belirterek,
2. Birkaç film ismi girerek: Verdiğiniz filmlere benzer film isteyerek, <br>
veri kümesinde uygun filmi bulabilirsiniz.

### Ali Batu ADA ###
Takım Kaptanı

### Fahriye Gül OLUR ###
Takım Üyesi

### Sertaç ATEŞ ###
Danışman Öğretmen

### Saadin OYUCU ###
Proje Mentörü

# __*Projemizin Çalışması için Gerekenler*__

## Proje Bağlılık Listesi

#### Film Öneri Sisteminin Ara Yüzü ile Çalışması İçin Gerekli Dosyalar:

Dosya Adı|
---|
arayuz.py
filmOzetleriVeriKumesi_TURKCE.csv

#### Film Öneri Sisteminin Ara Yüzü ile Çalışması İçin Gerekli Kurulumlar

Kütüphane Adı | Pip ile İndirme | PyPI sitesi
------------|------------|-
pip 22.2.2 | **yok** | https://pypi.org/project/pip/
pandas 1.4.3 | pip install pandas | https://pypi.org/project/pandas/
google colab 1.0.0 | pip install google-colab | https://pypi.org/project/google-colab
tkinter 3.12.0a0 | pip install tk | Standart Kütüphanedir.
PIL 1.1.7  | pip install Pillow==1.7.1 | https://pypi.org/project/Pillow/1.7.1/
tensorflow 2.9.1 | pip install tensorflow | https://pypi.org/project/tensorflow
psutil 5.9.1  | pip install psutil | https://pypi.org/project/psutil/
zemberek-python 0.1.3 | pip install zemberek-python | https://pypi.org/project/zemberek-python/
nltk 3.7 | pip install nltk | https://pypi.org/project/nltk/
TurkishStemmer 1.3 | pip install TurkishStemmer | https://pypi.org/project/TurkishStemmer/
sklearn 0.0 | pip install sklearn | https://pypi.org/project/sklearn/

#### Film Öneri Sisteminin Veri Kümesinin Türkçeleştirilmesine Katkı Sağlamak İçin Gerekli Dosyalar:

Dosya Adı|
---|
VeriKumesininTurkcelestirilmesi.ipynb
wiki_movie_plots_deduped.csv

#### Film Öneri Sisteminin Veri Kümesinin Türkçeleştirilmesine Katkı Sağlamak İçin Gerekli Kurulumlar

Kütüphane Adı | Pip ile İndirme | PyPI sitesi
------------|------------|-
pip 22.2.2 | **yok** | https://pypi.org/project/pip/
pandas 1.4.3 | pip install pandas | https://pypi.org/project/pandas/

#### Film Öneri Sisteminin ÖZETTEN FİLM BULMASINA Katkı Sağlamak İçin Gerekli Dosyalar:

Dosya Adı|
---|
filmOzetindenBenzerFilmlerinBulunmasi.ipynb
filmOzetleriVeriKumesi_TURKCE.csv

#### Film Öneri Sisteminin ÖZETTEN FİLM BULMASINA Katkı Sağlamak İçin Gerekli Kurulumlar

Kütüphane Adı | Pip ile İndirme | PyPI sitesi
------------|------------|-
pip 22.2.2 | **yok** | https://pypi.org/project/pip/

#### Film Öneri Sisteminin VERİLEN FİLMLERDEN FİLM BULMASINA Katkı Sağlamak İçin Gerekli Dosyalar:

Dosya Adı|
---|
toplam10filmIsmindenOzetlerineBakipBenzerFilmlerinBulunmasi.ipynb
filmOzetleriVeriKumesi_TURKCE.csv

#### Film Öneri Sisteminin VERİLEN FİLMLERDEN FİLM BULMASINA Katkı Sağlamak İçin Gerekli Kurulumlar

Kütüphane Adı | Pip ile İndirme | PyPI sitesi
------------|------------|-
pip 22.2.2 | **yok** | https://pypi.org/project/pip/
pandas 1.4.3 | pip install pandas | https://pypi.org/project/pandas/


# Veri Kümesi
Veri kümesi olarak [wiki_movie_plots_deduped.csv](https://www.kaggle.com/datasets/jrobischon/wikipedia-movie-plots?resource=download) adlı dosyayı kullandık. Sütun açıklamaları aşağıda tablo halinde verilmiştir:

| İsim              | Açıklama                                                              | Satır Sayısı (Unknown) |Satır Sayısı (NaN) | Satır Sayısı (Dolu) |
| ----------------- | --------------------------------------------------------------------- | ---------------------- | ----------------- | ------------------- |
| Çıkış Yılı        | Filmin yayınlandığı yıl                                               |            0           |         0         |       34886         |
| Orijinal İsmi     | Film başlığı                                                          |            2           |         0         |       34886         |
| Yapıldığı Ülke    | Filmin kökeni (ör. Amerikan, Bollywood, Tamil vb.)                    |            0           |         0         |       34886         |
| Yönetmeni         | Yönetmen(ler)                                                         |           1124         |         0         |       34886         |
| Oyuncu Kadrosu    | Baş aktör ve aktrisler                                                |            1           |        1422       |       33464         |
| Türü              | Film Tür(ler)i                                                        |            0           |         0         |       34886         |
| Veri Kaynağı      | Konu açıklamasının çıkarıldığı Wikipedia sayfasının URL'si            |            0           |         0         |       34886         |
| Olay Dizisi       | Film konusunun uzun biçimli açıklaması (UYARI: Spoiler içerebilir!!!) |            0           |         0         |       34886         | 


# Projemizin Ara Yüzü
Karşılama ekranında tavsiye türünü seçiyorsunuz. Sonra seçiminize göre ilgili ekrana geçip istenilenleri yazarak film önerilerimizi görüyorsunuz. Umarız hoşunuza gider.


![image](https://user-images.githubusercontent.com/109215656/184126090-d1f665e3-c092-4608-9d27-69e260eb38d2.png)

![image](https://user-images.githubusercontent.com/109215656/184126290-341b8715-3a5a-4396-8605-e5f0af92a945.png)

![image](https://user-images.githubusercontent.com/109215656/184126382-f582cccf-1ad3-497c-9f7a-31c5456db2a7.png)

