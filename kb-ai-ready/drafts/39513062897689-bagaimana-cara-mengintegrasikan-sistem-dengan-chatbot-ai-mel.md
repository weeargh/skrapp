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

1. Buka menu **Chatbot**, pilih submenu **Chatbot settings**, lalu klik tab **"API integration"**. Sistem menampilkan daftar API Connection yang sudah ada.
2. Pada Connection name yang ingin dikonfigurasi, klik **"Action"**, kemudian pilih **"View details"**. Halaman detail API Connection terbuka.
3. Klik **"Add function"**. Form penambahan fungsi baru muncul di layar.
4. Isi semua kolom: Function name, Description, API_path, API_method, API_headers, dan API_body sesuai kebutuhan API Anda.
5. Klik **"Add parameter"** untuk menambahkan parameter (gunakan maksimal satu parameter untuk menghindari halusinasi AI pada tahap Beta).
6. Isi Parameter name, Description, dan Type, lalu centang toggle **"Set as required"**.
7. Klik **"Add"** untuk menyimpan fungsi. Sistem menampilkan konfirmasi bahwa fungsi berhasil ditambahkan.## Expected Result  <!-- confidence:high ✓ -->

Fungsi API berhasil ditambahkan ke API Connection. Halaman detail API Connection menampilkan fungsi baru dalam daftar dengan status aktif. AI Chatbot sekarang dapat mengenali user input yang sesuai dengan deskripsi fungsi dan memanggil API untuk mengambil informasi yang diperlukan, memberikan respons yang lebih manusiawi berdasarkan data dari sistem eksternal.## Error States  <!-- confidence:medium ~ -->

• Halusinasi AI (kesalahan AI dalam memahami Function): Terjadi karena penggunaan parameter lebih dari satu. Solusi: Gunakan hanya satu parameter terlebih dahulu.
• Fungsi tidak dipanggil oleh AI: Kemungkinan deskripsi Function atau Parameter tidak jelas. Solusi: Pastikan Description di Function dan Parameter ditulis secara detail dan spesifik agar AI memahami tujuannya.
• API error response: Periksa kembali API_path, API_method, API_headers, dan API_body sudah benar sesuai dokumentasi API eksternal.

![13.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F53149538347033)
![1.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F39513122309913)
![2.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F39513062844185)
![3.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F39513297951001)
![4.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F39513710420633)
![114.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51038253023641)
![6.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F39513694247705)
![7.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F39513694249497)
![8.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F39513710438809)

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim dukungan Qontak jika:
• Fungsi sudah dikonfigurasi dengan benar tetapi AI tidak merespon sesuai harapan
• Menerima error response konsisten dari API meskipun konfigurasi sudah diverifikasi
• Memerlukan bantuan teknis terkait struktur API atau Function Calling dari OpenAI

Siapkan informasi: screenshot konfigurasi function, Description yang digunakan, contoh user input yang gagal, dan API response error message.