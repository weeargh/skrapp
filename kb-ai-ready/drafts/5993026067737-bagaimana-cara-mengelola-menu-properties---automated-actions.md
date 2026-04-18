---
title: Bagaimana Cara Mengelola Menu Properties - Automated Actions
canonical_url: https://help-center.qontak.com/hc/id/articles/5993026067737-Bagaimana-Cara-Mengelola-Menu-Properties-Automated-Actions
article_type: task
solvability_type: tool
products:
- Qontak CRM
product_surface: web
language: id
intent_tags:
- workflow-automation
- manage-menu-properties---automated-ac
- operation-workflow-automa
query_examples:
- Cara Mengelola Menu Properties - Automated Actions
- Bagaimana cara Mengelola Menu Properties - Automated Actions?
- Langkah-langkah Mengelola Menu Properties - Automated Actions di Qontak CRM
- How do I Mengelola Menu Properties - Automated Actions?
- Mau Mengelola Menu Properties - Automated Actions, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:medium ~ -->

Untuk mengelola Menu Properties - Automated Actions di Mekari Qontak CRM, Anda memerlukan:
- Akses ke Mekari Qontak CRM Dashboard
- Akun Mekari Qontak yang aktif
- Peran pengguna dengan akses ke menu Properties
- Pemahaman tentang modul yang akan digunakan sebagai entity action (seperti Deal, Task, atau Contact)
- Pengetahuan tentang trigger atau kondisi yang ingin mengaktifkan automated action

## Steps  <!-- confidence:high ✓ -->

1. Buka Dashboard Mekari Qontak CRM dan klik menu **Properties**. Halaman Properties akan terbuka.
2. Pilih tab **Automated Action**. Sistem akan menampilkan daftar automated action yang sudah ada.
3. Klik tombol **Add New** untuk membuat automated action baru. Form pengaturan action akan terbuka.
4. Isi judul dari action pada kolom yang tersedia. Pilih modul yang akan menjadi entity action (misalnya Deal). Tentukan trigger yang akan memicu action (misalnya ketika deal baru dibuat di stage tertentu).
5. Isi detail tugas otomatis: nama tugas, kategori, prioritas, tanggal jatuh tempo, dan tentukan apakah owner tugas mengikuti pemilik entity atau akun tertentu.
6. Klik tombol **Save Automated Action**. Sistem akan menampilkan pesan konfirmasi berhasil dan automated action akan aktif sesuai trigger yang ditentukan.
7. Untuk mengedit, klik icon **Pensil** pada action yang ingin diubah. Untuk menghapus, klik icon **Tempat Sampah**.

## Expected Result  <!-- confidence:high ✓ -->

Automated action berhasil dibuat dan tersimpan. Sistem akan menampilkan pesan konfirmasi. Ketika trigger terpenuhi (misalnya deal baru dibuat di stage yang ditentukan), sistem secara otomatis akan membuat tugas dengan detail yang telah dikonfigurasi dan memberikan notifikasi kepada pemilik entity. Automated action akan muncul di daftar tab Automated Action dengan status aktif.

## Error States  <!-- confidence:medium ~ -->

- **Automated action tidak berjalan**: Verifikasi trigger sudah dikonfigurasi dengan benar sesuai kondisi yang diinginkan. Periksa kembali modul dan entity yang dipilih.
- **Notifikasi tidak terkirim**: Pastikan pengaturan notifikasi pengguna aktif dan email/push notification sudah diaktifkan di settings akun.
- **Form tidak bisa disimpan**: Pastikan semua field wajib (judul action, modul, trigger, detail tugas) sudah diisi dengan lengkap.

## Escalation  <!-- confidence:medium ~ -->

Jika automated action tidak berjalan sesuai yang diharapkan setelah setup:
1. Verifikasi kembali konfigurasi trigger dan entity yang dipilih
2. Hapus cache browser dan coba lagi
3. Hubungi Mekari Qontak Support dengan informasi: nama automated action yang bermasalah, modul yang digunakan, trigger yang dikonfigurasi, dan screenshot halaman konfigurasi.
4. Sertakan juga timestamp kapan automated action seharusnya terpicu.