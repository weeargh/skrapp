---
title: Bagaimana Cara Mengintegrasikan Shopee dengan Qontak Omnichannel
canonical_url: https://help-center.qontak.com/hc/id/articles/31996013959065-Bagaimana-Cara-Mengintegrasikan-Shopee-dengan-Qontak-Omnichannel
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- multi-channel-integration
- integrate-shopee-dengan-qontak-omnichann
- conversation-management
query_examples:
- Cara Mengintegrasikan Shopee dengan Qontak Omnichannel
- Bagaimana cara Mengintegrasikan Shopee dengan Qontak Omnichannel?
- Langkah-langkah Mengintegrasikan Shopee dengan Qontak Omnichannel di Qontak Omnichannel
- How do I Mengintegrasikan Shopee dengan Qontak Omnichannel?
- Mau Mengintegrasikan Shopee dengan Qontak Omnichannel, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengintegrasikan Shopee dengan Qontak Omnichannel, Anda memerlukan:

• Role Admin di akun Qontak Omnichannel
• Akses ke menu Channel Integration
• Akun Shopee Seller yang aktif
• Shopee Seller ID (dapat ditemukan di URL profil toko Shopee Anda)
• Untuk Self Integration: akses ke Shopee Developer Console dan Shopee API credentials
• Koneksi internet yang stabil untuk proses otorisasi

## Steps  <!-- confidence:high ✓ -->


### B. Cara Melakukan Self Integration[](https://help-center.qontak.com/hc/id/articles/31996013959065-Bagaimana-Cara-Mengintegrasikan-Shopee-dengan-Qontak-Omnichannel#h_01HWYKEZ8PCKQC27511YTGPHM6)
**Penting**  
Untuk melakukan Self Integration, Anda wajib memiliki 
  1. Masuk ke Shopee Developer Console lalu copy **Live Partner id** dan **Live Partner Key** yang terdapat pada Shopee Developer Console serta **Shop ID** Anda.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774529339289)
  2. Pada halaman Shopee Integration di Qontak, Anda dapat klik **“Self Integration”**.  
![4.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49067716021529)
  3. Pada halaman **Add seller - Self integration** , klik **“Continue”** untuk melanjutkan.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774535875993)
  4. Masukkan **Shop ID** , **Live Partner id** dan **Live Partner Key** , didapatkan dari Shopee Developer Console Anda.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774529340953)
  5. Lalu pilih **Seller type** dari Shopee Anda.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774529342745)
  6. Dan klik **“Connect”** untuk mulai menghubungkan.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774529345945)
  7. Kemudian, klik **“Authorize in Shopee”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774535891737)
  8. Kemudian, pada Anda akan masuk ke halaman berikut dan klik tombol **“Confirm Authorization”**.**  
**![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774529347225)
  9. Maka akun Shopee Seller dan Qontak Omnichannel Anda sudah terdaftar.

## Error States  <!-- confidence:medium ~ -->

• **Shopee ID tidak ditemukan**: Pastikan Anda telah menyalin Shopee Seller ID yang benar dari URL profil toko Shopee
• **Otorisasi ditolak di Shopee**: Pastikan Anda login dengan akun Shopee Seller yang sama saat mengklik **Confirm Authorization**
• **Self Integration gagal**: Verifikasi bahwa Shopee Developer Console dan API credentials Anda sudah terdaftar dan aktif
• **Channel Integration menu tidak terlihat**: Periksa bahwa Anda memiliki role Admin di Qontak Omnichannel

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak jika:

• Integrasi gagal setelah mengikuti semua langkah Request Integration
• Status integrasi menunjukkan error atau "Failed" dan tidak berubah setelah 24 jam
• Pesan dari pelanggan Shopee tidak diterima di Qontak setelah integrasi berhasil
• Self Integration tetap gagal meski API credentials sudah benar

Siapkan screenshot error dan Shopee Seller ID Anda saat menghubungi support: support-qontak@mekari.com