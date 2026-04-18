---
title: Bagaimana Cara Membatasi Aktivitas Perpindahan Deal secara Backward pada Mekari
  Qontak CRM
canonical_url: https://help-center.qontak.com/hc/id/articles/44890554326681-Bagaimana-Cara-Membatasi-Aktivitas-Perpindahan-Deal-secara-Backward-pada-Mekari-Qontak-CRM
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
- Cara Membatasi Aktivitas Perpindahan Deal secara Backward pada Mekari Qontak CRM
- Bagaimana cara Membatasi Aktivitas Perpindahan Deal secara Backward pada Mekari
  Qontak CRM?
- Langkah-langkah Membatasi Aktivitas Perpindahan Deal secara Backward pada Mekari
  Qontak CRM di Qontak CRM
- How do I Membatasi Aktivitas Perpindahan Deal secara Backward pada Mekari Qontak
  CRM?
- Mau Membatasi Aktivitas Perpindahan Deal secara Backward pada Mekari Qontak CRM,
  caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.3
---

## Prerequisites  <!-- confidence:high ✓ -->

1. Akun Qontak CRM aktif dengan akses login
2. Role Admin atau Owner (fitur ini hanya dapat diakses oleh Admin/Owner)
3. Minimal satu Pipeline sudah dibuat di menu Properties → tab Deals
4. Akses ke menu Properties dengan izin untuk mengedit Pipeline
5. Memahami urutan tahap (stage order) yang berlaku pada Pipeline Anda

## Steps  <!-- confidence:high ✓ -->

1. Masuk ke akun Qontak CRM Anda dan buka menu **Properties**.
2. Pilih tab **Deals**. Sistem menampilkan daftar Pipeline.
3. Klik tab **Pipelines**. Anda melihat tabel Pipeline list lengkap.
4. Pilih salah satu Pipeline dan klik tombol **Edit**. Halaman edit Pipeline terbuka.
5. Centang toggle **Deal stage cannot move backwards**. Toggle berubah status aktif (hijau).
6. Klik tombol **Save Pipeline**. Pop-up konfirmasi muncul.
7. Klik tombol **Restrict** pada pop-up untuk mengonfirmasi. Sistem menyimpan pengaturan.
8. Navigasi ke menu **Deals**. Pada Pipeline yang dibatasi, agent tidak dapat memindahkan Deal ke tahap sebelumnya.

## Expected Result  <!-- confidence:high ✓ -->

Pembatasan perpindahan Deal secara backward berhasil diterapkan. Pop-up informasi menampilkan pesan bahwa pembatasan pergerakan tahap pada Deals akan berlaku untuk semua Deal (yang sudah ada dan baru) pada Pipeline yang diaktifkan. Di menu Deals, agent melihat bahwa Deal hanya dapat dipindahkan ke tahap dengan urutan yang lebih tinggi (forward), dan fitur Rotten time kembali berfungsi efektif tanpa dapat direset melalui manipulasi tahap.

## Error States  <!-- confidence:low ? -->

No common errors documented.

## Escalation  <!-- confidence:medium ~ -->

Jika toggle **Deal stage cannot move backwards** tidak muncul atau tidak responsif setelah Anda membuka halaman edit Pipeline:
1. Verifikasi bahwa Anda login dengan role Admin atau Owner.
2. Refresh halaman browser dan coba kembali.
3. Jika masalah persisten, catat informasi berikut sebelum menghubungi Qontak Support:
   - Nama Pipeline yang bermasalah
   - ID akun Qontak CRM Anda
   - Screenshot halaman edit Pipeline
   - Browser dan versi yang digunakan