# Kapatma Zamanlayıcısı 電腦關機計時器

![GitHub release (latest by date)](https://img.shields.io/github/v/release/vasbabas/Kapatma_Sayaci_Projesi?style=for-the-badge)
![GitHub all releases](https://img.shields.io/github/downloads/vasbabas/Kapatma_Sayaci_Projesi/total?style=for-the-badge)
![GitHub stars](https://img.shields.io/github/stars/vasbabas/Kapatma_Sayaci_Projesi?style=for-the-badge)
![GitHub license](https://img.shields.io/github/license/vasbabas/Kapatma_Sayaci_Projesi?style=for-the-badge)

Windows için geliştirilmiş, şık ve kullanışlı bir bilgisayar kapatma zamanlayıcısı. Bilgisayarınızı istediğiniz saat ve dakika sonra otomatik olarak kapatın!

---

## 📖 Proje Hakkında

Bu proje, "bilgisayarı açık unuttum" derdine son vermek için geliştirilmiştir. Basit ve sezgisel arayüzü sayesinde, birkaç tıkla bilgisayarınızın ne zaman kapanacağını ayarlayabilir ve arkanıza yaslanabilirsiniz. İster bir dosya indiriyor olun, ister bir işlemi tamamlamasını bekleyin; Kapatma Zamanlayıcısı görevi sizin için tamamlar.

## ✨ Öne Çıkan Özellikler

⏰ **Esnek Zamanlama:** Hem saat hem de dakika cinsinden geri sayım ayarlama.
🚀 **Kullanıcı Dostu Kurulum:** `setup.exe` ile saniyeler içinde kolayca kurun.
🖥️ **Kısayol Desteği:** Kurulum sırasında Masaüstü ve Başlat Menüsü'ne kısayol ekleme seçeneği.
🗑️ **Temiz Kaldırma:** Denetim Masası'ndan tek tıkla programı tamamen kaldırabilme.
 iptal **İptal Seçeneği:** Başlatılmış bir zamanlayıcıyı istediğiniz an iptal etme.
📊 **Durum Bildirimi:** Zamanlayıcının durumunu (aktif, iptal edildi, kalan süre) anlık olarak gösteren arayüz.

---

## 🚀 Hızlı Kurulum (Tavsiye Edilen)

Programı kullanmanın en kolay yolu, sizin için hazırlanan kurulum dosyasını indirmektir.

1.  Projenin **[en son sürüm sayfasına gidin](https://github.com/vasbabas/Kapatma_Sayaci_Projesi/releases/latest)**.
2.  `Assets` (Dosyalar) bölümü altındaki `setup_kapatma_sayaci.exe` dosyasını indirin.
3.  İndirdiğiniz dosyayı çalıştırın ve kurulum sihirbazındaki adımları takip edin.

İşte bu kadar! Program artık bilgisayarınıza kuruldu.

## 💻 Kullanım

1.  Masaüstünüzdeki veya Başlat Menüsü'ndeki "Kapatma Zamanlayıcısı" kısayoluna tıklayarak programı başlatın.
2.  İlgili kutucuklara bilgisayarın kaç **saat** ve/veya kaç **dakika** sonra kapanmasını istediğinizi girin.
3.  `Zamanlayıcıyı Başlat` butonuna basın.
4.  Geri sayımı durdurmak isterseniz `İptal Et` butonunu kullanabilirsiniz.

---

## 👨‍💻 Geliştiriciler İçin (Kaynak Koddan Çalıştırma)

Bu projeye katkıda bulunmak veya kaynak kodunu kendiniz derlemek isterseniz aşağıdaki adımları izleyebilirsiniz.

### Gereksinimler

* [Python 3.x](https://www.python.org/downloads/)
* [Inno Setup](https://jrsoftware.org/isdl.php) (Kurulum dosyası oluşturmak için)

### Kurulum

1.  Projeyi klonlayın:
    ```sh
    git clone [https://github.com/vasbabas/Kapatma_Sayaci_Projesi.git](https://github.com/vasbabas/Kapatma_Sayaci_Projesi.git)
    ```
2.  Proje dizinine gidin:
    ```sh
    cd Kapatma_Sayaci_Projesi
    ```
3.  Bu proje standart `tkinter` kütüphanesini kullandığı için ek bir Python paket kurulumu gerektirmez.

### Derleme

1.  **Çalıştırılabilir `.exe` dosyası oluşturmak için:**
    * `pyinstaller` paketini kurun: `pip install pyinstaller`
    * Aşağıdaki komutu çalıştırın:
        ```sh
        pyinstaller --onefile --windowed --icon=icon.ico kapatma_sayaci.py
        ```

2.  **Kurulum dosyası (`setup.exe`) oluşturmak için:**
    * Inno Setup programını kurun.
    * Proje içindeki `setup_script.iss` dosyasına sağ tıklayıp `Compile` seçeneğini seçin.

## 🤝 Katkıda Bulunma

Katkılarınız projeyi daha iyi bir hale getirecektir! Lütfen bir "pull request" açmaktan veya "issue" oluşturmaktan çekinmeyin.

1.  Projeyi Fork'layın.
2.  Yeni bir Feature Branch'i oluşturun (`git checkout -b feature/AmazingFeature`).
3.  Değişikliklerinizi Commit'leyin (`git commit -m 'Add some AmazingFeature'`).
4.  Branch'inizi Push'layın (`git push origin feature/AmazingFeature`).
5.  Bir Pull Request açın.

Proje Linki: [https://github.com/vasbabas/Kapatma_Sayaci_Projesi](https://github.com/vasbabas/Kapatma_Sayaci_Projesi)
