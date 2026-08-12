---
seviye: giriş
on-kosul: yok
tip: kavram
son-guncelleme: 2026-08-11
dogrulandigi-surum: kavramsal — sürümden bağımsız
---

# Git nedir, neden var?

> **Bu sayfa şunu çözer:** Git'in hangi problemi çözdüğünü ve arka planda nasıl düşündüğünü
> anlarsın. Komut ezberlemeden önce buradaki modeli oturtmak, ilerideki her şeyi kolaylaştırır.
> **Ön koşul:** yok · **Süre:** ~10 dakika

---

## Tanıdık problem

Muhtemelen bir klasörün şuna benziyor:

```
model_egitim.py
model_egitim_v2.py
model_egitim_v2_calisan.py
model_egitim_SON.py
model_egitim_SON_gercek.py
```

Bu, elle yapılmış bir sürüm kontrol sistemi. Sorunları belli: hangi dosyanın ne farkı var
bilmiyorsun, iki hafta önceki haline dönmek istediğinde hangisi olduğunu hatırlamıyorsun,
arkadaşınla aynı dosyada çalıştığınızda birinizin değişikliği kayboluyor.

Git tam olarak bu işi otomatikleştiren araç: **projenin zaman içindeki her halini saklar, aralarındaki
farkı gösterir ve istediğin ana geri dönmene izin verir.**

## Temel fikir: commit bir fotoğraftır

Git'te attığın her `commit`, projenin o andaki halinin fotoğrafıdır. Bu fotoğraflar bir zincir
oluşturur:

```
[commit 1] ← [commit 2] ← [commit 3] ← şu anki halin
   veri        model        eğitim
   yüklendi    yazıldı      düzeltildi
```

Her fotoğrafın yanında şu bilgiler durur: kim attı, ne zaman attı, neyi değiştirdi ve **neden**
değiştirdi (commit mesajı). Üç ay sonra "bu satır neden böyle" diye sorduğunda cevabı burada bulursun.

Önemli olan şu: Git dosyaları değil, **değişiklikleri ve anları** takip eder. Bu yüzden bir
dosyanın 6 ay önceki halini geri getirmek, o dosyayı yedeklememiş olsan bile mümkündür.

## Üç alan modeli

Git'i öğrenirken en çok kafa karıştıran şey, bir değişikliğin doğrudan kaydedilmemesi. Arada
bir ara durak var. Üç alan şöyle:

```
┌──────────────────┐   git add    ┌──────────────────┐  git commit  ┌──────────────────┐
│  Çalışma alanı   │ ───────────► │  Hazırlık alanı  │ ───────────► │      Depo        │
│ (working dir)    │              │    (staging)     │              │   (repository)   │
│                  │              │                  │              │                  │
│ Editörde         │              │ "Bu değişiklik-  │              │ Kalıcı kayıt.    │
│ gördüğün,        │              │ leri bir sonraki │              │ Geçmişin bir     │
│ üzerinde         │              │ commit'e dahil   │              │ parçası oldu.    │
│ çalıştığın hal   │              │ et" dediklerin   │              │                  │
└──────────────────┘              └──────────────────┘              └──────────────────┘
```

**Hazırlık alanı neden var?** Çünkü yaptığın her değişiklik aynı commit'e ait olmayabilir.
Bir oturumda hem bir hatayı düzeltip hem de yeni bir özellik yazmış olabilirsin. Hazırlık alanı
sayesinde bunları iki ayrı commit olarak kaydedersin — geçmişin okunabilir kalır ve ileride
sadece birini geri almak isteyebilirsin.

Yeni başlayanların çoğu bu alanı gereksiz bir bürokrasi sanır ve hep `git add .` yazar. İlk
haftalarda sorun değil, ama bu ara duraklamanın ne işe yaradığını bilmek, ileride
"yanlış dosyayı commit'ledim" durumundan çıkmanı sağlayacak.

## Git ≠ GitHub

Bu ikisinin karıştırılması, sonraki bütün kafa karışıklıklarının kaynağı:

| | Git | GitHub |
|---|---|---|
| Nedir | Bilgisayarına kurduğun program | Bir web sitesi / servis |
| Ne yapar | Değişiklikleri kaydeder | Kaydedilenleri internette barındırır |
| Çalışmak için | İnternet gerekmez | İnternet gerekir |
| Alternatifi | Mercurial, SVN | GitLab, Bitbucket |

Git'i internetsiz bir dağ evinde de kullanabilirsin, sorunsuz çalışır. GitHub, o kayıtları
başkalarıyla paylaşmak, yedeklemek ve birlikte çalışmak için devreye girer.

Kısaca: **Git araç, GitHub o aracın çıktısını koyduğun yer.**

## Bunu neden yapay zekâ projelerinde önemsiyoruz?

- **Deney takibi.** "Learning rate 0.001'ken 0.87 almıştım" — hangi kod haliyle aldığını commit
  geçmişinden bulabilirsin.
- **Bozulan şeyi bulmak.** Dün çalışan eğitim kodu bugün hata veriyorsa, aradaki farkı Git tek
  komutla gösterir.
- **İşe alım.** ML pozisyonlarında GitHub profilin portföyün demek. Düzenli commit geçmişi olan
  bir proje, tek seferde yüklenmiş bir klasörden çok farklı okunur.
- **Ekip çalışması.** Bootcamp'te grup projesi yapacaksan zaten mecburi.

## Kafanda kalması gerekenler

- Commit = projenin o anki fotoğrafı + neden çekildiğinin açıklaması
- Değişiklik önce hazırlık alanına alınır, sonra commit'lenir
- Git bilgisayarında, GitHub internette
- Amaç dosya yedeklemek değil, **geçmişi okunabilir tutmak**

## Sonraki adım

→ [Kurulum ve ilk ayarlar](02-kurulum-ve-ilk-ayarlar.md)

---

<sub>Bu sayfada hata mı buldun? [Issue aç](https://github.com/Enes-CE/turkish-ai-handbook/issues/new/choose).</sub>
