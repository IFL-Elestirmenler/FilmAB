![Logo](https://github.com/IFL-Elestirmenler/FilmAB/blob/main/logo.png)

[FilmAB Projesi Demo - Ekran Ara Yüzü Kullanımı için **buraya** tıklayınız](https://github.com/IFL-Elestirmenler/FilmAB/blob/main/FilmAB%20Projesi%20Demo%20-%20Ekran%20Ara%20Y%C3%BCz%C3%BC%20Kullan%C4%B1m%C4%B1.mp4)

# FilmAB Projemiz
TeknoFest 2022 Samsun **Türkçe Doğal Dil İşleme Yarışması** kapsamında **Serbest Kategori** alanında Türkçe Veri Kümesi de oluşturduğumuz bir film öneri robotudur.
Arayüzümüz açıldığında size iki seçenek sunar:
1. Özet girerek: Nasıl bir film izlemek istediğinizi belirterek,
2. Birkaç film ismi girerek: Verdiğiniz filmlere benzer film isteyerek,
veri kümesinde uygun filmi bulabilirsiniz.
(#Acıkhack2022TDDİ)

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

## FilmAB (Film Ara Bul) Sistemi
### Türkçe Veri Kümesi Üretilmesi
**- Türkçe Film Özetleri bulunan bir kaynağa alanyazında (literatürde) rastlamadık.**<br>
IMDb Veri Kümeleri (https://www.imdb.com/interfaces/) ile NetFlix (https://www.kaggle.com/datasets/shivamb/netflix-shows), Amazon Prime (https://www.kaggle.com/datasets/shivamb/amazon-prime-movies-and-tv-shows), Disney+ (https://www.kaggle.com/datasets/shivamb/disney-movies-and-tv-shows) ve Hulu (https://www.kaggle.com/datasets/shivamb/hulu-movies-and-tv-shows) gibi platformların veri kümelerini incelediğimizde FİLM ÖZETLERİNE yer verilmediğini fark ettik. Wikipedia Movie Plots (https://www.kaggle.com/datasets/jrobischon/wikipedia-movie-plots) ve MPST (https://www.kaggle.com/datasets/cryptexcode/mpst-movie-plot-synopses-with-tags) isimli iki veri kümesinde İNGİLİZCE özetlere rastladık ve öncelikli olarak TÜRKÇE FİLM ÖZETİ içeren bir veri kümesi hazırlamaya karar verdik.
<br>**- Türkçe Film Özeti İçeren Veri Kümesi Üretilmesi (Huggingface - Doğal Dil İşleme / Çeviri Görevi)**<br>
Sınırlı kelimeyi uzun zamanda çeviren Dört Model (Helsinki-NLP/opus-mt-en-mul, Helsinki-NLP/opus-mt-tc-big-en-tr, Helsinki-NLP/opus-tatoeba-en-tr ve Helsinki-NLP/opus-mt-en-trk) dışında bir kaynak ve çözüm bulamayınca Huggingface - Doğal Dil İşleme / Çeviri Görevi modellerini kullanmaktan vazgeçtik.
<br>**- Türkçe Film Özeti İçeren Veri Kümesi Üretilmesi (TXTAI)**<br>
Bu kütüphane ile hem doğru çeviri hem de karakter sayısı sınırı sorunlarını yaşamadık ama süre ile ilgili problem devam ediyordu. Seçtiğimiz wikipedia-movie-plots veri kümesinde 35000 civarı film olması ve sadece çevirinin 3 veya daha fazla tam gün süreceğini düşünerek bu şekilde çözüm bulmaktan da vazgeçtik.
<br>**- Türkçe Film Özeti İçeren Veri Kümesi Üretilmesi (Google Translate)**<br>
İlk çıktığında herkesin kalbini kırmasına rağmen mevcut hali ile kalbimizi kazanan google translate bize ilk başlarda naz yaptı. Kararlı sürümünün (3.0.0) uyum sorununu stackoverflowdan öğrendiğimiz yöntem ile ([https://stackoverflow.com/](https://stackoverflow.com/questions/52455774/googletrans-stopped-working-with-error-nonetype-object-has-no-attribute-group)) googletrans 3.1.0a0 kurarak çözdük.
<br>**- Türkçe Film Özeti İçeren Veri Kümesi Üretilmesi (SORUN)**<br>
Google Colab Pro hesabı ile yaklaşık 4 saatte tamamlanan çevirilerden sonra veri kümemizin kirli olduğunu fark ettik. [1] ve [2] gibi alıntı bağlantılarını temizlemediğimizi farkettik. Bir sonraki çalışmamızda veri ön işlemlerine ve veri hazırlık işlemlerine daha dikkat etmemiz gerektiği dersini çıkartıp mevcut kirli veri kümemizi temizledik.
<br>**- Türkçe Film Özeti İçeren Veri Kümesi Üretilmesi (ÜRETİLEN VERİ KÜMESİ - filmOzetleriVeriKumesi_TURKCE.csv)**<br>
Ham veri kümesi olarak [wiki_movie_plots_deduped.csv](https://www.kaggle.com/datasets/jrobischon/wikipedia-movie-plots?resource=download) adlı dosyayı kullandık. ürettiğimiz veri kümesinin detayları aşağıda tablo halinde verilmiştir:

DOSYA ADI: [filmOzetleriVeriKumesi_TURKCE.csv](https://github.com/IFL-Elestirmenler/FilmAB/tree/main/Olu%C5%9Fturdu%C4%9Fumuz%20T%C3%BCrk%C3%A7e%20Veri%20K%C3%BCmeleri)


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

### Limonata'dan Şekeri Çıkar Suyu Çıkar Naneyi Çıkar ÖZÜ LİMON - LİMONA değil LİMO değil LEMAN hiç değil!
** - Proje kapsamında **snowballstemmer**, **nltk.stem** (PorterStemmer), **TurkishStemmer**, **nltk.stem** (WordNetLemmatizer), **nltk.stem** (LancasterStemmer) ve **nltk.stem** (RegexpStemmer) ile ZEMBEREK'i karşılaştırdık. Başka bir değişle, **Stemming**, yani kelime eklerini kaldırarak veya değiştirerek bir kelimenin ortak kök biçimini bulmak ve **Lemmatization**, yani bir kelimenin çekimli biçimlerinin temel biçimini bulmak üzerine çalıştık.

|STEMMING Yöntemi|STEMMING Aracı|Test kelimeleri: ['kalem', 'ilişkilendiremediklerimiz', 'gözlük', 'gözlem']|
|--------------------|--------------------|--------------------|
|Kök Bulma YÖNTEM 1| snowballstemmer |Çıktılar: ['kale', 'ilişkilendiremedik', 'gözlük', 'gözle']|
|Kök Bulma YÖNTEM 2| PorterStemmer |Çıktılar: ['kalem', 'ilişkilendiremediklerimiz', 'gözlük', 'gözlem'] |
|Kök Bulma YÖNTEM 3| TurkishStemmer |Çıktılar: ['kalem', 'ilişkilendiremedik', 'gözlük', 'gözle']
|Kök Bulma YÖNTEM 4| WordNetLemmatizer |Çıktılar: ['kalem', 'ilişkilendiremediklerimiz', 'gözlük', 'gözlem']
|Kök Bulma YÖNTEM 5| LancasterStemmer |Çıktılar: ['kalem', 'ilişkilendiremediklerim', 'gözlük', 'gözlem']
|Kök Bulma YÖNTEM 6| RegexpStemmer |Çıktılar: ['kalem', 'ilişkilendiremediklerimiz', 'gözlük', 'gözlem']
|**Kök Bulma YÖNTEM 7**|ZEMBEREK|Çıktılar: ['kale', 'ilişki', 'gözlük', 'gözlem']|

|**ZEMBEREK'in Analizi**|**Çıktısı**|
|---|---|
|WordAnalysis{input='kalem', normalizedInput='kalem', analysisResults=[Kale:Noun, Prop] kale:Noun+A3sg+m:P1sg [kale:Noun] kale:Noun+A3sg+m:P1sg [kalem:Noun] kalem:Noun+A3sg}|kale|
|WordAnalysis{input='ilişkilendiremediklerimiz', normalizedInput='ilişkilendiremediklerimiz', analysisResults=[ilişki:Noun] ilişki:Noun+A3sg len:Acquire→Verb dir:Caus→Verb+eme:Unable dik:PastPart→Noun+ler:A3pl+imiz:P1pl} |ilişki|
|WordAnalysis{input='gözlük', normalizedInput='gözlük', analysisResults=[gözlük:Noun] gözlük:Noun+A3sg [göz:Noun] göz:Noun+A3sg lük:Ness→Noun+A3sg}|gözlük|
|WordAnalysis{input='gözlem', normalizedInput='gözlem', analysisResults=[gözlem:Noun] gözlem:Noun+A3sg [Gözlem:Noun, Prop] gözlem:Noun+A3sg}|gözlem|

***ANALİZ:*** "kale" kelimesinin hatalı olmasına rağmen "ilişki" kelimesinin bulunması bizi ZEMBEREK kullanmaya sevk etti.

|Öz Bulucu|TF IDF Nesnesinin Dizeyinin (Matrisinin) Boyutu (aranilacak_tfidfDizeyi.shape)|
|---|---|
|Veri ön işlemleri olmadan|(34886, 225577)|
|nltk.stem| (34886, 215685)|
|TurkishStemmer| (34886, 113148)|
|Zemberek|(34886, 88404)|

***ANALİZ:*** Benzer kökten gelen kelimeler de kullanılan stemmer (öz bulucu / kök bulucu) aracının hassasiyetine göre azalıyor.

### Limonata'yı bir çıktı olarak düşünürsek şeker lazım, su lazım, limon lazım...
** Proje kapsamında simgeleştirme (tokenizer) olarak nltk ve trtokenizer kullandık. Bilimsel bir çalışma yürütmeden doğal gözlemimiz sonucu Türkçe Doğal Dil İşleme için daha uygun olarak trtokenizer'ı gördük ve onunla devam ettik.
** Veri kümemizde arama için anlamlı bir farklılık yaratmayacağını düşündüğümüz gereksiz kelimeleri (stopwords) nltk aracının standart stopwords bölümünü kullanarak veri kümemizden sildik/çıkardık.

### TF / IDF Matrisi Oluşturup Kosinüs Benzerliğinden Yararlandık
** Projemiz kapsamında verilen içeriğe göre (özet veya film ismi) nasıl tavsiyede bulunacağımızı araştırdık. https://www.datacamp.com/tutorial/recommender-systems-python benzer bir çalışma İngilizce olarak yapılmış ve kendi çalışmamıza uyarlamak istedik.
<br>*** TF (Terim Sıklığı): İlgili kelimenin dökümandaki frekansıdır. Kelimenin dökümanda geçme sayısını, dökümandaki toplam kelime sayısına bölerek elde edilir.
<br>*** DF (Döküman Sıklığı): TF ile benzemektedir ama bu kez diğer dökümanlara odaklanır. Döküman sayısının ilgili kelimenin geçtiği döküman sayısına bölünmesi ile hesaplanır.
<br>*** IDF (Ters Döküman Sıklığı): DF değerinin logaritması alınarak hesaplanır.
<br>** Projemiz kapsamında önce TF/IDF vektörlerinden oluşan bir dizey (matris) oluşturduk ve kelimelerin bu matristeki benzerliklerine bakarak tavsiye sistemimizi ortaya çıkardık.

### PROJEMİZDE EKSİK KALAN KISIM
*** Olay Dizilerimiz ile arananFilmOzetinin benzerliği üzerinde yeterince çalışamadık. Google Colab PRO hesabı ile sadece cosinüs benzerliğinden faydalandık diğer benzerliklerin karşılaştırmasını yapıp en verimlisini veya en performansı yüksek olanı belirleyemedik.

![image](https://user-images.githubusercontent.com/109214557/185698302-ff5df900-b348-440a-89ea-4d1762feddd4.png)

**Eksik Kalan Kısmı Araştırmak için Önerilerimiz:**

- https://goodboychan.github.io/python/datacamp/natural_language_processing/2020/07/17/04-TF-IDF-and-similarity-scores.html
- https://leimao.github.io/blog/Cosine-Similarity-VS-Pearson-Correlation-Coefficient/
- https://towardsdatascience.com/17-types-of-similarity-and-dissimilarity-measures-used-in-data-science-3eb914d2681
- https://towardsdatascience.com/9-distance-measures-in-data-science-918109d069fa
- https://scikit-learn.org/stable/modules/metrics.html
- https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html
- https://docs.scipy.org/doc/scipy/reference/spatial.distance.html

UYARI: Seçilen yöntemin seyrek dizeyleri (sparse matrices) destekleyip desteklemediğini dokümantasyonundan kontrol ediniz.

# Projemizin Ara Yüzü
Karşılama ekranında tavsiye türünü seçiyorsunuz. Sonra seçiminize göre ilgili ekrana geçip istenilenleri yazarak film önerilerimizi görüyorsunuz. Umarız hoşunuza gider.


![image](https://user-images.githubusercontent.com/109215656/184126090-d1f665e3-c092-4608-9d27-69e260eb38d2.png)

![image](https://user-images.githubusercontent.com/109215656/184126290-341b8715-3a5a-4396-8605-e5f0af92a945.png)

![image](https://user-images.githubusercontent.com/109215656/184126382-f582cccf-1ad3-497c-9f7a-31c5456db2a7.png)

## Katkılarından Ötürü Teşekkür Ederiz
- Sayın Saadin OYUCU | Mentör |
- Değerli Sertaç ATEŞ | Danışman Öğretmen |

## Takım Üyeleri
- Ali Batu ADA   | Takım Kaptanı | [allbattu](https://github.com/allbattu)
- Fahriye Gül OLUR  | Takım Üyesi | [fahriyegulolur](https://github.com/fahriyegulolur)
- Sertaç ATEŞ             | Danışman Öğretmen | [sertacates](https://github.com/sertacates)

## Hakkımızda
**Film AB | Özetten veya Seçtiğiniz Filmlerden Size Tavsiyelerde Bulunan Otonom Bir Danışman**, **İFL Eleştirmenler** takımı tarafından **Teknofest 2022 Türkçe Doğal Dil İşleme Yarışması** kapsamında düzenlenen Serbest Kategori alanında yarışması için oluşturulan bir DOĞAL DİL İŞLEME (Türkçe) projesidir.
