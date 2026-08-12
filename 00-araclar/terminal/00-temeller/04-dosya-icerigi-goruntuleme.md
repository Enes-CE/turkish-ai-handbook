---
seviye: giriş
on-kosul: [terminal/00-temeller/03-dosya-klasor-islemleri.md]
tip: komut
son-guncelleme: 2026-08-12
dogrulandigi-surum: bash (Git Bash / macOS / Linux ortak)
---

# Dosya içeriğini görmek

> **Bu sayfa şunu çözer:** Bir dosyanın içine terminalden bakmayı öğrenirsin — tamamını
> (`cat`), baş/son kısmını (`head`/`tail`), canlı büyüyen bir log'u (`tail -f`), büyük
> dosyaları sayfalayarak (`less`) ve satır sayısını (`wc -l`).
> **Ön koşul:** [Dosya ve klasör işlemleri](03-dosya-klasor-islemleri.md) · **Süre:** ~15 dakika

---

Önceki sayfada geri alınamaz komutlarla tanıştın. Bu sayfadaki bütün komutlar **sadece
okur** — hiçbiri dosyanı değiştirmez ya da siler. Rahatça dene.

## Tamamını basmak: cat

```bash
cat veri.csv
```

Beklenen çıktı:

```
isim,yas,sehir
Ayşe,29,Ankara
Mehmet,34,İzmir
Elif,41,İstanbul
```

`cat`, dosyanın tamamını ekrana basar — küçük dosyalar için pratik. Ama satır sayısı
binleri bulan bir dosyada (`egitim-verisi.csv` gibi) `cat` çalıştırırsan ekran saniyeler
içinde akıp gider, aradığın satırı yakalayamazsın. Büyük dosyalarda `cat` yerine `head`,
`tail` ya da `less` kullan.

İsmi "concatenate" (birleştirmek) kelimesinden gelir — birden fazla dosyayı arka arkaya
basmak için de kullanılır: `cat dosya1.txt dosya2.txt`.

## İlk ve son satırlar: head / tail

```bash
head egitim-verisi.csv
```

Beklenen çıktı: dosyanın ilk 10 satırı (varsayılan). Bir CSV'de bu genelde başlık satırını
ve birkaç örnek kaydı gösterir — sütunların ne olduğunu anlamak için yeterlidir.

Satır sayısı `-n` ile belirlenir:

```bash
head -n 3 egitim-verisi.csv
```

Beklenen çıktı: ilk 3 satır.

`tail` aynı mantıkla dosyanın **sonundan** gösterir:

```bash
tail -n 5 egitim-verisi.csv
```

Beklenen çıktı: son 5 satır.

## Canlı izleme: tail -f

Model eğitimi saatlerce sürebilir ve genelde bir log dosyasına yazar. `tail -f`, dosya
büyüdükçe yeni satırları anında ekrana basar — eğitimi terminalden canlı izlemenin
standart yolu budur:

```bash
tail -f egitim-log.txt
```

Beklenen çıktı: dosyanın son birkaç satırı, ardından yeni satır eklendikçe otomatik akar:

```
epoch 47/100 - loss: 0.312 - val_loss: 0.298
epoch 48/100 - loss: 0.305 - val_loss: 0.291
```

`tail -f` kendiliğinden durmaz — izlemeyi bitirince **`Ctrl+C`** ile çık.

## Büyük dosyalarda sayfalayarak okumak: less

```bash
less egitim-verisi.csv
```

Beklenen: dosya ekran ekran açılır, alt satırda konum bilgisi (genelde dosya adı) görürsün.
Dosyanın sonuna geldiğinde alt satırda `:` görürsün — bu, `less`'in yeni bir komut
beklediği andır.

İçinde gezinme:

- ok tuşları ya da boşluk (`Space`) — aşağı kaydır
- `b` — yukarı kaydır
- `/kelime` yazıp `Enter` — arama, `n` ile sonraki eşleşmeye atla

**Çıkmak: `q` tuşuna bas.** Bu, `less`'in içinden çıkmanın tek yolu — `Ctrl+C` burada
çoğu zaman işe yaramaz. Ekran kilitlenmiş gibi göründüğünde panik yapma, `q` yeter.

## Satır saymak: wc -l

Veri setinde kaç kayıt var sorusunun en hızlı cevabı:

```bash
wc -l egitim-verisi.csv
```

Beklenen çıktı:

```
10001 egitim-verisi.csv
```

Dosyada başlık satırı varsa gerçek kayıt sayısı = sonuç − 1'dir; burada `10001` çıktı
başlık satırını da içerdiği için gerçek kayıt sayısı 10000'dir. Bu kural sadece başlık
satırı olan dosyalar için geçerli — başlıksız bir dosyada sonucun tamamı kayıt sayısıdır.
Teknik detay: `wc -l` aslında satır sonu karakterlerini sayar; dosyanın son satırı bir
satır sonuyla bitmiyorsa sonuç gerçek satır sayısından bir eksik çıkabilir.

## Veri işlerinde tipik kullanım

- `head egitim-verisi.csv` — sütunlar ne, veri nasıl görünüyor
- `wc -l egitim-verisi.csv` — kaç kayıt var
- `tail -f egitim-log.txt` — eğitim şu an nerede, hata veriyor mu

## Aynı dosyaya dört farklı bakış

```
10.000 satırlık egitim-verisi.csv

cat egitim-verisi.csv     → 10.000 satırın hepsi ekrana akar, üsttekiler kaybolur
head egitim-verisi.csv    → sadece ilk 10 satır (varsayılan)
tail egitim-verisi.csv    → sadece son 10 satır (varsayılan)
less egitim-verisi.csv    → tek seferde bir ekran, gezinerek okunur, q ile çıkılır

  Hızlı bakış (sütunlar ne?)          →  head
  Son durumu gör (en son ne oldu?)    →  tail
  İçinde arama yap                    →  less
  Küçük dosyanın tamamını gör         →  cat
```

`head` ve `tail` asıl gücünü tek başına değil, bir **boru hattıyla** başka bir komuta
bağlandığında gösterir — bu, bir sonraki sayfanın konusu:
[Arama ve filtreleme](../01-gunluk-kullanim/01-arama-ve-filtreleme.md).

## Sık yapılan hatalar

| Hata | Sebebi | Çözüm |
|---|---|---|
| `less`'ten çıkamıyorum, ekran kilitlendi | `q` tuşu unutuldu | `q` tuşuna bas |
| `tail -f` hiç durmuyor, komut satırı geri gelmiyor | `tail -f` sürekli izlemeye devam eder, kendiliğinden bitmez | `Ctrl+C` ile çık |
| Büyük dosyada `cat` çalıştırdım, ekran akıp gitti | Dosya çok uzun, `cat` hepsini basıyor | `head`, `tail` ya da `less` kullan |
| `wc -l` sonucu beklediğimden bir fazla | Başlık satırı da sayılıyor | Gerçek kayıt sayısı = sonuç − 1 |

## Kendin dene

1. `echo` ile birkaç satırlık bir dosya oluştur:

```bash
echo "satir 1" > deneme.txt
echo "satir 2" >> deneme.txt
echo "satir 3" >> deneme.txt
```

(`>` dosyayı oluşturur/üzerine yazar, `>>` sonuna ekler — detayları
[Çıktıyı dosyaya yazmak](../01-gunluk-kullanim/02-cikti-yonlendirme.md) sayfasında.)

2. `cat deneme.txt` çalıştır, üç satırın da göründüğünü doğrula.
3. `head -n 1 deneme.txt` çalıştır, sadece `satir 1` çıktısını gördüğünü doğrula.
4. `wc -l deneme.txt` çalıştır, çıktının `3` olduğunu doğrula.

Bu üç komut da dosyanı değiştirmez — istediğin kadar tekrar çalıştırabilirsin.

## Sonraki adım

→ [Komut yapısı ve yardım okuma](05-komut-yapisi-ve-yardim.md)

---

<sub>Bu sayfada hata mı buldun? [Issue aç](https://github.com/Enes-CE/turkish-ai-handbook/issues/new/choose).</sub>
