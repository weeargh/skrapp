---
title: Bagaimana Cara Generate API Token pada Qontak Omnichannel
canonical_url: https://help-center.qontak.com/hc/id/articles/21045464958617-Bagaimana-Cara-Generate-API-Token-pada-Qontak-Omnichannel
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
product_surface: api
language: id
intent_tags:
- platform
- general-platform
query_examples:
- Cara Generate API Token pada Qontak Omnichannel
- Bagaimana cara Generate API Token pada Qontak Omnichannel?
- Langkah-langkah Generate API Token pada Qontak Omnichannel di Qontak Omnichannel
- How do I Generate API Token pada Qontak Omnichannel?
- Mau Generate API Token pada Qontak Omnichannel, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk melakukan generate API Token pada Qontak Omnichannel, Anda memerlukan:

- Akun Qontak Omnichannel aktif dengan akses Admin atau Supervisor
- Akses ke menu Settings di dashboard Qontak Omnichannel
- Koneksi internet stabil untuk membuka Web Qontak Omnichannel
- Keperluan integrasi yang membutuhkan API token untuk konektivitas sistem pihak ketiga

## Steps  <!-- confidence:high ✓ -->

1. Login ke akun Qontak Omnichannel Anda dengan kredensial Admin atau Supervisor.

2. Pada menu utama, klik **Settings** lalu pilih **API token**. Sistem akan menampilkan halaman API token management.

3. Pilih tab **Omnichannel**. Anda akan melihat daftar token yang tersedia dan status masing-masing.

4. Klik tombol **Generate** untuk membuat API token baru. Sistem akan menghasilkan token baru dan menampilkannya dalam status tersembunyi.

5. Klik **Show token** untuk memunculkan nilai token yang baru dibuat.

6. Klik tombol **Copy** untuk menyalin token ke clipboard dan gunakan untuk keperluan integrasi Anda.

## Expected Result  <!-- confidence:high ✓ -->

Setelah berhasil melakukan generate API Token, Anda akan melihat:

- Token baru muncul dalam daftar API token di tab Omnichannel
- Nilai token dapat ditampilkan dan disalin ke clipboard
- Status token menunjukkan tanggal pembuatan dan masa kadaluarsa (1 tahun dari waktu generate)
- Token siap digunakan untuk integrasi dengan sistem pihak ketiga
- Maksimal 2 (dua) token aktif dapat dibuat per akun Qontak Omnichannel

## Error States  <!-- confidence:medium ~ -->

**Token Kadaluarsa (Expired)**
- Indikator: Label kadaluarsa muncul di sebelah token yang sudah berusia 1 tahun
- Solusi: Klik tombol **Generate** yang muncul kembali untuk membuat token baru. Token lama tidak dapat digunakan lagi untuk integrasi.

**Batas Token Tercapai**
- Jika sudah memiliki 2 token aktif, Anda harus menghapus salah satu token lama sebelum membuat token baru.

**Token Tidak Dapat Disalin**
- Pastikan koneksi internet Anda stabil dan browser mendukung fungsi clipboard.

## Escalation  <!-- confidence:medium ~ -->

Hubungi Mekari Qontak Support jika:

- Tombol **Generate** tidak responsif atau API token tidak tercipta setelah beberapa menit
- Token yang baru dibuat tidak dapat digunakan untuk integrasi meskipun sudah dicopy dengan benar
- Terjadi error message spesifik pada halaman API token
- Anda perlu reset atau revoke semua token aktif karena keamanan

Sediakan informasi berikut saat menghubungi support:
- Screenshot halaman API token yang bermasalah
- Account ID atau email Qontak Omnichannel Anda
- Deskripsi masalah dan langkah yang sudah dicoba
- Waktu (jam dan tanggal) saat masalah terjadi