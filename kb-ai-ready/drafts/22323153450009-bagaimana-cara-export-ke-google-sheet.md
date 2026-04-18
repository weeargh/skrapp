---
title: Bagaimana Cara Export ke Google Sheet
canonical_url: https://help-center.qontak.com/hc/id/articles/22323153450009-Bagaimana-Cara-Export-ke-Google-Sheet
article_type: task
solvability_type: tool
products:
- Qontak CRM
product_surface: web
language: id
intent_tags:
- field-properties
- sales-management
query_examples:
- Cara Export ke Google Sheet
- Bagaimana cara Export ke Google Sheet?
- Langkah-langkah Export ke Google Sheet di Qontak CRM
- How do I Export ke Google Sheet?
- Mau Export ke Google Sheet, caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

• Akun Qontak CRM aktif dan sudah masuk login
• Akses level Member atau Admin
• Google Account yang terhubung dengan Qontak CRM
• Data Kontak, Task, Perusahaan, Deal, atau Produk sudah ada di Qontak CRM
• Akses ke menu Properties di sidebar kiri dashboard

## Steps  <!-- confidence:high ✓ -->

1. Buka dashboard Qontak CRM Anda
2. Klik menu **Properties** di sidebar kiri
3. Sistem akan menampilkan halaman Properties dengan beberapa pilihan menu
4. Klik **Ekspor ke GSheet**
5. Sistem akan menampilkan halaman Ekspor ke Google Sheet dengan opsi sinkronisasi
6. (Opsional) Klik tombol **Sinkronkan** untuk langsung sinkronisasi data ke Google Sheet sekarang
7. (Opsional) Aktifkan toggle **Auto Sync** dan tentukan jadwal di kolom **Sync Time** untuk sinkronisasi otomatis berkala
8. Sistem akan mencatat pengaturan Anda## Expected Result  <!-- confidence:high ✓ -->

Setelah mengikuti langkah-langkah di atas, halaman Ekspor ke Google Sheet akan menampilkan:
• URL Google Sheet tempat data Anda akan disimpan di kolom Google Sheet URL
• Tombol Sinkronkan untuk sinkronisasi manual
• Toggle Auto Sync untuk mengaktifkan jadwal otomatis
• Kolom Sync Time untuk menentukan waktu sinkronisasi

Data dari Qontak CRM (Kontak, Task, Perusahaan, Deal, Produk) akan tersinkronisasi ke Google Sheet sesuai pengaturan yang dipilih.

![7.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50120717679641)
![1.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50120662386713)

## Error States  <!-- confidence:medium ~ -->

• Google Account tidak terhubung: Pastikan Anda sudah menghubungkan Google Account dengan Qontak CRM melalui pengaturan integrasi terlebih dahulu
• URL Google Sheet tidak muncul: Refresh halaman atau coba logout dan login kembali ke Qontak CRM
• Sinkronisasi gagal: Periksa koneksi internet dan pastikan Google Sheet masih dapat diakses dengan akun yang terhubung
• Data tidak terupdate: Verifikasi bahwa toggle Auto Sync aktif dan jadwal Sync Time sudah ditentukan dengan benar

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak jika mengalami:
• Google Account tidak dapat terhubung meskipun sudah mengikuti proses integrasi
• Tombol Sinkronkan tidak berfungsi atau error message muncul
• Data tidak tersinkronisasi ke Google Sheet setelah 24 jam
• Akses ke menu Ekspor ke GSheet ditolak meskipun memiliki role Member/Admin

Sertakan screenshot halaman error, nama akun, dan waktu kejadian saat menghubungi support.