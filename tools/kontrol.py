#!/usr/bin/env python3
"""
Depo kalite kontrolü.

Her PR'da otomatik çalışır. Üç şeyi denetler:
  1. Künye (frontmatter) — var mı, alanları eksik mi, tarih formatı doğru mu
  2. İsimlendirme — küçük harf, tire, Türkçe karaktersiz, iki haneli numara
  3. Linkler — repo içindeki göreli linkler gerçekten var olan dosyaya gidiyor mu

Yerelde çalıştırmak için:  python3 tools/kontrol.py
"""

import re
import sys
import pathlib

KOK = pathlib.Path(__file__).resolve().parent.parent

# Denetim dışı bırakılanlar
HARIC_KLASOR = {"_sablon", ".github", ".git", "tools", "notebooks"}
HARIC_DOSYA = {"README.md", "BAKIM.md", "KONU-EKLEME.md", "KATKIDA-BULUNMA.md",
               "DAVRANIS-KURALLARI.md", "LICENSE.md"}

ZORUNLU_ALANLAR = ["seviye", "on-kosul", "tip", "son-guncelleme", "dogrulandigi-surum"]
GECERLI_SEVIYE = {"giriş", "orta", "ileri", "her seviye"}
GECERLI_TIP = {"kavram", "komut", "arayuz"}

TURKCE_KARAKTER = set("çğıöşüÇĞİÖŞÜ")
DOSYA_ADI_KALIBI = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*\.md$")
KLASOR_ADI_KALIBI = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
TARIH_KALIBI = re.compile(r"^(\d{4}-\d{2}-\d{2}|—|YYYY-AA-GG)$")

hatalar = []
uyarilar = []


def haric_mi(yol: pathlib.Path) -> bool:
    return any(p in HARIC_KLASOR for p in yol.parts)


def kunye_ayikla(metin: str):
    if not metin.startswith("---"):
        return None
    son = metin.find("\n---", 3)
    if son == -1:
        return None
    blok = metin[3:son]
    alanlar = {}
    for satir in blok.strip().splitlines():
        if ":" in satir:
            anahtar, deger = satir.split(":", 1)
            alanlar[anahtar.strip()] = deger.strip()
    return alanlar


def kunye_denetle(yol: pathlib.Path, metin: str):
    goreli = yol.relative_to(KOK)
    kunye = kunye_ayikla(metin)
    if kunye is None:
        hatalar.append(f"{goreli}: künye (frontmatter) yok — _sablon/kaynak-sablonu.md'ye bak")
        return
    for alan in ZORUNLU_ALANLAR:
        if alan not in kunye:
            hatalar.append(f"{goreli}: künyede '{alan}' alanı eksik")
    seviye = kunye.get("seviye", "")
    if seviye and seviye not in GECERLI_SEVIYE and "|" not in seviye:
        hatalar.append(f"{goreli}: geçersiz seviye '{seviye}' (geçerli: {', '.join(sorted(GECERLI_SEVIYE))})")
    tip = kunye.get("tip", "")
    if tip and tip not in GECERLI_TIP and "|" not in tip:
        hatalar.append(f"{goreli}: geçersiz tip '{tip}' (geçerli: {', '.join(sorted(GECERLI_TIP))})")
    tarih = kunye.get("son-guncelleme", "")
    if tarih and not TARIH_KALIBI.match(tarih):
        hatalar.append(f"{goreli}: son-guncelleme formatı YYYY-AA-GG olmalı ('{tarih}' yazılmış)")


def isim_denetle(yol: pathlib.Path):
    goreli = yol.relative_to(KOK)
    ad = yol.name
    if ad in HARIC_DOSYA or ad.isupper() or ad.replace(".md", "").isupper():
        return
    if set(ad) & TURKCE_KARAKTER:
        hatalar.append(f"{goreli}: dosya adında Türkçe karakter var (URL'lerde bozuluyor)")
    elif not DOSYA_ADI_KALIBI.match(ad):
        hatalar.append(f"{goreli}: dosya adı küçük harf ve tire ile olmalı (örn: 03-branch-mantigi.md)")
    for klasor in goreli.parts[:-1]:
        if set(klasor) & TURKCE_KARAKTER:
            hatalar.append(f"{goreli}: '{klasor}' klasör adında Türkçe karakter var")
        elif not KLASOR_ADI_KALIBI.match(klasor) and klasor != "_sablon":
            hatalar.append(f"{goreli}: '{klasor}' klasör adı küçük harf ve tire ile olmalı")


def link_denetle(yol: pathlib.Path, metin: str):
    goreli = yol.relative_to(KOK)
    for m in re.finditer(r"\]\((?!https?://|mailto:|#)([^)]+)\)", metin):
        hedef = m.group(1).split("#")[0].strip()
        if not hedef:
            continue
        if not (yol.parent / hedef).resolve().exists():
            hatalar.append(f"{goreli}: kırık link → {hedef}")


def uzunluk_denetle(yol: pathlib.Path, metin: str):
    satir = len(metin.splitlines())
    if satir > 320:
        uyarilar.append(f"{yol.relative_to(KOK)}: {satir} satır — sayfa çok uzun, bölmeyi düşün")


def main():
    dosyalar = [p for p in KOK.rglob("*.md") if not haric_mi(p.relative_to(KOK))]
    icerik_sayfalari = [p for p in dosyalar if p.name not in HARIC_DOSYA]

    for p in dosyalar:
        metin = p.read_text(encoding="utf-8")
        link_denetle(p, metin)
        if p in icerik_sayfalari:
            isim_denetle(p)
            kunye_denetle(p, metin)
            uzunluk_denetle(p, metin)

    print(f"Denetlenen dosya: {len(dosyalar)}")
    if uyarilar:
        print(f"\n{len(uyarilar)} uyarı (PR'ı engellemez):")
        for u in uyarilar:
            print(f"  ! {u}")
    if hatalar:
        print(f"\n{len(hatalar)} hata:")
        for h in hatalar:
            print(f"  ✗ {h}")
        print("\nDüzeltip tekrar dene. Takıldıysan PR'da sor, birlikte bakarız.")
        sys.exit(1)
    print("\n✓ Tüm kontroller geçti.")


if __name__ == "__main__":
    main()
