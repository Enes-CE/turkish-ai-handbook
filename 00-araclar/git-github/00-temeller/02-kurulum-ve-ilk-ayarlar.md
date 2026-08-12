---
seviye: giriş
on-kosul: [01-git-nedir.md]
tip: komut
son-guncelleme: 2026-08-10
dogrulandigi-surum: git 2.45
---

# Kurulum ve ilk ayarlar

> **Bu sayfa şunu çözer:** Bilgisayarına Git'i kurar ve ilk commit'ini atmadan önce yapılması
> gereken ayarları bir kere doğru yaparsın.
> **Ön koşul:** [Git nedir, neden var?](01-git-nedir.md) · **Süre:** ~15 dakika

---

## Neden gerek var?

Git kurulduğu anda çalışır ama **hiçbir şey bilmez**: commit'i kimin attığını, hangi editörü
açacağını, dosya satır sonlarını nasıl işleyeceğini. Bu ayarları baştan yapmazsan, ilerideki
"commit'lerim GitHub profilimde görünmüyor" veya "arkadaşımla aynı dosyada 400 satır fark
çıkıyor" gibi sorunların kaynağı burası olur.

## Kurulum

### Windows

[git-scm.com/download/win](https://git-scm.com/download/win) adresinden indir, kurulumda
gelen seçenekleri **varsayılan bırak**. İçinde Git Bash de geliyor; bu rehberdeki komutları
PowerShell yerine Git Bash'te çalıştırman en sorunsuz yol.

### macOS

```bash
brew install git
```

Homebrew yoksa: Terminal'e `git --version` yaz, macOS sana Command Line Tools kurulumunu önerecek. O da yeterli.

### Linux (Debian/Ubuntu)

```bash
sudo apt update && sudo apt install git
```

### Doğrulama

```bash
git --version
```

Beklenen çıktı (sürüm numarası farklı olabilir, sorun değil):

```
git version 2.45.2
```

Komut bulunamadı hatası alıyorsan terminali kapatıp yeniden aç — PATH güncellenmiş olmuyor.

## İlk ayarlar

Aşağıdakiler **bir kere** yapılır, bütün projeler için geçerli olur (`--global` bunu sağlıyor).

**1. Kimlik**

Her commit'e bu isim ve e-posta yazılır ve **geçmişten silinmesi kolay değildir.** Kurumsal
değil, kalıcı olarak kullanacağın bilgiyi yaz.

```bash
git config --global user.name "Adın Soyadın"
git config --global user.email "github-hesabindaki@eposta.com"
```

> ⚠️ E-posta, GitHub hesabındaki e-posta ile **aynı olmalı.** Farklıysa commit'lerin GitHub'da
> sana bağlanmaz, profilindeki yeşil katkı grafiğinde görünmez. E-postanı gizlemek istiyorsan
> GitHub → Settings → Emails bölümündeki `xxxxx+kullanici@users.noreply.github.com` adresini kullan.

**2. Varsayılan dal adı**

```bash
git config --global init.defaultBranch main
```

Eski Git sürümleri `master` kullanıyordu, GitHub ise `main`. Bu ayarı yapmazsan yeni açtığın
her repoda isim uyuşmazlığıyla uğraşırsın.

**3. Satır sonları**

Windows ile macOS/Linux dosya satır sonlarını farklı yazar. Ayarlanmazsa, siz aynı dosyaya
dokunmasanız bile Git dosyanın tamamını "değişmiş" gösterir.

Windows:

```bash
git config --global core.autocrlf true
```

macOS / Linux:

```bash
git config --global core.autocrlf input
```

**4. Türkçe karakterli dosya adları**

Varsayılan ayarda `veri_kümesi.csv` gibi dosyalar terminalde `veri_k\303\274mesi.csv` şeklinde görünür.

```bash
git config --global core.quotepath false
```

**5. Editör (isteğe bağlı)**

Git bazı durumlarda mesaj yazman için editör açar; varsayılan olarak gelen Vim'e alışkın
değilsen çıkamayabilirsin.

```bash
git config --global core.editor "code --wait"   # VS Code
```

## Kontrol

```bash
git config --global --list
```

Beklenen çıktı (satır sırası farklı olabilir):

```
user.name=Adın Soyadın
user.email=github-hesabindaki@eposta.com
init.defaultbranch=main
core.autocrlf=true
core.quotepath=false
```

## Sık yapılan hatalar

| Hata | Sebebi | Çözüm |
|---|---|---|
| Commit'ler GitHub profilinde görünmüyor | `user.email` GitHub hesabındakinden farklı | Doğru e-posta ile `git config --global user.email` tekrar çalıştırılır (eski commit'ler geriye dönük düzelmez) |
| `Author identity unknown` | Kimlik hiç ayarlanmamış | Yukarıdaki 1. adım |
| Hiç dokunmadığın dosyalar "değişmiş" görünüyor | Satır sonu ayarı | Yukarıdaki 3. adım |
| Terminalde garip karakterler | `core.quotepath` | Yukarıdaki 4. adım |

## Kendin dene

```bash
git config --global user.name
```

Ekranda kendi adını görüyorsan kurulum tamam. Görmüyorsan 1. adıma dön.

## Sonraki adım

→ [İlk repo, ilk commit](03-ilk-repo-ilk-commit.md)

---

<sub>Bu sayfada hata mı buldun? [Issue aç](https://github.com/Enes-CE/turkish-ai-handbook/issues/new/choose).</sub>
