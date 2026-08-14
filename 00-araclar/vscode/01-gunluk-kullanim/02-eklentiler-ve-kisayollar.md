---
seviye: orta
on-kosul: [vscode/00-temeller/01-kurulum-ve-arayuz.md]
tip: arayuz
son-guncelleme: 2026-08-14
dogrulandigi-surum: VS Code eklenti pazarı — arayüz hızlı değişebilir, bkz. BAKIM.md § 1
---

# Faydalı eklentiler ve kısayollar

> **Bu sayfa şunu çözer:** Bir eklentinin bakımlı olup olmadığını nasıl
> anlayacağını, hangi kategori eklentilerin gerçekten işine yarayacağını ve
> günlük iş akışını hızlandıracak kısayolları öğrenirsin.
> **Ön koşul:** [Kurulum ve arayüz](../00-temeller/01-kurulum-ve-arayuz.md) ·
> **Süre:** ~15 dakika

---

Eklenti listeleri en hızlı eskiyen içerik türü — bir eklenti bakımsız kalabilir,
adı değişebilir, yerini başka bir eklenti alabilir. Bu sayfa ürün adı listesi
vermek yerine kategori ve seçme kriteri anlatıyor; bu kısım kalıcı.

## Bir eklentiyi nasıl değerlendirirsin

Bu bölüm sayfanın en değerli kısmı — liste ezberlemek yerine burayı öğren.

Eklentiler panelinde bir eklentiye tıkladığında şunlara bak:

- **Son güncelleme tarihi** — birkaç yıl güncellenmemiş bir eklenti, güncel VS
  Code sürümüyle uyumsuz olabilir.
- **İndirme/kurulum sayısı** — yüksek sayı, geniş kullanım ve daha hızlı hata
  bildirimi/düzeltmesi demektir.
- **Yayıncının kimliği** — Microsoft gibi resmi bir yayıncı mı, yoksa kişisel
  bir hesap mı? Resmi eklentiler genelde daha uzun ömürlü bakım alır.
- **Açık issue sayısı ve yanıt hızı** — eklentinin GitHub deposuna bakarsan
  (çoğu eklenti açık kaynaklıdır), sorunların ne kadar hızlı çözüldüğünü görürsün.

Bu dört kritere bakmak, "en popüler 10 eklenti" listesi okumaktan daha kalıcı
bir beceri — liste bir yıl içinde eskir, değerlendirme yöntemi eskimez.

## Eklenti kategorileri

### Dil desteği

[Python eklentisi](../00-temeller/02-python-eklentisi-ve-yorumlayici.md)
sayfasında kurduğun Microsoft'un resmi Python eklentisi bu kategoride — zaten
kurulu.

### Linter / formatter

Kod stilini otomatik denetleyen (linter) ve düzelten (formatter) araçlar.
Kavramsal olarak ikisi farklı iş yapar: linter hataları/stil sorunlarını
işaretler, formatter kodu otomatik olarak yeniden biçimlendirir (boşluk, satır
uzunluğu gibi). Python dünyasında Ruff ve Black bu iki işi gören yaygın
araçlardan — isimlerini bilmen yeterli, hangisini seçeceğin zamanla değişebilir.

Ayar: `Editor: Format On Save` — kaydettiğinde otomatik biçimlendirme yapar,
komut paletinden aç/kapat.

### Git yardımcıları

[Entegre terminal ve Git arayüzü](../00-temeller/03-terminal-ve-git-arayuzu.md)
sayfasında gördüğün Kaynak Denetimi panelinin ötesinde, satır bazlı geçmiş
gösterimi sunan eklentiler var — kod satırının üzerine geldiğinde "bu satırı
kim, ne zaman, hangi commit'te değiştirdi" bilgisini gösterir. `git blame`'in
editördeki hâli.

### Uzak geliştirme

[SSH ile uzak makineye bağlanmak](../../terminal/02-ileri/01-ssh-ile-uzak-baglanti.md)
sayfasında terminalden bağlanmayı öğrenmiştin. Uzak geliştirme eklentileri bunu
bir adım öteye taşır: SSH ile bağlandığın sunucudaki kodu, yerel VS Code
arayüzünle açıp düzenleyebilirsin — dosyalar sunucuda kalır, sen kendi
editörünün tüm rahatlığıyla çalışırsın. Gerçekten güçlü bir özellik; GPU'lu bir
sunucuda çalışırken terminal ve editör arasında sürekli geçiş yapmak yerine tek
pencerede çalışırsın.

### Konteyner / ortam eklentileri

Projenin bütün ortamını (işletim sistemi, kütüphaneler) bir konteyner
tanımından kurup içinde geliştirmeni sağlayan eklentiler de var —
[Python Ortamları](../../python-ortamlari/README.md) bölümünde gördüğün
venv/conda'nın bir adım ötesi, farklı bir izolasyon katmanı. Bu depoda
ayrıntısına girmiyoruz.

## Eklenti maliyeti

Her kurulu eklenti, VS Code'un açılış süresini ve bellek kullanımını bir miktar
artırır. Aylardır açmadığın, artık kullanmadığın eklentileri kaldırmak
(eklenti sayfasından "Uninstall") genel performansı korur. "Belki lazım olur"
diye biriktirmek yerine ihtiyaç oldukça kur.

## Kısayollar

Önceki sayfalarda gördüklerinin üstüne, günlük iş akışını hızlandıran birkaç
kısayol daha:

| İşlem | Windows / Linux | macOS |
|---|---|---|
| Çok satırlı imleç (tıklayarak) | `Alt+Tık` | `Option+Tık` |
| Sıradaki eşleşmeyi de seç | `Ctrl+D` | `Cmd+D` |
| Satırı yukarı/aşağı taşı | `Alt+↑` / `Alt+↓` | `Option+↑` / `Option+↓` |
| Satırı kopyala | `Shift+Alt+↓` | `Shift+Option+↓` |
| Satırı yorum yap/aç | `Ctrl+/` | `Cmd+/` |
| Dosyada sembol arama | `Ctrl+Shift+O` | `Cmd+Shift+O` |
| Tanıma git | `F12` | `F12` |

Çok satırlı imleç kısayolları (`Alt+Tık` ve `Ctrl+D`) tabloda tek satırla
anlaşılmıyor, biraz açalım. `Ctrl+D`'nin somut kullanımı: bir kelimeyi seç,
`Ctrl+D`'ye arka arkaya bas — kelimenin dosyadaki sonraki geçtiği yerler de
imleçle işaretlenir ve hepsini aynı anda düzenleyebilirsin. Bir değişken adını
dosya içinde topluca değiştirmenin en hızlı yolu budur. `Alt+Tık` ise farklı
bir şey yapar: istediğin yerlere elle, tek tek imleç eklemeni sağlar — kelime
eşleşmesi aramaz, tıkladığın her nokta yeni bir imleç olur.

## Kısayolları öğrenme stratejisi

Bu tabloyu ezberlemeye çalışma. Komut paletinde bir komutu bulduğunda, yanında
varsa kısayolu da gösterilir — zamanla, sık kullandığın komutların kısayolunu
fark etmeden öğrenirsin. Öğrenmenin en verimli yolu kullanmaktır, ezberlemek
değil.

## Ayarları senkronlama (Settings Sync)

Yeni bir bilgisayara geçtiğinde ayarlarını, kısayollarını ve eklenti listeni
sıfırdan kurmak istemezsin. Komut paleti: `Settings Sync: Turn On` — bir
hesaba (GitHub ya da Microsoft) bağlanarak ayarlarını bulutta saklar, başka bir
bilgisayarda aynı komutla geri getirirsin.

## Projeye önerilen eklentiler: extensions.json

Bir ekip projesinde herkesin aynı eklentilere sahip olması işe yarar (örn. aynı
linter, aynı formatter). `.vscode/extensions.json` dosyası, projeyi açan birine
"bu eklentileri kurman önerilir" bildirimi gösterir:

```json
{
  "recommendations": ["ms-python.python"]
}
```

Bu dosya, [önceki sayfada](../00-temeller/02-python-eklentisi-ve-yorumlayici.md)
gördüğün `.vscode/settings.json` gibi genelde commit'lenir — takımın ortak
tercihini paylaşmanın yolu.

## Sık yapılan hatalar

| Hata | Sebebi | Çözüm |
|---|---|---|
| VS Code açılışı yavaşladı | Çok fazla, kullanılmayan eklenti birikmiş | Eklentiler panelinden kullanmadıklarını kaldır |
| Kurduğum eklenti çalışmıyor, güncellenmiyor | Eklenti bakımsız kalmış | Eklenti sayfasında son güncelleme tarihine bak, alternatif ara |
| Format On Save kodu beklemediğim şekilde değiştiriyor | Yanlış formatter seçili ya da ayarlar çakışıyor | Hangi formatter'ın aktif olduğunu kontrol et, ayarları çalışma alanına göre düzenle |
| `extensions.json`'daki öneriler kurulmuyor | Bu dosya sadece **önerir**, otomatik kurmaz | Bildirimdeki "Install" düğmesine tıkla |

## Kendin dene

1. Eklentiler panelini aç (`Ctrl+Shift+X` / `Cmd+Shift+X`).
2. Aklına gelen bir konuda (örn. "csv" ya da "markdown") arama yap, çıkan
   sonuçlardan birini seç.
3. O eklentinin sayfasında şunlara bak: son güncelleme ne zaman, kaç kurulum
   var, yayıncı kim.
4. Bu bilgilere bakarak, bu eklentiyi kurar mıydın kurmaz mıydın karar ver —
   kararını gerekçesiyle birlikte kendine yaz. Amaç eklentiyi kurmak değil,
   değerlendirme alışkanlığını pratik etmek.

## VS Code bölümünde ne öğrendin

5 sayfalık bir yolculuğun sonuna geldin:

- Kurulum, arayüzün beş bölgesi, komut paleti stratejisi
  ([01](../00-temeller/01-kurulum-ve-arayuz.md))
- Python eklentisi, yorumlayıcı seçimi, terminal/editör ayrımı
  ([02](../00-temeller/02-python-eklentisi-ve-yorumlayici.md))
- Entegre terminal ve Git arayüzü, arayüzün gizlediği komutlar
  ([03](../00-temeller/03-terminal-ve-git-arayuzu.md))
- Notebook çalıştırma, çekirdek/yorumlayıcı ayrımı ([01](01-notebook-calistirmak.md))
- Eklenti değerlendirme kriterleri, kısayollar (bu sayfa)

VS Code artık tanıdık bir araç. Sırada [Notebook ve Colab](../../notebook-ve-colab/README.md)
var — buradan öğrendiğin çekirdek/yorumlayıcı ayrımı, notebook dünyasının geri
kalanını anlamanı kolaylaştıracak.

## Sonraki adım

→ [Notebook ve Colab](../../notebook-ve-colab/README.md)

---

<sub>Bu sayfada hata mı buldun? [Issue aç](https://github.com/Enes-CE/turkish-ai-handbook/issues/new/choose).</sub>
