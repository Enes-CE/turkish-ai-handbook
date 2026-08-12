# Bakım Protokolü

Bu dosya içerik değil, **deponun kendisi hakkında**. Amaç: 3 yıl sonra da güvenilir olması.
Bir kaynak deposu içerik üretilmediği için değil, **eskidiği fark edilmediği için** ölür.

Buradaki kurallar **bütün konular için** geçerlidir. Yeni bir konu klasörü açarken ayrıca
[KONU-EKLEME.md](KONU-EKLEME.md), dışarıdan katkı gelirken [KATKIDA-BULUNMA.md](KATKIDA-BULUNMA.md)
okunur.

> **Not:** Bu dosya deponun bakımcıları içindir. Katkı vermek isteyen biri için giriş noktası
> [KATKIDA-BULUNMA.md](KATKIDA-BULUNMA.md)'dir.

---

## 1. Değişeni değişmeyenden ayır

Her sayfa üç kutudan birine girer. Kutu, o sayfanın ne sıklıkla kontrol edileceğini belirler.

| Tip | Örnek | Eskime hızı | Kontrol sıklığı |
|---|---|---|---|
| **Kavram** | Branch nedir, merge vs rebase farkı | Neredeyse hiç | Yılda 1 |
| **Komut** | `git restore`, `git reset` kullanımı | Yavaş (Git sürümleri) | Yılda 2 |
| **Arayüz** | GitHub ekranından PR açma, Actions sekmesi | Hızlı (UI değişir) | Her eğitim dönemi |

**Kural:** Aynı dosyada kavram ile arayüz anlatımını karıştırma. Karıştırırsan, GitHub bir butonun
yerini değiştirdiğinde hiç eskimeyen kavram anlatımını da elden geçirmek zorunda kalırsın.

## 2. Ekran görüntüsü politikası

Ekran görüntüsü en hızlı eskiyen ve güncellemesi en pahalı içerik türü.

- Bir şey **metinle anlatılabiliyorsa ekran görüntüsü koyma.** ("Sağ üstteki *Settings* → *Developer settings*" yeterli.)
- Koyacaksan hepsi `gorseller/` altında dursun ki bir UI değişiminde tek klasöre bakıp bitirebil.
- Dosya adı içeriği anlatsın: `gorseller/github-pr-acma-2026-08.png` — tarihi adına yaz, ne kadar
  eskidiğini açmadan gör.
- Terminal çıktısı için **ekran görüntüsü değil, kod bloğu** kullan. Aranabilir, kopyalanabilir, güncellemesi 5 saniye.

## 3. Her sayfanın künyesi zorunlu

Sayfa başındaki blok olmadan içerik eklenmez:

```markdown
---
seviye: giriş | orta | ileri
on-kosul: [00-temeller/02-kurulum-ve-ilk-ayarlar.md]
tip: kavram | komut | arayuz
son-guncelleme: 2026-08-10
dogrulandigi-surum: git 2.45 / GitHub web arayüzü
---
```

`son-guncelleme` alanı, "bu bilgi hâlâ doğru mu" sorusunun tek cevabı. Boş bırakılan sayfa,
6 ay sonra güvenilmez sayfadır.

## 4. İçerik müfredattan gelir, düzeltme sahadan

Bu deponun **yapısı** topluluk sorularına göre değil, konuların sistematik anlatımına göre
kurulur. İçindekiler listesi baştan bellidir ve sırayla doldurulur; bir konunun yazılması için
kimsenin sorup takılması beklenmez.

Sorular yapıyı değil, **doğruluğu** belirler:

```
Müfredat  →  sayfa yazılır (tahmin edilen hatalar dahil)
                      ↓
        Toplulukta gerçek soru gelir
                      ↓
   Sayfada bu hata var mı?
        ↓ hayır                      ↓ evet ama anlaşılmamış
  "Sık yapılan hatalar"a          Anlatım yeniden yazılır
  eklenir + hata indeksine
```

Sebep: yazan kişi kendi zorlandığı yerleri hatırlar, yeni başlayanın takıldığı yerleri değil.
Tahmin tohum, gelen sorular düzeltme mekanizmasıdır. İkisi çelişmez.

**Hata bilgisi iki yerde durur:**

- Her konu sayfasının kendi içindeki **"Sık yapılan hatalar"** tablosu — asıl yer, konu bağlamıyla birlikte.
- **Her konunun kendi `HATA-INDEKSI.md`'si** — öğretmez, yönlendirir. Çünkü insan hata aldığında
  konuya göre değil, ekrandaki mesaja göre arama yapar. Tek bir dev indeks yerine konu başına
  bir indeks tutulur; aksi halde Python hatası arayan biri Git hatalarının içinde kaybolur.

Yeni bir hata eklenirken **her iki yere de** işlenir; indekste sadece tek satırlık çözüm ve
konu sayfasına link olur.

## 5. Takvim

Dört eğitim dönemin var; bakımı ayrı bir işe dönüştürme, eğitim takvimine bağla.

| Ne zaman | Ne yapılır |
|---|---|
| Her eğitim başlamadan 1 hafta önce | `tip: arayuz` sayfaları hızlıca elden geçirilir |
| Her eğitim bittikten sonra | O dönem biriken sorular SSS'e işlenir |
| Yılda 1 kez (yıl başı) | Tüm komutlar güncel Git sürümünde çalıştırılıp doğrulanır |
| Ayda 1 (otomatik) | Ölü link taraması (GitHub Actions) |

## 6. Sürüm etiketi

Her eğitim dönemi başında `git tag v2026-guz` gibi bir etiket at. Katılımcı "hangi versiyona
bakıyordun" sorusuna net cevap verebilsin, sen de dönem içinde yaptığın değişikliklerin
kimseyi ortada bırakmadığından emin ol.

## 7. Yazım kuralları (tutarlılık için)

- Komutlar her zaman kod bloğunda, başına `$` koyma (kopyalamayı bozuyor).
- Tehlikeli komutların (`reset --hard`, `push --force`) üstüne mutlaka uyarı kutusu.
- Terimlerin Türkçesi ilk geçtiğinde parantez içinde İngilizcesi: dal (branch). Sonra İngilizcesi kullanılır —
  hata mesajları ve dokümanlar İngilizce çünkü.
- Bir sayfa 2-3 ekran boyunu geçiyorsa bölünür. Uzun sayfa okunmaz, güncellenmez.


## 8. Konu bazlı sorumluluk

Depo büyüdükçe her konunun bakım yükü farklılaşır:

| Konu | En hızlı eskiyen kısmı | Dikkat |
|---|---|---|
| Araçlar (Git, Colab, VS Code) | Arayüz ekranları | Her eğitim dönemi kontrol |
| Python | Neredeyse hiç | Yılda 1 yeterli |
| Makine Öğrenmesi | Kütüphane API'leri (sklearn) | Sürüm numarası künyeye yazılır |
| Derin Öğrenme | Framework sürümleri (torch) | Notebook'lar Colab'da çalıştırılıp doğrulanır |
| Generative AI | **Her şey** — model adları, fiyatlar, API'ler | 3 ayda bir; kavramları araç adlarından ayrı yaz |

Generative AI bölümünde özel kural: **model adı ve fiyat yazma zorunda değilsen yazma.**
"Bir dil modeline istem gönderilir" cümlesi eskimiyor; "GPT-4o'ya şu fiyattan istek atılır"
cümlesi altı ayda eskiyor.


## 9. Katkı geldikçe ölçek

Depo tek kişilik olmaktan çıktığında bakım yükü de dağıtılır:

- **Otomatik denetim insanı yormasın.** Künye, isimlendirme ve link kontrolü `tools/kontrol.py`
  ile PR'da otomatik çalışır. İnceleyen kişi bunlara bakmaz; anlatımın kalitesine bakar.
- **Yazılmamış her sayfa bir issue'dur.** Katkı vermek isteyen biri "ne yapabilirim" diye
  sormak zorunda kalmasın; açık issue listesi zaten menüdür.
- **Bir sayfa aynı anda tek kişiye atanır**, 14 gün hareket yoksa atama düşer. Bu kural baştan
  yazılı olduğu için kimse kırılmaz.
- **Bölüm sorumluluğu devredilebilir.** Bir konuya düzenli katkı veren biri çıkarsa
  `.github/CODEOWNERS` dosyasına eklenir ve o klasörün PR'ları ona da düşer.
- **Reddetme gerekçeli olur.** Kabul edilmeyenler listesi KATKIDA-BULUNMA.md'de açıkça yazılı;
  böylece ret kişisel değil, kurala dayalı olur.
