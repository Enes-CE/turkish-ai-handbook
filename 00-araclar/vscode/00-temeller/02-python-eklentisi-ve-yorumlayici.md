---
seviye: giriş
on-kosul: [python-ortamlari/00-temeller/04-venv-kullanimi.md]
tip: arayuz
son-guncelleme: 2026-08-14
dogrulandigi-surum: VS Code Python eklentisi — arayüz hızlı değişebilir, bkz. BAKIM.md § 1
---

# Python eklentisi ve yorumlayıcı seçimi

> **Bu sayfa şunu çözer:** "Terminalde çalışıyor ama VS Code'da çalışmıyor"
> şikâyetinin cevabını — VS Code'un hangi Python'u kullandığını nasıl seçtiğini
> ve editörle terminalin neden farklı Python'lara bağlanabildiğini öğrenirsin.
> **Ön koşul:** [venv ile ortam oluşturma](../../python-ortamlari/00-temeller/04-venv-kullanimi.md) ·
> **Süre:** ~15 dakika

---

## Python eklentisi

VS Code kendisi Python bilmez — Python desteği bir eklenti olarak gelir. Eklenti
şunları getirir:

- Söz dizimi vurgusu (syntax highlighting)
- Otomatik tamamlama
- Hata işaretleme (kod çalıştırmadan önce kırmızı çizgilerle)
- Kod çalıştırma
- Notebook desteği (Jupyter dosyaları için)

Kurulum: komut paletinden `Extensions: Install Extensions` yaz, açılan panelde
"Python" ara, Microsoft'un resmi eklentisini kur. Ya da kenar çubuğundaki
eklentiler simgesinden aynı panele ulaşabilirsin.

## Yorumlayıcı (interpreter) kavramı

[Python Ortamları](../../python-ortamlari/README.md) bölümünde "hangi Python
çalışıyor" sorusunu terminalde `which python` ile cevaplamayı öğrenmiştin. VS
Code için de aynı soru geçerli — editör, kodunu çalıştırırken ve hata kontrolü
yaparken **hangi Python'u** kullanacağını bilmek zorunda. Bu seçime "yorumlayıcı"
(interpreter) denir.

## Yorumlayıcı seçimi

Komut paleti: `Python: Select Interpreter`.

Açılan listede sistemindeki Python kurulumları ve varsa proje klasöründeki sanal
ortamlar görünür. [venv ile ortam oluşturma](../../python-ortamlari/00-temeller/04-venv-kullanimi.md)
sayfasında kurduğun `venv/` klasörü, VS Code tarafından genelde otomatik tanınır
ve listede önerilen olarak işaretlenir.

Seçtikten sonra, durum çubuğunda ([önceki sayfada](01-kurulum-ve-arayuz.md)
gördüğün en alttaki şeritte) seçili yorumlayıcının adı görünür — kontrol etmenin
en hızlı yolu budur.

## Terminal ve editör ayrı Python'lar kullanabilir

> ⚠️ **Bu sayfanın en kritik konusu.** Terminalde bir sanal ortamı
> aktifleştirmen, VS Code'un otomatik olarak o ortamı yorumlayıcı olarak
> seçmesi anlamına gelmez — ikisi ayrı sistemlerdir.

```
Proje klasörü
  │
  ├── Terminal (senin açtığın, aktifleştirdiğin)
  │     which python → venv/bin/python        (aktif ortam)
  │
  └── VS Code editörü
        Python: Select Interpreter → sistem Python'u   (farklı seçim!)

Sonuç: terminalde "python egitim.py" çalışır,
       editörde kod altında kırmızı çizgi: "import bulunamadı"
```

Bu yüzden "terminalde çalışıyor ama editör kırmızı çiziyor" (ya da tam tersi)
durumuyla sık karşılaşırsın. Çözüm her zaman aynı: `Python: Select Interpreter`
ile ikisini aynı ortama işaret ettir.

Bu, [Ortam sorunlarını çözmek](../../python-ortamlari/01-gunluk-kullanim/03-ortam-sorunlarini-cozmek.md)
sayfasında gördüğün "yanlış yorumlayıcı seçimi" başlığının tam karşılığı — orada
kısaca değinmiştik, burada detayını görüyorsun.

## VS Code venv'i bulamazsa

Proje kökünde `venv/` ya da `.venv/` varsa genelde otomatik önerilir. Önermezse,
`Python: Select Interpreter` listesinin altındaki `Enter interpreter path...`
seçeneğiyle yolu elle girebilirsin — Windows'ta `venv\Scripts\python.exe`,
macOS/Linux'ta `venv/bin/python`.

## Entegre terminalin otomatik aktifleştirmesi

VS Code, seçtiğin yorumlayıcı bir sanal ortamsa, içindeki terminalde yeni bir
sekme açtığında o ortamı otomatik aktifleştirmeye çalışır — `(venv)` işaretini
görürsün. Bu her zaman güvenilir çalışmaz (kabuk ayarları, eklenti sürümü gibi
sebeplerle bazen atlanır). Şüpheye düştüğünde önceki bölümlerde öğrendiğin kesin
yöntemi kullan:

```bash
which python
```

## Çalışma alanı ayarına yazılması

Seçtiğin yorumlayıcı, [önceki sayfada](01-kurulum-ve-arayuz.md) gördüğün çalışma
alanı ayarlarına, `.vscode/settings.json` dosyasına yazılır — projeye özeldir,
başka bir projede geçerli olmaz.

`.vscode/settings.json` genelde **commit'lenir** — takımın ortak ayarlarını
(formatter seçimi, satır uzunluğu, dosya kaydetme davranışı gibi) paylaşmanın
yolu budur; `venv/` klasörünün kendisiyle karıştırma, o ayrı bir konu.

Asıl sorun, içine **mutlak** bir yorumlayıcı yolu yazılmasıdır (`C:\Users\adin\...`
gibi) — bu, başka kimsenin bilgisayarında çalışmaz. Modern VS Code genelde göreli
bir yol yazar (`${workspaceFolder}/venv/bin/python` gibi), bu taşınabilirdir ve
sorun çıkarmaz. Pratik kural: dosyayı commit'le, ama içindeki yorumlayıcı yolunun
mutlak olup olmadığını kontrol et; mutlaksa ya göreliye çevir ya da o satırı çıkar.

## Kod çalıştırma yolları

İki temel yol:

- Editördeki ▷ (çalıştır) düğmesi — seçili yorumlayıcıyla dosyayı çalıştırır,
  çıktı entegre terminalde açılan yeni bir sekmede görünür.
- Terminalden doğrudan `python dosya.py` — hangi Python'un çalıştığı, o
  terminaldeki aktif ortama bağlıdır, VS Code'un seçtiği yorumlayıcıya değil.

İkisi farklı yorumlayıcılara bağlıysa, aynı dosya iki farklı sonuç verebilir —
bir önceki uyarının pratikteki karşılığı.

## Linter ve formatter

Kod yazarken stil hatalarını (linter) ve otomatik biçimlendirmeyi (formatter) da
eklentiler üstlenir — ayrıntısı
[Faydalı eklentiler ve kısayollar](../01-gunluk-kullanim/02-eklentiler-ve-kisayollar.md)
sayfasında.

## Sık yapılan hatalar

| Hata | Sebebi | Çözüm |
|---|---|---|
| Terminalde çalışıyor, editör "import bulunamadı" diyor | Editör farklı bir yorumlayıcı seçmiş | `Python: Select Interpreter` ile terminaldeki ortamı seç |
| `venv/` listede görünmüyor | VS Code henüz taramadı ya da ortam proje kökünde değil | `Enter interpreter path...` ile elle gir |
| Entegre terminal ortamı otomatik aktifleştirmiyor | Otomatik aktifleştirme her zaman güvenilir değil | `which python` ile kontrol et, gerekirse elle aktifleştir |
| Yorumlayıcı seçimim başka projede kayboldu | Seçim çalışma alanına özel, kullanıcı ayarına değil | Her projede ayrı seçim normaldir, tekrar seç |

## Kendin dene

1. [venv ile ortam oluşturma](../../python-ortamlari/00-temeller/04-venv-kullanimi.md)
   sayfasındaki gibi bir proje klasöründe `venv` kur, aktifleştir.
2. `code .` ile klasörü VS Code'da aç.
3. `Ctrl+Shift+P` ile komut paletini aç, `Python: Select Interpreter` yaz,
   listede `venv/`'i seç (önerilmiyorsa `Enter interpreter path...` ile elle gir).
4. Durum çubuğunda seçtiğin yorumlayıcının adının göründüğünü doğrula.
5. VS Code içinde `` Ctrl+` `` ile yeni bir terminal aç, `which python`
   çalıştır — çıktının, seçtiğin `venv/` klasörünü gösterdiğini doğrula. İkisi
   eşleşiyorsa, terminal ve editör artık aynı Python'a bakıyor demektir.

## Sonraki adım

→ [Entegre terminal ve Git arayüzü](03-terminal-ve-git-arayuzu.md)

---

<sub>Bu sayfada hata mı buldun? [Issue aç](https://github.com/Enes-CE/turkish-ai-handbook/issues/new/choose).</sub>
