---
seviye: ileri
on-kosul: [terminal/01-gunluk-kullanim/03-ortam-degiskenleri-ve-path.md]
tip: komut
son-guncelleme: 2026-08-12
dogrulandigi-surum: bash (Git Bash / macOS / Linux ortak)
---

# SSH ile uzak makineye bağlanmak

> **Bu sayfa şunu çözer:** Ekranı olmayan, sadece terminalden erişilebilen uzak bir
> bilgisayara (GPU'lu bir sunucu, kurum makinesi) bağlanmayı, oraya dosya taşımayı ve
> bağlantı kopsa bile işinin devam etmesini sağlamayı öğrenirsin.
> **Ön koşul:** [Ortam değişkenleri ve PATH](../01-gunluk-kullanim/03-ortam-degiskenleri-ve-path.md) ·
> **Süre:** ~25 dakika

---

## SSH nedir

SSH (Secure Shell), başka bir bilgisayarın terminaline **uzaktan, şifreli bir bağlantı
üzerinden** girmeni sağlayan protokol. Ekranı, klavyesi olmayan bir sunucuya "girmenin"
tek yolu genelde budur — fiziksel olarak o makinenin başına oturmadan, kendi
terminalinden onun kabuğuna bağlanırsın.

## Neden gerekir

- Kendi bilgisayarında olmayan bir GPU'yu kiralamak ve kullanmak
- Üniversite ya da kurum sunucusunda model eğitmek
- Kendi makinenin gücünün yetmediği bir işi, daha güçlü bir uzak makinede yapmak

## Temel bağlantı

```bash
ssh kullanici@sunucu-adresi
```

İlk bağlantıda şuna benzer bir soru çıkar:

```
The authenticity of host 'sunucu-adresi (1.2.3.4)' can't be established.
ED25519 key fingerprint is SHA256:...
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

Bu, "bu sunucuyu daha önce hiç görmedim, gerçekten bağlanmak istediğine emin misin"
sorusu — ilk bağlantıda normaldir, `yes` yazıp devam edersin. Aynı sunucuya sonraki
bağlantılarında bu soru bir daha çıkmaz. Çıkarsa (parmak izi **değişmişse**) bu ayrı
bir konu — aşağıdaki "Sık yapılan hatalar" tablosuna bak.

## Anahtar tabanlı giriş

Şifre yerine bir anahtar çifti kullanmak hem daha güvenli hem daha hızlıdır — her
seferinde şifre yazmazsın. Bu depoda
[GitHub'a bağlanmak](../../git-github/00-temeller/05-github-baglanti.md) sayfasında
`ssh-keygen` ile anahtar üretmeyi zaten öğrendin — aynı anahtar çifti (özel + genel)
mantığı burada da geçerli. Zaten bir anahtarın varsa yeniden üretmene gerek yok.

Anahtarını sunucuya tanıtmanın en kolay yolu:

```bash
ssh-copy-id kullanici@sunucu-adresi
```

Bu, genel anahtarını (`~/.ssh/id_ed25519.pub`) sunucudaki `~/.ssh/authorized_keys`
dosyasına ekler. `ssh-copy-id` yoksa (bazı sistemlerde gelmez) aynı işi elle de
yapabilirsin:

```bash
cat ~/.ssh/id_ed25519.pub | ssh kullanici@sunucu-adresi "cat >> ~/.ssh/authorized_keys"
```

Sonrasında `ssh kullanici@sunucu-adresi` şifre sormadan doğrudan bağlanır.

> ⚠️ **Özel anahtarını (uzantısız olan, `id_ed25519`) asla kimseyle paylaşma, hiçbir
> yere yükleme, repoya koyma.** Paylaşabileceğin tek dosya `.pub` uzantılı olan genel
> anahtar. Bu kural [GitHub'a bağlanmak](../../git-github/00-temeller/05-github-baglanti.md)
> sayfasında da geçiyordu — aynı anahtar, aynı kural.

## Bağlandıktan sonra: neredesin

```
YEREL MAKİNE (senin bilgisayarın)                  UZAK SUNUCU
┌───────────────────┐                  ┌────────────────────────┐
│ terminal penceren │     ssh ile      │ orada bir kabuk açılır │
│ egitim-verisi.csv │─────────────────►│ (kendi dosya sistemi)  │
│ egitim.py         │   bağlanırsın    │                        │
└───────────────────┘                  └────────────────────────┘

ssh'den ÖNCE:                          ssh'den SONRA:
komutlar burada çalışır                  komutlar BURADA çalışır
(kendi bilgisayarın)                   (sunucunun kendisi)
```

`ssh` ile bağlandıktan sonra yazdığın her komut — `ls`, `python egitim.py`, `pwd` —
artık **sunucuda** çalışır, senin bilgisayarında değil. `pwd` yazarsan sunucunun bir
klasörünü görürsün, kendi bilgisayarınınkini değil. Bağlantıyı kapatmak için `exit`
yazarsın ya da `Ctrl+D` basarsın — yerel makinene geri dönersin.

## scp ile dosya taşımak

`scp`, iki bilgisayar arasında SSH üzerinden dosya kopyalamanın yolu. Yön karışıklığı
en sık yapılan hata — kaynak her zaman ilk argüman, hedef ikinci argüman.

```
YEREL → UZAK:
  scp dosya.txt   kullanici@sunucu:/hedef/yol/
      └─ kaynak (yerel)
                  └─ hedef (uzak, sunucu adresi burada)

UZAK → YEREL:
  scp kullanici@sunucu:/kaynak/yol/dosya.txt   .
      └─ kaynak (uzak, sunucu adresi burada)
                                               └─ hedef (yerel)
```

Kural basit: sunucu adresi (`kullanici@sunucu:`) hangi tarafta yazılıysa, o taraf
**o bilgisayarı** temsil eder — kaynak da olabilir hedef de.

Yerelden sunucuya göndermek:

```bash
scp egitim-verisi.csv kullanici@sunucu-adresi:/home/kullanici/veri/
```

Sunucudan yerele indirmek:

```bash
scp kullanici@sunucu-adresi:/home/kullanici/sonuclar/model.pt .
```

Klasör kopyalamak için `cp -r`'de olduğu gibi `-r` gerekir:

```bash
scp -r sonuclar/ kullanici@sunucu-adresi:/home/kullanici/
```

## Uzun süren işler: bağlantı koparsa ne olur

[Çıktıyı dosyaya yazmak](../01-gunluk-kullanim/02-cikti-yonlendirme.md) sayfasında,
`&` ile arka planda başlatılan bir sürecin terminali kapatınca öldüğünü, bunun
çözümünün bu sayfada geleceğini söylemiştik — işte burada.

SSH bağlantısı için de aynı risk geçerli: bağlantı koparsa (internet kesilir, laptop
uyur, terminal kapanır), o oturumda başlattığın işlem de durur. Saatlerce sürecek bir
eğitimi bundan korumanın iki yolu var.

**`nohup`** — en basit çözüm:

```bash
nohup python egitim.py > egitim-log.txt 2>&1 &
```

`nohup` (no hang up), oturumu kapatsan bile sürecin çalışmaya devam etmesini sağlar.
Sınırı: sürece geri "bağlanamazsın", sadece log dosyasından izlersin.

Yönlendirme yazmadan sadece `nohup python egitim.py &` dersen, çıktı otomatik olarak
bulunduğun klasördeki `nohup.out` dosyasına yazılır. Yukarıdaki örnekte olduğu gibi
kendi log dosyanı belirtmek daha iyidir — çıktının tam olarak nerede olduğunu bilirsin.

**`tmux`** — daha esnek çözüm: terminalde ayrı bir "oturum" açar. O oturumda
çalıştırdığın iş, bağlantı kopsa bile devam eder — sonra tekrar bağlanıp o oturuma
**geri dönebilirsin** (`nohup`'ta yapamadığın şey):

```bash
tmux new -s egitim
python egitim.py
```

Oturumdan işi durdurmadan ayrılmak: `Ctrl+B` sonra `D`. Geri dönmek:

```bash
tmux attach -t egitim
```

`tmux`/`screen`'in tam kullanımı bu depoda ayrıca işlenmiyor — yukarıdakiler, bir
eğitim başlatıp güvenle bağlantıyı kapatman için yeterli.

## Sunucuda tehlikeli komutlar daha tehlikelidir

> ⚠️ **Sunucu genelde paylaşılan bir makinedir** — başkalarının verisi, başkalarının
> süreçleri de orada çalışıyor olabilir. `rm -rf` gibi bir komut yerel makinende
> sadece seni etkilerken, sunucuda yanlış çalıştırıldığında bir ekibin çalışmasını ya
> da paylaşılan verileri silebilir. Sunucuda silme/üzerine yazma işlemlerinde her
> zamankinden daha dikkatli ol; hangi klasörde olduğunu (`pwd`) iki kez kontrol et.

## Sık yapılan hatalar

| Hata | Sebebi | Çözüm |
|---|---|---|
| `Permission denied (publickey)` | Anahtar sunucuya tanıtılmamış | `ssh-copy-id` ile anahtarını ekle |
| `Connection refused` | Sunucu adresi/portu yanlış ya da sunucudaki SSH servisi kapalı | Adresi kontrol et, sunucunun çalışır durumda olduğundan emin ol |
| `WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!` | Sunucunun parmak izi değişti — sunucu yeniden kurulmuş olabilir AMA saldırı da olabilir | Körü körüne "yes" deme; sunucunun sahibine sorup değişikliği doğrula |
| `scp` dosyayı ters yöne kopyaladı | Kaynak/hedef sırası karıştırıldı | Kaynak her zaman ilk argüman, hedef ikinci |
| Bağlantı koptu, eğitim durdu | İş `&` ile ya da hiç korumasız çalıştırıldı | `nohup` ya da `tmux`/`screen` kullan |

## Kendin dene

Gerçek bir sunucuya erişimin olmasa bile, anahtar üretme ve yapısını inceleme
adımlarını kendi bilgisayarında deneyebilirsin. `-f` ile ayrı bir dosya adı
belirtiyoruz ki zaten var olan bir anahtarın (örneğin GitHub'a bağladığın) üzerine
yazılmasın:

1. `ssh-keygen -t ed25519 -C "deneme" -f ~/.ssh/deneme_anahtar` çalıştır.
2. `ls -la ~/.ssh/` ile klasörün içeriğine bak — iki yeni dosya görürsün:
   `deneme_anahtar` (özel anahtar, uzantısız) ve `deneme_anahtar.pub` (genel anahtar).
3. `cat ~/.ssh/deneme_anahtar.pub` ile genel anahtarın nasıl göründüğünü gör —
   `ssh-ed25519 AAAA...` ile başlar.
4. Özel anahtarı (`deneme_anahtar`) **açma ya da paylaşma** — sadece dosyanın orada
   durduğunu `ls` ile doğrulaman bu alıştırma için yeterli.

Alıştırma bitince bu deneme anahtarını silebilirsin — hiçbir yere tanıtılmadığı için
silmek güvenlidir: `rm ~/.ssh/deneme_anahtar ~/.ssh/deneme_anahtar.pub`

## Terminal bölümünde ne öğrendin

10 sayfalık bir yolculuğun sonuna geldin:

- **00-temeller** — terminalin GUI ile aynı dosyalara başka bir kapı olduğu, temel
  gezinme (`pwd`/`ls`/`cd`), dosya/klasör işlemleri, dosya içeriğini okuma, komutların
  ortak yapısı ([başlangıç noktası](../00-temeller/01-terminal-nedir.md))
- **01-gunluk-kullanim** — arama ve filtreleme (`grep`, `|`), çıktıyı dosyaya
  yönlendirme (`>`, `>>`), ortam değişkenleri ve PATH, Windows'a özgü seçenekler
  ([başlangıç noktası](../01-gunluk-kullanim/01-arama-ve-filtreleme.md))
- **02-ileri** — uzak bir makineye bağlanma (bu sayfa)

Terminal artık bir engel değil, elindeki bir araç.

## Sonraki adım

→ [Python Ortamları](../../python-ortamlari/README.md)

---

<sub>Bu sayfada hata mı buldun? [Issue aç](https://github.com/Enes-CE/turkish-ai-handbook/issues/new/choose).</sub>
