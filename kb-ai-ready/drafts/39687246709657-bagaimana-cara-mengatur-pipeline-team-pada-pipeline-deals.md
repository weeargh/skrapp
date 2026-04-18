---
title: Bagaimana Cara Mengatur Pipeline Team pada Pipeline Deals
canonical_url: https://help-center.qontak.com/hc/id/articles/39687246709657-Bagaimana-Cara-Mengatur-Pipeline-Team-pada-Pipeline-Deals
article_type: task
solvability_type: tool
products:
- Qontak CRM
product_surface: web
language: id
intent_tags:
- sales-pipeline-deals-tracking
- configure-pipeline-team
- sales-management
query_examples:
- Cara Mengatur Pipeline Team pada Pipeline Deals
- Bagaimana cara Mengatur Pipeline Team pada Pipeline Deals?
- Langkah-langkah Mengatur Pipeline Team pada Pipeline Deals di Qontak CRM
- How do I Mengatur Pipeline Team pada Pipeline Deals?
- Mau Mengatur Pipeline Team pada Pipeline Deals, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

1. Akun Qontak CRM aktif dengan akses login
2. Memiliki role/permission untuk mengakses menu **Properties**
3. Telah membuat minimal satu **Team** di Profile Settings
4. Telah membuat minimal satu **Pipeline** di Deal Properties, atau siap membuat pipeline baru
5. Pengguna yang akan diberikan akses harus sudah ditambahkan ke sistem dan ditugaskan ke tim tertentu

## Steps  <!-- confidence:high ✓ -->

1. Login ke akun CRM Anda dan pilih menu **Properties**.
2. Klik tab **"Deals"** pada halaman Properties.
3. Pada halaman **Deal Properties**, pilih pipeline yang ingin diatur aksesnya atau klik **"Create New Pipeline"** untuk membuat pipeline baru.
4. Untuk pipeline yang sudah ada, klik ikon **Edit** pada pipeline tersebut.
5. Gulir halaman ke bawah hingga menemukan kolom **Team**.
6. Pada kolom **Team**, isikan nama tim yang akan memiliki akses ke pipeline ini. Anda dapat menambahkan satu atau lebih tim.
7. Klik tombol **"Save Pipeline"** untuk menyimpan pengaturan.
8. Sistem akan menampilkan konfirmasi bahwa pengaturan pipeline team berhasil disimpan.

## Expected Result  <!-- confidence:high ✓ -->

Pengaturan Pipeline Team berhasil diterapkan. Tim yang Anda tentukan di kolom **Team** sekarang hanya dapat melihat pipeline tersebut pada indeks **Pipeline Deals**. Pengguna yang tidak termasuk dalam tim yang ditentukan tidak akan melihat pipeline ini di daftar pipeline. Perubahan langsung berlaku untuk semua pengguna, termasuk **Admin** dan **Owner** sesuai dengan role dan tim mereka.

## Error States  <!-- confidence:medium ~ -->

**Pengguna tidak melihat pipeline meskipun ditambahkan ke Team:**
- Verifikasi bahwa pengguna tersebut benar-benar ditugaskan ke tim yang dimaksud di Profile Settings → Teams.
- Pastikan pengguna login ulang agar perubahan akses ter-refresh.

**Tim tidak muncul di dropdown kolom Team:**
- Pastikan tim sudah dibuat terlebih dahulu di Profile Settings → Teams sebelum mengatur Pipeline Team.

## Escalation  <!-- confidence:medium ~ -->

Hubungi support Qontak jika:
- Pengaturan Pipeline Team tidak tersimpan meskipun tombol **"Save Pipeline"** sudah diklik
- Pengguna masih dapat melihat pipeline yang seharusnya tidak dapat diakses setelah 30 menit
- Fitur Pipeline Team tidak tersedia di menu Properties

Sediakan: screenshot pengaturan Pipeline Team, daftar tim dan pengguna yang terlibat, dan ID akun Qontak Anda.