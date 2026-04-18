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

Untuk mengintegrasikan chat panel Omnichannel dengan Qontak CRM Messenger:

1. Masuk ke akun Qontak Omnichannel Anda dengan kredensial Admin.
2. Buka menu **Integrations**, kemudian pilih **Qontak CRM**. Sistem menampilkan halaman integrasi CRM.
3. Klik tombol **Connect** untuk menyambungkan akun Qontak CRM yang akan diintegrasikan.
4. Klik tombol **Authorize** untuk memberikan otorisasi Omnichannel ke CRM. Sistem akan memeriksa subscription CRM Anda.
5. Jika subscription aktif, proses integrasi berhasil. Sistem menampilkan halaman integrasi CRM dengan status terhubung.

Catatan: Percakapan akan masuk ke CRM sebagai tiket dan tidak akan ditampilkan di inbox Omnichannel.## Expected Result  <!-- confidence:high ✓ -->

Setelah integrasi berhasil, Anda akan:

- Melihat halaman integrasi CRM dengan status **Connected** (terhubung)
- Dapat menerima pesan pada Qontak Omnichannel yang secara otomatis membuat tiket di Qontak CRM
- Melihat tombol **Disconnect** tersedia jika ingin memutuskan integrasi di masa mendatang

Integrasi memungkinkan alur kerja terpadu antara Omnichannel dan CRM tanpa duplikasi pesan di inbox.

![11.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50771314201497)
![12.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50771303044505)
![13.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50771303046297)
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