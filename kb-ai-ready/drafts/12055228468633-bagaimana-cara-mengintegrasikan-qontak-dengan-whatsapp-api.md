---
title: Bagaimana Cara Mengintegrasikan Qontak dengan WhatsApp API
canonical_url: https://help-center.qontak.com/hc/id/articles/12055228468633-Bagaimana-Cara-Mengintegrasikan-Qontak-dengan-WhatsApp-API
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: api
language: id
intent_tags:
- multi-channel-integration
- integrate-qontak-dengan-whatsapp-api
- conversation-management
query_examples:
- Cara Mengintegrasikan Qontak dengan WhatsApp API
- Bagaimana cara Mengintegrasikan Qontak dengan WhatsApp API?
- Langkah-langkah Mengintegrasikan Qontak dengan WhatsApp API di Qontak Omnichannel
- How do I Mengintegrasikan Qontak dengan WhatsApp API?
- Mau Mengintegrasikan Qontak dengan WhatsApp API, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.3
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengintegrasikan Qontak dengan WhatsApp API, Anda memerlukan:

1. **Role Admin** pada akun Qontak Omnichannel
2. **Akun Qontak Omnichannel** yang aktif
3. **Facebook Business Manager** (atau Meta Business Account) — dapat dibuat otomatis jika belum ada
4. **WhatsApp Business Account (WABA)** — akan diverifikasi melalui Facebook Business Manager
5. Akses ke menu **Channel Integration** di Qontak Omnichannel

Jika Anda belum memiliki Meta Business Account dan WhatsApp Business Profile, sistem Qontak akan secara otomatis mendeteksi dan mengarahkan Anda untuk membuatnya.

## Steps  <!-- confidence:high ✓ -->


Pada Qontak Omnichannel, Anda dengan _role_ Admin dapat mengintegrasikan akun Qontak Anda dengan **WhatsApp** melalui menu **Channel Integration**. Melalui menu ini, Anda dapat membuat akun **Facebook Business Manager**(atau **Meta Business Account**), lalu mengintegrasikan Qontak dengan **WhatsApp Business API (WABA)** dari **Facebook Business Manager** yang sudah terverifikasi sebelumnya.
Anda dapat mempelajari tentang:  
[**[Blog] WhatsApp Integration: 4 Cara Mudah Integrasi WA**](https://qontak.com/blog/whatsapp-integration/?utm_source=ecosystem&utm_medium=qontak+%28help+center%29)
**Penting**  
Mulai **tanggal 20 Agustus 2025** , semua pendaftaran **WABA** baru melalui Qontak akan otomatis terintegrasi dengan **Marketing Messages API (MM API)** untuk pengiriman _**campaign marketing**_.  
Akun WhatsApp yang terhubung dengan Qontak sebelum periode di atas dapat diintegrasikan ke **MM API** melalui 2 cara, yaitu:

###  **B. Sudah Memiliki Meta Business Account & WhatsApp Business Profile**[](https://help-center.qontak.com/hc/id/articles/12055228468633-Bagaimana-Cara-Mengintegrasikan-Qontak-dengan-WhatsApp-API#h_01KCG2JT3TWMHR2JKYK2A05XFS)
  1. Klik menu **Channel Integration**.
  2. Lalu pilih **WhatsApp.**  
**![1.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F53356189359001)**
  3. Klik**“Add WhatsApp”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F53356160571929)
  4. Lalu akan muncul _pop-up_ log in Facebook. Masukkan email/nomor telepon dan _password_ Facebook Anda, lalu klik **“Log in”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F53356189407129)
  5. Kemudian akan muncul konfirmasi dari Facebook dan klik **“Continue as (nama akun Anda)”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F53356189408793)
  6. Pada bagian ini, Anda dapat membaca **Syarat dan Ketentuan** untuk mengintegrasikan WhatsApp dengan Qontak. Anda dapat klik **Continue** untuk melanjutkan.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F53356189367833)

- Dengan melanjutkan, Anda telah menerima ketentuan terkait **Hosting Meta untuk Cloud API** , **Ketentuan WhatsApp Business dari Meta** , **Ketentuan Alat Bisnis Meta** , serta **Ketentuan Layanan Marketing Messages API.**  
-**Ads account** akan otomatis terbuat dengan status _Read-only_ **setelah pendaftaran selesai.**  
**![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F53356160525593)**
  7. Apabila Anda telah memiliki akun Facebook Business Manager yang terverifikasi, silakan pilih akun Anda pada kolom**'Business Portfolio'**. Setelah itu, kolom **Business Name** dan **Country** akan terisi secara otomatis. Klik **“Next”** untuk melanjutkan.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F53356160575769)

Demikian penjelasan terkait cara mengintegrasikan Qontak dengan WhatsApp API.

## Error States  <!-- confidence:low ? -->

No common errors documented.

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support (support-qontak@mekari.com) jika Anda mengalami:

1. **Integrasi gagal** meskipun Meta Business Account sudah terverifikasi — sertakan screenshot error dan nama akun Meta Business Manager Anda
2. **WABA tidak muncul** di dropdown pilihan akun — berikan informasi ID WhatsApp Business Account dan screenshot halaman Facebook Business Manager
3. **Pesan "Akun tidak terverifikasi"** — pastikan Meta Business Account sudah selesai verifikasi di Facebook Business Manager sebelum integrasi
4. **Marketing Messages API (MM API) tidak aktif** untuk akun lama — hubungi support dengan nomor WhatsApp Business Account Anda untuk bantuan migrasi manual