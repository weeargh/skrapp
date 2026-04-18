---
title: Bagaimana Cara Menggunakan Fitur Natural Language Processing (NLP)
canonical_url: https://help-center.qontak.com/hc/id/articles/20505171141657-Bagaimana-Cara-Menggunakan-Fitur-Natural-Language-Processing-NLP
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- conversational-ai-chatbot
- use-fitur-natural-language-process
- ai-chatbot-automation
query_examples:
- Cara Menggunakan Fitur Natural Language Processing (NLP)
- Bagaimana cara Menggunakan Fitur Natural Language Processing (NLP)?
- Langkah-langkah Menggunakan Fitur Natural Language Processing (NLP) di Qontak Omnichannel
- How do I Menggunakan Fitur Natural Language Processing (NLP)?
- Mau Menggunakan Fitur Natural Language Processing (NLP), caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk menggunakan fitur Natural Language Processing (NLP) pada chatbot Qontak, Anda memerlukan:

1. Akses ke Qontak Omnichannel atau Qontak Chat dengan izin manajemen chatbot
2. Conversation chatbot yang sudah dibuat dan memiliki fitur NLP yang diaktifkan saat pembuatan
3. Jika menggunakan subscription AI Elite bot, pastikan sudah mengatur Bot response accuracy pada saat membuat Conversation
4. Setidaknya satu User Input dan Bot Response sudah dikonfigurasi

## Steps  <!-- confidence:high ✓ -->

1. Buka menu Chatbot dan pilih Conversation yang sudah memiliki fitur NLP aktif. Sistem akan menampilkan detail conversation tersebut.
2. Klik ikon "+ (Tambah)" lalu pilih "User input". Form input akan terbuka.
3. Masukkan user input dan Trigger texts pada kolom yang disediakan, lalu klik tombol "Save". Anda dapat menambahkan multiple trigger texts untuk meningkatkan akurasi.
4. Kembali ke halaman chatbot dan klik "Preview Conversation" untuk memverifikasi bot response yang telah ditetapkan.
5. Konfigurasi jenis respons bot seperti Button, List, Text (with attachment), atau AI Response sesuai kebutuhan.

## Expected Result  <!-- confidence:high ✓ -->

Fitur Natural Language Processing (NLP) berhasil dikonfigurasi. Bot akan merespons user input berdasarkan Trigger texts yang telah Anda tetapkan. Saat user mengirim pesan yang cocok dengan salah satu trigger keyword, chatbot secara otomatis menampilkan Bot Response yang telah Anda atur. Semakin banyak Trigger texts yang ditambahkan, semakin tinggi tingkat akurasi respons chatbot.

## Error States  <!-- confidence:medium ~ -->

• Fitur NLP tidak aktif pada Conversation: Pastikan NLP sudah diaktifkan saat membuat Conversation. Anda perlu membuat Conversation baru dengan mengaktifkan fitur NLP.
• Akurasi respons rendah: Tambahkan lebih banyak Trigger texts untuk melatih chatbot dengan keyword yang lebih bervariasi.
• Bot response tidak muncul saat preview: Verifikasi bahwa Trigger texts sudah tersimpan dengan benar dan Bot Response sudah dikonfigurasi untuk User Input tersebut.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak jika:

• Fitur NLP tidak tersedia atau tidak dapat diaktifkan pada akun Anda
• Mengalami masalah teknis saat mengonfigurasi Trigger texts atau Bot Response
• Tingkat akurasi chatbot tetap rendah meskipun sudah menambahkan banyak keyword

Sediakan informasi: ID Conversation, screenshot error/hasil preview, daftar Trigger texts yang digunakan, dan deskripsi masalah yang dihadapi.