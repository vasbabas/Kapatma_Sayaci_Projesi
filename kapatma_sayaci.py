import tkinter as tk
from tkinter import messagebox
import os
import threading
import time

# --- ANA FONKSİYONLAR ---

def zamanlayiciyi_baslat():
    """Kullanıcının girdiği saat ve dakikayı saniyeye çevirir ve geri sayımı başlatır."""
    global geri_sayim_aktif
    global kalan_saniye

    try:
        saat = int(saat_girisi.get() or 0)
        dakika = int(dakika_girisi.get() or 0)
    except ValueError:
        messagebox.showerror("Hata", "Lütfen sadece sayı giriniz!")
        return

    toplam_saniye = (saat * 3600) + (dakika * 60)
    kalan_saniye = toplam_saniye

    if toplam_saniye <= 0:
        messagebox.showwarning("Uyarı", "Lütfen geçerli bir süre giriniz!")
        return

    # Windows'un kapatma komutunu ayarla
    os.system(f"shutdown /s /t {toplam_saniye}")
    
    # Butonları ve giriş alanlarını devre dışı bırak
    baslat_butonu.config(state=tk.DISABLED)
    iptal_butonu.config(state=tk.NORMAL)
    saat_girisi.config(state=tk.DISABLED)
    dakika_girisi.config(state=tk.DISABLED)

    geri_sayim_aktif = True
    # Geri sayım için yeni bir thread başlat
    threading.Thread(target=geri_sayimi_guncelle, daemon=True).start()
    
    status_label.config(text=f"{saat} saat {dakika} dakika sonra kapatılacak.", fg="green")

def zamanlayiciyi_iptal_et():
    """Planlanmış kapatma işlemini iptal eder."""
    global geri_sayim_aktif
    
    # Windows'un kapatma iptal komutunu çalıştır
    os.system("shutdown /a")
    
    # Butonları ve giriş alanlarını tekrar aktif et
    baslat_butonu.config(state=tk.NORMAL)
    iptal_butonu.config(state=tk.DISABLED)
    saat_girisi.config(state=tk.NORMAL)
    dakika_girisi.config(state=tk.NORMAL)
    
    geri_sayim_aktif = False
    status_label.config(text="Kapatma zamanlayıcısı iptal edildi.", fg="red")
    zaman_label.config(text="00:00:00")

def geri_sayimi_guncelle():
    """Ekranda geri sayımı gösterir."""
    global kalan_saniye
    global geri_sayim_aktif

    while kalan_saniye > 0 and geri_sayim_aktif:
        saatler = kalan_saniye // 3600
        dakikalar = (kalan_saniye % 3600) // 60
        saniyeler = kalan_saniye % 60
        
        zaman_formati = f"{saatler:02d}:{dakikalar:02d}:{saniyeler:02d}"
        zaman_label.config(text=zaman_formati)
        
        time.sleep(1)
        kalan_saniye -= 1
    
    if geri_sayim_aktif:
        zamanlayiciyi_iptal_et() # Zaman dolunca arayüzü sıfırla

def pencereyi_kapat():
    """Pencere kapatılırken zamanlayıcının iptal edilip edilmeyeceğini sorar."""
    if geri_sayim_aktif:
        if messagebox.askyesno("Onay", "Zamanlayıcı aktif. Çıkmak istediğinize emin misiniz? (Kapatma işlemi iptal edilecek)"):
            zamanlayiciyi_iptal_et()
            pencere.destroy()
    else:
        pencere.destroy()


# --- ARAYÜZ KURULUMU ---

pencere = tk.Tk()
pencere.title("Kapatma Zamanlayıcısı")
pencere.geometry("350x300")
pencere.resizable(False, False)

# Değişkenler
geri_sayim_aktif = False
kalan_saniye = 0

# Arayüz Elemanları
ana_cerceve = tk.Frame(pencere, padx=20, pady=20)
ana_cerceve.pack()

tk.Label(ana_cerceve, text="Bilgisayarı Ne Zaman Kapatmak İstersin?", font=("Helvetica", 12)).pack(pady=10)

giris_cercevesi = tk.Frame(ana_cerceve)
giris_cercevesi.pack(pady=5)

saat_girisi = tk.Entry(giris_cercevesi, width=5)
saat_girisi.pack(side=tk.LEFT, padx=5)
tk.Label(giris_cercevesi, text="saat").pack(side=tk.LEFT)

dakika_girisi = tk.Entry(giris_cercevesi, width=5)
dakika_girisi.pack(side=tk.LEFT, padx=5)
tk.Label(giris_cercevesi, text="dakika").pack(side=tk.LEFT)

buton_cercevesi = tk.Frame(ana_cerceve)
buton_cercevesi.pack(pady=20)

baslat_butonu = tk.Button(buton_cercevesi, text="Zamanlayıcıyı Başlat", command=zamanlayiciyi_baslat)
baslat_butonu.pack(side=tk.LEFT, padx=10)

iptal_butonu = tk.Button(buton_cercevesi, text="İptal Et", command=zamanlayiciyi_iptal_et, state=tk.DISABLED)
iptal_butonu.pack(side=tk.LEFT, padx=10)

status_label = tk.Label(ana_cerceve, text="Lütfen bir süre girip başlatın.", font=("Helvetica", 10), wraplength=300)
status_label.pack(pady=10)

zaman_label = tk.Label(ana_cerceve, text="00:00:00", font=("Courier", 24, "bold"))
zaman_label.pack(pady=10)

# Pencere kapatma protokolü
pencere.protocol("WM_DELETE_WINDOW", pencereyi_kapat)

pencere.mainloop()