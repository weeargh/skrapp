---
title: Bagaimana Cara Mengatur AI pada Chatbot Qontak
canonical_url: https://help-center.qontak.com/hc/id/articles/28235612558745-Bagaimana-Cara-Mengatur-AI-pada-Chatbot-Qontak
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
- Cara Mengatur AI pada Chatbot Qontak
- Bagaimana cara Mengatur AI pada Chatbot Qontak?
- Langkah-langkah Mengatur AI pada Chatbot Qontak di Qontak Omnichannel
- How do I Mengatur AI pada Chatbot Qontak?
- Mau Mengatur AI pada Chatbot Qontak, caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

1. Akses ke Qontak Omnichannel atau Qontak Chat dengan izin manajemen chatbot
2. Menu Chatbot sudah tersedia di akun Anda
3. Koneksi internet stabil untuk mengakses dan memproses URL atau file
4. File knowledge dalam format PDF (jika menggunakan metode impor file)
5. URL website yang ingin dijadikan sumber pelatihan AI (jika menggunakan metode URL eksternal)

## Steps  <!-- confidence:high ✓ -->

**Untuk Menambahkan URL:**
1. Buka menu Chatbot
2. Klik "Training sources" di bagian AI resources
3. Klik "Add source" dan pilih External URL
4. Salin URL eksternal yang diinginkan dan klik "Save"
5. Sistem memproses URL tersebut
6. Preview data muncul; edit jika ada konten tidak relevan
7. Klik "Save and train" untuk menyimpan

**Untuk Impor File Knowledge:**
1. Buka menu Chatbot
2. Klik "Training sources" di bagian AI resources
3. Klik "Add source" dan pilih File upload
4. Klik "browse" atau drag file PDF ke kolom yang disediakan
5. Klik "Save" untuk mengimpor file

## Expected Result  <!-- confidence:high ✓ -->

Setelah menambahkan URL: URL eksternal berhasil ditambahkan sebagai sumber pelatihan AI. Data dari website ditampilkan dalam preview dan siap digunakan oleh AI Chatbot.

Setelah impor file: File knowledge berhasil diimpor ke sistem. Konten file tersimpan sebagai sumber pengetahuan AI dan dapat digunakan untuk melatih chatbot menjawab pertanyaan pelanggan.

## Error States  <!-- confidence:medium ~ -->

1. **URL tidak dapat diakses**: Pastikan URL valid, website dapat diakses publik, dan tidak memerlukan login atau autentikasi khusus.
2. **File terlalu besar atau format tidak didukung**: Gunakan file PDF sesuai contoh format. Download "PDF example" untuk referensi format yang benar.
3. **Preview menampilkan data tidak lengkap**: Edit preview untuk menghapus konten tidak relevan sebelum klik "Save and train".
4. **Resync gagal**: Periksa apakah website masih tersedia dan tidak ada perubahan struktur halaman.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak jika mengalami:
1. URL atau file tidak berhasil diproses setelah beberapa menit
2. Error message spesifik muncul saat menyimpan training source
3. AI tidak mengenali konten yang sudah dilatih

Siapkan informasi: nama website/nama file, screenshot error, ID percakapan chatbot, dan waktu saat error terjadi.