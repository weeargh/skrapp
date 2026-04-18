---
title: Bagaimana Cara Mengatur DNS Record
canonical_url: https://help-center.qontak.com/hc/id/articles/48958258449433-Bagaimana-Cara-Mengatur-DNS-Record
article_type: task
solvability_type: tool
products:
- Qontak CRM
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- email-campaign
- configure-dns-record
- marketing-campaign-manage
query_examples:
- Cara Mengatur DNS Record
- Bagaimana cara Mengatur DNS Record?
- Langkah-langkah Mengatur DNS Record di Qontak CRM
- How do I Mengatur DNS Record?
- Mau Mengatur DNS Record, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengatur DNS Record guna mendukung fitur Email Campaign, Anda memerlukan:

1. Langganan aktif ke paket Broadcast, Service Suite, Sales Suite, atau Qontak 360
2. Akses ke akun Qontak Omnichannel dengan peran Campaign management
3. Subdomain yang belum digunakan pada layanan email lain
4. Akses ke Domain Manager penyedia domain Anda
5. Email untuk menerima informasi DNS Records dari tim Qontak

Subdomain harus eksklusif untuk pengiriman campaign melalui Qontak dan tidak boleh digunakan untuk kebutuhan lain.

## Steps  <!-- confidence:high ✓ -->

1. Buka halaman pendaftaran subdomain dan email pengirim di akun Qontak Anda.

2. Pada kolom "Company Sub-domain", masukkan nama subdomain (contoh: mail.mekari.com). Pada kolom "Email", masukkan alamat email pengirim (contoh: noreply@mail.mekari.com). Pastikan bagian subdomain pada kedua kolom identik.

3. Centang persetujuan yang tersedia, lalu klik tombol "Daftarkan sekarang" untuk mengirimkan permintaan.

4. Tunggu email dari tim Qontak berisi informasi DNS Records (dikirim dalam 1x24 jam, hari kerja).

5. Login ke Domain Manager Anda dan masukkan DNS Records yang diterima untuk menyelesaikan pendaftaran subdomain.## Expected Result  <!-- confidence:high ✓ -->

Setelah menyelesaikan semua langkah, Anda akan menerima email dari tim Qontak yang berisi informasi DNS Records lengkap (record tipe MX, TXT, dan lainnya). Sistem akan menampilkan subdomain dan email pengirim yang berhasil terdaftar di akun Qontak Anda. Subdomain dan email pengirim kemudian siap digunakan untuk membuat Email Campaign melalui fitur Campaign di Qontak Omnichannel.

![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50344321699481)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50344540069401)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50344540070169)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50344540075289)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50344553181209)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50344553182617)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50344553184281)

## Error States  <!-- confidence:medium ~ -->

Subdomain dan email pengirim tidak cocok: Pastikan bagian subdomain sebelum domain utama (contoh: "mail" pada "mail.mekari.com") sama persis pada kolom "Company Sub-domain" dan bagian sebelum simbol @ pada kolom "Email". Jika berbeda, tim Qontak akan mendaftarkan sesuai kolom "Company Sub-domain".

Subdomain sudah digunakan: Pilih subdomain baru yang belum terdaftar di layanan email manapun.

Email tidak diterima: Periksa folder spam atau gunakan email alternatif yang Anda gunakan untuk login Qontak.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak jika:

1. DNS Records tidak diterima dalam 1x24 jam (hari kerja)
2. Mengalami kesulitan memasukkan DNS Records ke Domain Manager
3. Subdomain atau email pengirim tidak muncul di akun Qontak setelah pendaftaran
4. Menerima pesan error saat mengklik tombol "Daftarkan sekarang"

Siapkan informasi berikut saat menghubungi support: subdomain yang didaftarkan, email pengirim, nama penyedia domain, dan screenshot error jika ada.