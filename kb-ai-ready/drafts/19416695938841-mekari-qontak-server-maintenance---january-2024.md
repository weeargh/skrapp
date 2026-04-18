---
title: Mekari Qontak Server Maintenance - January 2024
canonical_url: https://help-center.qontak.com/hc/id/articles/19416695938841-Mekari-Qontak-Server-Maintenance-January-2024
article_type: task
solvability_type: hybrid
products:
- Qontak CRM
- Qontak Omnichannel
- Qontak Chat
product_surface: api
language: id
intent_tags:
- product-scheduled-maintenance
- general-platform
query_examples:
- Cara Mekari Qontak Server Maintenance - January 2024
- Bagaimana cara Mekari Qontak Server Maintenance - January 2024?
- Langkah-langkah Mekari Qontak Server Maintenance - January 2024 di Qontak CRM
- How do I Mekari Qontak Server Maintenance - January 2024?
- Mau Mekari Qontak Server Maintenance - January 2024, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.9
---

## Prerequisites  <!-- confidence:high ✓ -->

Anda memiliki akun Mekari Qontak yang aktif dengan akses ke salah satu atau lebih dari produk berikut: Qontak CRM, Qontak Omnichannel, atau Qontak Chat. Jika Anda menerapkan Whitelist pada IP Address, pastikan Anda memiliki akses administrator untuk memperbarui konfigurasi IP Address sebelum tanggal pemeliharaan server.

## Steps  <!-- confidence:high ✓ -->

1. Catat tanggal dan waktu pemeliharaan: Sabtu, 20 Januari 2024, pukul 01.00–06.00 WIB.
2. Jika Anda menggunakan Whitelist IP Address, tambahkan kelima IP Address Mekari Qontak terbaru (147.139.199.222, 149.129.246.53, 149.129.195.216, 149.129.194.207, 149.129.251.213) ke dalam daftar whitelist tanpa menghapus IP Address lama.
3. Jika Anda menjalankan layanan 24/7, informasikan kepada pelanggan Anda bahwa Chat tidak dapat diterima selama periode pemeliharaan.
4. Catat nomor hotline Customer Support: +62851 7326 7551 (WhatsApp) untuk situasi darurat yang perlu dieskalasikan.

## Expected Result  <!-- confidence:high ✓ -->

Setelah pemeliharaan selesai pada pukul 06.00 WIB, Mekari Qontak akan kembali beroperasi normal. Qontak Omnichannel akan dapat diakses kembali, semua channel (META, Telegram, Web Chat, Line) dan integrasi akan menerima chat secara normal. Notifikasi WhatsApp dari Qontak CRM akan berfungsi kembali, dan proses Moving Stage Ticket/Deals akan berjalan tanpa delay.

## Error States  <!-- confidence:high ✓ -->

Selama pemeliharaan (01.00–06.00 WIB): (1) Qontak Omnichannel tidak dapat diakses pukul 01.00–03.00 WIB; (2) Chat dari channel META, Telegram, Web Chat, Line, dan Tokopedia tidak diterima; (3) Pengguna yang sudah login melihat notifikasi error; (4) Pengiriman OTP mengalami delay; (5) Reply Chatbot tertunda; (6) Integrasi API eksternal tidak dapat diakses. Semua kondisi ini normal dan akan pulih setelah pukul 06.00 WIB.

## Escalation  <!-- confidence:high ✓ -->

Jika Anda mengalami kendala darurat yang memerlukan eskalasi selama periode pemeliharaan (01.00–06.00 WIB pada 20 Januari 2024), hubungi Customer Support Mekari Qontak melalui WhatsApp di nomor +62851 7326 7551. Siapkan informasi akun Anda. Untuk pertanyaan umum, hubungi Customer Success Mekari Qontak Anda atau kirim email ke support-qontak@mekari.com.