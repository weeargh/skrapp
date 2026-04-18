---
title: Bagaimana Cara Membuat Welcome Message Chatbot
canonical_url: https://help-center.qontak.com/hc/id/articles/8177492075545-Bagaimana-Cara-Membuat-Welcome-Message-Chatbot
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- conversational-ai-chatbot
- create-welcome-message-chatbot
- ai-chatbot-automation
query_examples:
- Cara Membuat Welcome Message Chatbot
- Bagaimana cara Membuat Welcome Message Chatbot?
- Langkah-langkah Membuat Welcome Message Chatbot di Qontak Omnichannel
- How do I Membuat Welcome Message Chatbot?
- Mau Membuat Welcome Message Chatbot, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.3
---

## Prerequisites  <!-- confidence:high ✓ -->

Sebelum membuat Welcome Message Chatbot, pastikan Anda memiliki:

1. Akses ke Qontak Omnichannel atau Qontak Chat dengan izin manajemen chatbot
2. Conversation sudah dibuat sebelumnya di menu Chatbot
3. Quota Bot Response masih tersedia (terlihat di bagian kiri atas halaman dashboard)
4. Pemahaman tentang tipe Bot Response: Text, Button, dan List

## Steps  <!-- confidence:high ✓ -->

1. Pada halaman dashboard Chatbot, klik salah satu nama Conversation yang telah dibuat sebelumnya.
   Sistem akan menampilkan detail conversation dan menunjukkan Bot response quota di bagian kiri atas.

2. Klik kotak bubble untuk mengisi Welcome Message.
   Halaman Bot Response Settings - General akan terbuka.

3. Isi kolom Bot Response Type, Bot Response Name, dan Bot Response Content:
   - Pilih tipe "Text" untuk Welcome Message
   - Masukkan nama (default: "Welcome message")
   - Tulis konten pesan pembuka (contoh: "Welcome to Qontak AI-powered chatbot")

4. Opsional: Tambahkan variable dengan klik "Add variable" untuk personalisasi pesan berdasarkan data customer.

5. Opsional: Lampirkan file di bagian Attachment (maksimal 10 file, ukuran max 64 MB per file).

6. Klik tombol Save untuk menyimpan Welcome Message.

## Expected Result  <!-- confidence:high ✓ -->

Setelah Welcome Message berhasil dibuat dan disimpan:

1. Pesan pembuka akan ditampilkan otomatis saat customer memulai percakapan dengan chatbot
2. Bot Response Name muncul di daftar Bot Response pada conversation tersebut
3. Welcome Message siap digunakan dalam alur chatbot yang telah dikonfigurasi
4. Conversation dapat dilanjutkan dengan menambahkan User Input dan Bot Response tambahan, kemudian dipublish

## Error States  <!-- confidence:low ? -->

No common errors documented.

## Escalation  <!-- confidence:medium ~ -->

Jika Anda mengalami masalah saat membuat Welcome Message Chatbot, hubungi tim support Qontak dengan informasi berikut:

1. Tangkapan layar (screenshot) halaman Bot Response Settings saat error terjadi
2. Nama Conversation yang bermasalah
3. Deskripsi masalah spesifik (contoh: tombol Save tidak merespons, pesan error muncul)
4. ID akun Qontak Anda
5. Jenis browser dan versi yang digunakan