---
title: Bagaimana Cara Mengelola dan Mengintegrasikan Qontak dengan Google My Business
canonical_url: https://help-center.qontak.com/hc/id/articles/38951713398937-Bagaimana-Cara-Mengelola-dan-Mengintegrasikan-Qontak-dengan-Google-My-Business
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- multi-channel-integration
- integrate-qontak-dengan-google-my-busine
- conversation-management
query_examples:
- Cara Mengelola dan Mengintegrasikan Qontak dengan Google My Business
- Bagaimana cara Mengelola dan Mengintegrasikan Qontak dengan Google My Business?
- Langkah-langkah Mengelola dan Mengintegrasikan Qontak dengan Google My Business
  di Qontak Omnichannel
- How do I Mengelola dan Mengintegrasikan Qontak dengan Google My Business?
- Mau Mengelola dan Mengintegrasikan Qontak dengan Google My Business, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk melakukan integrasi Qontak Omnichannel dengan Google My Business, Anda memerlukan:

- Peran Admin pada akun Qontak Omnichannel
- Akun Google Business yang telah terdaftar
- Lokasi bisnis yang telah diverifikasi di Google Business Profile Console (wajib untuk menerima review dari customer)
- Akses ke menu Channel Integration pada Qontak Omnichannel

Tanpa verifikasi lokasi di Google Business Profile Console, pesan review tidak dapat diterima oleh Qontak.

## Steps  <!-- confidence:high ✓ -->

1. Masuk ke akun Qontak Omnichannel Anda dengan peran Admin, kemudian buka menu **Integrations**.
2. Pilih submenu **Google My Business**. Sistem menampilkan halaman Google My Business Qontak.
3. Klik tombol **"Add business"**. Anda diarahkan ke halaman syarat dan langkah integrasi.
4. Klik **"Continue"**. Sistem membuka halaman Google Business untuk otorisasi.
5. Centang semua izin yang diperlukan agar Mekari Qontak dapat mengelola profil bisnis Google Anda.
6. Kembali ke halaman utama Google My Business pada Mekari Qontak.
7. Klik **"Business Account"** untuk memilih akun Google Business yang telah terverifikasi. Sistem menampilkan semua lokasi bisnis terdaftar.
8. Centang lokasi bisnis yang ingin Anda kelola review-nya, atau klik **"Select all locations"** untuk mengintegrasikan semua lokasi.
9. Klik **"Save"**. Sistem menampilkan pesan konfirmasi integrasi berhasil.

## Expected Result  <!-- confidence:high ✓ -->

Setelah klik tombol **"Save"**, sistem menampilkan pesan konfirmasi bahwa akun Google Business Anda telah berhasil terintegrasi dengan Mekari Qontak. Lokasi bisnis yang Anda pilih kini akan menampilkan review dari customer pada Qontak Omnichannel, dan Anda dapat mengelola review tersebut melalui menu Google My Business di Qontak.

## Error States  <!-- confidence:medium ~ -->

- **Lokasi tidak terverifikasi**: Jika lokasi bisnis belum diverifikasi di Google Business Profile Console, review dari customer tidak dapat diterima oleh Qontak. Solusi: Verifikasi lokasi terlebih dahulu di Google Business sebelum melanjutkan integrasi.
- **Tidak dapat mengakses halaman Google Business**: Pastikan Anda masuk dengan akun Google yang terdaftar pada Google Business. Keluar dan masuk kembali dengan akun yang benar.
- **Business Account tidak muncul**: Refresh halaman atau pastikan akun Google Business memiliki status Admin pada akun Anda.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim dukungan Qontak (support-qontak@mekari.com) jika:

- Integrasi gagal meskipun semua persyaratan terpenuhi
- Lokasi bisnis tidak muncul di daftar Business Locations setelah memilih Business Account
- Pesan review masih tidak terima setelah verifikasi lokasi

Sertakan screenshot halaman integrasi, ID akun Qontak, dan nama Business Account yang bermasalah.