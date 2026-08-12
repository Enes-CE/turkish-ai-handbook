# Katkıda Bulunma

Bu depo topluluk katkısına açık. Katkı vermek için uzman olman gerekmiyor — yazım hatası
düzeltmek de, bir sayfayı baştan yazmak da aynı derecede değerli.

Bu dosya iki soruyu cevaplar: **ne kabul ediliyor** ve **süreç nasıl işliyor**.

---

## Katkı türleri

| Tür | Zorluk | Nereden başlanır |
|---|---|---|
| Yazım/dilbilgisi düzeltmesi | Kolay | Doğrudan PR aç |
| Kırık link, eskimiş ekran görüntüsü | Kolay | Doğrudan PR aç |
| Mevcut sayfaya "sık yapılan hata" eklemek | Kolay | Doğrudan PR aç |
| Hata indeksine yeni satır | Kolay | Doğrudan PR aç |
| Yeni sayfa yazmak | Orta | **Önce issue** (aşağıya bak) |
| Yeni bölüm / konu önermek | Zor | **Önce issue**, tartışılır |

İlk katkın olacaksa `iyi-ilk-katki` etiketli issue'lara bak — bunlar küçük, kapsamı belli
ve kimsenin üzerinde çalışmadığı işler.

## Yeni sayfa yazacaksan: önce issue

Müfredattaki her yazılmamış sayfa için bir issue var. Yazmak istediğin sayfanın issue'suna
yorum bırak (*"bunu ben yazabilirim"*), sana atansın, sonra başla.

Bu adım bürokrasi değil, koruma: iki kişinin aynı sayfayı bir hafta boyunca ayrı ayrı yazıp
birinin emeğinin çöpe gitmesini engelliyor.

Bir sayfa aynı anda **tek kişiye** atanır. 14 gün hareket olmazsa atama düşer ve issue tekrar
açılır — kimse kırılmasın diye baştan yazılı kural olsun istedik.

## Süreç

```
1. Depoyu fork'la
2. Yeni bir dal aç:  git switch -c sayfa/branch-mantigi
3. Yaz
4. Kontrolü çalıştır: python3 tools/kontrol.py
5. Commit'le ve fork'una push'la
6. PR aç, şablondaki maddeleri işaretle
7. Geri bildirim gelir → düzelt → birleştirilir
```

Dal adı önerisi: `sayfa/...`, `duzeltme/...`, `hata-indeksi/...`

Bu adımların hepsi zaten [Git & GitHub](00-araclar/git-github/) bölümünde anlatılıyor.
İlk PR'ını buraya atmak, öğrendiğini uygulamanın en iyi yolu.

## İçerik kuralları

Her sayfa [`_sablon/kaynak-sablonu.md`](_sablon/kaynak-sablonu.md) yapısına uyar. Otomatik
kontrol künyeyi ve isimlendirmeyi denetler, ama asıl kalite şu dört maddede:

**1. Bir sayfa, bir soru.** Sayfanın başındaki "Bu sayfa şunu çözer" cümlesini tek cümlede
yazamıyorsan konu çok geniştir; ikiye böl.

**2. Ön koşulu belirt, tekrar anlatma.** Aynı konu iki sayfada anlatılırsa biri güncellenir,
diğeri unutulur ve depo kendi kendisiyle çelişir. Anlatılmış bir şeye link ver.

**3. Komutun çıktısını da yaz.** "Şu komutu çalıştır" yetmez; okuyan kişi ne göreceğini
bilmeli ki doğru gidip gitmediğini anlasın.

**4. Ekran görüntüsünü son çare olarak kullan.** Metinle anlatılabiliyorsa metinle anlat.
Görsel en hızlı eskiyen ve güncellemesi en pahalı içerik. Zorunluysa konunun kendi
`gorseller/` klasörüne koy, adına tarih yaz.

Dil ve biçim kuralları: [BAKIM.md § 7](BAKIM.md)
Klasör ve isimlendirme kuralları: [KONU-EKLEME.md](KONU-EKLEME.md)

## Kabul edilmeyenler

Peşinen bilinsin ki emek boşa gitmesin:

- **Yapay zekâ ile üretilip okunmadan gönderilen içerik.** Taslak için kullanman sorun değil,
  hatta faydalı — ama gönderdiğin her komutu kendi makinende çalıştırmış olman gerekiyor.
  Çalışmayan komut, öğrenen kişiyi bir saat kaybettirir.
- **Başka kaynaktan kopyalanmış metin.** Kendi cümlelerinle yaz; alıntı yapıyorsan kaynak ver.
- **Kapsam dışı içerik.** Belirli bir ürünün reklamı, kişisel blog yönlendirmesi, kurs satışı.
- **Müfredat dışı sayfa.** Yeni konu iyi bir fikir olabilir ama önce issue'da konuşulur.
- **Tek PR'da devasa değişiklik.** 10 dosyayı aynı anda değiştiren PR incelenemez; böl.

## İnceleme

PR'lar genelde birkaç gün içinde incelenir. Bakılan şeyler:

- Otomatik kontrol geçti mi
- Şablona uygun mu, künye dolu mu
- Komutlar gerçekten çalışıyor mu
- Anlatım, hedeflenen seviyedeki birine hitap ediyor mu

Değişiklik istenmesi normaldir ve içeriğin kötü olduğu anlamına gelmez — bu depoda tutarlılık,
tek tek sayfaların mükemmelliğinden daha önemli. İstenen düzeltmeler açık ve gerekçeli yazılır;
"şöyle olsun" değil, "şu yüzden şöyle olsun".

## Katkı verenler

Birleştirilen her PR sahibi, deponun katkı verenler listesinde yer alır. Bir sayfayı baştan
yazdıysan, sayfanın altına adını ve profil linkini ekleyebilirsin.

## Sorular

Takıldığın yerde issue aç ya da mevcut bir issue'ya yorum yaz. "Bu soru aptalca mı" diye
düşünme — bu depo zaten o soruları cevaplamak için var.

---

Katılan herkesin [Davranış Kuralları](DAVRANIS-KURALLARI.md)'na uyması beklenir.
