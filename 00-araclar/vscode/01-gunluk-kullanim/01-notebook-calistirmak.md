---
seviye: orta
on-kosul: [notebook-ve-colab/00-temeller/01-jupyter-nedir.md]
tip: arayuz
son-guncelleme: 2026-08-14
dogrulandigi-surum: VS Code Jupyter desteği — arayüz hızlı değişebilir, bkz. BAKIM.md § 1
---

# Notebook'ları VS Code'da çalıştırmak

> **Bu sayfa şunu çözer:** Notebook'un ne olduğunu ve hücre mantığını
> biliyorsun — burada VS Code içinde bir notebook'u açıp çalıştırmayı, en
> kritik olarak da çekirdek seçiminin yorumlayıcı seçiminden **ayrı** olduğunu
> öğreniyorsun.
> **Ön koşul:** [Jupyter nedir, hücre mantığı](../../notebook-ve-colab/00-temeller/01-jupyter-nedir.md) ·
> **Süre:** ~15 dakika

---

## .ipynb dosyasını açmak

Bir `.ipynb` dosyasına çift tıklamak yeterli — Python eklentisi ve içindeki
Jupyter desteği notebook arayüzünü otomatik açar. Hücre yapısı, çalıştırma
sırası gibi kavramlar
[Jupyter nedir, hücre mantığı](../../notebook-ve-colab/00-temeller/01-jupyter-nedir.md)
sayfasının konusu — burada onu bildiğini varsayıyoruz, VS Code'daki kullanımına
odaklanıyoruz.

## Çekirdek (kernel) seçimi: yorumlayıcıdan AYRI bir seçim

Önceki bölümde
[yorumlayıcı seçmeyi](../00-temeller/02-python-eklentisi-ve-yorumlayici.md)
öğrenmiştin — VS Code'a `.py` dosyaları için hangi Python'u kullanacağını
söylemek. Notebook'larda ayrıca bir **çekirdek (kernel)** seçimi var, sağ üstte
görünür. Bu ikisi görünüşte aynı işi yapar (hangi Python) ama **ayrı
ayarlardır**: yorumlayıcı seçili olması, aynı ortamın çekirdek olarak da
seçildiği anlamına gelmez.

```
Proje klasörü
  │
  ├── .py dosyası çalıştırma
  │     Python: Select Interpreter → venv           (yorumlayıcı)
  │
  └── .ipynb dosyası çalıştırma
        Sağ üstteki çekirdek seçici → sistem Python  (farklı seçim!)

Sonuç: aynı projede .py dosyaları venv'i kullanır,
       notebook hücreleri sistem Python'unu kullanır — iki farklı ortam
```

Bu yüzden bir notebook hücresinde `ModuleNotFoundError` alıp "ama ben bu paketi
kurdum" diye şaşırabilirsin — muhtemelen kurduğun yer ile çekirdeğin baktığı yer
farklı. Çözüm: sağ üstteki çekirdek seçiciye tıkla, aynı `venv/`'i seç.

## Sanal ortamın çekirdek olarak görünmesi

venv'in çekirdek listesinde çıkması için o ortamda `ipykernel` paketinin kurulu
olması gerekebilir. VS Code, kurulu değilse genelde bunu fark edip "ipykernel'i
kurmak ister misin" diye sorar — evet dersen otomatik kurar.

## Hücre çalıştırma kısayolları

| İşlem | Windows / Linux | macOS |
|---|---|---|
| Çalıştır, sonraki hücreye geç | `Shift+Enter` | `Shift+Enter` |
| Çalıştır, aynı hücrede kal | `Ctrl+Enter` | `Ctrl+Enter` |

## Hücre ekleme, silme, tip değiştirme

- Yeni kod hücresi: hücrenin altındaki `+ Code`
- Yeni markdown hücresi: `+ Markdown`
- Silme: hücrenin solundaki çöp kutusu simgesi ya da komut modunda `D` `D`
  (iki kez, Jupyter'in standart kısayolu). `Delete` tuşu hücreyi değil,
  hücrenin içeriğini siler
- Kod ↔ markdown dönüştürme: hücreyi seçip `M` (markdown'a çevir) ya da `Y`
  (koda çevir) — önce hücrenin solundaki boşluğa tıklayarak komut moduna geç

## Değişken gezgini ve veri görüntüleyici

Bir hücre çalıştıktan sonra üstteki araç çubuğunda "Variables" düğmesi belirir —
o an bellekte hangi değişkenlerin olduğunu, tipini, değerini listeler. Bir
`DataFrame` değişkenine tıklarsan, ayrı bir sekmede **tablo görünümünde**,
sayfalanabilir ve sıralanabilir şekilde açılır. Bu, VS Code'un Colab'a göre
güçlü olduğu bir nokta — Colab'da aynı işi görmek için genelde `df.head()`
yazman gerekir.

## .py ile notebook arası dönüşüm

`# %%` işaretleriyle bölünmüş normal bir `.py` dosyası, VS Code'da neredeyse bir
notebook gibi çalışır — her `# %%` bir hücre sınırı sayılır, üstünde
"Run Cell" bağlantısı belirir. Tersi de mümkün: bir notebook'u `.py` olarak
dışa aktarabilirsin (komut paleti: `Jupyter: Export to Python Script`).

Bu, Git'le çalışırken önemli — `.ipynb` dosyaları JSON formatında olduğu için
`git diff` çıktısı okunaksızdır, `.py` dosyaları ise normal metin gibi
diff'lenir. Detayı
[Notebook'larla çalışmak](../../git-github/01-gunluk-kullanim/06-notebook-ile-git.md)
sayfasında.

## VS Code vs Colab

| | VS Code | Colab |
|---|---|---|
| Çalıştığı yer | Yerel bilgisayarın | Google'ın bulutu |
| GPU | Sadece bilgisayarında varsa | Ücretsiz GPU erişimi |
| Git uyumu | Doğal, entegre | Ayrı adımlar gerekir |
| Paylaşım | Repo/link paylaşımı | Tek tıkla bağlantı paylaşımı |
| Kurulum | Gerekli | Tarayıcı yeterli |

Kısa özet: GPU'ya ihtiyacın varsa ya da hızlıca birine bir şey göstermek
istiyorsan Colab; Git'le düzenli çalıştığın, yerel kaynakların yettiği bir
proje için VS Code. İkisi birbirini dışlamaz — aynı projeyi geliştirmede VS
Code, ağır eğitimde Colab kullanmak yaygın bir kombinasyon.

## Sık yapılan hatalar

| Hata | Sebebi | Çözüm |
|---|---|---|
| Notebook'ta `ModuleNotFoundError`, ama terminalde paket kurulu | Çekirdek, paketin kurulu olduğu ortamdan farklı | Sağ üstteki çekirdek seçiciden doğru `venv/`'i seç |
| venv çekirdek listesinde yok | `ipykernel` o ortamda kurulu değil | VS Code'un önerisini kabul et ya da elle `pip install ipykernel` |
| `.ipynb` dosyasında `git diff` okunmuyor | Notebook dosyası JSON formatında | `.py` olarak dışa aktarıp diff'i orada gör, ya da [Notebook'larla çalışmak](../../git-github/01-gunluk-kullanim/06-notebook-ile-git.md) sayfasındaki yöntemi kullan |
| Hücreleri sırayla çalıştırmadım, sonuçlar tutarsız | Notebook'un çalıştırma sırası tuzağı | Bu, [Jupyter nedir, hücre mantığı](../../notebook-ve-colab/00-temeller/01-jupyter-nedir.md) sayfasının konusu |

## Kendin dene

1. `code .` ile bir klasör aç (venv kurulu bir proje olsun —
   [venv ile ortam oluşturma](../../python-ortamlari/00-temeller/04-venv-kullanimi.md)
   sayfasındaki gibi).
2. Komut paletinden `Jupyter: Create New Jupyter Notebook` yaz, yeni bir
   `.ipynb` dosyası oluştur.
3. Sağ üstteki çekirdek seçiciye tıkla, proje klasöründeki `venv/`'i seç.
4. Bir hücreye `import sys; print(sys.executable)` yaz, çalıştır (`Shift+Enter`).
5. Çıktının, seçtiğin `venv/` klasörünün içindeki Python'u gösterdiğini
   doğrula — bu, çekirdeğin doğru ortama bağlandığının kanıtı.

## Sonraki adım

→ [Faydalı eklentiler ve kısayollar](02-eklentiler-ve-kisayollar.md)

---

<sub>Bu sayfada hata mı buldun? [Issue aç](https://github.com/Enes-CE/turkish-ai-handbook/issues/new/choose).</sub>
