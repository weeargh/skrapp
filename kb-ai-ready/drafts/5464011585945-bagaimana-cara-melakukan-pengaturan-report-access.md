---
title: Bagaimana Cara Melakukan Pengaturan Report Access
canonical_url: https://help-center.qontak.com/hc/id/articles/5464011585945-Bagaimana-Cara-Melakukan-Pengaturan-Report-Access
article_type: task
solvability_type: tool
products:
- Mekari Qontak
product_surface: web
language: id
intent_tags:
- user-permissions
- perform-pengaturan-report-access
- general-platform
query_examples:
- Cara Melakukan Pengaturan Report Access
- Bagaimana cara Melakukan Pengaturan Report Access?
- Langkah-langkah Melakukan Pengaturan Report Access di Mekari Qontak
- How do I Melakukan Pengaturan Report Access?
- Mau Melakukan Pengaturan Report Access, caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

• Anda harus memiliki akses level Admin di Qontak CRM perusahaan Anda
• Akses ke dashboard Qontak di qontak.com
• Pengguna yang akan diatur akses Report Access sudah terdaftar di sistem
• Pengaturan Report Access hanya dapat diakses oleh user dengan level admin

## Steps  <!-- confidence:high ✓ -->

**Untuk pengaturan saat penambahan pengguna baru:**

1. Klik tanda panah di sebelah kanan username Anda (kanan atas dashboard)
2. Pilih "Profile Settings" — Sistem akan menampilkan halaman pengaturan profil
3. Klik "Add User" pada tab Account Settings — Form penambahan pengguna akan terbuka
4. Lengkapi informasi pengguna (nama, email, tim, dan role)
5. Scroll ke bagian bawah formulir ke bagian "Request Access"
6. Pilih salah satu dari 3 opsi akses Report: Everything (semua laporan), Team Only (laporan tim saja), atau Owned Only (laporan pengguna saja)
7. Aktifkan tombol "ON" untuk memberikan akses unduh report (opsional)
8. Klik "Create User" — Pengguna baru berhasil ditambahkan dengan pengaturan akses yang ditentukan

**Untuk mengubah pengaturan pada pengguna yang sudah ada:**

1. Klik tanda panah di sebelah kanan username Anda (kanan atas dashboard)
2. Pilih "Profile Settings" — Halaman pengaturan profil akan ditampilkan
3. Pilih tab "User Permissions" dan pilih nama pengguna dari daftar
4. Pilih tab "Report Access" — Opsi pengaturan Report Access akan muncul
5. Pilih salah satu dari 3 opsi akses: Everything, Team Only, atau Owned Only
6. Aktifkan atau nonaktifkan tombol akses unduh report sesuai kebutuhan
7. Klik "Update User" atau tombol simpan — Pengaturan Report Access berhasil diperbarui## Expected Result  <!-- confidence:high ✓ -->

Pengaturan Report Access berhasil tersimpan di sistem. Pengguna yang ditambahkan atau diperbarui akan memiliki akses ke laporan sesuai dengan opsi yang dipilih (Everything, Team Only, atau Owned Only). Penampilan data report pada menu Dashboard akan disesuaikan secara otomatis sesuai dengan pengaturan akses yang ditentukan. Jika akses unduh report diaktifkan, pengguna dapat mengunduh laporan sesuai dengan level akses mereka.

![Screenshot 2023-08-08 at 10.55.18.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36766089340313)
![Screenshot 2023-08-08 at 11.31.53.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F21569876972057)
![b3.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36766089286297)
![b4.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36766085921433)
![b5.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36766085926425)
![b6.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F5463903993113)
![c2.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F5463876976793)
![c3.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36766085938713)
![c4.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F5463896625433)
![c5.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F5463882906393)
![c6.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36766089329945)
![c7.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F5463911520025)

## Error States  <!-- confidence:medium ~ -->

Beberapa kondisi yang perlu diperhatikan:

• Jika Anda bukan user level admin, menu "Profile Settings" dan opsi pengaturan Report Access tidak akan tersedia — hubungi administrator perusahaan Anda untuk mengaktifkan akses
• Jika pengguna tidak menerima email undangan setelah penambahan, verifikasi bahwa alamat email yang dimasukkan benar dan email administrator aktif
• Perubahan pengaturan Report Access memerlukan waktu beberapa menit untuk terefleksi sepenuhnya pada menu Dashboard

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak jika mengalami kondisi berikut:

• Tombol atau opsi pengaturan Report Access tidak muncul meskipun Anda adalah user level admin
• Perubahan pengaturan Report Access tidak terrefleksi di menu Dashboard setelah menunggu lebih dari 5 menit
• Pengguna baru tidak dapat mengakses laporan sesuai dengan pengaturan yang telah ditentukan

Sediakan informasi berikut saat menghubungi support: nama pengguna yang bermasalah, screenshot dari halaman Report Access, dan deskripsi detail tentang pengaturan yang ingin diterapkan.