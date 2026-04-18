---
title: Bagaimana Cara Mengintegrasikan Sistem dengan Chatbot AI Melalui API Integration
canonical_url: https://help-center.qontak.com/hc/id/articles/39513062897689-Bagaimana-Cara-Mengintegrasikan-Sistem-dengan-Chatbot-AI-Melalui-API-Integration
article_type: task
solvability_type: tool
products:
- Qontak Chat
product_surface: api
language: id
intent_tags:
- conversational-ai-chatbot
- integrate-sistem-dengan-chatbot-ai-melal
- ai-chatbot-automation
query_examples:
- Cara Mengintegrasikan Sistem dengan Chatbot AI Melalui API Integration
- Bagaimana cara Mengintegrasikan Sistem dengan Chatbot AI Melalui API Integration?
- Langkah-langkah Mengintegrasikan Sistem dengan Chatbot AI Melalui API Integration
  di Qontak Chat
- How do I Mengintegrasikan Sistem dengan Chatbot AI Melalui API Integration?
- Mau Mengintegrasikan Sistem dengan Chatbot AI Melalui API Integration, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:medium ~ -->

1. Akses ke Qontak Chat dengan izin pengelolaan chatbot
2. Conversation sudah dibuat di menu Chatbot
3. API Connection sudah dikonfigurasi di tab "API integration"
4. Akun OpenAI atau akses ke fitur Function Calling dari OpenAI
5. Pemahaman dasar tentang struktur API (endpoint, method, headers, body)
6. Minimal satu User Input dan Bot Response sudah dikonfigurasi

## Steps  <!-- confidence:high ✓ -->


Fitur Chatbot telah berhasil melakukan koneksi ke sistem lain melalui **API Integration**. Untuk meningkatkan kualitas dari koneksi Chatbot agar dapat melakukan respon dengan lebih manusiawi, kami telah mengaktifkan **Konfigurasi API** untuk **Chatbot AI** dengan memanfaatkan fitur di **OpenAI** yang disebut **Function Calling**.
Dengan fitur ini, AI dapat memperoleh informasi tentang beberapa hal yang telah dibagikan oleh pelanggan (seperti: nomer resi, dsb.), serta dapat menggunakan informasi tersebut untuk menjawab pertanyaan pelanggan dengan respon yang lebih manusiawi. Berikut ini merupakan tahapan dalam mengintegrasikan sistem dengan Chatbot.
  1. Hal pertama yang perlu Anda lakukan adalah melakukan koneksi terlebih dahulu dengan masuk ke menu **Chatbot** , lalu pilih submenu **Chatbot settings** , dan klik tab **"API integration"**. Kemudian klik **“Add API connection”** untuk melakukan koneksi. Pelajari selengkapnya [di sini](https://help-center.qontak.com/hc/id/articles/27509223794073-Bagaimana-Cara-Melakukan-Pengaturan-Chatbot#h_01HKXVVB1Z602HH452K9K40Y11).  
![13.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F53149538347033)
  2. Setelah menyiapkan koneksi, kita perlu menentukan parameter fungsi sehingga AI dapat mengambil informasi. Pada salah satu **Connection name** , klik **"Action"** , lalu pilih **"View details"**. Kemudian, klik **“Add function”** pada halaman _detail_ **API Connection**.  
![1.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F39513122309913)
  3. Kemudian isikan kolom-kolom berikut.  
![2.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F39513062844185)  
**Keterangan:**
**No** | **Nama Fitur** | **Penjelasan**  
---|---|---  
1 | **Function name** | Isikan nama pada **Function** yang akan digunakan.  
2 | **Description** | Deskripsikan fungsi. Dalam hal ini, Anda **wajib** mengisikan deskripsi agar AI dapat memahami tujuan dari **Function**. Deskripsi tersebut akan membantu AI dalam mengenali user input yang dimasukkan atau ditanyakan.  
3 | **API_path** | Isikan alamat yang memungkinkan Anda mengakses API dan berbagai fiturnya  
4 | **API_method** | Isikan API_method untuk melakukan _release_ pada permintaan metode dan respons metode  
5 | **API_headers** | Isikan bagian API_headers.  
6 | **API_body** | Isikan bagian API_body.  
7 | **Add parameter** |  Tambahkan fungsi parameter dengan klik tombol tersebut.   
Apabila Anda menambahkan parameter, maka akan muncul kolom berikut yang terdiri dari **Parameter name** , **Description** , dan **Type**. Kemudian centang toggle **“Set as required”** agar sistem AI dapat bekerja.  
![3.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F39513297951001) Pada kolom **Description** , Anda perlu mengisikan deskripsi secara jelas agar AI dapat memahami tujuan dari **Function**. Deskripsi tersebut akan membantu AI dalam mengenali user input yang dimasukkan atau ditanyakan.  
Untuk saat ini, harap gunakan hanya **satu parameter** terlebih dahulu untuk menghindari halusinasi (kesalahan AI dalam memahami **Function**) dikarenakan pemanggilan **Function** masih dalam **Tahap Beta**.
  4. Setelah keseluruhan data terisi, klik **“Add”**.  
![4.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F39513710420633)
  5. Setelah semua koneksi diatur, masuk ke halaman **Conversations** pada menu Chatbot, lalu pilih salah satu **Conversation name**.  
![114.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51038253023641)
  6. Pada salah satu **Conversation name** tersebut, Anda dapat mengatur respons bot mana yang akan terhubung ke API. Pada bagian **AI response** , klik **“knowledge sources”** seperti pada tampilan berikut.   
![6.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F39513694247705)

API Integration ini hanya akan ditampilkan di **AI Bot Response**. Jadi, Anda perlu membuat **AI Bot Response** terlebih dahulu.
  7. Lalu akan muncul kotak informasi **Bot response - Welcome message** berikut, setelah itu pilih tab **API Integration**. Centang kotak **Use API Learning Source**.  
![7.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F39513694249497)
  8. Kemudian, Anda **wajib** memilih **API Connection** yang telah dibuat sebelumnya dan memilih **Parameter**.  
![8.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F39513710438809)
  9. Jika semua langkah sudah dilakukan, **Chatbot AI** dapat terhubung ke **API** untuk mendapatkan informasi.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim dukungan Qontak jika:
• Fungsi sudah dikonfigurasi dengan benar tetapi AI tidak merespon sesuai harapan
• Menerima error response konsisten dari API meskipun konfigurasi sudah diverifikasi
• Memerlukan bantuan teknis terkait struktur API atau Function Calling dari OpenAI

Siapkan informasi: screenshot konfigurasi function, Description yang digunakan, contoh user input yang gagal, dan API response error message.