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


Pada Qontak Omnichannel, Anda sebagai Admin/Supervisor dapat melakukan generate API token. Kemudian, Anda dapat menggunakan API token tersebut untuk keperluan integrasi. Berikut adalah langkah - langkahnya.
  1. Pada Qontak Omnichannel Anda, masuk ke menu **Settings** lalu klik **API token**.
  2. Kemudian pilih tab **"Omnichannel"**.  
![1.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49491403552281)

Demikian adalah pandauan untuk generate API Token pada Qontak Omnichannel.

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