# MODÜLLER VE GELİŞİM AŞAMALARI
## Film Özetinden Film Tespit Modülü
 - YÖNTEM: Özetlerin benzerliğinden yararlanarak film önerisinde bulunuyoruz.
## Verilen Film İsimlerinden Film Tespit Modülü
 - YÖNTEM: Verilen filmlerin önce özetlerini işleyip  anahtar kelimeleri çıkartıyoruz, ardından anahtar kelimeler ile özet benzerliğinden yararlanarak film önerisinde bulunuyoruz.
## Ara Yüz Modülü
 - YÖNTEM:  Girdinin alındığı ve film önerilerini okunur biçimde sunan arayüz ile kullanıcının daha rahat ve kolay şekilde arama yapmasını sağlıyoruz. 

## FilmAB Projesi - Süreç Yönetim Tablosu
[FilmAB Projesi - Süreç Yönetim Tablosu](https://github.com/orgs/IFL-Elestirmenler/projects/1/views/1) aracılığıyla projemizin gelişim aşamalarını görebilirsiniz. Neye nasıl karar verdiğimizi hangi konuyu ne zaman tamamladığımızı ve benzer tüm iletişimi görebilirsiniz.

## FilmAB (Film Ara Bul) Sistemi
- Türkçe Veri Kümesi Üretilmesi
- Türkçe Film Özetleri bulunan bir kaynağa alanyazında (literatürde) rastlamadık.
- Türkçe Film Özeti İçeren Veri Kümesi Üretilmesi (Huggingface - Doğal Dil İşleme / Çeviri Görevi)
- Türkçe Film Özeti İçeren Veri Kümesi Üretilmesi (TXTAI)
- Türkçe Film Özeti İçeren Veri Kümesi Üretilmesi (Google Translate)
- Türkçe Film Özeti İçeren Veri Kümesi Üretilmesi (SORUN)
- Türkçe Film Özeti İçeren Veri Kümesi Üretilmesi (ÜRETİLEN VERİ KÜMESİ - filmOzetleriVeriKumesi_TURKCE.csv)
- Proje kapsamında snowballstemmer, nltk.stem (PorterStemmer), TurkishStemmer, nltk.stem (WordNetLemmatizer), nltk.stem (LancasterStemmer) ve nltk.stem (RegexpStemmer) ile ZEMBEREK'i karşılaştırdık.
- TF / IDF Matrisi Oluşturup Kosinüs Benzerliğinden Yararlandık
