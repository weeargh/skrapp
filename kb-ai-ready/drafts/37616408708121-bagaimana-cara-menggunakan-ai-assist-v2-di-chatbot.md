---
title: Bagaimana Cara Menggunakan AI Assist V2 di Chatbot
canonical_url: https://help-center.qontak.com/hc/id/articles/37616408708121-Bagaimana-Cara-Menggunakan-AI-Assist-V2-di-Chatbot
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- conversational-ai-chatbot
- use-ai-assist-v2
- ai-chatbot-automation
query_examples:
- Cara Menggunakan AI Assist V2 di Chatbot
- Bagaimana cara Menggunakan AI Assist V2 di Chatbot?
- Langkah-langkah Menggunakan AI Assist V2 di Chatbot di Qontak Omnichannel
- How do I Menggunakan AI Assist V2 di Chatbot?
- Mau Menggunakan AI Assist V2 di Chatbot, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

1. Akses ke Qontak Omnichannel atau Qontak Chat dengan izin manajemen chatbot
2. Langganan paket AI Elite Bot aktif
3. Percakapan (conversation) sudah dibuat di menu Chatbot
4. Pengetahuan (knowledge) sudah diimpor di menu Training Source
5. User Input dan Bot Response sudah dikonfigurasi untuk percakapan

## Steps  <!-- confidence:high ✓ -->

**Bagian A: Mengaktifkan AI Assist V2 di Percakapan**

1. Buka menu Chatbot, klik tab "Conversations"
2. Pilih percakapan yang sudah ada atau buat percakapan baru
3. Klik ikon "settings" pada bagian Default fallback
4. Geser toggle "AI response" untuk mengaktifkan AI response
5. Sistem akan menampilkan AI response sudah ditambahkan pada percakapan

**Bagian B: Mengatur AI Assist**

1. Klik "AI training" pada percakapan yang sudah ditambahkan AI
2. Klik "Select Source" untuk memilih pengetahuan yang akan digunakan
3. Centang checkbox source yang diinginkan
4. (Opsional) Klik nama source untuk melihat preview di bagian kanan
5. Klik "Select" untuk menyimpan
6. Sistem akan menampilkan informasi "Training completed" di bagian atas

**Bagian C: Mengatur AI Response**

1. Klik kolom "bot response" pada percakapan
2. Pada Bot response type, pilih "AI response"
3. Masukkan Bot response name yang diinginkan
4. Klik "Select specific sources" untuk memilih learning source
5. Centang learning name yang diinginkan, klik "Select" untuk menyimpan
6. Klik "Save" untuk menyimpan AI response
7. Untuk menambah AI response lainnya, klik ikon tambah (+), pilih "AI response", masukkan nama, tambahkan learning source, lalu klik "Save"

## Expected Result  <!-- confidence:high ✓ -->

AI Assist V2 berhasil diaktifkan dan dikonfigurasi. Anda akan melihat:

1. Toggle "AI response" pada Default fallback dalam status aktif
2. Informasi "Training completed" ditampilkan setelah memilih source
3. AI Response muncul di daftar Bot Response dengan nama yang telah ditetapkan
4. Sistem siap menggunakan pengetahuan yang dipilih untuk merespon pelanggan dalam percakapan

## Error States  <!-- confidence:medium ~ -->

• **Tombol "Select Source" tidak tersedia**: Pastikan pengetahuan (knowledge) sudah diimpor di menu Training Source terlebih dahulu
• **Informasi "Training completed" tidak muncul**: Verifikasi bahwa minimal satu source telah dipilih dan disimpan dengan benar
• **AI Response tidak merespons pelanggan**: Jika tidak ada learning source yang dipilih pada Bot Response, AI akan menggunakan pengetahuan dari menu AI resources sebagai fallback

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim dukungan Qontak jika:

1. Fitur AI Assist V2 tidak terlihat meskipun paket AI Elite Bot sudah aktif
2. Toggle "AI response" tidak dapat diaktifkan pada Default fallback
3. Pengetahuan (knowledge) tidak berhasil diimpor di menu Training Source
4. AI Response memberikan jawaban yang tidak sesuai dengan pengetahuan yang dipilih

Siapkan informasi: ID akun, nama percakapan, learning source yang digunakan, dan screenshot error jika ada.