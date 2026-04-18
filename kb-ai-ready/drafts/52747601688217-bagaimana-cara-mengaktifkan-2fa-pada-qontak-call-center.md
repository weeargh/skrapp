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

**Metode 1: Aktivasi 2FA dengan Email**

1. Masuk ke akun Qontak Call Center Anda.
2. Klik ikon profil di sudut kanan atas, kemudian pilih tombol **"Manage Account"**. Sistem akan membuka halaman pengaturan akun.
3. Klik tab **"Security and credentials"**. Anda akan melihat bagian Two-Factor Authentication.
4. Klik tombol **"Enable Two-Factor Authentication"**.
5. Klik tombol **"Send verification code"**. Sistem akan mengirimkan kode verifikasi ke email terdaftar Anda.
6. Buka email Anda, salin kode verifikasi, dan masukkan ke kolom Verification code di aplikasi. Klik tombol **"Continue"**.
7. Jendela pop-up akan muncul menampilkan Recovery Key Anda. Klik tombol **"Download"** untuk menyimpan Recovery Key sebagai file.
8. Sistem akan menampilkan pesan konfirmasi bahwa 2FA berhasil diaktifkan.

**Metode 2: Aktivasi 2FA dengan Aplikasi Authenticator**

1. Masuk ke akun Qontak Call Center Anda.
2. Klik ikon profil, kemudian pilih **"Manage Account"**.
3. Klik tab **"Security and credentials"**.
4. Scroll ke bawah hingga menemukan bagian **Two-Factor Authentication**.
5. Pastikan Anda sudah mengunduh aplikasi Authenticator dari App Store atau Google Play terlebih dahulu.
6. Klik tombol untuk mengaktifkan metode berbasis Authenticator.
7. Sistem akan menampilkan QR code. Buka aplikasi Authenticator Anda dan pindai QR code tersebut.
8. Aplikasi Authenticator akan menghasilkan kode 6 digit. Masukkan kode ini ke kolom verifikasi di Qontak Call Center dan klik **"Verify"**.
9. Jendela pop-up akan menampilkan Recovery Key Anda. Klik **"Download"** untuk menyimpannya di tempat aman.
10. Sistem akan menampilkan pesan konfirmasi bahwa 2FA dengan Authenticator berhasil diaktifkan.

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/52747638213401

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/52747622589977

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/52747622599449

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/52747622600089

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/52747622602393

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/52747622605209

## Expected Result  <!-- confidence:high ✓ -->

- Fitur 2FA berhasil diaktifkan pada akun Anda
- Pesan konfirmasi "Two-Factor Authentication has been enabled" ditampilkan di layar
- Recovery Key berhasil diunduh dan tersimpan
- Pada login berikutnya, Anda akan diminta memasukkan kode 2FA yang dikirim ke email atau dihasilkan oleh aplikasi Authenticator
- Akun Anda sekarang terlindungi dengan lapisan keamanan tambahan

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