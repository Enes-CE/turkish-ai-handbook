---
seviye: her seviye
on-kosul: yok
tip: komut
son-guncelleme: 2026-08-11
dogrulandigi-surum: git 2.45
---

# Hata Mesajı İndeksi

> **Bu sayfa şunu çözer:** Aldığın hata mesajını buradan aratırsın, hem kısa çözümü hem de
> konunun anlatıldığı sayfayı bulursun.

**Nasıl aranır:** `Ctrl+F` ile hata mesajının **en ayırt edici 2-3 kelimesini** arat.
Örneğin `fatal: refusing to merge unrelated histories` için → `unrelated histories`.

Bu sayfa bir öğretim sayfası değil, **yönlendirme katmanı**. Konunun tamamını öğrenmek için
sağdaki bağlantıya git.

---

## Kurulum ve kimlik

| Hata / durum | Kısa çözüm | Detay |
|---|---|---|
| `git: command not found` | Terminali kapatıp aç; kurulmadıysa kur | [Kurulum](00-temeller/02-kurulum-ve-ilk-ayarlar.md) |
| `Author identity unknown` | `git config --global user.name` / `user.email` | [Kurulum](00-temeller/02-kurulum-ve-ilk-ayarlar.md) |
| Commit'ler GitHub profilinde görünmüyor | `user.email` GitHub hesabındakiyle aynı olmalı | [Kurulum](00-temeller/02-kurulum-ve-ilk-ayarlar.md) |
| Dokunmadığın dosyalar "değişmiş" görünüyor | Satır sonu ayarı: `core.autocrlf` | [Kurulum](00-temeller/02-kurulum-ve-ilk-ayarlar.md) |
| Türkçe karakterli dosya adları bozuk görünüyor | `git config --global core.quotepath false` | [Kurulum](00-temeller/02-kurulum-ve-ilk-ayarlar.md) |
| Vim açıldı, çıkamıyorum | `Esc` → `:wq` → `Enter` | [Kurulum](00-temeller/02-kurulum-ve-ilk-ayarlar.md) |

## Depo ve commit

| Hata / durum | Kısa çözüm | Detay |
|---|---|---|
| `fatal: not a git repository` | Yanlış klasördesin ya da `git init` yapılmamış | [İlk repo](00-temeller/03-ilk-repo-ilk-commit.md) |
| `nothing to commit, working tree clean` | Değişiklik yok ya da `add` yapılmadı | [İlk repo](00-temeller/03-ilk-repo-ilk-commit.md) |
| `src refspec main does not match any` | Henüz hiç commit atılmamış | [İlk repo](00-temeller/03-ilk-repo-ilk-commit.md) |
| `git diff` boş çıkıyor ama dosya değişti | Değişiklik zaten hazırlanmış: `git diff --staged` | [Değişiklikleri takip etmek](00-temeller/04-degisiklikleri-takip-etmek.md) |
| Yanlış dosyayı `add` ettim | `git restore --staged <dosya>` | [Değişiklikleri takip etmek](00-temeller/04-degisiklikleri-takip-etmek.md) |
| Commit mesajını yanlış yazdım (henüz push edilmedi) | `git commit --amend -m "..."` | [Değişiklikleri takip etmek](00-temeller/04-degisiklikleri-takip-etmek.md) |

## GitHub bağlantısı

| Hata / durum | Kısa çözüm | Detay |
|---|---|---|
| `Support for password authentication was removed` | Token ya da SSH kur | [GitHub'a bağlanmak](00-temeller/05-github-baglanti.md) |
| `Permission denied (publickey)` | SSH anahtarı GitHub'a eklenmemiş | [GitHub'a bağlanmak](00-temeller/05-github-baglanti.md) |
| `refusing to merge unrelated histories` | `git pull origin main --allow-unrelated-histories` | [GitHub'a bağlanmak](00-temeller/05-github-baglanti.md) |
| `Updates were rejected...` | Önce `git pull`, sonra `push`. `--force` kullanma | [GitHub'a bağlanmak](00-temeller/05-github-baglanti.md) |
| `remote origin already exists` | `git remote set-url origin <adres>` | [GitHub'a bağlanmak](00-temeller/05-github-baglanti.md) |

## Henüz yazılmamış bölümlerin hataları

Aşağıdaki başlıklar ilgili sayfalar yazıldıkça doldurulacak:

- Çakışma (`CONFLICT (content)`, `Automatic merge failed`) → *01-gunluk-kullanim*
- Büyük dosya reddi (`file exceeds GitHub's file size limit`) → *01-gunluk-kullanim*
- Notebook çakışmaları → *01-gunluk-kullanim*
- `detached HEAD` → *02-geri-alma*
- Silinen çalışmayı kurtarma (`reflog`) → *02-geri-alma*

---

<sub>Aradığını bulamadın mı? [Issue aç](https://github.com/Enes-CE/turkish-ai-handbook/issues/new/choose) — eklenecek.</sub>
