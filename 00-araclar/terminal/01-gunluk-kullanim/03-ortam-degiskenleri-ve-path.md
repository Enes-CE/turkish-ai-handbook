---
seviye: orta
on-kosul: [terminal/00-temeller/05-komut-yapisi-ve-yardim.md]
tip: kavram
son-guncelleme: 2026-08-12
dogrulandigi-surum: kavramsal — sürümden bağımsız
---

# Ortam değişkenleri ve PATH

> **Bu sayfa şunu çözer:** Terminalin komutları nasıl bulduğunu (PATH), programların
> birbiriyle veri paylaştığı ad-değer çiftlerini (ortam değişkenleri) ve API anahtarı
> gibi gizli bilgileri koda gömmeden yönetmeyi öğrenirsin.
> **Ön koşul:** [Komut yapısı ve yardım okuma](../00-temeller/05-komut-yapisi-ve-yardim.md) ·
> **Süre:** ~20 dakika

---

## Ortam değişkeni nedir

Kabuk oturumunun taşıdığı ad-değer çiftleridir; programlar çalışırken bunları okuyabilir.

```bash
echo $HOME
```

Beklenen çıktı: `/c/Users/adin`

```bash
echo $PATH
```

Beklenen çıktı: `:` ile ayrılmış bir klasör listesi, örn. `/usr/local/bin:/usr/bin:/bin`

Hepsini birden listelemek için:

```bash
env
```

Beklenen çıktı: uzun bir `AD=değer` listesi.

## PATH nedir: komutlar nereden bulunuyor

`python` yazdığında kabuk bunu nereden çalıştıracağını nasıl biliyor? Cevap PATH:

```
kullanıcı yazar: python
        │
        ▼
PATH'teki klasörler sırayla taranır:
  /usr/local/bin   →  python var mı?  hayır
  /usr/bin         →  python var mı?  hayır
  /c/Python312     →  python var mı?  EVET → bu çalıştırılır
        │
  hiçbirinde bulunamazsa:
        ▼
  "python: command not found"
```

`command not found` hatasının gerçek anlamı budur: program bilgisayarında yok demek
değildir — PATH'teki klasörlerin hiçbirinde **bulunamadı** demektir. Program kurulu
olabilir ama PATH'e eklenmemiş olabilir.

## which: bir komut nereden geliyor

```bash
which python
```

Beklenen çıktı: `/c/Python312/python` gibi tam bir yol. Git Bash'te `which` kullanılır
(Windows'un kendi cmd/PowerShell'inde karşılığı `where`'dir, ama bu depo Git Bash
kullanıyor).

Birden fazla `python` kuruluysa (örn. hem sistem Python'u hem Anaconda), `which python`
hangisinin çalıştığını gösterir — bu tür karışıklıkları çözmenin ilk adımı budur.

## export: geçici değişken tanımlamak

```bash
export API_ANAHTARI="deneme-1234"
```

```bash
echo $API_ANAHTARI
```

Beklenen çıktı: `deneme-1234`

Bu değişken sadece **bu terminal oturumunda** yaşar. Terminali kapatıp yeni bir tane
açtığında kaybolur — bunu birazdan kendin deneyeceksin.

Oturum bitmeden bir değişkeni silmek istersen:

```bash
unset API_ANAHTARI
```

## Kalıcı yapmak: kabuğun başlangıç dosyası

Her terminal açılışında otomatik tanımlanmasını istiyorsan, `export` satırını kabuğun
başlangıç dosyasına eklersin. Hangi dosya olduğu kabuğa göre değişir:

- **Git Bash (Windows):** `~/.bash_profile` — Git Bash varsayılan olarak `.bashrc`'yi
  değil `.bash_profile`'ı okur. `.bashrc`'ye eklersen çoğu kurulumda hiçbir şey olmaz.
- **Linux (bash):** `~/.bashrc`
- **macOS (zsh, varsayılan):** `~/.zshrc`

```bash
echo 'export API_ANAHTARI="deneme-1234"' >> ~/.bash_profile
```

Değişikliği mevcut terminalde hemen görmek için dosyayı yeniden yükle:

```bash
source ~/.bash_profile
```

`source` olmadan değişiklik yalnızca **yeni açılan** terminallerde etkili olur.

> ⚠️ **PATH'i elle düzenlerken `$PATH`'i unutma:**
>
> ```bash
> export PATH="$PATH:/yeni/yol"
> ```
>
> Başındaki `$PATH` kritik — bu, "mevcut PATH'i koru, sonuna yeni klasörü ekle" demektir.
> `$PATH` olmadan `export PATH="/yeni/yol"` yazarsan bütün PATH'in üzerine yazarsın;
> `python`, `git`, `ls` dahil neredeyse hiçbir komut çalışmaz hâle gelir, çünkü kabuk
> onları artık hiçbir yerde aramıyor. Düzeltmesi basit: terminali kapatıp yeni bir tane
> aç, hasar sadece o oturuma özeldi.

## API anahtarını koda gömmemek

> ⚠️ **API anahtarı, şifre gibi gizli bilgileri asla kodun içine yazma — ortam
> değişkeninde tut.** Kod bir gün Git'e, oradan da belki herkese açık bir depoya
> gidebilir; içine gömülü bir anahtar da onunla birlikte gider.

Zaten `export` edilmiş bir değişkeni Python'dan okumak:

```python
import os
anahtar = os.getenv("API_ANAHTARI")
```

Birçok proje bu değişkenleri terminalden `export` etmek yerine `.env` adlı bir dosyada
tutar. Ama dikkat: **Python `.env` dosyasını kendiliğinden okumaz.** Sadece `.env`
dosyası oluşturup yukarıdaki `os.getenv(...)`'i çağırırsan sonuç `None` olur — dosyanın
var olması yetmez, biri onu okuyup ortam değişkenine dönüştürmeli. Bunun için
`python-dotenv` kütüphanesi kullanılır:

```python
from dotenv import load_dotenv
import os

load_dotenv()
anahtar = os.getenv("API_ANAHTARI")
```

`.env` dosyası **asla** Git'e commit'lenmez — `.gitignore`'a eklenir. Detayı
[.gitignore ve büyük dosyalar](../../git-github/01-gunluk-kullanim/05-gitignore-buyuk-dosyalar.md)
sayfasında.

## Windows'ta ortam değişkenleri: iki ayrı katman

Git Bash içinde `export` ile tanımladığın değişken, Windows'un kendi sistem ortam
değişkenlerinden (Denetim Masası → Sistem → Gelişmiş sistem ayarları) **ayrı bir
şeydir**. Biri sadece Git Bash oturumunda yaşar, diğeri bütün Windows programları için
geçerlidir.

Python kurulumunda gördüğün "Add Python to PATH" seçeneği, tam olarak bu Windows sistem
PATH'ine Python'un klasörünü ekler — `export`'un aksine, kapattığın her terminalde kalıcıdır.

## Sık yapılan hatalar

| Hata | Sebebi | Çözüm |
|---|---|---|
| `command not found` ama program kurulu | Program PATH'te değil | `which komut` ile ara, yoksa kurulum klasörünü PATH'e ekle |
| Terminali kapatıp açınca değişkenim kayboldu | `export` ile tanımlandı ama başlangıç dosyasına eklenmedi | Kalıcı yapmak için kabuğunun başlangıç dosyasına ekle, `source` ile yükle |
| Git Bash'te `~/.bashrc`'ye ekledim, hiçbir şey olmadı | Git Bash varsayılan olarak `.bashrc`'yi değil `.bash_profile`'ı okur | `~/.bash_profile`'a ekle |
| Başlangıç dosyasını değiştirdim ama hiçbir şey olmadı | `source` çalıştırılmadı | `source` ile ilgili dosyayı çalıştır ya da yeni bir terminal aç |
| PATH'i değiştirdikten sonra hiçbir komut çalışmıyor | `$PATH` olmadan üzerine yazıldı | Yeni terminal aç (hasar o oturuma özeldi), bu sefer `export PATH="$PATH:/yol"` yaz |

## Kendin dene

1. `export DENEME_DEGISKENI="merhaba"` çalıştır.
2. `echo $DENEME_DEGISKENI` ile `merhaba` çıktısını doğrula.
3. Yeni bir terminal penceresi aç (mevcut olanı kapatma).
4. Yeni pencerede `echo $DENEME_DEGISKENI` çalıştır — boş çıktı görürsün. Bu, `export`'un
   sadece o an içinde bulunduğun oturuma ait olduğunu, kalıcı olmadığını kanıtlar.

## Sonraki adım

→ [Windows'ta terminal seçenekleri](04-windows-terminal-secenekleri.md)

---

<sub>Bu sayfada hata mı buldun? [Issue aç](https://github.com/Enes-CE/turkish-ai-handbook/issues/new/choose).</sub>
