---
seviye: orta
on-kosul: [terminal/00-temeller/04-dosya-icerigi-goruntuleme.md]
tip: komut
son-guncelleme: 2026-08-12
dogrulandigi-surum: bash (Git Bash / macOS / Linux ortak)
---

# Arama ve filtreleme

> **Bu sayfa şunu çözer:** Dosya içinde metin aramayı (`grep`) ve komutların çıktısını
> birbirine bağlamayı (boru hattı `|`) öğrenirsin — veri işleriyle uğraşırken en çok
> kullanacağın ikili budur.
> **Ön koşul:** [Dosya içeriğini görmek](../00-temeller/04-dosya-icerigi-goruntuleme.md) ·
> **Süre:** ~20 dakika

---

## grep: dosya içinde metin aramak

```bash
grep hata egitim-log.txt
```

Beklenen çıktı: `hata` kelimesini içeren satırlar:

```
epoch 12/100 - hata: gradient patlaması tespit edildi
epoch 58/100 - hata: NaN loss
```

Sık kullanılan bayraklar:

- `-i` — büyük/küçük harf duyarsız arama

```bash
grep -i HATA egitim-log.txt
```

- `-n` — satır numarasını da göster

```bash
grep -n hata egitim-log.txt
```

Beklenen çıktı: `47:epoch 12/100 - hata: gradient patlaması tespit edildi`

- `-c` — sadece kaç eşleşme olduğunu göster

```bash
grep -c hata egitim-log.txt
```

Beklenen çıktı: `2`

- `-v` — eşleşmeyenleri göster (tersi)

```bash
grep -v hata egitim-log.txt
```

- `-r` — bir klasörde özyinelemeli (recursive) arama

```bash
grep -r hata .
```

## Boru hattı (|): bir komutun çıktısını diğerine bağlamak

Bir komutun çıktısını, başka bir komutun girdisi yapmanın yolu boru hattı (`|`). Sol
taraftaki komut ne üretirse, sağ taraftaki komut onu okur:

```
cat egitim-log.txt              10.000 satır (tüm log)
        │
        ▼  | grep hata
        2 satır (sadece hata içerenler)
        │
        ▼  | wc -l
        2   (kaç tane olduğu)
```

Tek komutla:

```bash
cat egitim-log.txt | grep hata | wc -l
```

Beklenen çıktı: `2`

Zincir istediğin kadar uzayabilir — her `|` veriyi biraz daha daraltır.

Yukarıdaki zincir boru hattının mantığını göstermek için `cat` ile kuruldu, ama `grep`
zaten dosya adını doğrudan alabilir — `grep hata egitim-log.txt` yazmak, `cat
egitim-log.txt | grep hata` ile aynı işi tek adımda yapar. Boru hattı asıl olarak
girdisi bir dosya **olmayan** durumlarda gereklidir — örneğin bir komutun çıktısını
filtrelemek: `ls | grep veri`.

## Zincirleme örnekler

CSV'de belirli bir değeri içeren kayıtları saymak:

```bash
grep Ankara egitim-verisi.csv | wc -l
```

İlk 5 hatayı görmek:

```bash
grep hata egitim-log.txt | head -n 5
```

## find: dosya ADINA göre arama

`grep` dosyanın **içeriğine** bakar, `find` dosyanın **adına** bakar — ikisi farklı sorulara
cevap verir.

```bash
find . -name "*.csv"
```

Beklenen çıktı: bulunduğun klasörden itibaren `.csv` uzantılı tüm dosyaların yolları.

Sadece dosya ya da sadece klasörle sınırlamak için `-type`:

```bash
find . -type f -name "*.csv"    # sadece dosyalar
find . -type d -name "veri*"    # sadece klasörler
```

Boyuta göre arama:

```bash
find . -size +10M
```

Beklenen çıktı: 10 MB'tan büyük dosyalar.

## Gerçek senaryolar

- Eğitim log'unda hata satırlarını bulmak: `grep -n hata egitim-log.txt`
- CSV'de belirli bir değeri içeren kayıtları saymak: `grep Ankara egitim-verisi.csv | wc -l`
- Klasörde tüm `.csv` dosyalarını bulmak: `find . -name "*.csv"`

## Büyük/küçük harf ve Türkçe karakter uyarısı

`grep` varsayılan olarak harfe duyarlıdır: `Ankara` ile `ankara` farklı sonuç verir,
`-i` bunu kapatır. Türkçe karakterli aramalarda dikkatli ol — Türkçede `I` harfi `i`
harfinin büyüğü değildir (büyüğü `İ`'dir), bu yüzden `-i` beklediğin gibi davranmayabilir.
Sonuç boş çıkarsa aranan kelimenin hem büyük hem küçük harfli hâlini ayrı ayrı dene.

## Sık yapılan hatalar

| Hata | Sebebi | Çözüm |
|---|---|---|
| `grep` sonuç vermedi ama orada olduğunu biliyorum | Büyük/küçük harf ya da Türkçe karakter uyuşmazlığı | `-i` dene, kelimeyi hem büyük hem küçük harfle dene |
| Boru hattının sağına dosya adı yazdım, çalışmadı (`grep hata \| log.txt`) | `\|`'nin sağında bir **komut** olmalı, dosya değil | Dosyaya yazmak için `>` kullanılır — bir sonraki sayfanın konusu |
| `find` hiçbir şey bulamadı | `-name` deseni tırnaksız yazıldı, kabuk `*`'ı kendisi genişletti | Deseni tırnak içine al: `"*.csv"` |
| `grep -r` çok yavaş ya da gereksiz yerlerde arıyor | `.git` gibi büyük klasörler de taranıyor | Aramayı belirli bir klasörle sınırla: `grep -r hata proje/` |

## Kendin dene

1. Birkaç satırlık örnek bir log dosyası oluştur:

```bash
echo "epoch 1 - basarili" > deneme-log.txt
echo "epoch 2 - hata: NaN" >> deneme-log.txt
echo "epoch 3 - basarili" >> deneme-log.txt
echo "epoch 4 - hata: gradyan patladi" >> deneme-log.txt
```

2. `grep hata deneme-log.txt` çalıştır, iki satırın göründüğünü doğrula.
3. `grep hata deneme-log.txt | wc -l` çalıştır, sonucun `2` olduğunu doğrula.
4. `grep -c hata deneme-log.txt` çalıştır, aynı `2` sonucunu tek komutla aldığını gör.

## Sonraki adım

→ [Çıktıyı dosyaya yazmak](02-cikti-yonlendirme.md)

---

<sub>Bu sayfada hata mı buldun? [Issue aç](https://github.com/Enes-CE/turkish-ai-handbook/issues/new/choose).</sub>
