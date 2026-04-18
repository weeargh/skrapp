---
title: Bagaimana Cara Mengaplikasikan WhatsApp Flow pada Chatbot Qontak Omnichannel
canonical_url: https://help-center.qontak.com/hc/id/articles/46327133282073-Bagaimana-Cara-Mengaplikasikan-WhatsApp-Flow-pada-Chatbot-Qontak-Omnichannel
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- platform
- general-platform
query_examples:
- Cara Mengaplikasikan WhatsApp Flow pada Chatbot Qontak Omnichannel
- Bagaimana cara Mengaplikasikan WhatsApp Flow pada Chatbot Qontak Omnichannel?
- Langkah-langkah Mengaplikasikan WhatsApp Flow pada Chatbot Qontak Omnichannel di
  Qontak Omnichannel
- How do I Mengaplikasikan WhatsApp Flow pada Chatbot Qontak Omnichannel?
- Mau Mengaplikasikan WhatsApp Flow pada Chatbot Qontak Omnichannel, caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengaplikasikan WhatsApp Flow pada Chatbot Qontak Omnichannel, Anda membutuhkan:

- Akun Qontak Omnichannel aktif dengan akses peran Admin atau Supervisor
- WhatsApp Flow template yang sudah dibuat sebelumnya di WhatsApp Business Manager (hubungi tim support di support-qontak@mekari.com untuk membuat WhatsApp Flow)
- Chatbot sudah dikonfigurasi di Qontak Omnichannel
- Koneksi internet stabil untuk mengakses halaman Chatbot

## Steps  <!-- confidence:high ✓ -->

1. Login ke akun Qontak Omnichannel Anda, lalu pilih menu Chatbot. Sistem akan menampilkan daftar chatbot.

2. Klik tab Conversation. Sistem akan menampilkan daftar percakapan yang tersedia.

3. Pilih salah satu Conversation name dari daftar. Halaman conversation terbuka menampilkan detail conversation.

4. Klik ikon tambah, lalu pilih Form. Dialog form creation terbuka.

5. Pilih WhatsApp Flow template yang sudah dibuat di WhatsApp Business Manager. Pratinjau form akan ditampilkan. Klik tombol Next untuk melanjutkan.

6. Isi field Bot response name, Header text, Message content, Button text, dan Next action sesuai kebutuhan Anda.

7. Klik tombol Save untuk menyimpan form. Form akan ditambahkan ke conversation.

8. WhatsApp Flow akan dikirim otomatis ke customer sebagai Bubble message dengan status "Awaiting submission".

9. Setelah customer mengisi form, klik tombol View submitted data pada Bubble message untuk melihat data yang telah disubmit.

## Expected Result  <!-- confidence:high ✓ -->

Setelah berhasil mengaplikasikan WhatsApp Flow pada Chatbot:

- Form WhatsApp Flow muncul dalam daftar conversation dan siap dikirim
- Customer menerima Bubble message berisi WhatsApp Flow dengan judul, deskripsi, dan status "Awaiting submission"
- Setelah customer mengisi form, tombol View submitted data muncul pada Bubble message
- Data yang disubmit customer dapat dilihat dan diakses melalui halaman chatbot

## Error States  <!-- confidence:medium ~ -->

- **WhatsApp Flow template tidak tersedia di dropdown**: Pastikan Anda sudah menghubungi tim support di support-qontak@mekari.com untuk membuat WhatsApp Flow template terlebih dahulu di WhatsApp Business Manager.
- **Tombol Form tidak muncul**: Periksa bahwa Anda memiliki peran Admin atau Supervisor. Peran lain tidak memiliki akses untuk menambahkan form.
- **Form gagal tersimpan**: Pastikan semua field (Bot response name, Header text, Message content, Button text, Next action) telah diisi dengan benar sebelum klik Save.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak di support-qontak@mekari.com jika:

- Anda memerlukan bantuan membuat WhatsApp Flow template baru di WhatsApp Business Manager
- WhatsApp Flow tidak dikirim otomatis ke customer meskipun sudah dikonfigurasi
- Data customer tidak tersimpan setelah form disubmit
- Menerima pesan error saat menyimpan form

Sertakan informasi: screenshot halaman chatbot, nama conversation, dan deskripsi masalah yang dihadapi.