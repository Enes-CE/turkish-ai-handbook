---
seviye: giriş
on-kosul: [terminal/00-temeller/02-dosya-sistemi-ve-yol.md]
tip: komut
son-guncelleme: 2026-08-12
dogrulandigi-surum: bash (Git Bash / macOS / Linux ortak)
---

# Dosya ve klasör işlemleri

> **Bu sayfa şunu çözer:** Terminalde klasör/dosya oluşturmayı (`mkdir`, `touch`),
> kopyalamayı (`cp`), taşımayı/yeniden adlandırmayı (`mv`) ve silmeyi (`rm`) öğrenirsin.
> Bu sayfadaki son komut geri alınamaz — dikkatli oku.
> **Ön koşul:** [Dosya sistemi ve yol kavramı](02-dosya-sistemi-ve-yol.md) · **Süre:** ~15 dakika

---

## Klasör oluşturmak: mkdir

```bash
mkdir deneme
```

Çıktı vermez, sessiz çalışır. Doğrulaması `ls`.

İç içe klasörleri tek seferde oluşturmak için `-p`:

```bash
mkdir -p deneme/alt/daha-alt
```

`-p` olmadan `alt` klasörü henüz yoksa `mkdir deneme/alt/daha-alt` hata verir. `-p` ara
klasörleri de otomatik oluşturur.

## Boş dosya oluşturmak: touch

```bash
touch deneme/notlar.txt
```

Var olan bir dosyada `touch` çalıştırırsan içeriği **silinmez** — sadece dosyanın "son
değiştirilme" tarihi güncellenir.

## Kopyalamak: cp

```bash
cp deneme/notlar.txt deneme/notlar-yedek.txt
```

Klasör kopyalamak için `-r` (recursive) gerekir:

```bash
cp -r deneme deneme-yedek
```

`-r` olmadan bir klasörü kopyalamaya çalışırsan `omitting directory` hatası alırsın.

## Taşımak ve yeniden adlandırmak: mv

Burada kafa karışabilir: `mv` hem taşımak hem yeniden adlandırmak için kullanılır. Aslında
ikisi de aynı işlem — terminal "kaynağı hedefe taşı" der, hedef bir klasörse dosya oraya
gider, hedef yeni bir isimse dosya o isme dönüşür.

Taşımak (hedef bir klasör):

```bash
mv deneme/notlar-yedek.txt deneme/alt/
```

Yeniden adlandırmak (hedef aynı klasörde farklı bir isim):

```bash
mv deneme/notlar.txt deneme/gunluk-notlar.txt
```

## cp, mv, rm: dosya nereye gidiyor

Üçü de kaynaktan yola çıkar ama sonuç farklıdır:

```
        KAYNAK                       HEDEF

cp:   [dosya.txt]   ── kopyala ──►  [dosya.txt]
      (yerinde kalır)                (yeni oluşur)
      → dosya artık İKİ yerde var

mv:   [dosya.txt]   ── taşı ────►   [dosya.txt]
      (kaynaktan silinir)           (burada oluşur)
      → dosya SADECE hedefte var

rm:   [dosya.txt]   ── sil ─────►   (hiçbir yer)
      (silinir)
      → dosya HİÇBİR yerde yok
```

## Silmek: rm

> ⚠️ **Terminalde sildiğin dosya Geri Dönüşüm Kutusu'na / Çöp Kutusu'na GİTMEZ.**
> GUI'de yanlışlıkla sildiğin bir dosyayı oradan geri alabilirsin; `rm` ile sildiğin dosya
> **anında ve kalıcı olarak** kaybolur. Geri alma komutu yoktur.

```bash
rm deneme/notlar-yedek.txt
```

Doğrulaması yine `ls` — dosyanın artık listede olmadığını görürsün.

Klasör silmek için `-r` gerekir:

```bash
rm -r deneme-yedek
```

### rm -rf neden özellikle tehlikeli

> ⚠️ **`rm -rf` en tehlikeli terminal komutlarından biridir.** `-r` klasörün içindekileri
> de siler, `-f` (force) onay sormadan ve hata varsa bile durmadan siler. Yanlış
> klasördeyken çalıştırırsan — örneğin `cd` ile nereye gittiğini karıştırıp proje
> klasörü yerine ev dizininde çalıştırırsan — geri dönüşü olmayan bir kayıp yaşarsın.
> Yolu eksik yazmak bile yeterlidir: `deneme-alani` içindeki sadece `alt` klasörünü
> silmek isterken `rm -rf alt` yazacağına klasör adını unutup `rm -rf .` yazarsan,
> bulunduğun klasördeki her şeyi — yani projenin tamamını — silersin.
> Bu depoda `rm -rf` hangi sayfada geçerse geçsin, çalıştırmadan önce ne sildiğini
> mutlaka iki kez kontrol et.

## Silmeden önce güvenlik alışkanlığı

Önce `ls` ile neyi sileceğini gör, emin olduktan sonra `rm` çalıştır:

```bash
ls deneme-yedek      # önce bak, ne var
rm -r deneme-yedek    # emin olduktan sonra sil
```

Bu iki adımı ayırmak, "yanlış klasörü sildim" hatasına karşı en basit önlemdir.

Bir güvenlik ağı daha istersen `-i` (interactive) bayrağını kullan — her dosya için tek
tek onay sorar:

```bash
rm -i dosya.txt
```

Beklenen çıktı:

```
rm: remove regular file 'dosya.txt'? 
```

`y` yazıp `Enter`'a basarsan siler, başka bir tuşa basarsan vazgeçer. Yeni başlarken
`rm -i` alışkanlığı, "emin değilken sil" hatasını komut seviyesinde engeller.

## Boşluklu ve Türkçe karakterli dosya adları

Pratikte ikisinden de kaçınmak işini kolaylaştırır:

- Boşluk, komutlarda tırnak ya da kaçış gerektirir; script'lerde unutulursa hata kaynağı olur.
- Türkçe karakterler (`ç`, `ğ`, `ı`, `ö`, `ş`, `ü`) farklı işletim sistemi/araç
  kombinasyonlarında farklı kodlanabilir, dosyayı paylaşırken bozulma riski taşır.

Bu depo da kendi dosya adlarında aynı kuralı uyguluyor (bkz.
[KONU-EKLEME.md](../../../KONU-EKLEME.md)). Tire ile ayrılmış küçük harf ASCII isimler
tercih edilir: `proje-notlari.txt` gibi.

## Sık yapılan hatalar

| Hata | Sebebi | Çözüm |
|---|---|---|
| `mkdir: cannot create directory: No such file or directory` | Ara klasörler henüz yok | `-p` kullan: `mkdir -p yol/alt/daha-alt` |
| `cp: omitting directory` | Klasör kopyalanırken `-r` unutuldu | `cp -r kaynak hedef` |
| `rm: cannot remove: Is a directory` | Klasör silinirken `-r` unutuldu | `rm -r klasor` |
| Sildiğim dosyayı geri istiyorum | `rm` kalıcı siler, çöp kutusu yok | Geri alma yolu yok — önemli dosyaları silmeden önce yedekle |

## Kendin dene

Hepsi kendi oluşturduğun, önemsiz bir klasörde geçer — güvenle deneyebilirsin.

1. `mkdir deneme-alani` ile klasör oluştur, `cd deneme-alani` ile içine gir.
2. `touch ilk-dosya.txt` ile bir dosya oluştur, `ls` ile gördüğünü doğrula.
3. `cp ilk-dosya.txt ikinci-dosya.txt` ile kopyala, `ls` ile iki dosya olduğunu gör.
4. `mv ikinci-dosya.txt yeniden-adli-dosya.txt` ile yeniden adlandır, `ls` ile kontrol et.
5. `cd ..` ile bir üst dizine çık, `pwd` ile gerçekten bir üst dizinde olduğunu doğrula.
   `ls deneme-alani` ile sileceğin klasörün içine son bir kez bak, sonra `rm -r deneme-alani`
   ile sil, `ls` ile artık orada olmadığını doğrula.

## Sonraki adım

→ [Dosya içeriğini görmek](04-dosya-icerigi-goruntuleme.md)

---

<sub>Bu sayfada hata mı buldun? [Issue aç](https://github.com/Enes-CE/turkish-ai-handbook/issues/new/choose).</sub>
