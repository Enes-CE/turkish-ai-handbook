---
seviye: giriş
on-kosul: [python-ortamlari/00-temeller/01-python-kurulumu.md]
tip: kavram
son-guncelleme: 2026-08-15
dogrulandigi-surum: kavramsal — sürümden bağımsız
---

# Jupyter nedir, hücre mantığı

> **Bu sayfa şunu çözer:** Notebook'un ne olduğunu, hücre ve çekirdek
> kavramlarını ve neden veri/AI işlerinde bu kadar yaygın olduğunu anlarsın.
> VS Code'da nasıl çalıştırıldığı ya da Colab'a özgü detaylar burada değil —
> sırasıyla ilgili sayfalarda.
> **Ön koşul:** [Python kurulumu](../../python-ortamlari/00-temeller/01-python-kurulumu.md) ·
> **Süre:** ~10 dakika

---

## Notebook nedir

Bir notebook (`.ipynb` dosyası), kod, kodun çıktısı ve açıklama metninin
**aynı belgede** yaşadığı bir çalışma biçimi. Bir `.py` betik dosyasında sadece
kod vardır, çalıştırdığında sonucu terminale basar ve kaybolur. Notebook'ta her
parça (hücre) ayrı çalıştırılır, çıktısı (sayı, tablo, grafik) tam o hücrenin
altında kalıcı olarak durur.

## Neden veri/AI işlerinde bu kadar yaygın

Veri işleriyle uğraşırken çalışma biçimi genelde **keşifsel**dir: veriye
bakarsın, bir şey denersin, sonucu (bir grafiği, bir tabloyu) görürsün, ona
göre sonraki adıma karar verirsin. Bir betik dosyasında bu döngü yavaştır — her
denemede dosyanın tamamını baştan çalıştırman, üstelik verinin yeniden
yüklenmesini beklemen gerekir. Notebook'ta tek bir hücreyi çalıştırıp sonucu
görür, hemen yanındaki hücrede bir sonraki denemeyi yaparsın — veri zaten
bellekte, yeniden yüklemene gerek yok.

## Hücre kavramı

İki tip hücre var:

- **Kod hücresi** — Python kodu içerir, çalıştırıldığında sonuç hemen altında
  görünür.
- **Markdown hücresi** — açıklama metni içerir (başlık, madde listesi,
  formül), çalıştırıldığında biçimlendirilmiş metin olarak görünür.

Bir kod hücresi çalıştırıldığında, içindeki kod arkada çalışan Python sürecine
gönderilir, sonuç geri gelip hücrenin altına yazılır.

## Çekirdek (kernel) nedir

Notebook'un arkasında sürekli çalışan bir Python süreci — **çekirdek**. Her
hücreyi çalıştırdığında kod bu sürece gönderilir, orada işlenir, sonuç geri
döner. Notebook arayüzü sadece bir pencere; asıl iş çekirdekte olur.

Çekirdeği yeniden başlattığında (restart), o ana kadar tanımladığın **her
şey** — değişkenler, yüklenmiş veriler, import edilmiş kütüphaneler —
kaybolur. Hücreler ekranda dursa da, çekirdek onları hiç görmemiş gibi baştan
başlar.

## Durum (state): hem güç hem tuzak

Çekirdek, çalıştırdığın hücrelerin bıraktığı değişkenleri bellekte tutar —
buna **durum (state)** denir. Bir hücrede `df = pd.read_csv(...)` çalıştırırsan,
sonraki herhangi bir hücrede `df`'i doğrudan kullanabilirsin; yeniden
yüklemene gerek yok. Bu, notebook'u hızlı yapan şey.

Ama aynı özellik bir tuzak da kurar:

```
Hücre [1]  df = pd.read_csv(...)   ──►  Çekirdek  ──►  df bellekte durur
Hücre [2]  df = df.dropna()        ──►  Çekirdek  ──►  df güncellenir (bellekte)
Hücre [3]  df.describe()           ──►  Çekirdek  ──►  bellekteki df'e göre sonuç

Arayüz (gördüğün ekran) ◄── sonuç ──── Çekirdek ◄── değişkenler burada yaşar
```

Bellekteki `df`, ekranda gördüğün hücre sırasına değil, **hangi hücreleri
hangi sırayla çalıştırdığına** bağlıdır.

## Hücre numaraları [1], [2] ne demek

Bir hücreyi çalıştırdığında solunda `[1]`, `[2]` gibi bir numara belirir. Bu
numara hücrenin ekrandaki **sırasını değil**, kaçıncı **çalıştırma** olduğunu
gösterir. Üçüncü hücreyi çalıştırıp sonra birinci hücreye dönüp tekrar
çalıştırırsan, birinci hücre `[4]` olur — ekranda hâlâ en üstte dursa da,
çekirdeğe en son giden odur.

Bu ayrım kritik: ekranda yukarıdan aşağı okunabilir görünen bir notebook,
aslında bambaşka bir sırayla çalıştırılmış olabilir. Bunun yol açtığı
tuzakları ve önlemesini [Notebook'ta iyi pratikler](02-notebook-iyi-pratikler.md)
sayfasında göreceksin.

## Notebook ne zaman kullanılmaz

Notebook keşif için iyidir, her şey için değil:

- **Üretime giden kod** — bir web servisi, bir otomasyon script'i notebook
  olarak çalıştırılmaz.
- **Tekrar kullanılacak fonksiyonlar** — bir fonksiyonu birden fazla yerde
  kullanacaksan, bir `.py` modülüne taşınmalı.
- **Uzun süreli eğitim işleri** — saatlerce sürecek bir model eğitimi,
  [SSH ile bağlanıp](../../terminal/02-ileri/01-ssh-ile-uzak-baglanti.md)
  `nohup`/`tmux` ile arka planda çalıştırılan bir `.py` script'i olarak daha
  güvenlidir.

Genel akış: notebook'ta keşfet, işe yarayan kısmı `.py` dosyasına taşı.

## .ipynb dosyasının içi JSON

Bir `.ipynb` dosyası aslında bir JSON dosyasıdır — hücreler, çıktılar, hatta
grafiklerin görüntüleri bile bu JSON'un içine gömülür. Bu, Git'le çalışırken
sorun çıkarır: `git diff` çıktısı okunaksız hâle gelir, iki kişinin aynı
notebook'u değiştirmesi neredeyse her zaman çakışmayla sonuçlanır. Detayı ve
çözüm önerilerini
[Notebook'larla çalışmak](../../git-github/01-gunluk-kullanim/06-notebook-ile-git.md)
sayfasında bulabilirsin.

## Aynı çekirdek, farklı arayüzler

Jupyter Notebook, JupyterLab, VS Code'un notebook desteği
([VS Code'da nasıl çalıştırıldığını](../../vscode/01-gunluk-kullanim/01-notebook-calistirmak.md)
zaten gördün) ve Google Colab — hepsi aynı çekirdek mantığı üzerine kurulu,
farklı arayüzler. Hangisini seçeceğin sonraki sayfaların konusu.

## Sık yapılan hatalar

| Yanılgı | Sebebi | Doğrusu |
|---|---|---|
| "Hücreleri yukarıdan aşağı okuyorum, demek ki öyle çalıştı" | Çalıştırma sırası, ekrandaki sıra değil, hücre numaralarıyla belirlenir | Hücre numaralarına (`[1]`, `[2]`) bak, ekran sırasına değil |
| "Değişkenim kayboldu, notebook bozuldu" sanmak | Çekirdek yeniden başlatılmış (restart), durum sıfırlanmış | Değişkeni oluşturan hücreyi tekrar çalıştır |
| Notebook'u yeniden açınca grafikler/tablolar hâlâ görünüyor, değişkenlerin de bellekte olduğunu sanmak | Çıktı (grafik, tablo, sayı) `.ipynb` dosyasının içinde kayıtlıdır, değişkenin kendisi değil — çekirdek kapanınca bellek gider, dosyadaki çıktı kalır | Bir hücrede o değişkeni kullanmak istersen önce hücreleri baştan çalıştırman gerekir; ekranda gördüğün çıktı, çalışır durumda bir çekirdeğin kanıtı değildir |
| Fonksiyonu birden fazla notebook'ta kopyala-yapıştır yapmak | Notebook paylaşılan kod için uygun yer değil | Fonksiyonu bir `.py` dosyasına taşı, oradan import et |

## Kafanda kalması gerekenler

- Notebook = kod + çıktı + açıklama metni aynı belgede
- Çekirdek, arkada çalışan Python süreci; hücreler oraya gönderilir
- Durum (state) bellekte tutulur — hızlı ama sıra bağımlı
- Hücre numarası = çalıştırma sırası, ekran sırası değil
- Keşif için notebook, kalıcı/tekrar kullanılan kod için `.py`

## Sonraki adım

→ [Notebook'ta iyi pratikler](02-notebook-iyi-pratikler.md)

---

<sub>Bu sayfada hata mı buldun? [Issue aç](https://github.com/Enes-CE/turkish-ai-handbook/issues/new/choose).</sub>
