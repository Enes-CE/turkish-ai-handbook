# Yeni Konu Ekleme

Bu depo beş konuya (ve zamanla daha fazlasına) ev sahipliği yapacak. Her konu kendi kurallarını
icat ederse depo altı ay içinde gezilemez hale gelir. Yeni bir konu klasörü açarken bu dosyadaki
sıra takip edilir.

---

## Klasör düzeni

Her konu **aynı** iskelete sahiptir:

```
0X-konu-adi/
├── README.md              ← zorunlu: bu konunun içindekiler tablosu
├── HATA-INDEKSI.md        ← zorunlu: hata mesajı → çözüm → sayfa
├── 00-temeller/           ← bölümler, iki haneli numarayla
├── 01-.../
├── gorseller/             ← sadece bu konunun görselleri
└── notebooks/             ← çalıştırılabilir örnekler (Python/ML/DL/GenAI için)
```

**Derinlik kuralı: en fazla üç seviye.** `konu / bolum / sayfa.md`. Dördüncü seviyeye ihtiyaç
duyuyorsan konu çok geniş demektir, ikiye böl.

## İsimlendirme

| Kural | Doğru | Yanlış |
|---|---|---|
| Küçük harf, tire ile ayrılmış | `makine-ogrenmesi` | `Makine Ogrenmesi` |
| Türkçe karakter yok (klasör/dosya adında) | `derin-ogrenme` | `derin-öğrenme` |
| İki haneli numara öneki | `03-model-degerlendirme.md` | `3-model-degerlendirme.md` |
| Numara sıra bildirir, kalıcıdır | Araya girecekse `02b-` kullan | Tüm dosyaları yeniden numaralama |

Türkçe karakterler **başlıklarda ve metinde serbest**, sadece dosya/klasör adlarında yok —
farklı işletim sistemleri ve URL'ler bozuluyor.

## Yeni konu açarken sıra

1. `_sablon/konu-README-sablonu.md` kopyalanıp konu klasörüne `README.md` olarak konur
2. Müfredat **baştan sona** belirlenir ve README'ye yazılır (yazılmamış sayfalar `[ ]` olarak durur)
3. Yazılmamış sayfalar için iskelet dosyalar oluşturulur — böylece README'de kırık link olmaz
4. Boş bir `HATA-INDEKSI.md` açılır
5. Kök `README.md`'deki konu tablosuna satır eklenir
6. Sayfalar sırayla `_sablon/kaynak-sablonu.md`'ye göre yazılır

Adım 2 atlanmaz: müfredat baştan belli olmazsa konu, birbirini tutmayan yazılar yığınına döner.

## Konular arası bağlantı

Konular birbirine referans verecek — Makine Öğrenmesi sayfası Python'daki bir sayfaya, oradaki
bir sayfa Git'e. Kurallar:

- **Göreli yol kullan** (`../../01-python/...`), mutlak GitHub linki değil. Repo adı değişirse
  hepsi kırılır.
- **Kopyalama, linkle.** Aynı anlatım iki konuda tekrar ediyorsa biri asıl, diğeri link olur.
  İkiye kopyalanan bilgi, ikiye ayrılan gerçektir — biri güncellenir, diğeri unutulur.
- Ön koşul başka bir konudaysa künyeye tam yolu yaz: `on-kosul: [01-python/00-temeller/03-fonksiyonlar.md]`

## Durum işaretleri

Kök README'deki tabloda ve konu README'lerinde aynı işaretler kullanılır:

🟢 tamamlandı · 🟡 devam ediyor · ⚪ planlandı

Sayfa listelerinde `[x]` hazır, `[ ]` sırada.

## Notebook kuralları (Python / ML / DL / GenAI için)

- Notebook'lar `notebooks/` altında, ilgili sayfadan linklenir
- **Çıktılar temizlenmiş halde commit'lenir** (Kernel → Restart & Clear Output)
- Her notebook'un başında Colab rozeti bulunur; kullanıcı tıklayıp kurulum yapmadan çalıştırabilmeli
- Veri seti repoya konmaz; indirme kodu notebook'un içinde olur

← [Ana sayfa](README.md) · [Bakım Protokolü](BAKIM.md)
