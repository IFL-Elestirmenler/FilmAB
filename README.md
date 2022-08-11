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


Bu şekilde readme.md dosyasını güncelleyelim.

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

# projemizin Ara Yüzü
Karşılama ekranında tavsiye türünü seçiyorsunuz seçiminize göre ilgili ekrana geçip istenilenleri yazıp film önerilerimizi görüyorsunuz. Umarız hoşunuza gider.


![image](https://user-images.githubusercontent.com/109215656/184126090-d1f665e3-c092-4608-9d27-69e260eb38d2.png)

![image](https://user-images.githubusercontent.com/109215656/184126290-341b8715-3a5a-4396-8605-e5f0af92a945.png)

![image](https://user-images.githubusercontent.com/109215656/184126382-f582cccf-1ad3-497c-9f7a-31c5456db2a7.png)

