---
title: Bagaimana Cara Melakukan Integrasi dan Mengatur Konfigurasi Channel pada Qontak
  CRM
canonical_url: https://help-center.qontak.com/hc/id/articles/15545770743065-Bagaimana-Cara-Melakukan-Integrasi-dan-Mengatur-Konfigurasi-Channel-pada-Qontak-CRM
article_type: task
solvability_type: tool
products:
- Qontak CRM
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- multi-channel-integration
- configure-konfigurasi-channel
- conversation-management
query_examples:
- Cara Melakukan Integrasi dan Mengatur Konfigurasi Channel pada Qontak CRM
- Bagaimana cara Melakukan Integrasi dan Mengatur Konfigurasi Channel pada Qontak
  CRM?
- Langkah-langkah Melakukan Integrasi dan Mengatur Konfigurasi Channel pada Qontak
  CRM di Qontak CRM
- How do I Melakukan Integrasi dan Mengatur Konfigurasi Channel pada Qontak CRM?
- Mau Melakukan Integrasi dan Mengatur Konfigurasi Channel pada Qontak CRM, caranya
  gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk melakukan integrasi dan mengatur konfigurasi channel pada Qontak CRM, Anda memerlukan:

- Role **Owner** atau **Admin** pada akun Qontak CRM
- Akun Qontak Omnichannel yang aktif
- Token API Admin dari akun Omnichannel (user Admin tersebut juga harus berperan sebagai owner pada akun CRM)
- Akses ke menu **Properties** pada akun CRM Anda
- Setidaknya satu channel yang sudah dikonfigurasi di Omnichannel (WhatsApp, Instagram, atau channel lainnya)

## Steps  <!-- confidence:high ✓ -->

**Bagian A: Integrasi Channel dengan CRM**

1. Masuk ke akun **Qontak CRM** dan pilih menu **Properties**. Sistem akan menampilkan halaman konfigurasi akun.
2. Klik tombol **Channel Integration**. Halaman integrasi channel akan terbuka.
3. Klik tombol **Hubungkan**. Sistem akan menampilkan form input untuk memasukkan token API.
4. Salin dan masukkan **Omnichannel API token** dari akun Omnichannel Anda, lalu klik tombol **Hubungkan**. Sistem akan memverifikasi token dan menampilkan status koneksi berhasil.

**Bagian B: Konfigurasi Channel**

5. Setelah integrasi berhasil, klik tombol **Atur konfigurasi**. Sistem akan menampilkan dua pilihan integrasi.
6. Pilih salah satu opsi: **Integrasikan semua channel ke satu pipeline** atau **Integrasikan setiap channel ke pipeline berbeda**. Sistem akan menampilkan form konfigurasi sesuai pilihan Anda.
7. Tentukan modul tujuan (**Deals**, **Tiket**, atau keduanya) dan konfigurasi pipeline yang sesuai, lalu simpan. Sistem akan menampilkan konfirmasi konfigurasi berhasil disimpan.## Expected Result  <!-- confidence:high ✓ -->

Setelah menyelesaikan semua langkah, hasil yang diharapkan adalah:

- Halaman **Channel Integration** menampilkan status **Terhubung** dengan informasi akun Omnichannel Anda.
- Sistem akan secara otomatis membuat **Deal** atau **Tiket** baru ketika ada pesan masuk ke Omnichannel dari channel yang terintegrasi.
- Isi percakapan chat akan tersimpan pada timeline **Deal** atau **Tiket** di modul yang Anda pilih.
- Data pelanggan yang mengirimkan chat akan otomatis tersimpan di menu **Kontak** pada CRM Anda.
- Integrasi siap digunakan untuk mengelola komunikasi omnichannel dari dashboard CRM.

![4.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36773919924761)
![5.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36773912573337)
![6.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36773919928985)
![7.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36773912573977)
![8.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36773912577561)
![16.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36773912586137)
![17.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36773919946137)
![ID Integration.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36773912595481)
![19.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36773912602521)
![23.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36773919979417)
![15.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36773912635417)

## Error States  <!-- confidence:medium ~ -->

Kesalahan umum yang mungkin terjadi:

- **Token API tidak valid**: Pastikan Anda menyalin token API Admin yang benar dari akun Omnichannel. Token harus dari user yang juga berperan sebagai owner pada akun CRM.
- **Koneksi gagal**: Periksa koneksi internet Anda dan pastikan akun Omnichannel dan CRM aktif serta milik organisasi yang sama.
- **Tombol Atur konfigurasi tidak muncul**: Integrasi mungkin belum sepenuhnya berhasil. Coba logout dan login kembali ke akun CRM Anda.
- **Permission denied**: Hanya user dengan role **Owner** atau **Admin** yang dapat mengakses halaman **Channel Integration**. Hubungi administrator akun jika role Anda berbeda.

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support (support-qontak@mekari.com) jika Anda mengalami:

- Token API tidak diterima oleh sistem meski sudah benar.
- Integrasi berhasil tetapi Deal atau Tiket tidak otomatis terbuat dari pesan masuk.
- Tombol atau menu integrasi tidak muncul di akun CRM Anda.
- Data pelanggan tidak tersimpan di menu **Kontak** setelah integrasi.

Sertakan screenshot halaman error, ID akun CRM dan Omnichannel Anda, serta deskripsi masalah yang dialami.