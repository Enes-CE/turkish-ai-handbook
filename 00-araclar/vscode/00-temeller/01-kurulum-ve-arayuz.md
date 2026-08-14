---
seviye: giriş
on-kosul: yok
tip: arayuz
son-guncelleme: 2026-08-14
dogrulandigi-surum: VS Code — arayüz hızlı değişebilir, bkz. BAKIM.md § 1
---

# Kurulum ve arayüz

> **Bu sayfa şunu çözer:** VS Code'u kurar, arayüzün beş ana bölgesini ve komut
> paletini tanırsın — bundan sonraki her sayfa buradan devam eder.
> **Ön koşul:** yok · **Süre:** ~15 dakika

---

## VS Code nedir, neden bu kadar yaygın

VS Code (Visual Studio Code), Microsoft'un ücretsiz, hafif kod editörü.
Python/veri işlerinde fiili standart hâline gelmesinin sebepleri:

- Hafif — büyük bir IDE gibi açılışta dakikalar sürmez
- Eklentilerle genişler — ihtiyacın olan dili/aracı eklenti olarak eklersin,
  gerekmeyeni yüklemezsin
- Ücretsiz ve açık kaynaklı

Alternatifler de var: Jupyter (notebook tabanlı çalışma için, ayrı bir bölümde ele
alınıyor), PyCharm (Python'a özel, daha ağır ama daha "her şey dahil" bir IDE). Bu
depo VS Code'u temel alıyor çünkü hem hafif hem esnek; kavramların çoğu editörler
arası taşınır.

## Kurulum

code.visualstudio.com adresinden işletim sistemine uygun sürümü indir.

- **Windows:** Kurulum sırasında "Add to PATH" ve "Add 'Open with Code' action"
  kutularını işaretlemeni öneririz — ilki terminalden `code` komutunu
  çalıştırabilmeni sağlar (birazdan göreceksin), ikincisi bir klasöre sağ
  tıklayıp doğrudan VS Code'da açmanı.
- **macOS:** İndirilen `.zip`'i aç, `Visual Studio Code.app`'i Uygulamalar
  klasörüne taşı. Windows'un aksine, `code .` komutunun terminalde çalışması
  için ek bir adım gerekir: VS Code'u aç, komut paletinden
  `Shell Command: Install 'code' command in PATH` çalıştır. Windows'ta bu işi
  kurulumdaki PATH kutusu otomatik hallediyor, macOS'ta elle yapılır.
- **Linux:** Dağıtımına uygun paket (`.deb`, `.rpm`) ya da paket yöneticisi
  üzerinden kur.

## Arayüzün beş ana bölgesi

```
┌────────┬─────────────┬───────────────────┐
│ Kenar  │ Yan panel   │ Editör alanı      │
│ çubuğu │ (dosyalar,  │                   │
│        │ arama, Git, │ (açtığın dosyalar │
│        │ ...)        │ burada görünür)   │
├────────┴─────────────┴───────────────────┤
│    Panel (terminal, sorunlar, çıktı)     │
├──────────────────────────────────────────┤
│               Durum çubuğu               │
└──────────────────────────────────────────┘
```

- **Kenar çubuğu (activity bar)** — en soldaki dar şerit. Yan panelde ne
  göründüğünü seçer: dosyalar, arama, Git, eklentiler.
- **Yan panel** — kenar çubuğunda seçtiğin şeyin detayı. Genelde dosya ağacı
  burada durur.
- **Editör alanı** — ortadaki büyük bölge, açtığın dosyaların göründüğü yer.
- **Panel** — alttaki bölge; terminal, sorunlar listesi, çıktı sekmeleri burada.
- **Durum çubuğu** — en alttaki ince şerit; aktif Python yorumlayıcısı,
  satır/sütun numarası gibi bilgiler burada görünür.

## Komut paleti: sayfanın merkezi

`Ctrl+Shift+P` (Windows/Linux) ya da `Cmd+Shift+P` (macOS) — VS Code'da neredeyse
her işlem buradan yapılabilir. Menülerde tıklama yolu aramak yerine, ne yapmak
istediğini yazarsın:

- `Python: Select Interpreter` — hangi Python'un kullanılacağını seçer (bir
  sonraki sayfanın konusu)
- `Preferences: Open Settings (JSON)` — ayarlar dosyasını doğrudan açar
- `View: Toggle Terminal` — terminali açıp kapatır

Bu depoda menü tıklama yolu yerine mümkün olduğunca komut paleti komut adı
vereceğiz — menüler arayüz güncellemeleriyle değişir, komut paleti komutları
yıllardır aynı kalıyor.

## Klasör açmak ve çalışma alanı

VS Code tek bir dosya değil, **klasör** açar — açtığın klasöre "çalışma alanı"
(workspace) denir. Bu önemli çünkü
[terminal bölümünde öğrendiğin çalışma dizini kavramıyla](../../terminal/00-temeller/02-dosya-sistemi-ve-yol.md)
doğrudan bağlantılı: VS Code'un içindeki terminal, o an açık olan çalışma
alanının klasöründe başlar; göreli yollar bu klasöre göre çözülür.

Klasör açmak için komut paleti: `File: Open Folder`.

## code . : terminalden VS Code açmak

Kurulumda "Add to PATH" işaretlediysen, terminalde bulunduğun klasörü doğrudan
VS Code'da açabilirsin:

```bash
code .
```

`.` bulunduğun klasörü temsil eder
([Dosya sistemi ve yol kavramı](../../terminal/00-temeller/02-dosya-sistemi-ve-yol.md)
sayfasından hatırlarsın). Bu, Gezgin'den klasör tıklayıp VS Code'u açmaktan çok
daha hızlı — terminal ile editör arasındaki köprü budur.

## Ayarlar: kullanıcı vs çalışma alanı

İki katman:

- **Kullanıcı ayarları** — bilgisayarındaki tüm projelerde geçerli, genel
  tercihlerin (yazı tipi boyutu, tema gibi).
- **Çalışma alanı ayarları** — sadece o an açık olan klasöre özel; projeye özgü
  ayarlar (örn. hangi Python yorumlayıcısının kullanılacağı) burada durur ve
  `.vscode/settings.json` dosyasında saklanır.

Komut paleti: `Preferences: Open User Settings (JSON)` ya da
`Preferences: Open Workspace Settings (JSON)`.

## Temel kısayollar

| İşlem | Windows / Linux | macOS |
|---|---|---|
| Komut paleti | `Ctrl+Shift+P` | `Cmd+Shift+P` |
| Dosya arama (hızlı aç) | `Ctrl+P` | `Cmd+P` |
| Terminal açma/kapatma | `` Ctrl+` `` | `` Cmd+` `` |
| Dosya içinde arama | `Ctrl+F` | `Cmd+F` |
| Projede arama | `Ctrl+Shift+F` | `Cmd+Shift+F` |

`Ctrl+P` ile dosya arama, dosya ağacında tıklayarak gezinmekten çok daha
hızlıdır — dosya adının birkaç harfini yaz, listeden seç.

## Sık yapılan hatalar

| Hata | Sebebi | Çözüm |
|---|---|---|
| `code .` çalışmıyor: `command not found` | Windows'ta kurulumda "Add to PATH" işaretlenmedi; macOS'ta `Shell Command: Install 'code' command in PATH` hiç çalıştırılmadı | Windows'ta kurulum dosyasını tekrar çalıştırıp PATH kutusunu işaretle (kaldırmaya gerek yok); macOS'ta komut paletinden yukarıdaki komutu çalıştır. İkisinde de **açık terminali kapatıp yeni bir tane aç** — PATH değişikliği zaten [açık bir terminalde geçerli olmuyordu](../../terminal/01-gunluk-kullanim/03-ortam-degiskenleri-ve-path.md) |
| Terminaldeki `pwd` ile beklediğim klasör eşleşmiyor | Yanlış klasör "çalışma alanı" olarak açılmış | `File: Open Folder` ile doğru klasörü aç |
| Ayarı değiştirdim ama başka projede kaybolmuş | Çalışma alanı ayarı yazılmış, kullanıcı ayarı değil | Genel tercihleri kullanıcı ayarlarına yaz |
| Komut paletinde aradığım komut çıkmıyor | Komut, kurulu olmayan bir eklentiye ait | İlgili eklentinin kurulu olduğunu doğrula |

## Kendin dene

1. Terminalde boş bir klasör oluştur: `mkdir vscode-deneme && cd vscode-deneme`.
2. `code .` çalıştır — VS Code'un bu klasörü çalışma alanı olarak açtığını gör.
3. `Ctrl+Shift+P` ile komut paletini aç, `View: Toggle Terminal` yaz ve
   çalıştır — VS Code içinde bir terminal açılır.
4. Açılan terminalde `pwd` çalıştır — çıktının, 1. adımda oluşturduğun klasörle
   aynı olduğunu doğrula. Bu, "çalışma alanı = terminalin başladığı yer"
   ilişkisinin kanıtı.

## Sonraki adım

→ [Python eklentisi ve yorumlayıcı seçimi](02-python-eklentisi-ve-yorumlayici.md)

---

<sub>Bu sayfada hata mı buldun? [Issue aç](https://github.com/Enes-CE/turkish-ai-handbook/issues/new/choose).</sub>
