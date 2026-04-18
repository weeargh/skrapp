---
title: Bagaimana Cara Add dan Update Deal Secara Massal Versi Web
canonical_url: https://help-center.qontak.com/hc/id/articles/26437621611801-Bagaimana-Cara-Add-dan-Update-Deal-Secara-Massal-Versi-Web
article_type: task
solvability_type: tool
products:
- Qontak CRM
product_surface: web
language: id
intent_tags:
- sales-pipeline-deals-tracking
- sales-management
query_examples:
- Cara Add dan Update Deal Secara Massal Versi Web
- Bagaimana cara Add dan Update Deal Secara Massal Versi Web?
- Langkah-langkah Add dan Update Deal Secara Massal Versi Web di Qontak CRM
- How do I Add dan Update Deal Secara Massal Versi Web?
- Mau Add dan Update Deal Secara Massal Versi Web, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk menambah dan meng-update deal secara massal di Qontak CRM versi Web, Anda memerlukan:

1. Akun Qontak CRM aktif dengan akses login
2. Permission untuk mengakses menu Deals
3. Deals yang sudah ada di sistem (jika melakukan update)
4. Software spreadsheet (Excel, Google Sheets, atau editor CSV)
5. Nama pipeline, nama stage, dan ID slug deal yang ingin diupdate
6. Untuk update deals: ID slug harus cocok dengan data existing deal

## Steps  <!-- confidence:high ✓ -->

1. Login ke akun Qontak CRM Anda.
   → Beranda Qontak CRM terbuka.

2. Klik menu **Deals**.
   → Halaman daftar Deals ditampilkan.

3. Klik tombol **"Add Tickets"** lalu pilih **Bulk add & update deals**.
   → Halaman Bulk add & update deals terbuka dengan dua opsi template.

4. Klik **CSV template** atau **Excel template** untuk mengunduh template spreadsheet.
   → File template unduhan dimulai ke perangkat Anda.

5. Buka template unduhan dan isi data sesuai kebutuhan Anda (jangan isi Slug ID untuk deals baru; isi pipeline, stage, dan ID slug dengan benar untuk update deals).
   → Data dalam spreadsheet lengkap dan siap diunggah.

6. Kembali ke halaman **Bulk add & update deals**, klik **"Choose file"** dan pilih file template yang sudah diisi.
   → Nama file template ditampilkan di kolom upload.

7. Klik tombol **"Upload"**.
   → Sistem memproses file dan menampilkan hasil upload (berhasil atau gagal).

## Expected Result  <!-- confidence:high ✓ -->

Setelah upload berhasil, semua deal baru dan update deal ditampilkan di menu **Deals** Qontak CRM Anda dengan:

- Deal baru tersimpan dengan data lengkap
- Deal yang diupdate menampilkan informasi terbaru (nama deal, pipeline, stage, dan field lainnya sesuai template)
- Status deals tersinkronisasi dengan pipeline dan stage yang Anda atur
- Maksimal 3000 baris berhasil diproses dalam satu kali upload

Untuk verifikasi, Anda dapat membuka menu Deals dan melihat daftar deals terbaru Anda.

## Error States  <!-- confidence:medium ~ -->

Deals gagal diunggah jika:

- **Pipeline atau stage tidak ditemukan**: Pastikan nama pipeline dan stage dalam spreadsheet cocok dengan pipeline dan stage yang ada di sistem Qontak CRM Anda.
- **ID slug tidak valid untuk update**: Jika melakukan update, pastikan ID slug cocok dengan data deals existing. Anda dapat menemukan ID slug dari URL rincian profil deals atau dari data deals yang diunduh sebelumnya.
- **Slug ID diisi untuk deals baru**: Deals baru tidak memerlukan Slug ID; kosongkan kolom ini.
- **Format file tidak didukung**: Upload hanya menerima file CSV atau Excel (XLS/XLSX).
- **Jumlah baris melebihi batas**: Maksimal 3000 baris per upload; kurangi jumlah data jika diperlukan.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak jika:

- File berhasil diunggah tetapi deals tidak muncul di menu **Deals** setelah menunggu beberapa menit.
- Pesan error muncul saat upload tanpa deskripsi yang jelas.
- Permission untuk mengakses menu **Deals** atau fitur **Bulk add & update deals** tidak tersedia meskipun akun sudah login.
- Kesalahan pipeline atau stage tidak terselesaikan setelah verifikasi ulang.

Saat menghubungi support, siapkan: screenshot halaman error, screenshot template spreadsheet yang diunggah, ID akun Qontak CRM, dan deskripsi masalah spesifik.