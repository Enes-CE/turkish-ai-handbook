---
seviye: giriş
on-kosul: [python-ortamlari/00-temeller/01-python-kurulumu.md]
tip: komut
son-guncelleme: 2026-08-14
dogrulandigi-surum: pip — sürüm numarası verilmedi, komut sözdizimi kalıcı
---

# pip ile paket kurmak

> **Bu sayfa şunu çözer:** Python paketlerini `pip` ile kurmayı, sürümünü belirtmeyi,
> kurulu paketleri görmeyi ve kaldırmayı öğrenirsin.
> **Ön koşul:** [Python kurulumu](01-python-kurulumu.md) · **Süre:** ~15 dakika

---

## pip nedir

`pip`, Python'ın paket yöneticisi — PyPI'dan (Python Package Index) paket indirir,
kurar. Kütüphaneler, `import` etmeden önce bilgisayarına inmesi gereken kod
parçalarıdır; bu indirme/kurma işini yapan araç `pip`.

## pip install: temel kullanım

```bash
python -m pip install requests
```

Beklenen çıktı: indirme ve kurulum satırları, sonunda `Successfully installed requests-...`

Önceki sayfada değindiğimiz alışkanlığı burada da uygula: `pip install ...` yerine
`python -m pip install ...` yaz — hangi Python'a kurduğunu garantiler.

## Sürüm belirtme

```bash
python -m pip install pandas==2.2.0
```

`==`, tam olarak o sürümü kurar.

```bash
python -m pip install "pandas>=2.0"
```

`>=`, en az o sürümü (ya da daha yenisini) kurar. Tırnaklar burada süs değil,
zorunlu: `>` karakteri kabukta (Git Bash dahil) çıktı yönlendirme anlamına gelir —
[Çıktıyı dosyaya yazmak](../../terminal/01-gunluk-kullanim/02-cikti-yonlendirme.md)
sayfasında öğrendiğin şeyin ta kendisi. Tırnaksız yazarsan kabuk `>` işaretini
yönlendirme sanır, `pandas=2.0` adında boş bir dosya oluşturur ve pip'e sadece
`pandas` gider — sürüm sınırı sessizce kaybolur.

**Neden önemli:** "Pandas ile çalışıyor" demek yetmez — hangi sürümüyle çalıştığını
bilmen gerekir. Kütüphaneler zamanla API değiştirir; sürüm belirtmeden kurduğun bir
paket altı ay sonra farklı davranabilir, kodun sessizce kırılabilir. Ekip
çalışmasında da herkesin aynı sürümü kullanması, "bende çalışıyor ama sende
çalışmıyor" sorununu önler.

## pip list: kurulu paketleri görme

```bash
pip list
```

Beklenen çıktı: kurulu tüm paketlerin adı ve sürümü, alfabetik liste.

## pip show: bir paket hakkında detay

```bash
pip show requests
```

Beklenen çıktı:

```
Name: requests
Version: 2.32.3
Summary: Python HTTP for Humans.
Location: /c/Python312/Lib/site-packages
Requires: certifi, charset-normalizer, idna, urllib3
```

`Location` satırı paketin tam olarak nereye kurulduğunu, `Requires` satırı hangi
paketlere bağımlı olduğunu gösterir.

## pip uninstall

```bash
pip uninstall requests
```

Onay ister (`Proceed (y/n)?`), `y` yazıp devam edersin.

`pip uninstall` sadece belirttiğin paketi kaldırır — onunla birlikte gelen
bağımlılıkları (`certifi`, `urllib3` gibi) sistemde bırakır. Zamanla biriken bu
artıklar, sanal ortam kullanmanın bir başka sebebidir: ortamı tamamen silmek,
içindeki her şeyi tek seferde temizler.

## pip install --upgrade

```bash
python -m pip install --upgrade requests
```

Zaten kurulu bir paketi en son sürüme günceller.

## Paket nereye kuruluyor, bağımlılık ne demek

```
python -m pip install requests
        │
        ▼
PyPI'dan indirilir
        │
        ▼
requests'in ihtiyaç duyduğu paketler de indirilir:
  certifi, charset-normalizer, idna, urllib3   ← bağımlılıklar
        │
        ▼
hepsi birlikte kurulur → site-packages/ klasörüne
  (pip show requests → Location satırında tam yolu görürsün)
```

Bir paketi kurunca genelde yalnız gelmez — onun ihtiyaç duyduğu başka paketler de
(**bağımlılıklar**) otomatik kurulur. İki farklı projenin aynı bağımlılığın **farklı**
sürümlerine ihtiyaç duyması çakışmaya yol açabilir — bu sorunun çözümü
[Ortam sorunlarını çözmek](../01-gunluk-kullanim/03-ortam-sorunlarini-cozmek.md)
sayfasında; burada sadece kavramı tanı.

## Bunu sisteme değil, sanal ortama kurmalısın

> ⚠️ **Yukarıdaki komutları şimdi çalıştırırsan, paketler doğrudan bilgisayarındaki
> "sistem" Python'ına kurulur.** Bir proje `pandas 2.2`, başka bir proje `pandas 1.5`
> istediğinde ikisi aynı sistemde bir arada duramaz — biri diğerinin üzerine yazılır.
> Bu sayfada pip'i **öğrenmen** yeterli; bir sonraki sayfada
> ([Sanal ortam neden gerekli](03-sanal-ortam-nedir.md)) her proje için ayrı, izole
> bir kurulum alanı oluşturmayı göreceksin — asıl kurulumlarını oradan sonra yapacaksın.

## "externally-managed-environment" hatası

Bazı güncel Linux dağıtımlarında (ve bazı macOS Homebrew kurulumlarında) sisteme
doğrudan `pip install` çalıştırmaya çalışırsan şu hatayı alabilirsin:

```
error: externally-managed-environment
```

Bu, işletim sisteminin kendi Python'unu paketlerin bozmasını engellemek için koyduğu
bir kilit. İnternette önerilen `--break-system-packages` bayrağıyla bu kilidi
zorlamak **yanlış çözüm** — kilidin koyulma sebebini ortadan kaldırmaz, sadece
susturur. Doğru çözüm tam olarak bu sayfanın işaret ettiği yer: sanal ortam kullanmak.
Bir sonraki sayfa bunu gösteriyor.

## Colab/Jupyter içinde pip

Notebook hücresinde pip komutu iki farklı şekilde yazılır:

- `!pip install requests` — hücrenin başına `!` koyup terminal komutu gibi çalıştırır.
- `%pip install requests` — Jupyter'e özel "magic" komut; hücrenin çalıştığı Python'a
  kurulumu garanti eder.

**`%pip` tercih edilir** — `!pip`'in yanlış Python'a kurma riski `%pip`'te yoktur.
Detayı [Notebook ve Colab](../../notebook-ve-colab/README.md) bölümünde.

## Sık yapılan hatalar

| Hata | Sebebi | Çözüm |
|---|---|---|
| `pip install` sonrası `import` hata veriyor: `No module named ...` | Paket farklı bir Python'a kuruldu | `python -m pip install ...` kullan; `which python` ve `which pip`'in aynı yere baktığını doğrula |
| `error: externally-managed-environment` | Sistem Python'u dış paket kurulumuna kilitli | `--break-system-packages` ile zorlama — sanal ortam kullan (bir sonraki sayfa) |
| `pip uninstall` sonrası hâlâ `import` çalışıyor | Birden fazla Python/pip kurulu, başka bir kopyadan kaldırıldı | `pip show paket` ile hangi kurulumdan kaldırdığını kontrol et |
| Paket kurdum ama sürümü beklediğim gibi değil | Sürüm belirtilmeden kurulunca en yeni sürüm geldi | `paket==istediğin-sürüm` ile sabitle |

## Kendin dene

1. `python -m pip install requests` çalıştır.
2. `pip show requests` çalıştır — `Location` satırında paketin tam olarak nereye
   kurulduğunu gör.
3. `pip uninstall requests` çalıştır, `y` ile onayla.
4. `pip show requests` çalıştır — bu sefer paketin bulunamadığını (kurulu olmadığını)
   doğrula.

## Sonraki adım

→ [Sanal ortam neden gerekli](03-sanal-ortam-nedir.md)

---

<sub>Bu sayfada hata mı buldun? [Issue aç](https://github.com/Enes-CE/turkish-ai-handbook/issues/new/choose).</sub>
