---
title: Bagaimana Cara Melakukan Kustomisasi Webchat Header
canonical_url: https://help-center.qontak.com/hc/id/articles/5658044409241-Bagaimana-Cara-Melakukan-Kustomisasi-Webchat-Header
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- multi-channel-integration
- perform-kustomisasi-webchat-header
- conversation-management
query_examples:
- Cara Melakukan Kustomisasi Webchat Header
- Bagaimana cara Melakukan Kustomisasi Webchat Header?
- Langkah-langkah Melakukan Kustomisasi Webchat Header di Qontak Omnichannel
- How do I Melakukan Kustomisasi Webchat Header?
- Mau Melakukan Kustomisasi Webchat Header, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.3
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk melakukan kustomisasi Webchat header di Qontak Omnichannel, Anda memerlukan:

- **Role Admin** pada akun Qontak Omnichannel (hanya pengguna dengan role Admin yang dapat melakukan kustomisasi)
- **Akun Qontak Omnichannel** yang aktif
- **Widget Webchat** yang sudah dibuat sebelumnya di menu Channel Integrations
- Akses ke menu **Channel Integrations** → **Web chat**

Jika Anda tidak memiliki role Admin, hubungi tim support Qontak di support-qontak@mekari.com untuk mengubah role akun Anda.

## Steps  <!-- confidence:high ✓ -->

1. Masuk ke akun Omnichannel Anda dengan kredensial Admin.

2. Buka menu **Channel Integrations** dan pilih **Web chat**. Sistem menampilkan daftar widget yang tersedia.

3. Klik tombol **Actions** pada widget yang ingin dikustomisasi, lalu pilih **Set up widget**. Halaman pengaturan widget terbuka.

4. Pada bagian **Widget Appearance**, atur warna **widget header** sesuai preferensi Anda.

5. Pada bagian **Widget Content**, pilih salah satu kondisi: **Online**, **Offline**, **Pre Chat Form**, atau **Greeting**.

6. Untuk kondisi **Online**: Klik bagian **Online** dan isikan pesan yang menginformasikan bahwa agen sedang online dan siap menanggapi.

7. Untuk kondisi **Offline**: Klik bagian **Offline** dan isikan pesan yang menginformasikan bahwa agen sedang offline.

8. Untuk kondisi **Pre Chat Form**: Isikan title dan subtitle yang akan ditampilkan saat halaman webchat pertama kali dibuka.

9. Setelah selesai, sistem menyimpan perubahan secara otomatis.

## Expected Result  <!-- confidence:high ✓ -->

Setelah menyelesaikan kustomisasi Webchat header:

- Warna **widget header** berubah sesuai pilihan Anda
- Pesan untuk setiap kondisi (Online, Offline, Pre Chat Form, Greeting) tersimpan dan akan ditampilkan kepada pengunjung sesuai status agen
- Widget Webchat menampilkan header dengan informasi dan warna yang telah dikustomisasi
- Pengunjung website melihat pesan yang relevan dengan kondisi ketersediaan agen saat ini

## Error States  <!-- confidence:low ? -->

No common errors documented.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak di **support-qontak@mekari.com** jika:

- Anda tidak memiliki akses ke menu Channel Integrations (periksa role akun Anda)
- Tombol **Set up widget** tidak muncul atau tidak responsif
- Perubahan warna atau pesan tidak tersimpan
- Webchat header tidak menampilkan perubahan yang sudah dikustomisasi di website

Sertakan: nama akun, nama widget yang dikustomisasi, screenshot halaman pengaturan, dan deskripsi masalah yang Anda hadapi.