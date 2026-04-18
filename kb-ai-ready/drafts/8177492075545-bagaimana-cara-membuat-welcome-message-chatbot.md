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


3. Untuk mengisi Welcome message, Anda dapat klik kotak _bubble_.  
![111.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51037705692825)
Welcome message adalah pesan pembuka otomatis untuk memulai percakapan dengan customer.
  4. Setelah itu, akan muncul **Bot Response Settings - General** seperti berikut.  
****![112.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51037705696665)  
Keterangan:  
**** **No** |  **Kolom** |  **Penjelasan**  
---|---|---  
1 |  Bot Response Type |  Anda dapat memilih salah satu tipe Bot Response berikut:
     * Text
     * Button
     * List
Untuk Welcome message yang bersifat membuka percakapan, tipe Bot Response yang biasa digunakan adalah **Text.** Untuk penjelasan Bot Response Type yang lebih lengkap, baca guidebook [di sini.](https://help-center.qontak.com/hc/id/articles/12263090746137)  
2 |  Bot Response Name |  Isikan nama Bot Response di sini, dengan nama default "Welcome message".  
3 |  Bot Response Content |  Isikan respon bot di sini, dengan kalimat atau ucapan pembuka default seperti "Welcome to Qontak AI-powered chatbot". Tidak ada batasan karakter pada bubble Bot Response Content. Selain itu, Anda juga dapat klik **"Add variable"** yang berfungsi untuk menampilkan kembali data yang sudah ditambahkan (misalnya nama, email, atau jawaban lain) ke dalam balasan Chatbot, sehingga balasan yang dihasilkan menjadi lebih personal dan bersifat otomatis.  
4 |  Attachment |  Anda dapat melampirkan file di sini. Jumlah maksimal file yang dapat Anda unggah adalah 10 file dan maksimum ukuran file yang dapat diunggah adalah 64 MB. Jenis file yang bisa dapat diunggah adalah Image (.jpeg, .jpg, .png, dan .gif), Video (.mkv, .mov, and .mp4), dan Document (.pdf, .xlsx, .docx, .pptx , .xls, .csv, .s20, dan .cdr). Jika user melampirkan lebih dari 5 file, maka hanya 5 file pertama yang akan ditampilkan. Gunakan tombol X di samping file untuk menghapusnya.  
5 |  Conversations tags |  Anda dapat memasukkan tag pada percakapan bot yang muncul. Tag ini berguna untuk mengelompokkan percakapan berdasarkan tag yang Anda pilih. Klik [di sini](https://help-center.qontak.com/hc/id/articles/5662312564889) untuk mengetahui cara menambahkan tag.  
6 |  Additional Setting |  Gunakan pengaturan tambahan ini, untuk mengatur respon bot.  Untuk penjelasan Additional Setting yang lebih lengkap, baca guidebook [di sini.](https://help-center.qontak.com/hc/id/articles/12128813400857)  
7 |  Send purchase event |  _Toggle_**Send purchase event** adalah opsi untuk menandai respons bot sebagai peristiwa pembelian. Jika diaktifkan, sistem akan mengirimkan data bahwa transaksi telah terjadi, sehingga dapat digunakan untuk keperluan pencatatan, analitik, maupun integrasi dengan aplikasi lain.

Demikian cara membuat welcome message chatbot pada Mekari Qontak Omnichannel.

## Error States  <!-- confidence:low ? -->

No common errors documented.

## Escalation  <!-- confidence:medium ~ -->

Jika Anda mengalami masalah saat membuat Welcome Message Chatbot, hubungi tim support Qontak dengan informasi berikut:

1. Tangkapan layar (screenshot) halaman Bot Response Settings saat error terjadi
2. Nama Conversation yang bermasalah
3. Deskripsi masalah spesifik (contoh: tombol Save tidak merespons, pesan error muncul)
4. ID akun Qontak Anda
5. Jenis browser dan versi yang digunakan