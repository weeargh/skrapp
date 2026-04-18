---
title: Bagaimana Cara Mengintegrasikan Telegram
canonical_url: https://help-center.qontak.com/hc/id/articles/5555017491225-Bagaimana-Cara-Mengintegrasikan-Telegram
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- multi-channel-integration
- integrate-telegram
- conversation-management
query_examples:
- Cara Mengintegrasikan Telegram
- Bagaimana cara Mengintegrasikan Telegram?
- Langkah-langkah Mengintegrasikan Telegram di Qontak Omnichannel
- How do I Mengintegrasikan Telegram?
- Mau Mengintegrasikan Telegram, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengintegrasikan Telegram dengan Qontak Omnichannel, Anda memerlukan:

- **Role Admin** pada akun Qontak Omnichannel (hanya Admin yang dapat melakukan integrasi Telegram)
- **Akun Qontak Omnichannel** yang aktif
- **Token Telegram Bot** dari akun Telegram Anda
- Akses ke menu **Integrations** di Qontak Omnichannel

Perhatian: Pesan yang masuk dalam channel Telegram di Omnichannel hanya pesan yang dikirim melalui link, bukan melalui nomor telepon.

## Steps  <!-- confidence:high ✓ -->

1. Masuk ke akun Qontak Omnichannel dengan role Admin.
2. Buka menu **Integrations**. Halaman menampilkan daftar channel yang tersedia untuk diintegrasikan.
3. Klik tombol **Add Telegram Channel** untuk memulai proses integrasi.
4. Pada formulir integrasi Telegram yang muncul, masukkan **token Telegram** Anda di kolom yang tersedia.
5. Klik tombol **Install**. Sistem akan memverifikasi token Anda.
6. Jika verifikasi berhasil, pop-up notifikasi "success" akan muncul secara otomatis dan Telegram channel ditambahkan ke daftar integrations.
7. Untuk melihat detail informasi channel Telegram, klik ikon **Settings** pada nama Telegram yang telah terintegrasi.## Expected Result  <!-- confidence:high ✓ -->

Setelah integrasi berhasil:

- Channel Telegram muncul di daftar **Integrations** dengan status aktif
- **Admin, Supervisor, dan Agen** dapat menggunakan channel Telegram di menu **Inbox** untuk menerima dan mengirim pesan
- Halaman **Settings** menampilkan informasi detail channel Telegram Anda (semua field dalam kondisi non-editable)
- Pesan masuk dari Telegram link akan mulai tampil di chat panel Omnichannel

![1.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50699258760985)
![telegram.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774916307737)
![telegram2.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774892739225)
![telegram3.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774892739865)
![telegram4.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774916312985)
![telegram5.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774916315033)
![telegram6.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774892745369)
![telegram7.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774892747545)

## Error States  <!-- confidence:medium ~ -->

**Token Telegram tidak valid atau tidak ditemukan:**
- Pop-up notifikasi "error" akan muncul saat Anda mengklik tombol **Install**
- **Cara mengatasi:** Verifikasi bahwa token Telegram yang Anda masukkan benar. Token harus didapatkan dari Telegram BotFather. Periksa kembali token dan coba **Install** ulang.

**Akun Telegram tidak memiliki permission yang cukup:**
- Integrasi gagal dan error message muncul
- **Cara mengatasi:** Pastikan Anda memiliki akses admin di akun Telegram yang akan diintegrasikan.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak jika:

- Token Telegram sudah benar tetapi integrasi terus menampilkan error setelah beberapa kali percobaan
- Pesan dari Telegram tidak masuk ke chat panel setelah integrasi berhasil
- Anda tidak memiliki role Admin dan memerlukan bantuan untuk mengintegrasikan Telegram

**Kontak support:** support-qontak@mekari.com

**Informasi yang perlu disertakan:** Screenshot error message, token Telegram (jangan tampilkan secara lengkap), ID akun Qontak Omnichannel Anda.