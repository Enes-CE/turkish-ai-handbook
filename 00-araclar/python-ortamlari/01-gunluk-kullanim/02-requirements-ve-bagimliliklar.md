---
seviye: orta
on-kosul: [python-ortamlari/00-temeller/04-venv-kullanimi.md]
tip: komut
son-guncelleme: 2026-08-14
dogrulandigi-surum: pip freeze — sürüm numarası verilmedi, komut sözdizimi kalıcı
---

# requirements.txt ve bağımlılık dondurma

> **Bu sayfa şunu çözer:** "Bende çalışıyor, sende çalışmıyor" sorununu — kurulu
> paketlerini sabit bir listeye dökmeyi (`pip freeze`) ve başka bir makinede aynı
> ortamı kurmayı öğrenirsin.
> **Ön koşul:** [venv ile ortam oluşturma](../00-temeller/04-venv-kullanimi.md) ·
> **Süre:** ~20 dakika

---

## Sorun: paylaşım

Sanal ortam, sistemindeki çakışmayı çözdü — ama projeni GitHub'a atıp arkadaşın
indirdiğinde, ya da altı ay sonra kendi makinende tekrar kurmaya kalktığında,
"hangi paketler hangi sürümde gerekiyordu" sorusu hâlâ ortada. `venv/` klasörü
Git'e gitmiyor ([Sanal ortam neden gerekli](../00-temeller/03-sanal-ortam-nedir.md)
sayfasında öğrendiğin gibi), yani ortamın kendisi paylaşılamaz. Paylaşılan şey,
ortamı **yeniden kurmak için gereken tarif**: `requirements.txt`.

## pip freeze: kurulu paketleri listeleme

```bash
pip freeze
```

Beklenen çıktı:

```
certifi==2024.7.4
charset-normalizer==3.3.2
idna==3.7
requests==2.32.3
urllib3==2.2.2
```

`pip list`'ten farkı: `freeze`, doğrudan `pip install`'e verilebilecek
`paket==sürüm` formatında yazar.

## Dosyaya yazmak: pip freeze > requirements.txt

[Çıktıyı dosyaya yazmak](../../terminal/01-gunluk-kullanim/02-cikti-yonlendirme.md)
sayfasında öğrendiğin `>` burada devreye giriyor:

```bash
pip freeze > requirements.txt
```

> ⚠️ **`pip freeze`'i sanal ortam AKTİFKEN çalıştır.** Aktif değilken çalıştırırsan
> `pip`, sistem Python'una bakar ve o sistemde kurulu **her şeyi** listeler — sadece
> bu projenin ihtiyaç duyduğu birkaç paket değil, o bilgisayara zaman içinde
> kurulmuş yüzlerce paket. Ortaya 200 satırlık, işe yaramaz bir `requirements.txt`
> çıkar; bu dosyayı başka bir makinede `pip install -r` ile kurmaya çalıştığında ya
> saatlerce sürer ya da bitmeyen bir çakışma listesiyle karşılaşırsın. Çalıştırmadan
> önce `which python`'ın proje klasöründeki `venv/`'i gösterdiğini doğrula.

## Dosyadan kurmak: pip install -r

```bash
python -m pip install -r requirements.txt
```

Beklenen: dosyadaki her satır sırayla kurulur.

## requirements.txt bir köprüdür

```
Senin makinen                                 Başka makine (arkadaşın, sunucu, Colab)

venv aktif
  │
  ▼  pip freeze > requirements.txt
requirements.txt  ─────────► Git ─────────►  requirements.txt
                                                  │
                                                  ▼  python -m venv venv
                                                venv aktif
                                                  │
                                                  ▼  pip install -r requirements.txt
                                                aynı paketler, aynı sürümler
```

## Sürüm sabitleme stratejileri

- `paket==1.2.3` — tam sürüm. Uygulama projelerinde (özellikle üretime giden)
  tercih edilir; herkes birebir aynı sürümü kurar, sürpriz olmaz.
- `paket>=1.2` — en az bu sürüm. Bir kütüphane **geliştiriyorsan** (başkalarının
  senin paketini kullanacağı durumda) daha esnek olmak, kullanıcılarının kendi
  sürüm ihtiyaçlarıyla çakışmanı önler.
- `paket~=1.2` — uyumlu sürüm; `1.2.x`'in herhangi bir yamasını kabul eder ama
  `1.3`'e geçmez. İkisinin ortası: küçük güncellemelere izin verir, büyük API
  değişikliklerinden korur.

Genel kural: **uygulama projesinde katı ol (`==`), kütüphane yazarken esnek ol
(`>=` ya da `~=`).**

## freeze'in dezavantajı

`pip freeze`, senin doğrudan `pip install` ile kurduğun paketleri değil, **ortamda
kurulu olan her şeyi** listeler — bağımlılıkların bağımlılıkları dahil. Bu yüzden
zamanla dosya şişer, hangi satırın bilinçli bir kararın olduğu, hangisinin bir
başka paketin yan etkisi olduğu kaybolur.

Alternatif: elle yazılan, sade bir `requirements.txt` — sadece doğrudan kullandığın
paketleri, gerektiğinde sürüm sınırıyla birlikte yazarsın. Daha az otomatik ama
daha okunaklı. Büyük/karmaşık projelerde bu ayrımı yönetmek için `pip-tools` gibi
araçlar da var (bu depoda ayrıca işlenmiyor).

## requirements.txt Git'e gider

[Sanal ortam neden gerekli](../00-temeller/03-sanal-ortam-nedir.md) ve
[venv ile ortam oluşturma](../00-temeller/04-venv-kullanimi.md) sayfalarında
`venv/` klasörünün `.gitignore`'a eklendiğini, Git'e hiç gitmediğini görmüştün.
`requirements.txt` bunun tam tersi — **mutlaka commit'lenir**. Ortamın kendisi
kişisel ve tekrar üretilebilir; tarifi (`requirements.txt`) ise projenin bir
parçasıdır.

## conda karşılığı

conda dünyasında aynı işi `environment.yml` görür:

```bash
conda env export > environment.yml
```

Başka makinede kurmak:

```bash
conda env create -f environment.yml
```

[conda / Miniconda ne zaman tercih edilir](01-conda-ne-zaman.md) sayfasında
değindiğimiz gibi, `environment.yml` sadece Python paketlerini değil conda'nın
yönettiği Python dışı bağımlılıkları da kaydedebilir.

## Colab'da ya da başka bir makinede kurulum

Bir Colab hücresinde ya da yeni bir sunucuda projeyi çalıştırmaya başlarken tipik sıra:

```bash
git clone <repo-adresi>
cd repo-adi
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

Beş satır, projeyi sıfırdan aynı hâle getirir.

## Sık yapılan hatalar

| Hata | Sebebi | Çözüm |
|---|---|---|
| `requirements.txt` 200 satır, çoğu bu projeyle ilgisiz | `pip freeze`, ortam aktif değilken çalıştırıldı | Ortamı aktifleştir, `which python` ile doğrula, tekrar `freeze` al |
| `pip install -r requirements.txt` sürüm çakışması hatalarıyla duruyor | Dosya sistemin tüm paketlerini içeriyor, birbiriyle çelişen sürümler var | Aynı — aktif ortamda yeniden `freeze` al |
| Yeni klonlanan projede `ModuleNotFoundError` | `requirements.txt` hiç kurulmamış ya da ortam aktifleştirilmemiş | `pip install -r requirements.txt` çalıştır, önce ortamı aktifleştir |
| `environment.yml` başka makinede kurulmuyor | Dosya belirli bir işletim sistemine özgü derlenmiş paketler içeriyor olabilir | `conda env export --from-history` ile daha taşınabilir bir liste üret (sadece elle kurduğun paketleri yazar) |

## Kendin dene

1. `mkdir req-deneme && cd req-deneme`, `python -m venv venv`, aktifleştir
   (işletim sistemine uygun komut [venv ile ortam oluşturma](../00-temeller/04-venv-kullanimi.md)
   sayfasında).
2. `python -m pip install requests` çalıştır.
3. `which python` ile ortamın aktif olduğunu doğrula, sonra
   `pip freeze > requirements.txt`.
4. `cat requirements.txt` ile dosyanın içeriğine bak — `requests` ve onun
   bağımlılıklarını (`certifi`, `charset-normalizer`, `idna`, `urllib3`) görürsün.
5. `deactivate`, sonra `rm -rf venv` ile ortamı tamamen sil.
6. `python -m venv venv` ile yeni bir ortam kur, aktifleştir (yine
   [venv ile ortam oluşturma](../00-temeller/04-venv-kullanimi.md) sayfasındaki komutla).
7. `python -m pip install -r requirements.txt` çalıştır — az önce sildiğin ortamın
   aynısı birkaç saniyede geri gelir.

## Sonraki adım

→ [Ortam sorunlarını çözmek](03-ortam-sorunlarini-cozmek.md)

---

<sub>Bu sayfada hata mı buldun? [Issue aç](https://github.com/Enes-CE/turkish-ai-handbook/issues/new/choose).</sub>
