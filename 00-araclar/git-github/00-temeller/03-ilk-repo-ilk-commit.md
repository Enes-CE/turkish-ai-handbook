---
seviye: giriş
on-kosul: [00-temeller/02-kurulum-ve-ilk-ayarlar.md]
tip: komut
son-guncelleme: 2026-08-11
dogrulandigi-surum: git 2.45
---

# İlk repo, ilk commit

> **Bu sayfa şunu çözer:** Boş bir klasörü Git deposuna dönüştürür, ilk commit'ini atar ve
> geçmişini görürsün. Bu sayfanın sonunda Git'in temel döngüsünü tamamlamış olacaksın.
> **Ön koşul:** [Kurulum ve ilk ayarlar](02-kurulum-ve-ilk-ayarlar.md) · **Süre:** ~20 dakika

---

## Neden gerek var?

Git her klasörde otomatik çalışmaz; bir klasörü açıkça "bunu takip et" diye işaretlemen gerekir.
Bu sayfadaki dört komut (`init`, `status`, `add`, `commit`) Git kullanımının %80'ini oluşturur —
gerisi bu döngünün etrafındaki özel durumlar.

## Nasıl yapılır

**1. Bir çalışma klasörü oluştur**

```bash
mkdir ilk-git-projem
cd ilk-git-projem
```

**2. Klasörü Git deposuna dönüştür**

```bash
git init
```

Beklenen çıktı:

```
Initialized empty Git repository in /home/kullanici/ilk-git-projem/.git/
```

Bu komut klasörün içine gizli bir `.git` klasörü açar. Geçmişin tamamı orada tutulur.

> ⚠️ `.git` klasörünü silme veya taşıma — projenin bütün geçmişi orada. Klasörü silersen
> dosyaların kalır ama geçmiş tamamen gider.

Kontrol için:

```bash
ls -a
```

```
.  ..  .git
```

**3. Bir dosya oluştur**

```bash
echo "# İlk Git Projem" > README.md
```

**4. Git'in durumu nasıl gördüğüne bak**

```bash
git status
```

```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md

nothing added to commit but untracked files present
```

Buradaki anahtar kelime **untracked**: dosya klasörde var ama Git onu henüz takip etmiyor.
`git status` bu rehberdeki en çok kullanacağın komut; takıldığın her noktada önce bunu çalıştır,
Git genelde ne yapman gerektiğini de söyler.

**5. Dosyayı hazırlık alanına al**

```bash
git add README.md
```

Tekrar `git status`:

```
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md
```

Dosya artık **untracked** değil, **staged** (hazırlık alanında). Henüz kaydedilmedi.

**6. Commit'le**

```bash
git commit -m "İlk commit: README eklendi"
```

```
[main (root-commit) a1b2c3d] İlk commit: README eklendi
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
```

`a1b2c3d`, commit'in kimliği (hash). Her commit'in kendine ait böyle bir kimliği vardır ve
ileride bir commit'e atıfta bulunurken bunu kullanırsın.

**7. Geçmişi gör**

```bash
git log
```

```
commit a1b2c3d4e5f6... (HEAD -> main)
Author: Adın Soyadın <eposta@ornek.com>
Date:   Mon Aug 11 14:23:10 2026 +0300

    İlk commit: README eklendi
```

Buradaki isim ve e-posta [ilk ayarlarda](02-kurulum-ve-ilk-ayarlar.md) girdiklerin. Yanlışsa
şimdi düzelt — sonradan atılan commit'ler doğru olur ama geçmiştekiler değişmez.

Daha okunabilir bir özet için:

```bash
git log --oneline
```

```
a1b2c3d İlk commit: README eklendi
```

## Döngüyü tamamla

Şimdi ikinci bir tur atalım; asıl alışman gereken ritim bu:

```bash
echo "Bu proje Git öğrenmek için oluşturuldu." >> README.md
git status          # ne değişmiş?
git add README.md   # hazırla
git commit -m "README'ye açıklama satırı eklendi"
git log --oneline   # iki commit görmelisin
```

**Düzenle → `status` → `add` → `commit`.** Git kullanımı büyük ölçüde bu döngünün tekrarı.

## Sık yapılan hatalar

| Hata | Sebebi | Çözüm |
|---|---|---|
| `fatal: not a git repository` | Yanlış klasördesin ya da `git init` yapılmamış | `pwd` ile yeri kontrol et, gerekiyorsa `git init` |
| `nothing to commit, working tree clean` | Değişiklik yok ya da `git add` yapılmadı | `git status` ile bak, dosyayı `add` et |
| Commit ekranında Vim açıldı | `-m` ile mesaj yazılmadı | `Esc` → `:wq` → `Enter`. Sonraki sefer `-m "mesaj"` kullan |
| Ev dizininde `git init` yapıldı | Yanlış klasörde çalıştırıldı | O klasördeki `.git` silinir: `rm -rf .git` (dikkat: doğru klasörde olduğundan emin ol) |
| `Author identity unknown` | Kimlik ayarlanmamış | [İlk ayarlar](02-kurulum-ve-ilk-ayarlar.md) |

## Kendin dene

Yeni bir klasörde sıfırdan bir depo oluştur, içine iki farklı dosya koy ve bunları **iki ayrı
commit** olarak kaydet. Sonunda:

```bash
git log --oneline
```

çıktısında iki satır görüyorsan tamam. Tek satır görüyorsan iki dosyayı aynı commit'e koymuşsun —
`add` ve `commit` adımlarını dosya dosya tekrar dene.

## Sonraki adım

→ [Değişiklikleri takip etmek](04-degisiklikleri-takip-etmek.md)

---

<sub>Bu sayfada hata mı buldun? [Issue aç](https://github.com/Enes-CE/turkish-ai-handbook/issues/new/choose).</sub>
