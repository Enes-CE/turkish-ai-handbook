---
seviye: giriş
on-kosul: [terminal/00-temeller/01-terminal-nedir.md]
tip: komut
son-guncelleme: 2026-08-12
dogrulandigi-surum: bash (Git Bash / macOS / Linux ortak)
---

# Dosya sistemi ve yol kavramı

> **Bu sayfa şunu çözer:** Terminalde bulunduğun yeri (`pwd`), oradaki dosyaları (`ls`) ve
> başka bir yere gitmeyi (`cd`) öğrenirsin; mutlak ve göreli yolun farkını örneklerle görürsün.
> **Ön koşul:** [Terminal nedir, neden gerekli](01-terminal-nedir.md) · **Süre:** ~15 dakika

---

## Dosya sistemi bir ağaçtır

Her klasör bir üst klasörün içinde durur, o da kendi üstündekinin içinde — en tepede tek bir
kök vardır. Örnek bir ağaç:

```
/                                    (kök dizin)
└── c/                               (Windows'ta C: sürücüsü, Git Bash'te böyle görünür)
    └── Users/
        └── adin/
            ├── Belgeler/
            ├── Indirilenler/
            └── projeler/
                ├── turkish-ai-handbook/     ← şu an buradasın
                │   ├── 00-araclar/
                │   └── README.md
                └── baska-proje/
```

Terminal her zaman bu ağaçta bir yerdedir. GUI'de hangi klasörü çift tıklayıp açtığına
karşılık gelen şeye terminalde **çalışma dizini** denir.

## Neredesin: pwd

```bash
pwd
```

Beklenen çıktı:

```
/c/Users/adin/projeler/turkish-ai-handbook
```

`pwd` (print working directory), bulunduğun yerin tam adresini yazar. Kaybolduğunu
hissettiğin her an ilk yazacağın komut budur.

## Burada ne var: ls

```bash
ls
```

Beklenen çıktı: bulunduğun klasördeki dosya ve klasörlerin listesi.

İki bayrak sık kullanılır:

- `ls -l` — detaylı liste (boyut, tarih, izinler)
- `ls -a` — gizli dosyalar dahil (nokta ile başlayanlar, örn. `.git`)

İkisi birlikte: `ls -la`

## Yer değiştirmek: cd

```bash
cd Belgeler
```

Çıktı vermez — sessiz çalışır. Doğru yere gittiğini `pwd` ile kontrol edersin. Bir üst
klasöre çıkmak için:

```bash
cd ..
```

`cd` tek başına, hiç argümansız yazılırsa seni ev dizinine götürür.

```bash
cd -
```

`cd -` bir önceki bulunduğun dizine geri döndürür — iki klasör arasında gidip gelirken
çok işe yarar.

## Mutlak yol vs göreli yol

Bu sayfanın en kritik konusu. Aynı hedefe iki şekilde gidebilirsin:

```
Hedef: /c/Users/adin/projeler/baska-proje

MUTLAK YOL — kökten başlar, nereden çalıştırırsan çalıştır aynıdır
  cd /c/Users/adin/projeler/baska-proje

GÖRELİ YOL — bulunduğun yere göre değişir
  Şu an buradaysan:  /c/Users/adin/projeler/yapay-zeka-el-kitabi
    cd ../baska-proje

  Şu an buradaysan:  /c/Users/adin
    cd projeler/baska-proje
```

Mutlak yol her zaman `/` ile başlar (ya da Windows'ta sürücü harfiyle). Göreli yol
başlamaz — nereden yazdığına bağlıdır. Bir script'i başkasıyla paylaşacaksan mutlak yol
onun bilgisayarında çalışmaz; göreli yol genelde daha taşınabilirdir.

**Pratik kural:** günlük terminal kullanımında göreli yol daha pratiktir — kısa yazılır ve
Tab tamamlamayla hızlı gidersin. Script yazarken ise dikkatli ol: göreli yol, script'in
hangi klasörden çalıştırıldığına bağlıdır ve script'i başka bir yerden çalıştırdığında
kırılabilir.

## . ve .. ne demek

- `.` — şu an bulunduğun klasörün kendisi
- `..` — bir üst klasör

```bash
cd ..      # bir üst dizine çık
cd ../..   # iki üst dizine çık
```

## ~ (ev dizini) kısayolu

`~` senin kullanıcı klasörünü temsil eder (örn. `/c/Users/adin`).

```bash
cd ~/projeler
```

yazmak, `cd /c/Users/adin/projeler` yazmakla aynı sonucu verir.

## Windows'ta yol yazımı farkı

Aynı yer, iki farklı yazım:

- **Windows Gezgini:** `C:\Users\adin\Belgeler` (ters bölü `\`)
- **Git Bash:** `/c/Users/adin/Belgeler` (düz bölü `/`, sürücü harfi küçük ve başında `/`)

Bu rehberdeki bütün komutlar Git Bash / Unix yazımıyla verilir. Gezgin'den kopyaladığın bir
yolu doğrudan yapıştırırsan çalışmaz — sürücü harfini ve bölüleri çevirmen gerekir.

## Boşluklu klasör adları

`Program Files` gibi boşluklu isimlerde tırnak kullan, yoksa kabuk ismi iki ayrı argüman sanır:

```bash
cd "Program Files"
```

ya da boşluğu ters bölü ile kaçır:

```bash
cd Program\ Files
```

## Tab tamamlama

Yol yazarken en çok zaman kazandıran şey. Klasör adının ilk birkaç harfini yaz, `Tab`'a
bas — kabuk geri kalanını kendisi tamamlar. Birden fazla eşleşme varsa `Tab`'a iki kez
basınca olası seçenekleri listeler. Hem hızlandırır hem yazım hatasını önler; elle uzun
yol yazmak yerine hep tamamlatmayı alışkanlık hâline getir.

## Sık yapılan hatalar

| Hata | Sebebi | Çözüm |
|---|---|---|
| `No such file or directory` | Yol yanlış yazıldı ya da başka bir klasördesin | `pwd` ile neredeysen kontrol et, `ls` ile klasör adını doğrula |
| Boşluklu klasörde `cd` hata veriyor | Tırnak ya da kaçış kullanılmadı | `"Klasör Adı"` ya da `Klasör\ Adı` yaz |
| Windows'tan kopyaladığım yol (`C:\...`) çalışmıyor | Git Bash ters bölüyü farklı yorumluyor | `/c/Users/...` biçimine çevir |
| `cd` ile hep aynı ya da beklenmedik yere gidiyorum | `~` ya da göreli/mutlak yol karışıklığı | `pwd` ile başlangıç noktanı kontrol et, sonra tekrar dene |

## Kendin dene

1. `cd ~` yaz, sonra `pwd` ile ev dizininde olduğunu doğrula.
2. Bu depoyu bilgisayarına indirdiğin klasöre göreli bir yolla gir (örn.
   `cd Desktop/turkish-ai-handbook` — kendi yoluna göre değişir), `pwd` ile tam yolunu gör.
3. `cd ..` yaz, `pwd` çıktısının bir önceki adımdakinden tam olarak bir klasör kısa
   olduğunu doğrula.

Üçünde de `pwd` çıktısı beklediğin yeri gösteriyorsa, yol kavramını doğru kullanıyorsun.

## Sonraki adım

→ [Dosya ve klasör işlemleri](03-dosya-klasor-islemleri.md)

---

<sub>Bu sayfada hata mı buldun? [Issue aç](https://github.com/Enes-CE/turkish-ai-handbook/issues/new/choose).</sub>
