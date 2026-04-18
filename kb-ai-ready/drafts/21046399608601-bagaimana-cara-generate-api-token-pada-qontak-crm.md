---
title: Bagaimana Cara Generate API Token pada Qontak CRM
canonical_url: https://help-center.qontak.com/hc/id/articles/21046399608601-Bagaimana-Cara-Generate-API-Token-pada-Qontak-CRM
article_type: task
solvability_type: tool
products:
- Qontak CRM
product_surface: api
language: id
intent_tags:
- platform
- general-platform
query_examples:
- Cara Generate API Token pada Qontak CRM
- Bagaimana cara Generate API Token pada Qontak CRM?
- Langkah-langkah Generate API Token pada Qontak CRM di Qontak CRM
- How do I Generate API Token pada Qontak CRM?
- Mau Generate API Token pada Qontak CRM, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk generate API Token pada Qontak CRM, Anda membutuhkan:

- Akun Qontak CRM aktif dengan role Admin owner, Admin, atau Member
- Akses ke menu Properties di dashboard Qontak CRM
- Koneksi internet stabil untuk mengakses web Qontak CRM
- Hak akses untuk mengelola integrasi API (biasanya Admin owner atau Admin memiliki hak penuh)

## Steps  <!-- confidence:high ✓ -->

1. Login ke akun Qontak CRM Anda.
2. Pada menu utama, klik **Properties** kemudian pilih **API token**. Sistem akan menampilkan halaman API token management.
3. Klik tombol **Generate** untuk membuat API token baru. Anda dapat membuat hingga 2 (dua) token berbeda. Token yang baru dibuat akan muncul di layar.
4. Klik **Show token** untuk menampilkan token yang telah dibuat.
5. Klik **Copy** untuk menyalin token ke clipboard. Token siap digunakan untuk keperluan integrasi.

## Expected Result  <!-- confidence:high ✓ -->

Setelah berhasil generate API Token, Anda akan melihat:

- Token yang ditampilkan di halaman API token dengan status aktif
- Informasi masa kadaluarsa token (6 jam dari waktu generate)
- Tombol Copy yang memungkinkan Anda menyalin token untuk digunakan dalam integrasi
- Jika token telah kadaluarsa, label "Kadaluarsa" akan muncul dan tombol Generate muncul kembali untuk membuat token baru

## Error States  <!-- confidence:medium ~ -->

**API Token sudah kadaluarsa**: Jika token tidak lagi aktif (lebih dari 6 jam sejak generate), label "Kadaluarsa" akan ditampilkan. Solusi: klik tombol **Generate** kembali untuk membuat token baru.

**Tidak dapat mengakses menu API token**: Pastikan Anda memiliki role Admin owner atau Admin. Member mungkin memiliki akses terbatas. Hubungi Admin owner untuk verifikasi hak akses.

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support jika Anda mengalami:

- Tidak dapat mengakses menu Properties atau API token meskipun memiliki role yang sesuai
- Tombol Generate tidak berfungsi atau tidak merespons klik
- Token tidak dapat disalin dengan fitur Copy
- Pertanyaan teknis mengenai cara menggunakan API token untuk integrasi spesifik

Sediakan: nama akun Qontak CRM, screenshot error, dan deskripsi masalah saat menghubungi support-qontak@mekari.com