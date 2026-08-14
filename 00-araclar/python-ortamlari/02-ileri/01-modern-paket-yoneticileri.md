---
seviye: ileri
on-kosul: [python-ortamlari/01-gunluk-kullanim/02-requirements-ve-bagimliliklar.md]
tip: komut
son-guncelleme: 2026-08-14
dogrulandigi-surum: kavramsal — araç adları ve sürümleri hızlı değişir, kavramlar kalıcı
---

# Modern paket yöneticileri (uv, poetry)

> **Bu sayfa şunu çözer:** uv, poetry gibi araçların hangi problemi çözdüğünü ve
> sana şu an gerekip gerekmediğini anlarsın — araç kullanmayı değil, karar vermeyi
> öğreniyorsun.
> **Ön koşul:** [requirements.txt ve bağımlılık dondurma](../01-gunluk-kullanim/02-requirements-ve-bagimliliklar.md) ·
> **Süre:** ~15 dakika

---

Bu konu hızlı eskir — araç isimleri ve sürümleri değişebilir. Bu sayfa araçları
değil, **çözdükleri problemi** anlatıyor; o kısım kalıcı.

## Hangi problemleri çözüyorlar

- pip'in yavaşlığı, özellikle büyük bağımlılık ağaçlarında
- Bağımlılık çözümlemesinin belirsizliği — pip, çakışan isteklerin her zaman en
  iyi çözümünü bulamayabilir
- `requirements.txt`'nin doğrudan/dolaylı bağımlılık ayrımını kaybetmesi — bir
  önceki sayfada değindiğimiz `freeze`'in dezavantajı
- Ortam ve paket yönetiminin ayrı araçlarda olması — venv bir şey yapar, pip başka
  bir şey; modern araçlar bunu tek bir komut altında birleştirir

## pyproject.toml nedir

Modern Python projelerinde `requirements.txt` yerine (ya da onunla birlikte)
kullanılan, standart hâline gelen proje tanım dosyası. Farkı: `requirements.txt`
sadece bir paket listesidir; `pyproject.toml` projenin kendisini tanımlar — adı,
sürümü, bağımlılıkları, hangi Python sürümlerini desteklediği hepsi tek dosyada.

## Kilit dosyası (lock file) kavramı

Bu sayfanın en kalıcı kısmı — araç ne olursa olsun bu kavram kalır.

Önceki sayfada `pip freeze > requirements.txt` ile tam sürümler yazdırmıştın —
`==` kullanıyorsan zaten kesin bir sürüm var, sorun ne? Asıl fark şu:
`requirements.txt` **tek bir dosyada** iki farklı şeyi aynı anda yapmaya
çalışır — senin *niyetini* ve kurulacak *kesin sonucu*. Modern araçlar bu ikisini
**iki ayrı dosyaya** ayırır:

```
pyproject.toml (senin niyetin — elle yazılır, nadiren değişir)
  dependencies = ["pandas>=2.0"]
        │
        ▼  araç bağımlılıkları çözer (uv lock / poetry lock)
        │
kilit dosyası (çözülmüş SONUÇ — OTOMATİK üretilir, elle yazılmaz)
  pandas==2.2.2
  numpy==1.26.4                    ← pandas'ın bağımlılığı
  python-dateutil==2.9.0.post0
  pytz==2024.1

Kurulum kilit dosyasından yapılır → her makinede BİREBİR aynı sürümler
```

`requirements.txt` bu ikisini tek dosyada birleştirince ikisinden birini feda
eder:

- **Elle `pandas>=2.0` yazarsan:** niyetin belli, ama hangi tam sürümün
  kurulacağı kurulum anına bağlı — bugün `2.2.2`, altı ay sonra `2.4.0` kurulabilir.
  Kesinlik yok.
- **`pip freeze` ile `pandas==2.2.2` yazdırırsan:** kesinlik var, ama artık "ben
  aslında `2.0` ve üstünü kabul ediyordum, `2.2.2` sadece o an kurulan sürümdü"
  bilgisi kaybolur. Niyet yok.

Modern araçlarda ikisi bir arada durur: `pyproject.toml`'da niyetini yazarsın,
kilit dosyası aracın kendisi tarafından otomatik üretilir — sen elle dokunmazsın.

## uv

Hız odaklı bir araç; pip ve venv'in yerine geçebilir. Getirdiği temel şey: aynı
işlemleri (paket kurma, ortam oluşturma) çok daha hızlı yapması ve otomatik olarak
bir kilit dosyası üretmesi.

## poetry

Proje yönetimi odaklı; bağımlılık yönetimi, paketleme ve PyPI'a yayınlama
işlemlerini tek bir araçta toplar. Bir kütüphane yazıp paylaşacaksan, bu süreci
sadeleştirir.

## Ne zaman geçmeye değer

- Yeni bir projeye sıfırdan başlıyorsan
- Ekipçe çalışıyorsan ve herkesin birebir aynı ortamı kurması önemliyse
- pip'in kurulum süresi gerçekten can sıkıyorsa (büyük projelerde)

## Ne zaman değmez

- Henüz öğrenme aşamasındaysan — önce pip+venv'i anlamak daha değerli
- Mevcut bir proje pip+venv ile sorunsuz çalışıyorsa, sırf "daha yeni" diye geçmek
  gereksiz risk
- Ekipte kimse kullanmıyorsa — herkesin bilmediği bir araca geçmek, tek kişilik
  bir bağımlılık yaratır

## Öğrenme sırası

Önce pip ve venv'i anla — bu sayfaya kadarki yedi sayfa. Bu araçlar pip'in yerini
alsa da altta aynı kavramlar çalışır: sanal ortam izolasyonu, bağımlılık çözümü,
sürüm sabitleme. pip+venv'i anlamadan uv/poetry öğrenmek, altındaki mantığı
bilmeden bir kısayolu ezberlemek olur — bir sorun çıktığında neyin ters gittiğini
anlayamazsın.

## Sık yapılan hatalar

| Yanılgı | Sebebi | Doğrusu |
|---|---|---|
| "uv/poetry daha hızlı, direkt onunla başlayayım" | pip+venv'in altındaki kavramlar atlanır | Önce pip+venv ile bir proje kur, sorunları gör, sonra geç |
| Ekipte bazıları pip, bazıları poetry kullanıyor | Araç seçimi konuşulmadan yapılmış | Proje başına tek araç, ekip kararı gerekir |
| Kilit dosyasını Git'e commit'lememek | `requirements.txt` alışkanlığıyla "gereksiz" sanılmış | Kilit dosyası aynı işi daha kesin yapar — o da commit'lenir |
| Farklı araçların kilit dosyalarını karıştırmak | Her aracın kendi formatı var, birbirinin yerine geçmez | Projede tek bir araç kullan, kilit dosyasını o aracın beklediği formatta tut |

## Kendin dene

Araçlar kurulu olmayabilir — bu alıştırma onlar olmadan da yapılabilir.

1. Daha önce yazdığın (ya da
   [requirements.txt](../01-gunluk-kullanim/02-requirements-ve-bagimliliklar.md)
   sayfasındaki alıştırmadan kalma) bir `requirements.txt` dosyasını aç.
2. Listedeki paketlere bak: hangilerini sen doğrudan `pip install` ile kurdun,
   hangileri başka bir paketin bağımlılığı olarak geldi?
3. Bu ayrımı dosyadan çıkarabiliyor musun? Muhtemelen hayır — bu tam olarak
   "freeze'in dezavantajı" bölümünde bahsettiğimiz kayıp. Kilit dosyalarının
   çözdüğü sorun tam olarak bu.

## Python Ortamları bölümünde ne öğrendin

8 sayfalık bir yolculuğun sonuna geldin:

- Python'ı doğru kurmak, PATH ve Microsoft Store tuzağından kaçınmak
  ([01](../00-temeller/01-python-kurulumu.md))
- pip ile paket kurmak, sürüm belirtmek ([02](../00-temeller/02-pip-ile-paket-kurmak.md))
- Sanal ortamın neden gerektiği ([03](../00-temeller/03-sanal-ortam-nedir.md))
- venv ile gerçek bir ortam kurmak, aktifleştirmek ([04](../00-temeller/04-venv-kullanimi.md))
- conda'nın ne zaman gerektiğine karar vermek ([01](../01-gunluk-kullanim/01-conda-ne-zaman.md))
- `requirements.txt` ile ortamı paylaşmak ([02](../01-gunluk-kullanim/02-requirements-ve-bagimliliklar.md))
- Ortam sorunlarını teşhis etmek ([03](../01-gunluk-kullanim/03-ortam-sorunlarini-cozmek.md))
- Modern araçların çözdüğü problemi tanımak (bu sayfa)

Artık bir Python projesini sıfırdan kurup, paylaşıp, bozulduğunda onarabilecek
durumdasın.

## Sonraki adım

→ [VS Code](../../vscode/README.md)

---

<sub>Bu sayfada hata mı buldun? [Issue aç](https://github.com/Enes-CE/turkish-ai-handbook/issues/new/choose).</sub>
