---
title: Bagaimana Cara Mengaktifkan 2FA pada Qontak Call Center
canonical_url: https://help-center.qontak.com/hc/id/articles/52747601688217-Bagaimana-Cara-Mengaktifkan-2FA-pada-Qontak-Call-Center
article_type: task
solvability_type: tool
products:
- Bizphone
product_surface: mobile
language: id
intent_tags:
- call-center
- enable-2fa
- call-voice
query_examples:
- Cara Mengaktifkan 2FA pada Qontak Call Center
- Bagaimana cara Mengaktifkan 2FA pada Qontak Call Center?
- Langkah-langkah Mengaktifkan 2FA pada Qontak Call Center di Bizphone
- How do I Mengaktifkan 2FA pada Qontak Call Center?
- Mau Mengaktifkan 2FA pada Qontak Call Center, caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

- Akun Qontak Call Center aktif dengan peran Admin atau pengguna organisasi
- Email Anda sudah terverifikasi di sistem Qontak
- Akses ke aplikasi Authenticator dari App Store atau Google Play (opsional, hanya jika menggunakan metode Authenticator)
- Akses ke email yang terdaftar untuk menerima kode verifikasi 2FA
- Admin domain/organisasi telah mewajibkan 2FA pada akun Anda (atau Anda mengaktifkannya secara manual)

## Steps  <!-- confidence:high ✓ -->


Saat Admin _domain_ /organisasi mewajibkan 2FA untuk para penggunanya, pengguna harus melalui proses awal pengaturan 2FA pada saat login berikutnya.
Autentikasi Dua Faktor atau 2FA memberikan lapisan keamanan tambahan pada akun Anda. Setelah fitur ini diaktifkan, kami akan mengirimkan kode verifikasi ke email Anda setiap kali Anda melakukan login.
Pastikan email Anda sudah terverifikasi sebelum mengaktifkan fitur.
Pada penjelasan berikut ini, Anda akan mempelajari mulai dari cara mengaktifkan 2FA secara manual, menerapkan _Recovery key_ hingga mengaktifkan 2FA menggunakan aplikasi _Authenticator_. 
### A. Cara Mengaktifkan 2FA [](https://help-center.qontak.com/hc/id/articles/52747601688217-Bagaimana-Cara-Mengaktifkan-2FA-pada-Qontak-Call-Center#h_01KAX2MXY2E3HA2HJ53B59510W)
Untuk mengaktifkan 2FA pada akun Anda, ikuti langkah-langkah berikut:
  1. Masuk ke akun Call center Anda.
  2. Klik ikon profil, kemudian pilih **“Manage Account”**.  
**![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52747638213401)**
  3. Kemudian klik tab **“Security and credentials”**.  
**![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52747622589977)**
  4. Lalu, klik aktifkan **“Enable Two-Factor Authentication”**.  
**![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52747622599449)**
  5. Klik **“Send verification code”** kemudian sistem akan mengirimkan kode verifikasi ke email Anda. Periksa email, lalu masukan **Verification code**. Selanjutnya klik **“Continue”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52747622600089)
  6. Lalu akan muncul _pop up_ informasi berikut. Klik**“Download** untuk mengunduh **Recovery Key** Anda.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52747622602393)

Recovery Key dapat digunakan untuk mengakses akun Anda jika Anda kehilangan akses ke email dan tidak dapat menerima kode**Two-Factor Authentication**. Berikut merupakan hal-hal penting terkait **Recovery Key** :  
- Perlakukan **Recovery Key** dengan tingkat perhatian yang sama seperti ketika Anda menjaga kata sandi.  
- Simpan **Recovery Key** di tempat yang aman untuk mencegah risiko terkunci dari akun Anda.
  7. Setelah Anda mengaktifkan 2FA, saat masuk berikutnya ke portal Anda akan diminta untuk memasukkan kode 2FA yang dikirim ke alamat email Anda, atau menggunakan **Recovery Key** untuk login.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52747622605209)

### B. Cara Mengaktifkan 2FA dengan Aplikasi Authenticator[](https://help-center.qontak.com/hc/id/articles/52747601688217-Bagaimana-Cara-Mengaktifkan-2FA-pada-Qontak-Call-Center#h_01KAX2MXYV72SV5HVCFY547JCK)
Aplikasi **Authenticator** digunakan untuk **two-factor authentication (2FA)** karena memberikan lapisan keamanan tambahan selain hanya menggunakan _username_ dan _password_.
Aplikasi **Authenticator** menawarkan metode yang aman, praktis, dan hemat biaya untuk menerapkan autentikasi dua faktor, sehingga memberikan perlindungan kuat terhadap akses yang tidak sah.
Untuk mengaktifkan autentikasi 2FA, ikuti langkah-langkah berikut:
  1. Masuk ke akun **Qontak Call Center** Anda.
  2. Klik ikon profil, kemudian pilih **“Manage Account”**.  
**![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52747638213401)**
  3. Lalu klik tab **“Security and credentials”**.  
**![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52747622589977)**

## Error States  <!-- confidence:medium ~ -->

- **Email belum terverifikasi**: Jika email Anda belum diverifikasi, Anda tidak dapat mengaktifkan 2FA. Solusi: Verifikasi email Anda terlebih dahulu melalui pengaturan profil sebelum mengaktifkan 2FA.
- **Kode verifikasi tidak diterima**: Jika kode 2FA tidak sampai ke email, periksa folder Spam atau Junk. Klik **"Send verification code"** kembali untuk meminta kode baru.
- **QR code tidak dapat dipindai (metode Authenticator)**: Pastikan pencahayaan cukup dan kamera perangkat Anda berfungsi. Coba pindai ulang atau masukkan kode setup secara manual dari aplikasi Authenticator.
- **Recovery Key hilang**: Jika Anda tidak mengunduh Recovery Key, hubungi support Qontak untuk bantuan pemulihan akses.

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support jika:
- Email Anda tidak dapat diverifikasi
- Anda tidak menerima kode verifikasi 2FA setelah menunggu 10 menit
- Anda mengalami error saat mengaktifkan fitur 2FA
- Anda kehilangan akses ke email dan Recovery Key Anda juga hilang
- Anda lupa password dan tidak dapat masuk untuk mengatur 2FA

Sediakan informasi:
- Email akun Qontak Anda
- Nama organisasi/domain
- Pesan error lengkap (jika ada)
- Screenshot layar saat error terjadi