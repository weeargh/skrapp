---
title: Pembaruan Endpoint Open API pada Mekari Qontak API sebelum 11 April 2025
canonical_url: https://help-center.qontak.com/hc/id/articles/44509078667673-Pembaruan-Endpoint-Open-API-pada-Mekari-Qontak-API-sebelum-11-April-2025
article_type: task
solvability_type: tool
products:
- Qontak CRM
product_surface: api
language: id
intent_tags:
- whats-new-on-qontak
- general-platform
query_examples:
- Cara Pembaruan Endpoint Open API pada Mekari Qontak API sebelum 11 April 2025
- Bagaimana cara Pembaruan Endpoint Open API pada Mekari Qontak API sebelum 11 April
  2025?
- Langkah-langkah Pembaruan Endpoint Open API pada Mekari Qontak API sebelum 11 April
  2025 di Qontak CRM
- How do I Pembaruan Endpoint Open API pada Mekari Qontak API sebelum 11 April 2025?
- Mau Pembaruan Endpoint Open API pada Mekari Qontak API sebelum 11 April 2025, caranya
  gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: null
faithfulness_threshold: null
---

<!-- ═══════════════════════════════════════════════════════════
     REVIEW SCAFFOLD — TASK
     The sections below are missing. Fill them in, then delete
     this comment block before approving.
     ═══════════════════════════════════════════════════════════

## Prerequisites

<!-- List required conditions, permissions, or setup steps -->

## Steps

<!-- Numbered action steps. Each step: action → expected UI response -->

## Expected Result

<!-- What the user should see / confirmation message after completion -->

## Error States

<!-- Common errors and their fixes. Leave empty if none. -->

## Escalation

<!-- When to contact support and what info to provide -->

-->

Salam hangat dari Mekari Qontak,

Terima kasih telah memilih Mekari Qontak sebagai partner bisnis di perusahaan Anda

Kami ingin menginformasikan mengenai **pembaruan pada endpoint API Mekari Qontak untuk mendapatkan akses token API**. Pembaruan ini akan dilakukan pada **11 April 2025**. Sebelum proses berlangsung, berikut ini beberapa hal yang perlu Anda perhatikan:

1. Anda perlu menginformasikan kepada tim Engineering Anda untuk segera mengubah endpoint di konfigurasi Mekari Qontak API sesuai dengan Module dan Aktivitas yang Anda gunakan.
2. Rincian perubahan Endpoint:

1. Sebelum melanjutkan panduan ini, pastikan akun Anda telah mendapatkan otorisasi untuk **Mekari Developer**([https://developers.mekari.com/](https://developers.mekari.com/)). Jika anda tidak dapat mengakses Mekari Developer, berarti akun belum diotorisasi. Silakan hubungi spesialis atau tim support untuk mendapatkan akses.
2. Untuk mendapatkan autentikasi API, login pada akun Mekari Developer anda, lalu ikuti panduan dibawah: a. Buka Mekari Developer dan login dengan akun Mekari SSO Anda. b. Pilih Applications ( guide dokumentasi ) c. Buat aplikasi baru dengan mengisi nama aplikasi, nama perusahaan, dan memilih scope yang diperlukan. - Pada bagian ‘Authorized Scope’ Anda perlu mencentang scope yang diperlukan untuk integrasi. Setiap scope mewakili endpoint API tertentu. Pilihlah hanya scope yang benar-benar dibutuhkan untuk aplikasi internal perusahaan Anda. Anda dapat membuat dua aplikasi terpisah untuk scope Qontak Chat dan Qontak CRM jika diperlukan, guna meningkatkan keamanan, dengan menghasilkan Client ID & Client Secret yang berbeda. d. Catat Client ID dan Client Secret. e. Pilih HMAC Validator, lalu isi Client ID , Client Secret , HTTP Method , Full API URL , dan Date Header . f. Klik Submit, lalu salin Authorization Header yang muncul.

1. Selebihnya mengenai dokumen Open API dapat diakses melalui:
a. Qontak CRM: [https://documenter.getpostman.com/view/22728681/2sAXxV6A5V#1476859d-d470-483a-b6bc-a04db4b2b027](https://documenter.getpostman.com/view/22728681/2sAXxV6A5V#1476859d-d470-483a-b6bc-a04db4b2b027) 
b. Qontak Omnichannel: [https://docs.qontak.com/docs/omnichannel-hub/3f11066e2ce6c-api-mekari-v1-0](https://docs.qontak.com/docs/omnichannel-hub/3f11066e2ce6c-api-mekari-v1-0)

### Mengapa perlu diperbarui?

1. Memastikan setiap permintaan API Anda terverifikasi dengan benar untuk mencegah akses tidak sah.
2. Mengikuti Standar Terkini: Mempermudah pengelolaan dan kompatibilitas dengan pembaruan selanjutnya.
3. Keamanan Data Lebih Kuat: Menambahkan lapisan perlindungan ekstra untuk menjaga keamanan pengguna.

Demikian yang dapat kami sampaikan. Apabila Anda memiliki pertanyaan lebih lanjut, silakan sampaikan ke [support-qontak@mekari.com](https://support-qontak@mekari.com) atau WhatsApp Hotline Support di 6285180971599.