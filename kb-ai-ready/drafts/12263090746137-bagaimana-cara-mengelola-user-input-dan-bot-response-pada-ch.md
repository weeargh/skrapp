---
title: Bagaimana Cara Mengelola User Input dan Bot Response pada Chatbot
canonical_url: https://help-center.qontak.com/hc/id/articles/12263090746137-Bagaimana-Cara-Mengelola-User-Input-dan-Bot-Response-pada-Chatbot
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- conversational-ai-chatbot
- manage-user-input
- ai-chatbot-automation
query_examples:
- Cara Mengelola User Input dan Bot Response pada Chatbot
- Bagaimana cara Mengelola User Input dan Bot Response pada Chatbot?
- Langkah-langkah Mengelola User Input dan Bot Response pada Chatbot di Qontak Omnichannel
- How do I Mengelola User Input dan Bot Response pada Chatbot?
- Mau Mengelola User Input dan Bot Response pada Chatbot, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Sebelum mengelola User Input dan Bot Response pada Chatbot, pastikan Anda memiliki:

1. Akses ke Qontak Omnichannel atau Qontak Chat dengan izin pembuatan chatbot
2. Conversation yang sudah dibuat di menu Chatbot
3. Welcome Message sudah dikonfigurasi sebelumnya
4. Pemahaman tentang struktur percakapan chatbot dalam bentuk Tree Diagram

## Steps  <!-- confidence:high ✓ -->

1. Buka menu Chatbot dan pilih Conversation yang ingin Anda konfigurasi.
2. Klik tombol "+" kemudian pilih "User input" untuk membuat User Input baru.
3. Sidebar User Input akan muncul. Pilih Input Type: All types (semua jenis input), Image (hanya gambar), atau Text (hanya teks).
4. Jika memilih Input Type "Text", tentukan Input handling: Specific user input (bot merespons input sesuai kata/kalimat yang ditentukan) atau Save user input to variable (menyimpan jawaban pengguna ke variabel).
5. Ulangi langkah 2-4 untuk membuat User Input tambahan sesuai kebutuhan.
6. Klik tombol "+" kemudian pilih "Bot Response" untuk membuat respons bot.
7. Konfigurasi Bot Response sesuai kebutuhan percakapan Anda.## Expected Result  <!-- confidence:high ✓ -->

Setelah menyelesaikan langkah-langkah di atas, User Input dan Bot Response berhasil dikonfigurasi. Chatbot Anda akan:

- Menerima input pengguna sesuai tipe yang ditentukan (teks, gambar, atau semua jenis)
- Merespons dengan Bot Response yang telah Anda rancang
- Menyimpan data pengguna ke variabel jika Anda mengaktifkan opsi "Save user input to variable"
- Menampilkan alur percakapan dalam bentuk Tree Diagram yang siap untuk dipublikasikan

> Screenshot: 120.png
> Image: https://help-center.qontak.com/hc/article_attachments/51040302976025

> Screenshot: 121.png
> Image: https://help-center.qontak.com/hc/article_attachments/51040281074201

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36774149609625

> Screenshot: 122.png
> Image: https://help-center.qontak.com/hc/article_attachments/51040281077785

> Screenshot: 124.png
> Image: https://help-center.qontak.com/hc/article_attachments/51132823692313

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36774149638809

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36774173180313

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36774149640729

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36774173228057

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36774173228697

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36774173181849

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36774173233817

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36774173236633

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36774149645977

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36774149655961

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36774173246745

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36774173240857

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36774149667609

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36774149663385

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36774173243929

## Error States  <!-- confidence:medium ~ -->

Masalah umum yang mungkin Anda hadapi:

- **Bot tidak merespons input pengguna**: Pastikan Input Type yang dipilih sesuai dengan format input pengguna (jika memilih "Text", pengguna harus mengirim teks).
- **Input tidak tersimpan di variabel**: Pastikan opsi "Save user input to variable" sudah diaktifkan pada User Input.
- **Specific user input tidak berfungsi**: Verifikasi bahwa kata/kalimat trigger yang ditentukan di kolom User input cocok dengan input pengguna (perhatian terhadap huruf besar/kecil dan spasi).
- **Conversation tidak bisa disimpan**: Pastikan minimal satu User Input dan Bot Response sudah dikonfigurasi untuk setiap node percakapan.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak jika Anda mengalami:

- Fitur Trigger text (AI package subscriber) tidak berfungsi dengan baik
- Variabel yang disimpan tidak muncul di Bot Response meskipun sudah dikonfigurasi
- Conversation mengalami error saat menyimpan User Input atau Bot Response

Siapkan informasi berikut saat menghubungi support:
- Screenshot konfigurasi User Input dan Bot Response
- Nama Conversation yang bermasalah
- Langkah spesifik yang menghasilkan error
- Tipe input dan handling yang Anda gunakan