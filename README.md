# Yapay Zekâ El Kitabı

> Türkçe yapay zekâ öğrenme kaynakları — *Turkish-language AI learning resources*

Türkçe, ücretsiz ve sürekli güncellenen bir yapay zekâ öğrenme kaynağı deposu.
Sıfırdan başlayan biri için baştan sona bir yol; belli bir konuda takılan biri için ise
tek tek okunabilen bağımsız sayfalar.

Her sayfa **tek bir soruya cevap verir**, seviyesi ve ön koşulu bellidir.

---

## Konular

| # | Konu | Kapsam | Durum |
|---|---|---|---|
| 00 | [Araçlar](00-araclar/) | Git & GitHub, terminal, sanal ortamlar, Colab | 🟡 Git/GitHub, Terminal yazılıyor |
| 01 | [Python](01-python/) | Temel sözdiziminden veri işlemeye | ⚪ Planlandı |
| 02 | [Makine Öğrenmesi](02-makine-ogrenmesi/) | Kavramlar, model kurma, değerlendirme | ⚪ Planlandı |
| 03 | [Derin Öğrenme](03-derin-ogrenme/) | Sinir ağları, eğitim, mimariler | ⚪ Planlandı |
| 04 | [Generative AI](04-generative-ai/) | LLM'ler, prompt, RAG, ajanlar | ⚪ Planlandı |

🟢 tamamlandı · 🟡 devam ediyor · ⚪ planlandı

**Araçlar bölümü neden 00?** Diğer dört konunun hepsinde ihtiyaç duyulduğu için. Hangi konudan
başlarsan başla, bir noktada Git'e ve terminale ihtiyacın olacak.

---

## Nereden başlamalıyım?

| Durumun | Başlangıç noktan |
|---|---|
| Hiç kod yazmadım | [Python](01-python/) → sonra [Araçlar](00-araclar/) |
| Kod yazıyorum, Git bilmiyorum | [Git & GitHub](00-araclar/git-github/) |
| Bootcamp'e katıldım, projeye başlayacağım | [Git & GitHub](00-araclar/git-github/) → ilgili konu |
| Belirli bir hata alıyorum | İlgili konunun `HATA-INDEKSI.md` dosyası |

---

## Sayfalar nasıl okunur?

Her sayfanın başında bir künye var:

| Alan | Ne işe yarar |
|---|---|
| `seviye` | giriş / orta / ileri |
| `on-kosul` | Bu sayfadan önce okunması gereken sayfa |
| `tip` | kavram / komut / arayuz — arayüz sayfaları en hızlı eskiyenler |
| `son-guncelleme` | İçeriğin en son ne zaman doğrulandığı |

---

## Katkıda bulunmak

Bu depo topluluk katkısına açık ve katkı vermek için uzman olman gerekmiyor. Yazım hatası
düzeltmek de bir sayfayı baştan yazmak da değerli.

- İlk katkın olacaksa: **`iyi-ilk-katki`** etiketli issue'lara bak
- Yeni sayfa yazacaksan: önce ilgili issue'ya yorum bırak, sana atansın
- Göndermeden önce: `python3 tools/kontrol.py`

Kuralların tamamı → **[KATKIDA-BULUNMA.md](KATKIDA-BULUNMA.md)**

PR göndermeyi bilmiyorsan sorun değil — [tam olarak burada anlatılıyor](00-araclar/git-github/).
İlk PR'ını bu depoya atmak, öğrendiğini uygulamanın en iyi yolu.

## Bakımcılar için

| Dosya | İçeriği |
|---|---|
| [KATKIDA-BULUNMA.md](KATKIDA-BULUNMA.md) | Katkı süreci, kabul/ret kriterleri, inceleme |
| [BAKIM.md](BAKIM.md) | İçeriğin güncel tutulması, bakım takvimi, yazım kuralları |
| [KONU-EKLEME.md](KONU-EKLEME.md) | Yeni konu klasörü açma adımları, isimlendirme |
| [DAVRANIS-KURALLARI.md](DAVRANIS-KURALLARI.md) | Topluluk kuralları |
| [_sablon/](_sablon/) | Sayfa, konu README ve hata indeksi şablonları |
| [tools/kontrol.py](tools/kontrol.py) | Künye, isimlendirme ve link denetimi |

## Lisans

İçerik [CC BY 4.0](LICENSE.md) — kaynak göstererek serbestçe kullanılabilir, çoğaltılabilir.
