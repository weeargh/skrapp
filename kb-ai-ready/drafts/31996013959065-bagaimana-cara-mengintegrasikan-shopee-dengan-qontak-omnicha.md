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

### A. Request Integration

1. Buka profil toko Shopee Seller Anda dan klik tombol **Lihat Toko Saya**
2. Salin Shopee Seller ID dari URL browser
3. Masuk ke Qontak Omnichannel, buka menu **Channel Integration**, pilih tab **E-commerce**
4. Klik tombol **Add seller**, pilih **Request Integration**, lalu klik **Continue**
5. Masukkan Shopee ID yang telah disalin dan pilih **Seller type** toko Anda
6. Centang persetujuan **"I have read..."** dan klik **Submit**
7. Login kembali ke akun Shopee Seller Anda
8. Klik **Confirm Authorization** untuk menyelesaikan integrasi

### B. Self Integration

Langkah-langkah Self Integration memerlukan akses Shopee Developer Console dan dokumentasi lengkap (lihat bagian "Penting" di artikel lengkap untuk prasyarat tambahan).

## Expected Result  <!-- confidence:high ✓ -->

Setelah langkah terakhir selesai, akun Shopee Seller Anda akan menampilkan status **Connected** atau **Terhubung** di menu Channel Integration tab E-commerce. Anda dapat menerima dan mengirimkan pesan kepada pelanggan Shopee melalui Qontak Omnichannel. Anda juga dapat mengklik menu **Actions** untuk melihat **View details** (detail integrasi) atau **Disconnect** (memutuskan integrasi).

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