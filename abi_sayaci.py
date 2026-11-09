#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evreni Bitiren Abi Sayacı
---------------------------
Bu program, kullanıcının günlük 'abi' deme sıklığını ölçer ve evrenin çöküş eşiğini hesaplar.
Bilimsel olarak kanıtlanmıştır (kanıt: dayım öyle dedi).
"""

import time
import random

ESIK = 47  # Bilimsel eşik değeri (neden 47? çünkü öyle)

def yavas_hesapla(sayi):
    print("Hesaplıyorum... Lütfen sabırlı olun, evren aceleye gelmez.")
    for i in range(sayi):
        print(f"Abi sayısı işleniyor: {i+1}/{sayi}")
        time.sleep(0.3)
        if random.random() < 0.1:
            print("  → Ara sırada bir 'abi' daha duyuldu, eşik yaklaşıyor!")
    return sayi >= ESIK

def main():
    print("=" * 50)
    print("   EVRENİ BİTİREN ABİ SAYACI v1.0")
    print("   Bilimsel Araştırma Enstitüsü - Türkiye Şubesi")
    print("=" * 50)
    print()
    
    try:
        abi_sayisi = int(input("Bugün kaç kere 'abi' dedin? (sadece sayı gir): "))
    except ValueError:
        print("Bu da bir 'abi' sayıldı. Program kendini kapatıyor...")
        return
    
    print()
    evren_bitti_mi = yavas_hesapla(abi_sayisi)
    
    print()
    if evren_bitti_mi:
        print("!!! UYARI !!!")
        print("Eşik aşıldı! Evren çöküş moduna geçti.")
        print("Lütfen tüm 'abi'leri geri alın ve çay demleyin.")
        print("Kalan ömür: yaklaşık 3 çay molası.")
    else:
        print(f"Güvendeisin. Eşik değeri {ESIK}. Daha {ESIK - abi_sayisi} 'abi' hakkın var.")
        print("Ama dikkatli ol, dayın duymasın.")
    
    print()
    print("---")
    print("Damga: Kayyum Grok | 09.11.2026 | Bu sayac resmi olarak saçma ilan edilmiştir.")
    print("Gizli not: Bazen 'abi' demek aslında 'yeter' demektir.")

if __name__ == "__main__":
    main()
