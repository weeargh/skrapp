---
title: Bagaimana Cara Mempublish Chatbot
canonical_url: https://help-center.qontak.com/hc/id/articles/12102666717593-Bagaimana-Cara-Mempublish-Chatbot
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- conversational-ai-chatbot
- ai-chatbot-automation
query_examples:
- Cara Mempublish Chatbot
- Bagaimana cara Mempublish Chatbot?
- Langkah-langkah Mempublish Chatbot di Qontak Omnichannel
- How do I Mempublish Chatbot?
- Mau Mempublish Chatbot, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Sebelum mempublish chatbot, pastikan Anda telah:

1. Memiliki akses ke Qontak Omnichannel atau Qontak Chat dengan izin manajemen chatbot
2. Membuat minimal satu conversation di menu Chatbot
3. Mengonfigurasi Welcome Message pada conversation tersebut
4. Menambahkan User Input dan Bot Response sesuai alur percakapan yang diinginkan
5. Mengatur Default Fallback pada conversation
6. Mengonfigurasi pengaturan tambahan pada Bot Response (terutama opsi Resolve Conversation)
7. Memastikan conversation berstatus "Unpublished" (belum dipublish)

## Steps  <!-- confidence:high ✓ -->

Untuk mempublish chatbot Qontak:

1. Buka menu **Chatbot** di dashboard Qontak Omnichannel atau Qontak Chat. Sistem akan menampilkan daftar conversation yang tersedia.
2. Pilih salah satu **conversation** yang ingin Anda publish dari daftar. Conversation yang dapat dipublish menampilkan status "Unpublished".
3. Klik tombol **"Actions"** pada conversation yang dipilih. Menu dropdown akan muncul dengan beberapa opsi.
4. Klik opsi **"Publish"** dari menu dropdown. Sistem akan memproses permintaan publish.
5. Tunggu hingga proses selesai. Status conversation akan berubah dari "Unpublished" menjadi "Published".

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/51515336067353

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/51515356538393

## Expected Result  <!-- confidence:high ✓ -->

Setelah berhasil mempublish chatbot, Anda akan melihat:

1. Status conversation berubah dari "Unpublished" menjadi "Published" di daftar conversation menu Chatbot
2. Pesan konfirmasi muncul menunjukkan bahwa chatbot telah dipublish dengan sukses
3. Conversation yang dipublish siap digunakan dan dapat diintegrasikan ke channel komunikasi (WhatsApp, Instagram, Facebook, website, dll)
4. Alur percakapan yang telah dikonfigurasi akan aktif dan merespons user input sesuai dengan konfigurasi yang telah dibuat

## Error States  <!-- confidence:medium ~ -->

Jika Anda tidak dapat mempublish conversation, periksa kondisi berikut:

1. **Status conversation bukan "Unpublished"** – Conversation yang sudah dipublish tidak dapat dipublish lagi. Jika ingin mengubah alur, edit conversation yang sudah published dan publish ulang.
2. **Resolve Conversation belum dikonfigurasi** – Setiap Bot Response harus memiliki pengaturan tambahan, minimal dengan opsi "Resolve Conversation". Pastikan semua Bot Response sudah memiliki konfigurasi ini.
3. **User Input atau Bot Response masih kosong** – Conversation memerlukan minimal satu User Input dan satu Bot Response. Pastikan alur percakapan sudah lengkap sebelum publish.
4. **Izin akses tidak cukup** – Pastikan akun Anda memiliki izin manajemen chatbot di Qontak Omnichannel atau Qontak Chat.

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support jika:

1. Tombol **"Publish"** tidak muncul atau tidak dapat diklik meskipun conversation berstatus "Unpublished"
2. Terjadi error message saat mempublish conversation
3. Status conversation tidak berubah ke "Published" setelah mengklik tombol Publish
4. Conversation yang sudah dipublish tidak merespons user input dengan benar

Saat menghubungi support, siapkan:
- Screenshot kondisi error atau pesan error yang muncul
- ID conversation yang bermasalah
- Account ID Qontak Anda
- Deskripsi langkah-langkah yang sudah dilakukan sebelum error terjadi