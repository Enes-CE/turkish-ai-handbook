---
seviye: giriş
on-kosul: [terminal/00-temeller/02-dosya-sistemi-ve-yol.md]
tip: komut
son-guncelleme: 2026-08-14
dogrulandigi-surum: python.org / Homebrew / apt kurulumu — sürüm numarası verilmedi
---

# Python kurulumu

> **Bu sayfa şunu çözer:** Python'ı bilgisayarına doğru şekilde kurar, "command not
> found" ya da Microsoft Store'un açılması gibi en yaygın kurulum tuzaklarından
> kaçınırsın.
> **Ön koşul:** [Dosya sistemi ve yol kavramı](../../terminal/00-temeller/02-dosya-sistemi-ve-yol.md) ·
> **Süre:** ~20 dakika

---

## Neden gerek var?

Bootcamp'lerde en çok zaman kaybettiren adım genelde ilk kurulumdur — kod yazmaya
başlamadan önce `python: command not found` ya da Microsoft Store'un açılması gibi
sorunlarla boğuşmak. Bu sayfa, kurulumu bir kere doğru yapıp bu sorunları baştan
önlemeyi hedefliyor.

## Hangi sürüm

En yeni sürüm her zaman en iyi seçim değildir — kütüphanelerin (özellikle veri
bilimi/ML kütüphanelerinin) yeni bir Python sürümüne uyum sağlaması zaman alır.
**Kalıcı kural: en yeni kararlı sürümün bir gerisini tercih et.** Yeni çıkan bir
sürümde bazı paketler henüz derlenmemiş/desteklenmemiş olabilir; bunun sonucu genelde
anlaşılmaz bir kurulum hatasıdır.

Burada belirli bir sürüm numarası verilmiyor çünkü bu bilgi hızlı eskir — kurulum
anında python.org'daki güncel kararlı sürümü, ondan bir öncekiyle karşılaştırıp seç.

## Windows kurulumu

python.org'dan indirilen kurulum dosyasını çalıştır.

> ⚠️ **Kurulum ekranındaki "Add python.exe to PATH" kutusunu mutlaka işaretle.**
> İşaretlemezsen Python kurulur ama terminal onu bulamaz — `python` yazdığında
> `command not found` alırsın. Bunun nedeni
> [Ortam değişkenleri ve PATH](../../terminal/01-gunluk-kullanim/03-ortam-degiskenleri-ve-path.md)
> sayfasında anlattığımız şey: program PATH'e eklenmeden terminal onu bulamaz. Kutuyu
> işaretlemeyi unuttuysan, kurulumu PATH kutusunu işaretleyerek tekrarlamak, elle PATH
> düzenlemekten daha az sorunlu bir çözümdür.

### Microsoft Store tuzağı

Windows'ta `python` yazdığında bazen hiç hata almazsın ama beklediğin gibi de
çalışmaz — Microsoft Store açılır, "Python'ı yüklemek ister misiniz" der. Bu,
Windows'un "app execution alias" adlı özelliğinden kaynaklanır: `python` komutu
Store'a yönlendirilmiş bir kısayoldur, gerçek bir Python kurulu olmasa bile bu
davranış görülür.

Çözüm: Windows Ayarlar → Uygulamalar → Gelişmiş uygulama ayarları → Uygulama yürütme
diğer takma adları (App execution aliases) bölümünden `python.exe`/`python3.exe` için
olan anahtarları kapat. Menü adımlarını burada tam vermiyoruz çünkü Windows sürümüne
göre değişiyor — güncel adımlar için "app execution aliases python" araması yeterli.

## macOS kurulumu

macOS'ta sistemle gelen bir Python zaten var ama **bunu kullanma** — işletim
sisteminin kendi araçları buna bağımlı, üzerine paket kurup bir şeyi bozarsan sistem
etkilenebilir, ayrıca genelde eski bir sürümdür. İki iyi seçenek:

- python.org'dan indirip kurmak
- Homebrew ile kurmak: `brew install python`

## Linux kurulumu

Çoğu dağıtımda Python zaten kuruludur (`python3` olarak). Dağıtımının paket
yöneticisiyle güncel bir sürüm kurabilirsin, örn. Debian/Ubuntu'da:

```bash
sudo apt install python3 python3-pip python3-venv
```

`python3-venv` ayrı bir paket olarak eklendi çünkü Debian/Ubuntu'da sanal ortam
desteği Python'la birlikte gelmez — sonraki sayfalarda `venv` kullanacağız.

## python vs python3, pip vs pip3

Linux ve macOS'ta genelde `python3` ve `pip3` komutları kullanılır — tarihsel olarak
sistemin artık neredeyse hiç kalmamış Python 2'siyle karışmasın diye. `python`
yazınca `command not found` alıyorsan `python3` dene.

Windows'ta python.org kurulumunda genelde hem `python` hem `py` (Python launcher)
gelir. `py`, birden fazla Python sürümü kurulu olduğunda hangisini çalıştıracağını
seçmene izin verir (örn. `py -3.11`) — bu depoda ayrıca işlenmiyor, ihtiyacın olursa
`py --help` ile seçenekleri gör.

**Alışkanlık edinmeye değer:** `pip install ...` yerine `python -m pip install ...`
yazmak. Bu, `pip`'in her zaman o an çalışan `python` ile aynı kuruluma bağlı
çalışmasını garanti eder. Birden fazla Python kuruluysa `pip` ve `python` farklı
kurulumlara bağlı olabilir — "`pip` ile kurdum ama Python içinde `import` edemiyorum"
sorununun kalıcı çözümü budur.

## Kurulumu doğrulama

```bash
python --version
```

Beklenen çıktı: `Python 3.x.x` gibi bir sürüm bilgisi. `command not found` alırsan
`python3 --version` dene.

```bash
pip --version
```

Beklenen çıktı: pip sürümü ve hangi Python'a bağlı olduğunu gösteren bir yol bilgisi.

## Birden fazla Python kuruluysa

```
kullanıcı yazar: python
        │
        ▼
PATH'teki klasörler sırayla taranır:
  .../Anaconda3            →  python var mı?  EVET → BU çalıştırılır
  /c/Python312              →  (taranmaz bile, ilki zaten bulundu)
  .../Microsoft/WindowsApps →  (taranmaz)
```

Birden fazla Python kurulu olduğunda (örn. hem python.org sürümü hem Anaconda),
hangisinin çalıştığı PATH'te **hangisinin önce** listelendiğine bağlıdır — aynı
mantık, [Ortam değişkenleri ve PATH](../../terminal/01-gunluk-kullanim/03-ortam-degiskenleri-ve-path.md)
sayfasında anlatılmıştı, burada Python'a özel hâli.

Hangisinin çalıştığını bulmak için:

```bash
which python
```

Beklenen çıktı: çalışan Python'ın tam yolu, örn. `/c/Users/adin/anaconda3/python`.

## Sık yapılan hatalar

| Hata | Sebebi | Çözüm |
|---|---|---|
| `command not found: python` | Kurulumda "Add to PATH" işaretlenmedi | Kurulumu PATH kutusunu işaretleyerek tekrarla |
| `python` yazınca Microsoft Store açılıyor | Windows'un app execution alias'ı devrede | Ayarlar → Uygulamalar → Gelişmiş uygulama ayarları → Uygulama yürütme takma adlarından kapat |
| `python --version` beklenmedik/eski bir sürüm gösteriyor | Birden fazla Python kurulu, PATH'te başka biri önde | `which python` ile hangisinin çalıştığını bul |
| `pip` çalışıyor ama kurduğum paket Python'da görünmüyor | `pip` ve `python` farklı kurulumlara bağlı | `python -m pip install ...` kullan — bu, pip'i o an çalışan Python'a bağlı çalıştırır |

## Kendin dene

1. `python --version` çalıştır, bir sürüm numarası gördüğünü doğrula (görmüyorsan
   `python3 --version` dene).
2. `pip --version` çalıştır, sürüm bilgisiyle birlikte hangi Python'a bağlı olduğunu
   gösteren yol bilgisini oku.
3. `which python` ile çalışan Python'ın tam dosya yolunu bul — bu yol, kurulum
   sırasında PATH'e eklenen Python'ı doğrular. (`which`, Git Bash/macOS/Linux'ta
   kullanılır; PowerShell'de karşılığı `where python`'dır.)

## Sonraki adım

→ [pip ile paket kurmak](02-pip-ile-paket-kurmak.md)

---

<sub>Bu sayfada hata mı buldun? [Issue aç](https://github.com/Enes-CE/turkish-ai-handbook/issues/new/choose).</sub>
