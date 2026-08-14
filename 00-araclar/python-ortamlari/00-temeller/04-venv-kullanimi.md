---
seviye: giriş
on-kosul: [python-ortamlari/00-temeller/03-sanal-ortam-nedir.md]
tip: komut
son-guncelleme: 2026-08-14
dogrulandigi-surum: python venv modülü (standart kütüphane) — sürüm numarası verilmedi
---

# venv ile ortam oluşturma

> **Bu sayfa şunu çözer:** Önceki sayfada "neden" sorusunu cevapladık, burada gerçek
> bir sanal ortam kurup aktifleştirip kullanmayı öğreniyorsun.
> **Ön koşul:** [Sanal ortam neden gerekli](03-sanal-ortam-nedir.md) · **Süre:** ~20 dakika

---

## Ortam oluşturma

```bash
python -m venv venv
```

Sessizce çalışır, çıktı vermez. Bulunduğun klasörde `venv/` adında yeni bir klasör
oluşur.

Klasör adı olarak `venv` ya da `.venv` ikisi de yaygın — nokta ile başlayan `.venv`,
`ls` çıktısında gizlenir ([Dosya içeriğini görmek](../../terminal/00-temeller/04-dosya-icerigi-goruntuleme.md)
sayfasında `ls -a` ile gizli dosyaları gördüğünü hatırla). Bu sayfada `venv` kullanıyoruz
— hangisini seçersen seç, projende tutarlı kal.

## Ortamın içinde ne var

```
projem/
├── venv/                        ← sanal ortam, sadece bir klasör
│   ├── Scripts/                 (Windows)  ya da  bin/  (macOS/Linux)
│   │   ├── python
│   │   ├── pip
│   │   └── activate
│   └── Lib/site-packages/       ← kurduğun paketler buraya iner
├── egitim.py
└── requirements.txt
```

Windows'ta çalıştırılabilir dosyalar `Scripts/` klasöründe, macOS/Linux'ta `bin/`
klasöründe durur — birazdan aktifleştirme komutunda bu fark karşına çıkacak.

## Aktifleştirme

Bu sayfanın en çok hata alınan yeri — üç farklı kabuk, üç farklı komut. Hangi
kabukta olduğundan emin değilsen
[Windows'ta terminal seçenekleri](../../terminal/01-gunluk-kullanim/04-windows-terminal-secenekleri.md)
sayfasındaki yöntemlerle kontrol et.

**Git Bash (Windows):**

```bash
source venv/Scripts/activate
```

**PowerShell:**

```powershell
venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

`Scripts` ile `bin` farkı tesadüf değil — az önceki ağaç şemasında gördüğün klasör
farkının aynısı: Windows `Scripts/`, Unix `bin/` kullanır.

> ⚠️ **PowerShell'de "running scripts is disabled on this system" hatası.**
> PowerShell'in script çalıştırma politikası varsayılan olarak kısıtlıdır, `.ps1`
> dosyalarını (aktifleştirme script'i dahil) engeller. Çözüm — PowerShell'i normal
> kullanıcı olarak aç ve çalıştır:
>
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
> ```
>
> Bu, sadece senin kullanıcı hesabın için geçerli olur ve şunu söyler: kendi
> bilgisayarında yazdığın yerel script'ler imzasız çalışabilir, internetten
> indirilen (uzak) script'ler ise imzalı olmak zorundadır — sistem genelini
> değiştirmez, sadece bu ayrımı kurar. Onaylamak için `Y` yaz.

## Aktif olduğunu doğrulama

İki yol var. Kabuk satırının başında genelde `(venv)` görünür — ama önceki sayfada
söylediğimiz gibi bu garanti değil. Kesin yol:

```bash
which python
```

Beklenen çıktı: proje klasöründeki `venv/Scripts/python` (Windows) ya da
`venv/bin/python` (macOS/Linux) yolu — sistemdeki Python değil.

## Ortam içinde paket kurmak

```bash
python -m pip install requests
```

Artık güvenle çalıştırabilirsin — bu kurulum sadece bu `venv/` klasörüne gider,
sisteme bulaşmaz.

## Deaktifleştirme

```bash
deactivate
```

PATH eski hâline döner, `(venv)` görünümü kaybolur.

## Ortamı silmek

Ortam sadece bir klasör olduğu için, silmek de klasörü silmek kadar basit:

```bash
deactivate
rm -rf venv
```

[Dosya ve klasör işlemleri](../../terminal/00-temeller/03-dosya-klasor-islemleri.md)
sayfasında öğrendiğin `rm -rf` uyarısı burada da geçerli — geri alınamaz. Risk burada
daha düşük çünkü `venv/` içinde kaybedecek "senin" bir şey yok, hepsi yeniden
kurulabilir; yine de yanlış klasörde çalıştırmamaya dikkat et.

## .gitignore'a ekleme

Önceki sayfada söz verdiğimiz şeyi burada uygula:

```bash
echo "venv/" >> .gitignore
```

Bu tek satır, `venv/` klasörünün Git'e hiç commit'lenmemesini sağlar.

## VS Code'un ortamı tanıması

VS Code, projende bir `venv/` klasörü gördüğünde genelde bunu otomatik fark eder ve
kullanmayı önerir; ayarları [VS Code](../../vscode/README.md) bölümünde.

## Her yeni terminalde tekrar aktifleştirme

Aktifleştirme kalıcı değildir — terminali kapatıp yeni bir tane açtığında ya da başka
bir proje klasörüne geçtiğinde, o ortamı tekrar aktifleştirmen gerekir. Bu, önceki
sayfada "aktifleştirme kalıcı değil" dediğimiz şeyin pratikte karşına çıkışı.

## Sık yapılan hatalar

| Hata | Sebebi | Çözüm |
|---|---|---|
| PowerShell: "running scripts is disabled on this system" | Script çalıştırma politikası kısıtlı | Yukarıdaki `Set-ExecutionPolicy` komutunu çalıştır |
| PowerShell'de `source venv/Scripts/activate` çalışmıyor | `source`, PowerShell'de yok — bu bir Bash komutu | PowerShell'de doğrudan `venv\Scripts\Activate.ps1` çalıştır |
| Aktifleştirirken `No such file or directory` | Yanlış klasördesin ya da Scripts/bin karıştırıldı | `pwd` ile proje kökünde olduğunu doğrula, işletim sistemine uygun klasörü kullan |
| `pip install` çalıştı ama `import` edemiyorum | Ortam aktif değil | `which python` ile kontrol et, gerekirse tekrar aktifleştir |

## Kendin dene

1. `mkdir venv-deneme && cd venv-deneme` ile boş bir klasör oluştur, içine gir.
2. `python -m venv venv` ile ortamı kur.
3. İşletim sistemine uygun komutla aktifleştir (yukarıdaki üç komuttan biri).
4. `which python` ile çalışan Python'ın `venv/` klasörünün içinde olduğunu doğrula.
5. `python -m pip install cowsay` çalıştır. (`requests` değil, bilinçli olarak
   daha az yaygın bir paket seçiyoruz — [pip ile paket kurmak](02-pip-ile-paket-kurmak.md)
   sayfasındaki alıştırmada `requests`'i zaten sistemine kurmuş olabilirsin, bu da
   aşağıdaki testi geçersiz kılar.)
6. `deactivate` çalıştır.
7. `which python` ile bu sefer sistemin Python'unun döndüğünü gör — artık `venv/`
   içindeki değil.
8. `python -c "import cowsay"` çalıştır — `ModuleNotFoundError` alırsın, çünkü
   `cowsay` sadece `venv/` içine kurulmuştu, sisteme değil. İzolasyonun kanıtı bu.
   (Eğer hata almazsan, bu paket daha önce sistemine kurulmuş demektir — ortamı
   deaktifleştirdikten sonra `pip uninstall cowsay` ile sistemden kaldırıp adım
   7-8'i tekrar dene.)

## Sonraki adım

→ [conda / Miniconda ne zaman tercih edilir](../01-gunluk-kullanim/01-conda-ne-zaman.md)

---

<sub>Bu sayfada hata mı buldun? [Issue aç](https://github.com/Enes-CE/turkish-ai-handbook/issues/new/choose).</sub>
