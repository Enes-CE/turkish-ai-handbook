#!/usr/bin/env python3
"""
Konu bazlı yazım durumu raporu.

Her konu klasörünü (README.md + HATA-INDEKSI.md ikilisini birlikte barındıran klasörler)
tarar, içindeki sayfaların iskelet mi yoksa yazılmış mı olduğunu tespit eder ve konunun
README'sindeki [x]/[ ] işaretleriyle karşılaştırır.

Sadece rapor basar, hiçbir dosyayı değiştirmez.

Çalıştırmak için:  python3 tools/durum.py
"""

import re
import sys
import pathlib

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

KOK = pathlib.Path(__file__).resolve().parent.parent

# Denetim dışı bırakılanlar
HARIC_KLASOR = {"_sablon", ".github", ".git", "tools", "notebooks", "gorseller"}

# Bir sayfanın iskelet olduğunu gösteren iz. Biçimlendirme (kalın, blok alıntı vb.)
# değişse de bu ifade sabit kalıyor.
ISKELET_IZI = "Bu sayfa henüz yazılmadı"

CHECKLIST_KALIBI = re.compile(r"^- \[([ xX])\] \[.*?\]\(([^)]+)\)", re.MULTILINE)


def haric_mi(yol: pathlib.Path) -> bool:
    return any(p in HARIC_KLASOR for p in yol.relative_to(KOK).parts)


def konu_klasorlerini_bul():
    konular = []
    for readme in sorted(KOK.rglob("README.md")):
        klasor = readme.parent
        if klasor == KOK or haric_mi(klasor):
            continue
        if (klasor / "HATA-INDEKSI.md").exists():
            konular.append(klasor)
    return konular


def sayfa_yazilmis_mi(yol: pathlib.Path) -> bool:
    metin = yol.read_text(encoding="utf-8")
    return ISKELET_IZI not in metin


def konu_sayfalarini_topla(klasor: pathlib.Path):
    sayfalar = []
    for p in klasor.rglob("*.md"):
        if haric_mi(p):
            continue
        if p.name in {"README.md", "HATA-INDEKSI.md"}:
            continue
        sayfalar.append(p)
    return sorted(sayfalar)


def readme_tutarliligini_kontrol_et(klasor: pathlib.Path):
    readme_metin = (klasor / "README.md").read_text(encoding="utf-8")
    uyarilar = []
    for esleme in CHECKLIST_KALIBI.finditer(readme_metin):
        isaretli = esleme.group(1).lower() == "x"
        hedef = esleme.group(2).split("#")[0].strip()
        if not hedef or hedef.startswith(("http://", "https://")):
            continue
        hedef_yolu = (klasor / hedef).resolve()
        if not hedef_yolu.exists():
            uyarilar.append(f"{hedef}: README'de linkli ama dosya yok")
            continue
        gercek_yazilmis = sayfa_yazilmis_mi(hedef_yolu)
        if isaretli and not gercek_yazilmis:
            uyarilar.append(f"{hedef}: README'de [x] işaretli ama sayfa hâlâ iskelet")
        elif not isaretli and gercek_yazilmis:
            uyarilar.append(f"{hedef}: sayfa yazılmış ama README'de [ ] işaretli")
    return uyarilar


def main():
    konular = konu_klasorlerini_bul()
    if not konular:
        print("Hiç konu klasörü bulunamadı.")
        return

    toplam_yazilan = 0
    toplam_sayfa = 0

    for klasor in konular:
        ad = klasor.relative_to(KOK).as_posix()
        sayfalar = konu_sayfalarini_topla(klasor)
        toplam = len(sayfalar)
        yazilan = sum(1 for p in sayfalar if sayfa_yazilmis_mi(p))
        toplam_yazilan += yazilan
        toplam_sayfa += toplam

        print(f"\n{ad}")
        print(f"  Yazılan: {yazilan}/{toplam}")

        uyarilar = readme_tutarliligini_kontrol_et(klasor)
        if uyarilar:
            for u in uyarilar:
                print(f"  ⚠ {u}")
        else:
            print("  ✓ README işaretleri tutarlı")

    print(f"\nToplam: {toplam_yazilan}/{toplam_sayfa} sayfa yazıldı")


if __name__ == "__main__":
    main()
