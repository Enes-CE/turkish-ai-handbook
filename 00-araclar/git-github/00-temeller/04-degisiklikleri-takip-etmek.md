---
seviye: giriş
on-kosul: [00-temeller/03-ilk-repo-ilk-commit.md]
tip: komut
son-guncelleme: 2026-08-11
dogrulandigi-surum: git 2.45
---

# Değişiklikleri takip etmek

> **Bu sayfa şunu çözer:** Commit atmadan önce neyi commit'lediğini görürsün, yanlış eklediğin
> dosyayı hazırlık alanından çıkarırsın ve altı ay sonra okunabilir commit mesajları yazarsın.
> **Ön koşul:** [İlk repo, ilk commit](03-ilk-repo-ilk-commit.md) · **Süre:** ~20 dakika

---

## Neden gerek var?

Önceki sayfada `add` ve `commit`'i öğrendin. Ama gerçek projede sorun şu: bir oturumun sonunda
sekiz dosya değişmiş oluyor ve hangisinde ne yaptığını tam hatırlamıyorsun. Körlemesine
`git add .` yazıp commit'lersen, geçmişin "güncellemeler" başlıklı anlamsız kayıtlara dönüşür.

Bu sayfa, commit atmadan önce **görmeyi** öğretiyor.

## Durumu okumak

```bash
git status
```

Çıktıda üç grup olabilir — hangisinde olduğunu ayırt etmek önemli:

| Grup | Anlamı | Nasıl ilerlersin |
|---|---|---|
| `Untracked files` | Git bu dosyayı hiç görmemiş | `git add <dosya>` |
| `Changes not staged for commit` | Git dosyayı biliyor, ama son değişiklik hazırlanmamış | `git add <dosya>` |
| `Changes to be committed` | Hazırlık alanında, commit'e girecek | `git commit` |

Kısa hali (uzun çıktıya alıştıktan sonra çok pratik):

```bash
git status -s
```

```
 M model.py        ← değişmiş, hazırlanmamış
M  utils.py        ← değişmiş, hazırlanmış
?? veri.csv        ← untracked
```

İlk sütun hazırlık alanını, ikinci sütun çalışma alanını gösterir.

## Farkı görmek

`status` hangi dosyanın değiştiğini söyler, **ne değiştiğini** söylemez. Onun için `diff` var.

**Henüz hazırlanmamış değişiklikler:**

```bash
git diff
```

```diff
diff --git a/model.py b/model.py
index 83db48f..f735c2d 100644
--- a/model.py
+++ b/model.py
@@ -3,5 +3,5 @@
 def egit(model, veri):
-    lr = 0.01
+    lr = 0.001
     return model.fit(veri, learning_rate=lr)
```

`-` ile başlayan satır silinen, `+` ile başlayan eklenen hali. Yani bu değişiklik learning
rate'i 0.01'den 0.001'e çekmiş.

**Hazırlık alanındaki değişiklikler:**

```bash
git diff --staged
```

Bu ikisi farklı şeyleri gösterir ve karıştırılması çok yaygın: `git add` yaptıktan sonra düz
`git diff` boş çıkar, çünkü artık hazırlanmamış değişiklik kalmamıştır. Panik yapma, bir şey
kaybolmadı — `--staged` ile bak.

> **Alışkanlık önerisi:** Commit atmadan önce refleks olarak `git diff --staged` çalıştır.
> Bu tek alışkanlık, yanlışlıkla commit'lenen API anahtarlarının ve unutulmuş `print()`
> satırlarının çoğunu engeller.

## Hazırlık alanından geri çıkarmak

Yanlış dosyayı `add` ettiysen:

```bash
git restore --staged veri.csv
```

Dosya hazırlık alanından çıkar, **içeriğine dokunulmaz**. Sadece "bu commit'e girmesin" demiş olursun.

> ⚠️ `git restore veri.csv` (yani `--staged` olmadan) bambaşka bir komut: dosyadaki
> **kaydedilmemiş değişiklikleri siler** ve geri getirilemez. İki komutu karıştırma.

## Seçerek hazırlamak

Aynı dosyada birbiriyle ilgisiz iki değişiklik yaptıysan, dosyanın sadece bir kısmını hazırlayabilirsin:

```bash
git add -p model.py
```

Git değişiklikleri parça parça gösterir ve her biri için sorar. Cevaplar:

| Tuş | Anlamı |
|---|---|
| `y` | Bu parçayı hazırla |
| `n` | Hazırlama |
| `s` | Parçayı daha küçük parçalara böl |
| `q` | Çık |

İlk haftalarda gerekmez, ama "commit'lerim çok karışık" hissi geldiğinde çözüm burası.

## Commit mesajı yazmak

Geçmişin okunabilirliği tamamen buna bağlı. İyi bir mesajın iki kuralı:

**1. Ne yaptığını değil, neyi çözdüğünü yaz.**

```
✗ güncelleme
✗ değişiklikler
✗ fix
✓ Eğitim sırasında learning rate 0.001'e düşürüldü (loss dalgalanıyordu)
```

**2. Emir kipiyle ve kısa başlıkla başla (~50 karakter), gerekirse boş satır bırakıp detay yaz.**

```bash
git commit -m "Veri yükleyiciye eksik değer kontrolü ekle" -m "NaN içeren satırlar eğitimi bozuyordu; artık yükleme sırasında atılıyor."
```

Şu testi uygula: **`git log --oneline` çıktısını üç ay sonra okuyan biri (yani sen) ne olduğunu anlıyor mu?**

Son commit'in mesajını düzeltmek istersen (henüz GitHub'a göndermediysen):

```bash
git commit --amend -m "Yeni mesaj"
```

## Geçmişte gezinmek

```bash
git log --oneline --graph --all      # dallarla birlikte görsel özet
git log -3                           # son 3 commit
git log --oneline model.py           # sadece bu dosyaya dokunan commit'ler
git show a1b2c3d                     # o commit'te tam olarak ne değişmiş
```

Bu dört komut, "bu satır neden böyle" sorusunun cevabını bulmak için yeterli.

## Sık yapılan hatalar

| Hata | Sebebi | Çözüm |
|---|---|---|
| `git diff` boş çıkıyor ama dosyayı değiştirdim | Değişiklik zaten `add` edilmiş | `git diff --staged` |
| `git add .` ile veri seti / gizli dosya commit'lendi | Her şey körlemesine eklendi | `.gitignore` kullan → [ilgili sayfa](../01-gunluk-kullanim/05-gitignore-buyuk-dosyalar.md) |
| `git restore` ile yazdıklarım silindi | `--staged` unutulmuş | Kaydedilmemiş değişiklik geri gelmez; commit'lenmişse [Geri alma](../02-geri-alma/01-reset-revert-restore.md) |
| `diff` çıktısından çıkamıyorum | Sayfalama açık (`less`) | `q` tuşu |

## Kendin dene

Bir dosyada iki ayrı satırı değiştir. Sonra:

1. `git add -p` ile **sadece birini** hazırla
2. `git diff --staged` ile hazırladığını, `git diff` ile hazırlamadığını gör
3. İlkini commit'le, ikincisini ayrı bir commit olarak kaydet

`git log --oneline` çıktısında iki anlamlı satır varsa hedefe ulaştın.

## Sonraki adım

→ [GitHub'a bağlanmak](05-github-baglanti.md)

---

<sub>Bu sayfada hata mı buldun? [Issue aç](https://github.com/Enes-CE/turkish-ai-handbook/issues/new/choose).</sub>
