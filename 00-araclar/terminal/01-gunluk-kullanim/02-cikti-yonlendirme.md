---
seviye: orta
on-kosul: [terminal/01-gunluk-kullanim/01-arama-ve-filtreleme.md]
tip: komut
son-guncelleme: 2026-08-12
dogrulandigi-surum: bash (Git Bash / macOS / Linux ortak)
---

# Çıktıyı dosyaya yazmak

> **Bu sayfa şunu çözer:** Bir komutun çıktısını ekrana değil dosyaya yazmayı (`>`, `>>`)
> öğrenirsin; standart çıktı ile standart hatanın neden ayrı kanallar olduğunu ve `tee`
> ile "hem ekrana hem dosyaya" yazmayı görürsün.
> **Ön koşul:** [Arama ve filtreleme](01-arama-ve-filtreleme.md) · **Süre:** ~15 dakika

---

Önceki sayfada bir komutun çıktısını başka bir komuta (`|`) bağlamayı öğrendin. Bu
sayfada aynı çıktıyı bir dosyaya yönlendiriyorsun — hedef artık bir komut değil, bir dosya.

## > : çıktıyı dosyaya yazmak

```bash
ls > dosya-listesi.txt
```

Çıktı ekrana basılmaz, doğrudan `dosya-listesi.txt`'ye yazılır. Doğrulaması `cat
dosya-listesi.txt`.

> ⚠️ **`>` hedef dosya zaten varsa içeriğinin üzerine yazar — sormadan, geri alınamaz
> şekilde.** `egitim-log.txt` dosyan varsa ve yanlışlıkla `echo "test" > egitim-log.txt`
> çalıştırırsan, o dosyadaki bütün önceki içerik anında kaybolur. `rm` kadar tehlikeli
> bir davranış, sadece daha az fark edilir — çünkü komut "silme" değil "yazma" gibi görünür.

## >> : dosyanın sonuna eklemek

```bash
echo "yeni satir" >> egitim-log.txt
```

Var olan içeriği korur, sonuna ekler. `>` ile `>>` arasındaki fark tek karakter ama
sonuç tamamen farklı — hangisini yazdığına dikkat et.

## Standart çıktı ve standart hata

Her komutun aslında iki ayrı çıktı kanalı vardır:

```
                    ┌─────────────────────┐
                    │        komut        │
                    └──────────┬──────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                            │
                 ▼                            ▼
       stdout (kanal 1)              stderr (kanal 2)
       normal çıktı                  hata mesajları
                 │                            │
                 ▼                            ▼
        ekran (varsayılan)            ekran (varsayılan)
```

Varsayılan olarak ikisi de ekrana basılır, bu yüzden ayrımı normalde fark etmezsin. Ama
yönlendirirken önemli hâle gelir:

```bash
komut > cikti.txt
```

Bu sadece **stdout**'u dosyaya yazar; hata mesajları (**stderr**) hâlâ ekrana basılır.

Sadece hataları ayrı bir dosyaya yazmak için:

```bash
komut 2> hata.txt
```

`2`, stderr'in kanal numarasıdır (stdout `1`'dir, genelde yazılmaz çünkü varsayılandır).

İkisini birleştirip tek dosyaya yazmak için:

```bash
komut > tumu.txt 2>&1
```

`2>&1`, "kanal 2'yi (stderr) kanal 1'in (stdout) o an gittiği yere gönder" demektir.
Kabuk yönlendirmeleri soldan sağa, sırayla işler ve `2>&1` çalıştığı anda stdout'un o
anki hedefinin bir **kopyasını** alır — kalıcı bir bağ kurmaz. `> tumu.txt` önce
yazılırsa, o an stdout zaten dosyaya bakıyordur; `2>&1` de stderr'i aynı dosyaya
bağlar. Sırayı tersine çevirip `2>&1 > tumu.txt` yazarsan, `2>&1` çalıştığı anda
stdout hâlâ ekrana bakıyordur — stderr o an ekrana kopyalanır, sonra stdout dosyaya
taşınır ama stderr ekranda kalmaya devam eder. Bu yüzden sıra önemli: `2>&1` her
zaman `> tumu.txt`'den **sonra** yazılır.

"Log dosyam neden boş" sorusunun cevabı genelde budur: komut hata verip stderr'e
yazıyordur ama sen sadece stdout'u (`>`) yönlendirmişsindir.

## /dev/null: çıktıyı çöpe atmak

Bir çıktıyı hiç görmek istemiyorsan:

```bash
komut > /dev/null
```

`/dev/null`, yazılan her şeyi yutan özel bir "dosya"dır — hiçbir yere kaydedilmez.
Gürültülü bir komutun çıktısını görmezden gelmek istediğinde işe yarar. Hem stdout hem
stderr'i susturmak için:

```bash
komut > /dev/null 2>&1
```

## tee: hem ekrana bas hem dosyaya yaz

`>` çıktıyı sadece dosyaya gönderir, ekranda hiçbir şey görmezsin. Aynı anda hem izlemek
hem kaydetmek istiyorsan `tee`:

```bash
python egitim.py | tee egitim-log.txt
```

Beklenen: eğitim çıktısı hem ekranda akar hem `egitim-log.txt`'ye yazılır — eğitim
bitince `tail -f egitim-log.txt` ile de izleyebilirsin.

`tee` de tıpkı `>` gibi varsayılan olarak dosyanın üzerine yazar. Sonuna eklemek
istersen `>` yerine `>>` kullandığın gibi, `tee` yerine `tee -a` kullanırsın.

## Gerçek senaryo: uzun eğitimi kaydedip izlemek

```bash
python egitim.py > egitim-log.txt 2>&1 &
```

(sonundaki `&` komutu arka planda çalıştırır ama terminali kapattığında süreç de
sonlanır. Uzun bir eğitimi terminalden bağımsız, terminali kapatsan bile çalışmaya
devam edecek şekilde başlatmak için `nohup` ya da `screen` gerekir — bunlar
[SSH ile uzak makineye bağlanmak](../02-ileri/01-ssh-ile-uzak-baglanti.md) sayfasında
ele alınıyor.)

Sonra:

```bash
tail -f egitim-log.txt
```

ile canlı izlersin — bunu önceki sayfada öğrenmiştin.

## Sık yapılan hatalar

| Hata | Sebebi | Çözüm |
|---|---|---|
| Log dosyam boş çıkıyor ama komut hata verdi | Sadece stdout (`>`) yönlendirildi, stderr ekrana gitti | `2>&1` ekle: `komut > log.txt 2>&1` |
| Dosyamın eski içeriği kayboldu | `>` kullanıldı, `>>` gerekiyordu | Eklemek için `>>`, üzerine yazmak için `>` |
| `2>&1` çalışmadı, hata hâlâ ekranda | Sıra yanlış: `2>&1 > log.txt` yazıldı | `2>&1` her zaman `> log.txt`'den **sonra** gelmeli |
| `tee` sonrası dosya boş | Komut hiç çıktı üretmedi ya da `tee`'den önce hata oldu | Komutu tek başına çalıştırıp çıktı üretip üretmediğini kontrol et |

## Kendin dene

1. `echo "birinci" > deneme-cikti.txt` çalıştır, `cat deneme-cikti.txt` ile içeriği gör.
2. `echo "ikinci" >> deneme-cikti.txt` çalıştır, `cat deneme-cikti.txt` ile iki satır
   olduğunu doğrula.
3. `echo "ucuncu" > deneme-cikti.txt` çalıştır — dikkat, bu sefer `>>` değil `>`. `cat
   deneme-cikti.txt` ile bak: birinci ve ikinci satır kayboldu, sadece `ucuncu` kaldı.

Bu üçüncü adım tam olarak `>`'in üzerine yazma davranışını gösteriyor — bunu kendi
gözünle görmek, uyarıyı okumaktan daha kalıcı öğretir.

## Sonraki adım

→ [Ortam değişkenleri ve PATH](03-ortam-degiskenleri-ve-path.md)

---

<sub>Bu sayfada hata mı buldun? [Issue aç](https://github.com/Enes-CE/turkish-ai-handbook/issues/new/choose).</sub>
