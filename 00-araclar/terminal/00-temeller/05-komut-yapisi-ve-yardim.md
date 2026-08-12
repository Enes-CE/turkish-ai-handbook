---
seviye: giriş
on-kosul: [terminal/00-temeller/01-terminal-nedir.md]
tip: kavram
son-guncelleme: 2026-08-12
dogrulandigi-surum: kavramsal — sürümden bağımsız
---

# Komut yapısı ve yardım okuma

> **Bu sayfa şunu çözer:** Şu ana kadar kullandığın komutların ortak yapısını çözümlersin —
> bundan sonra hiç görmediğin bir komutla karşılaşınca da kendi başına anlayabilirsin.
> `--help` okumayı, man sayfalarını ve komut geçmişini de öğrenirsin.
> **Ön koşul:** [Terminal nedir, neden gerekli](01-terminal-nedir.md) · **Süre:** ~15 dakika

---

## Her komutun ortak iskeleti

Önceki sayfalarda kullandığın `head -n 3 veri.csv` komutunu parçalarına ayıralım:

```
head        -n        3        veri.csv
 │           │         │           │
 │           │         │           └── argüman: üzerinde çalışılacak dosya
 │           │         └── bayrağın değeri: kaç satır
 │           └── bayrak (seçenek): davranışı değiştirir
 └── komut: ne yapılacağını söyler
```

Genel şablon: `komut [bayraklar] [argümanlar]`. Önceki sayfalardaki diğer komutlar da
aynı şablona uyar:

```
ls    -l  -a           → komut + iki bayrak, argüman yok (varsayılan: bulunduğun klasör)
rm    -r  klasor        → komut + bayrak + argüman
cat   dosya1 dosya2     → komut + iki argüman, bayrak yok
```

## Kısa bayrak, uzun bayrak

- **Kısa bayrak:** tek tire + tek harf — `-l`, `-a`, `-r`
- **Uzun bayrak:** çift tire + kelime — `--all`, `--recursive`

İkisi genelde aynı şeyi yapar; uzun bayrak daha okunaklı, kısa bayrak daha hızlı yazılır.

Kısa bayraklar birleştirilebilir:

```bash
ls -l -a
```

ile

```bash
ls -la
```

aynı sonucu verir. Bunu daha önce `ls -la` olarak kullanmıştın — şimdi neden çalıştığını
biliyorsun.

## Sıra ne zaman önemli

Bayraklar genelde komuttan hemen sonra, argümanlar en sonda gelir. Alışkanlık olarak
bayrakları argümandan önce yazmak en güvenlisi:

```bash
head -n 3 veri.csv
```

Argümanların **sırası** genelde önemlidir — bayrakların sırası değil. `cp kaynak hedef`
ile `cp hedef kaynak` tamamen farklı sonuç verir: biri dosyayı hedefe kopyalar, diğeri
tam tersini dener.

## --help okumak

```bash
ls --help
```

Beklenen çıktı: kısa kullanım özeti ve bayrak listesi. Örnek satırlar:

```
  -l                         use a long listing format
  -a, --all                  do not ignore entries starting with .
```

Köşeli parantez `[]` isteğe bağlı olduğunu gösterir: `[FILE]` demek "dosya belirtmesen
de çalışır" demektir. Büyük harfli yer tutucular (`FILE`, `DIRECTORY`, `PATTERN`) senin
dolduracağın yeri gösterir — kelimenin kendisini değil.

`--help` çok yaygındır ama evrensel değildir. Bazı komutlar `-h` bekler, bazılarında
komutu hiç argümansız çalıştırmak kullanım özetini basar. `--help` "bilinmeyen bayrak"
diye hata verirse bu ikisini dene.

## man sayfaları

Daha detaylı belge için:

```bash
man ls
```

Gezinme `less` ile aynıdır: ok tuşları/boşlukla ilerle, `/kelime` ile ara, **`q` ile çık**.

Git Bash'te `man` bazen kurulu gelmez — o durumda `--help` yeterlidir, bu depodaki
örneklerin çoğu zaten `--help` kullanır.

## Tab tamamlama komut adları için de çalışır

Önceki sayfada Tab tamamlamayı yol yazarken görmüştük; komut adlarında da çalışır:

```bash
gi<Tab>
```

`git` gibi eşleşen komutu tamamlar (ya da birden fazla eşleşme varsa listeler).

## Komut geçmişi

- **Yukarı ok (`↑`)** — bir önceki komuta dön, tekrar tekrar basarak daha eskiye git
- **Aşağı ok (`↓`)** — yukarı çıktıktan sonra tekrar daha yeni komutlara doğru ilerlemeni sağlar
- **`Ctrl+R`** — geçmişte arama; birkaç harf yaz, eşleşen son komut çıkar

Uzun bir komutu yeniden yazmak yerine geçmişten çağırmak, terminalde en çok zaman
kazandıran ikinci alışkanlıktır — birincisi Tab tamamlama.

## Bilmediğin bir komutla karşılaşınca

1. Önce `komut --help` çalıştır, ne işe yaradığını ve bayraklarını gör.
2. Zararsız bir örnekle dene — mümkünse önce bir okuma komutuyla (`ls`, `cat` gibi) test
   et, silme/üzerine yazma bayrağına hemen atlama.
3. Emin değilsen bu depodaki [Hata Mesajı İndeksi](../HATA-INDEKSI.md)'ne bak ya da
   issue aç.

## Sık yapılan hatalar

| Hata | Sebebi | Çözüm |
|---|---|---|
| `--help` çıktısı uzun, ekran doldu, gerisini göremedim | Çıktı bir ekrandan uzun | `less` ile sayfalayarak oku (bu boru hattı yapısı bir sonraki sayfada) |
| Bayrağı yanlış yazdım: `-all` yazdım, `--all` değil | Tek tire ile çift tire karıştırıldı | Kısa bayrak tek harf + tek tire, uzun bayrak kelime + çift tiredir |
| `man komut` çalışmıyor | Git Bash'te `man` kurulu olmayabilir | `komut --help` kullan |
| `Ctrl+R` ile arama sırasında kayboldum | İlk defa kullanılıyor, tuş alışılmadık | `Ctrl+C` ile aramadan çık, `Enter` ile bulduğun komutu çalıştır |

## Kendin dene

Daha önce kullandığın bir komutun `--help` çıktısını oku ve henüz kullanmadığın bir
bayrağı bul, zararsız bir örnekte dene:

```bash
ls --help
```

Çıktıda `-t` (değişiklik tarihine göre sırala) ya da `-h` (boyutları okunaklı göster)
gibi henüz görmediğin bir bayrak bul, `ls -lh` gibi bir kombinasyonla dene. `-h` tek
başına bir şey değiştirmez, sadece `-l` ile birlikte anlam taşır — `ls -h` denersen hiç
fark görmezsin, bu normal.

## Bu bölümde ne öğrendin

00-temeller bölümünün sonuna geldin:

- Terminal, GUI ile aynı dosyalara başka bir kapı ([01](01-terminal-nedir.md))
- `pwd`/`ls`/`cd` ile gezinme, mutlak/göreli yol ([02](02-dosya-sistemi-ve-yol.md))
- `mkdir`/`touch`/`cp`/`mv`/`rm` ile oluşturma, kopyalama, taşıma, silme — ve `rm`'in
  geri alınamaz olduğu ([03](03-dosya-klasor-islemleri.md))
- `cat`/`head`/`tail`/`less`/`wc` ile dosya içeriğini okuma ([04](04-dosya-icerigi-goruntuleme.md))
- Komutların ortak yapısı ve yardım alma (bu sayfa)

Bundan sonra terminalde karşına çıkan hemen her komutu bu iskeletle okuyabilirsin.

## Sonraki adım

→ [Arama ve filtreleme](../01-gunluk-kullanim/01-arama-ve-filtreleme.md)

---

<sub>Bu sayfada hata mı buldun? [Issue aç](https://github.com/Enes-CE/turkish-ai-handbook/issues/new/choose).</sub>
