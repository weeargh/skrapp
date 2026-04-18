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


Automated Action adalah cara untuk menambahkan fungsionalitas ke Qontak CRM tanpa melakukan pemrograman apa pun. Fitur ini dapat digunakan untuk memicu tindakan atau aksi tertentu secara otomatis.
Berikut langkah-langkah untuk mengelola Menu Properties - Automated Actions:
  1. Pilih menu **P****roperties.**

Misalnya, Anda membuat suatu _automated action_ membuat tugas baru ketika ada deal baru dibuat di suatu _pipeline_ dan _stage_ tertentu. Jadi, ketika sebuah deal di buat di suatu _stage_ , _system_ akan membuat tugas baru dengan judul dan _detail_ yang sudah dibuat di _default**automated action**_ dan memberikan notifikasi ke pembuat deal tersebut. Saat Anda sudah menentukan _entity_ dan _trigger_ dalam suatu deal, Anda dapat membuat tugas yang akan diberikan secara otomatis dengan _trigger_ tersebut.
  4. Isikann nama tugas, kategori, prioritas, detail tugas maupun kolom lainnya seperti due date setiap tugas yg dibuat, dan tentukan apakah dari setiap tugas yang dibuat akan memiliki _owner_ yang sama dengan pemilik entitas atau hanya 1 akun menjadi _owner_ setiap tugas tersebut.  
![mceclip6.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F10416230369305)
  5. Klik **“Save Automated Action”** untuk menyimpan _action_.  
![4.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36776434962329)
  6. Maka _automated action_ akan otomatis berjalan sesuai dengan _trigger_ yang telah dibuat.

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