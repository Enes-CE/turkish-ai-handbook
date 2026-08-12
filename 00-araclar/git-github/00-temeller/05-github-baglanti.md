---
seviye: giriş
on-kosul: [00-temeller/04-degisiklikleri-takip-etmek.md]
tip: arayuz
son-guncelleme: 2026-08-11
dogrulandigi-surum: git 2.45 / GitHub web arayüzü (Ağustos 2026)
---

# GitHub'a bağlanmak

> **Bu sayfa şunu çözer:** Yerel deponu GitHub'a gönderirsin, başkasının deposunu bilgisayarına
> indirirsin ve kimlik doğrulamayı bir kere düzgün kurup şifre sorununu bir daha yaşamazsın.
> **Ön koşul:** [Değişiklikleri takip etmek](04-degisiklikleri-takip-etmek.md) · **Süre:** ~30 dakika

> ℹ️ Bu sayfa GitHub arayüzüne değindiği için rehberdeki en hızlı eskiyen sayfa. Menü isimleri
> değişmiş olabilir; adımlar aynı kalır. Fark görürsen [issue aç](https://github.com/Enes-CE/turkish-ai-handbook/issues/new/choose).

---

## Neden gerek var?

Şu ana kadar yaptığın her şey bilgisayarında kaldı. Diskin bozulursa proje de geçmişi de gider.
GitHub'a bağlanmak üç şeyi aynı anda çözüyor: yedek, paylaşım ve portföy.

## Kimlik doğrulama: token mı, SSH mi?

GitHub 2021'den beri şifreyle `push` kabul etmiyor. İki seçeneğin var:

| | Personal Access Token (HTTPS) | SSH anahtarı |
|---|---|---|
| Kurulum | Daha hızlı | Biraz daha uzun |
| Kullanım | İlk seferde token yapıştırılır | Hiçbir şey sorulmaz |
| Süre | Genelde süreli, yenilenmesi gerekir | Süresiz |
| Kurumsal ağ / güvenlik duvarı | Sorunsuz | Bazen 22 numaralı port kapalı olur |

**Öneri:** Kendi bilgisayarınsa SSH kur, bir kere yapıp unutursun. Ortak/geçici bir makinedeysen token kullan.

### Seçenek A — SSH anahtarı

**1. Anahtar üret** (`-C` sonrasına GitHub e-postanı yaz):

```bash
ssh-keygen -t ed25519 -C "eposta@ornek.com"
```

Sorulan üç şeyde de `Enter`'a basman yeterli (varsayılan konum, parola boş).

**2. Genel anahtarı kopyala:**

```bash
cat ~/.ssh/id_ed25519.pub
```

Çıkan `ssh-ed25519 AAAA...` ile başlayan satırın tamamını kopyala.

> ⚠️ `.pub` uzantılı olan **genel** anahtar, paylaşılabilir. Uzantısız olan (`id_ed25519`)
> **özel** anahtarın — onu kimseyle paylaşma, repoya koyma.

**3. GitHub'a ekle:** Sağ üstteki profil resmi → *Settings* → sol menüde *SSH and GPG keys* →
*New SSH key* → başlık ver, anahtarı yapıştır → *Add SSH key*.

**4. Test et:**

```bash
ssh -T git@github.com
```

```
Hi kullaniciadin! You've successfully authenticated, but GitHub does not provide shell access.
```

Bu mesaj başarı demek — "shell access" kısmı hata değil.

### Seçenek B — Personal Access Token

*Settings* → *Developer settings* → *Personal access tokens* → *Tokens (classic)* →
*Generate new token*. `repo` yetkisini işaretle, süre seç, oluştur.

> ⚠️ Token sadece bir kez gösterilir. Kapatmadan önce güvenli bir yere kaydet. Kaybedersen
> yenisini üretmen gerekir.

`push` sırasında şifre sorulduğunda şifre yerine bu token'ı yapıştır. Her seferinde sormaması için:

```bash
git config --global credential.helper store
```

(Bu, token'ı diske düz metin olarak yazar. Ortak makinede kullanma.)

## Yereldeki depoyu GitHub'a göndermek

**1. GitHub'da boş repo oluştur:** Sağ üstte `+` → *New repository*. İsim ver.

> ⚠️ **README, .gitignore veya lisans ekleme seçeneklerini işaretleme.** Yerelde zaten commit'in
> var; GitHub tarafında da commit oluşursa iki ayrı geçmiş çakışır ve
> `refusing to merge unrelated histories` hatasını alırsın.

**2. Uzak adresi tanımla** (adresi repo sayfasındaki *Code* düğmesinden kopyala):

```bash
git remote add origin git@github.com:kullaniciadin/repo-adi.git
```

`origin`, uzak deponun takma adı. Standart isimdir, değiştirmeye gerek yok.

Kontrol:

```bash
git remote -v
```

```
origin  git@github.com:kullaniciadin/repo-adi.git (fetch)
origin  git@github.com:kullaniciadin/repo-adi.git (push)
```

**3. Gönder:**

```bash
git push -u origin main
```

`-u` sadece ilk seferde gerekli; sonraki gönderimlerde `git push` yeterli olur.

Sayfayı yenilediğinde dosyalarını GitHub'da görüyorsan tamam.

## Başkasının deposunu indirmek

```bash
git clone git@github.com:kullaniciadin/repo-adi.git
cd repo-adi
```

`clone`, dosyaları ve **tüm geçmişi** indirir; `origin` da otomatik ayarlanır. Yani indirdiğin
depoda `git log` çalışır, geçmişi gezebilirsin.

> ZIP olarak indirmek ile `clone` arasındaki fark tam olarak budur: ZIP'te geçmiş yoktur.

## Değişiklikleri çekmek

Başka bir cihazdan veya GitHub arayüzünden değişiklik yapıldıysa, çalışmaya başlamadan önce:

```bash
git pull origin main
```

**Günlük ritim:** `pull` → çalış → `add` → `commit` → `push`. Sabah çekmeden başlamak,
bootcamp grup projelerinde en sık çakışma sebebidir.

## Sık yapılan hatalar

| Hata | Sebebi | Çözüm |
|---|---|---|
| `Support for password authentication was removed` | Şifreyle push denendi | Token veya SSH kur (yukarıda) |
| `Permission denied (publickey)` | SSH anahtarı GitHub'a eklenmemiş | `ssh -T git@github.com` ile test et, 3. adımı tekrarla |
| `refusing to merge unrelated histories` | GitHub'da README ile repo açılmış | `git pull origin main --allow-unrelated-histories` |
| `Updates were rejected...` | Uzakta sende olmayan commit var | Önce `git pull`, sonra `push`. `--force` **kullanma** |
| `remote origin already exists` | `remote add` ikinci kez çalıştırıldı | `git remote set-url origin <adres>` |
| `src refspec main does not match any` | Henüz hiç commit atılmamış | Önce bir commit at, sonra push |

## Kendin dene

Önceki sayfalarda oluşturduğun yerel depoyu GitHub'a gönder. Sonra onu **başka bir klasöre**
`clone` et ve orada `git log --oneline` çalıştır — commit geçmişinin aynen geldiğini gör.

## Sonraki adım

→ [Branch mantığı](../01-gunluk-kullanim/01-branch-mantigi.md)

---

<sub>Bu sayfada hata mı buldun? [Issue aç](https://github.com/Enes-CE/turkish-ai-handbook/issues/new/choose).</sub>
