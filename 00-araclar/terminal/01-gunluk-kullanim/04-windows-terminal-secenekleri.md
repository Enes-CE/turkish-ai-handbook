---
seviye: orta
on-kosul: [terminal/00-temeller/01-terminal-nedir.md]
tip: arayuz
son-guncelleme: 2026-08-12
dogrulandigi-surum: Windows 10/11 — arayüz hızlı değişebilir, bkz. BAKIM.md § 1
---

# Windows'ta terminal seçenekleri

> **Bu sayfa şunu çözer:** Windows'ta karşına çıkan dört farklı "terminal" seçeneğinin
> (CMD, PowerShell, Git Bash, WSL) ne olduğunu ve hangisini ne zaman kullanacağını
> öğrenirsin.
> **Ön koşul:** [Terminal nedir, neden gerekli](../00-temeller/01-terminal-nedir.md) ·
> **Süre:** ~10 dakika

---

> **Bu sayfa yalnızca Windows kullanıcıları içindir.** macOS ya da Linux kullanıyorsan
> atlayabilirsin — [Ortam değişkenleri ve PATH](03-ortam-degiskenleri-ve-path.md)'ten
> sonra doğrudan [SSH ile uzak makineye bağlanmak](../02-ileri/01-ssh-ile-uzak-baglanti.md)'a
> geçebilirsin.

## Dört seçenek

| Seçenek | Ne olduğu | Komut sözdizimi | Ne zaman tercih edilir |
|---|---|---|---|
| **CMD** | Windows'un en eski komut satırı | Kendine özgü (`dir`, `copy`) | Neredeyse hiç — eski `.bat` script'leri çalıştırman gerekmedikçe |
| **PowerShell** | Microsoft'un modern kabuğu | Kendine özgü (`Get-ChildItem`, ama `ls` takma adı da çalışır) | Windows'a özgü sistem yönetimi işleri |
| **Git Bash** | Git'le birlikte gelen, Unix sözdizimi konuşan kabuk | Unix (`ls`, `cd`, `grep`) | **Bu depodaki her şey için** — varsayılan tercih |
| **WSL** | Windows içinde çalışan gerçek bir Linux | Tam Unix/Linux | Linux'a özgü araçlar ya da GPU'lu derin öğrenme kurulumları gerektiğinde |

## Neden bu depoda Git Bash öneriliyor

Bu rehberdeki bütün komutlar Unix sözdizimiyle yazıldı (`ls`, `pwd`, `grep`, `|`, `>`).
Bunun iki sebebi var:

- İnternetteki eğitimlerin, StackOverflow cevaplarının ve kütüphane dokümanlarının
  büyük çoğunluğu da Unix sözdizimi kullanıyor — Git Bash'te öğrendiğin her şey
  doğrudan transfer olur.
- macOS ve Linux kullanan ekip arkadaşlarınla aynı komutları paylaşabilirsin;
  PowerShell'e özgü bir komut onlarda çalışmaz.

## Sözdizimi farkları

| İşlem | CMD | PowerShell | Git Bash (bu depo) |
|---|---|---|---|
| Klasördeki dosyaları listele | `dir` | `Get-ChildItem` (takma ad: `ls`) | `ls` |
| Bulunduğun yeri göster | `cd` (argümansız) | `pwd` | `pwd` |
| Ev dizini | `%USERPROFILE%` | `$HOME` ya da `~` | `~` |
| Yol yazımı | `C:\Users\adin` | `C:\Users\adin` | `/c/Users/adin` |
| Ortam değişkeni okuma | `%VAR%` | `$env:VAR` | `$VAR` |

Bu tablo ezberlenmek için değil — "başka birinin ekran görüntüsündeki komut neden
benimkiyle aynı görünmüyor" sorusuna hızlı cevap için.

## Windows Terminal: bu bir kabuk DEĞİL

Sık karıştırılan bir nokta: **Windows Terminal bir kabuk değil, sekmeli bir penceredir.**
İçinde CMD, PowerShell, Git Bash ve WSL'in hepsi ayrı sekmeler olarak çalışabilir:

```
┌───────────────────────────────────────────────────────┐
│ Windows Terminal (pencere)                            │
│                                                       │
│ ┌────────────┬────────────┬────────────┬────────────┐ │
│ │    CMD     │ PowerShell │  Git Bash  │    WSL     │ │  ← sekmeler
│ └────────────┴────────────┴────────────┴────────────┘ │
│                                                       │
│ (aktif sekmedeki kabuk burada çalışır)                │
└───────────────────────────────────────────────────────┘
```

Windows Terminal'i kullanmak zorunda değilsin — Git Bash'i kendi penceresinde de
açabilirsin. Windows Terminal sadece hepsini tek pencerede, sekmeler hâlinde
toplamanı sağlayan bir araç.

## WSL nedir, ne zaman gerekir

WSL (Windows Subsystem for Linux), Windows içinde çalışan **gerçek bir Linux**'tur —
Git Bash gibi "Unix'e benzeyen" değil, gerçek bir Linux çekirdeği.

- **Gerekir:** GPU'lu derin öğrenme kurulumları (bazı CUDA/sürücü kombinasyonları
  Windows'ta değil WSL içinde sorunsuz çalışır), Linux'a özgü araçlar ya da paketler.
- **Gerekmez:** Bu rehberin kapsadığı işlerin büyük çoğunluğu için Git Bash yeterli.
  WSL kurulumu ekstra adım ve ekstra bakım demek — ihtiyacın olduğunda kur, baştan kurma.

Kurulum adımları bu sayfanın kapsamı dışında; ihtiyacın olduğunda güncel resmi
belgeye bakman en sağlıklısı, çünkü kurulum adımları Windows sürümüne göre değişiyor.

## VS Code'da varsayılan terminal

VS Code'un kendi içindeki terminal de yukarıdaki kabuklardan birini çalıştırır —
varsayılanı Git Bash olarak ayarlamak, entegre terminalde de aynı Unix sözdizimini
kullanmanı sağlar. Bu ayar [VS Code](../../vscode/) bölümünde ele alınıyor.

## Git Bash'in sınırları

Git Bash her şeyi çözmez. Bazı Windows'a özgü araçlar (bazı kurulum sihirbazları,
bazı sistem yönetimi komutları) Git Bash içinde beklendiği gibi çalışmaz ya da hiç
çalışmaz. Böyle bir durumla karşılaşırsan PowerShell'e geçmek gerekebilir — bu bir
başarısızlık değil, doğru aracı doğru işe kullanmaktır.

## Sık yapılan hatalar

| Hata | Sebebi | Çözüm |
|---|---|---|
| Bir öğreticideki komut çalışmıyor | Öğretici PowerShell/CMD sözdizimi kullanıyor, sen Git Bash'tesin (ya da tersi) | Yukarıdaki sözdizimi tablosuna bak, karşılığını bul |
| Windows Terminal'i "kabuk" sanıp içinde komut denedim, hata aldım | Windows Terminal bir pencere, kabuk değil — hangi sekmede olduğun önemli | Sekmenin hangi kabuk olduğunu kontrol et |
| Bir kurulum sihirbazı ya da araç Git Bash'te çalışmadı | Bazı Windows araçları Git Bash ile uyumsuz | PowerShell'de dene |
| WSL kurdum ama Git Bash'teki dosyalarımı göremiyorum | WSL kendi ayrı dosya sistemini kullanır | WSL içinden Windows dosyalarına `/mnt/c/...` üzerinden erişilir |

## Kendin dene

Hangi kabukta olduğunu anlamak için `ls` yazıp denemek **işe yaramaz** — PowerShell'de
`ls`, `Get-ChildItem`'ın bir takma adı olarak zaten çalışır. "ls çalıştı, demek ki
Git Bash'teyim" düşüncesi yaygın bir yanılgıdır.

Daha güvenilir bir yöntem:

```bash
echo $0
```

Git Bash'te bu genelde `bash` ya da `-bash` gibi bir çıktı verir. (`$SHELL` değil
`$0` kullanıyoruz çünkü `$SHELL` senin *giriş* kabuğunu gösterir, o an çalıştığın
kabuğu değil — Git Bash'te sık sık boş döner ya da beklenmedik bir değer verir.)

En kesin doğrulama için, PowerShell'de **hiçbir takma adı olmayan** bir Unix
komutu dene:

```bash
grep --version
```

Bir sürüm bilgisi basıyorsa Git Bash ya da WSL'desin. `command not found` ya da
"tanınmayan komut" hatası alırsan PowerShell ya da CMD'desin — çünkü `grep`'in
`ls`'nin aksine PowerShell'de hiçbir karşılığı ya da takma adı yok.

## Sonraki adım

→ [SSH ile uzak makineye bağlanmak](../02-ileri/01-ssh-ile-uzak-baglanti.md)

---

<sub>Bu sayfada hata mı buldun? [Issue aç](https://github.com/Enes-CE/turkish-ai-handbook/issues/new/choose).</sub>
