---
title: Bagaimana Cara Mengaktifkan AI pada Chatbot
canonical_url: https://help-center.qontak.com/hc/id/articles/28236260430233-Bagaimana-Cara-Mengaktifkan-AI-pada-Chatbot
article_type: task
solvability_type: tool
products:
- Qontak Chat
product_surface: web
language: id
intent_tags:
- conversational-ai-chatbot
- ai-chatbot-automation
query_examples:
- Cara Mengaktifkan AI pada Chatbot
- Bagaimana cara Mengaktifkan AI pada Chatbot?
- Langkah-langkah Mengaktifkan AI pada Chatbot di Qontak Chat
- How do I Mengaktifkan AI pada Chatbot?
- Mau Mengaktifkan AI pada Chatbot, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:medium ~ -->

Sebelum mengaktifkan AI pada chatbot, pastikan Anda memiliki:

1. Akses ke Qontak Chat dengan izin manajemen chatbot
2. Conversation (percakapan) yang sudah dibuat di menu Chatbot
3. User Input dan Bot Response sudah dikonfigurasi
4. Knowledge base AI dan instruksi kepada AI sudah diatur sebelumnya
5. Default Fallback settings sudah dikonfigurasi pada conversation

## Steps  <!-- confidence:high ✓ -->

1. Buka menu **Chatbot** dan pilih conversation yang ingin Anda terapkan AI.
   → Sistem akan menampilkan detail conversation.

2. Klik tombol **"Default fallback"**.
   → Panel pengaturan Default fallback akan terbuka.

3. Geser toggle **"AI response"** ke posisi aktif (on).
   → Toggle akan berubah warna menunjukkan AI response sudah diaktifkan.

4. Klik tombol **"Save changes"**.
   → Sistem akan menyimpan pengaturan AI response pada conversation tersebut.

5. Klik tombol **"Publish"** untuk menyimpan dan mempublikasikan conversation.
   → Status conversation akan berubah menjadi "Published" dan AI siap digunakan.

## Expected Result  <!-- confidence:high ✓ -->

Setelah menyelesaikan langkah-langkah di atas, AI berhasil diaktifkan pada conversation Anda. Toggle AI response pada Default fallback menunjukkan status aktif (on). Conversation dengan status "Published" kini siap menggunakan AI untuk merespons pesan pengguna yang tidak cocok dengan User Input yang sudah didefinisikan. Respons AI akan dikirimkan berdasarkan Knowledge base dan instruksi AI yang telah Anda atur sebelumnya.

## Error States  <!-- confidence:medium ~ -->

Tidak ada error umum yang didokumentasikan untuk fitur ini.

Jika toggle AI response tidak dapat digeser atau tombol Save changes tidak merespons, pastikan:
- Conversation sudah tersimpan sebelumnya
- Knowledge base AI sudah diatur dengan instruksi yang valid
- Anda memiliki izin manajemen chatbot yang tepat
- Tidak ada User Input atau Bot Response yang belum dikonfigurasi

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support jika mengalami:
- Toggle AI response tidak dapat diaktifkan meski Knowledge base sudah diatur
- Tombol Publish tidak berfungsi setelah mengaktifkan AI response
- AI response tidak merespons pesan pengguna setelah conversation dipublikasikan

Siapkan informasi berikut saat menghubungi support:
- ID conversation yang bermasalah
- Screenshot toggle AI response dan Default fallback settings
- Daftar Knowledge base dan instruksi AI yang sudah dikonfigurasi
- Pesan error atau notifikasi yang muncul (jika ada)