---
title: Bagaimana Cara Mengintegrasikan Qontak CRM
canonical_url: https://help-center.qontak.com/hc/id/articles/5642795619737-Bagaimana-Cara-Mengintegrasikan-Qontak-CRM
article_type: task
solvability_type: tool
products:
- Qontak CRM
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- multi-channel-integration
- integrate-qontak-crm
- conversation-management
query_examples:
- Cara Mengintegrasikan Qontak CRM
- Bagaimana cara Mengintegrasikan Qontak CRM?
- Langkah-langkah Mengintegrasikan Qontak CRM di Qontak CRM
- How do I Mengintegrasikan Qontak CRM?
- Mau Mengintegrasikan Qontak CRM, caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengintegrasikan Qontak CRM dengan Qontak Omnichannel, Anda memerlukan:

- **Role Admin** pada akun Qontak Omnichannel (hanya pengguna Admin yang dapat melakukan integrasi)
- **Akun Qontak Omnichannel** yang sudah aktif
- **Akun Qontak CRM** yang sudah aktif dan memiliki subscription aktif
- Akses ke menu **Integrations** di Qontak Omnichannel

Jika Anda tidak memiliki role Admin, hubungi tim support kami di support-qontak@mekari.com untuk meminta akses yang diperlukan.

## Steps  <!-- confidence:high ✓ -->


**Integrations** merupakan sebuah fitur Omnichannel Qontak di mana para customer bisa menghubungkan berbagai platform dengan chat panel seperti email atau Instagram.
**Penting**  
Hanya pengguna dengan**role Admin yang dapat melakukan integrasi**. Apabila Anda tidak memiliki akun dengan role Admin, Anda dapat menghubungi tim _support_ kami di [support-qontak@mekari.com](https://help-center.qontak.com/hc/id/articles/support-qontak@mekari.com)
Untuk mengintegrasikan chat panel dengan Qontak CRM Messenger pada Web, Anda perlu mengikuti langkah-langkah berikut:
  1. Masuk ke akun Omnichannel Anda.
  2. Pilih **Integrations** , lalu klik **Qontak CRM**.  
![11.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50771314201497)
  3. Klik **“Connect”** untuk menyambungkan akun qontak CRM yang akan diintegrasikan.  
![12.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50771303044505)
Untuk tampilan integrasi pada CRM tidak akan muncul pada inbox karena yang masuk pada inbox hanya untuk pembuatan tiket ke CRM.
  4. Klik **“Authorize”** untuk mengintegrasikan Omnichannel dengan CRM.  
![13.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50771303046297)
  5. Selanjutnya, sistem akan memeriksa _subscription_ CRM. jika terdapat _subscription_ maka, proses integrasi berhasil dan Anda akan melihat tampilan halaman integrasi CRM.  
![14.1.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50771413989657)

## Error States  <!-- confidence:medium ~ -->

Kemungkinan kendala yang dapat terjadi:

- **Subscription CRM tidak aktif**: Sistem akan menampilkan pesan kesalahan saat melakukan verifikasi subscription. Pastikan subscription CRM Anda aktif sebelum mengulang integrasi.
- **Role bukan Admin**: Jika Anda tidak memiliki role Admin, tombol **Connect** dan **Authorize** tidak akan tersedia. Hubungi administrator akun Anda untuk meningkatkan akses.
- **Otorisasi ditolak**: Jika Anda memilih "Tolak" saat proses Authorize, integrasi akan dibatalkan dan Anda harus memulai dari langkah 3 kembali.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak jika mengalami:

- Subscription CRM tidak terdeteksi meski sudah aktif
- Tombol **Connect** atau **Authorize** tidak responsif
- Integrasi gagal setelah proses Authorize selesai
- Pesan tidak masuk ke CRM setelah integrasi berhasil

Hubungi: **support-qontak@mekari.com**

Sertakan informasi:
- Email akun Qontak Omnichannel Anda
- Screenshot halaman integrasi atau pesan error
- Waktu integrasi dicoba