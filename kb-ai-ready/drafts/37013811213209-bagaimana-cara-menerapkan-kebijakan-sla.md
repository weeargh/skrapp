---
title: Bagaimana Cara Menerapkan Kebijakan SLA
canonical_url: https://help-center.qontak.com/hc/id/articles/37013811213209-Bagaimana-Cara-Menerapkan-Kebijakan-SLA
article_type: task
solvability_type: tool
products:
- Qontak CRM
product_surface: web
language: id
intent_tags:
- sla-management-countdown
- customer-support-ticketin
query_examples:
- Cara Menerapkan Kebijakan SLA
- Bagaimana cara Menerapkan Kebijakan SLA?
- Langkah-langkah Menerapkan Kebijakan SLA di Qontak CRM
- How do I Menerapkan Kebijakan SLA?
- Mau Menerapkan Kebijakan SLA, caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.3
---

## Prerequisites  <!-- confidence:high ✓ -->

Anda ingin menerapkan kebijakan SLA pada perusahaan Anda di Mekari Qontak CRM. Sebelum memulai, pastikan:

- Anda memiliki akses ke akun Qontak CRM
- Peran Anda adalah Admin atau Owner
- Paket langganan Anda adalah Ultimate atau Enterprise di service suite Qontak
- Fitur SLA Management hanya berlaku untuk Ticket Module
- Pipeline sudah dibuat sebelumnya pada Ticket Module

## Steps  <!-- confidence:high ✓ -->

1. Buka akun CRM Anda, kemudian klik menu **Properties**.
   - Sistem menampilkan halaman Properties dengan beberapa tab pilihan.

2. Pilih tab **SLA Management**.
   - Layar menampilkan daftar kebijakan SLA yang sudah ada (jika ada).

3. Klik tombol **Create Policy**.
   - Form pembuatan kebijakan SLA terbuka.

4. Isi kolom **Policy name** dengan nama kebijakan dan kolom **Description** dengan deskripsi kebijakan SLA Anda.
   - Sistem menyimpan input teks Anda.

5. Pilih **Pipeline** dari dropdown (wajib dipilih terlebih dahulu).
   - Pipeline yang tersedia pada Ticket Module ditampilkan.

6. Klik tombol **Add condition** untuk menambahkan hingga 4 kondisi penerapan kebijakan.
   - Form kondisi baru muncul.

7. Pilih **Field** dari dropdown (hanya field dengan tipe Dropdown atau Selection yang tersedia).
   - Field dan Stage dari Pipeline terpilih ditampilkan.

8. Tentukan **Resolution time** sebagai batas waktu penyelesaian tiket.
   - Sistem menyimpan waktu yang Anda tentukan.

## Expected Result  <!-- confidence:high ✓ -->

Setelah menyelesaikan semua langkah, kebijakan SLA berhasil dibuat dan tersimpan di Mekari Qontak CRM. Kebijakan SLA yang baru Anda buat akan:

- Muncul dalam daftar kebijakan SLA pada tab **SLA Management**
- Berlaku pada tiket yang sesuai dengan kondisi yang telah Anda tetapkan
- Menampilkan informasi Policy name, Description, Pipeline yang dipilih, dan kondisi-kondisi yang diterapkan
- Dapat dikelola lebih lanjut melalui opsi edit, duplikasi, penghapusan, atau lihat Log aktivitas

## Error States  <!-- confidence:low ? -->

No common errors documented.

## Escalation  <!-- confidence:medium ~ -->

Jika Anda mengalami masalah saat menerapkan kebijakan SLA, hubungi tim dukungan Mekari Qontak dengan informasi berikut:

- ID akun CRM Anda
- Screenshot dari halaman SLA Management atau form Create Policy yang menampilkan masalah
- Deskripsi detail tentang langkah mana yang tidak berfungsi
- Paket langganan Anda (Ultimate atau Enterprise)
- Nama Pipeline dan kondisi yang ingin Anda terapkan