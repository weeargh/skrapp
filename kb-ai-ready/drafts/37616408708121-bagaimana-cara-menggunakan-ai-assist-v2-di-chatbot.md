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


### B. Mengatur AI Assist[](https://help-center.qontak.com/hc/id/articles/37616408708121-Bagaimana-Cara-Menggunakan-AI-Assist-V2-di-Chatbot#h_01J7JDWFA8ZS8XD528DF6480WF)
Selanjutnya, Anda akan mengatur pengetahuan yang akan digunakan AI dalam percakapan.
  1. Setelah AI pada percakapan ditambahkan, selanjutnya, Anda dapat mengatur AI Assist dengan klik **“AI training”**.  
**![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F37616417564569)**
  2. Anda akan masuk ke halaman AI training, di sini Anda dapat memilih pengetahuan yang akan digunakan ke dalam percakapan dengan klik **“Select Source”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F37616417565721)
  3. Pilih _source_ yang ingin Anda gunakan pada percakapan dengan mencentang _checkbox_.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F37616408667929)
  4. Anda juga dapat melihat _preview_ dari _source_ tersebut dengan klik **“nama source”**. Maka _preview_ akan terlihat di bagian kanan.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F37616408669977)

### C. Mengatur AI Response[](https://help-center.qontak.com/hc/id/articles/37616408708121-Bagaimana-Cara-Menggunakan-AI-Assist-V2-di-Chatbot#h_01J7JDWFA8W1YC5YBKTB4R9ZRC)
Setelah memilih pengetahuan untuk percakapan, selanjutnya Anda dapat membuat Bot response baru yang akan menggunakan AI dalam percakapan. Dengan bot respons ini, Anda dapat menggunakan AI misalnya mengucapkan kalimat pembuka (_greetings_). 
  1. Pada percakapan yang sudah diterapkan AI, klik kolom **“bot response”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F37616408671769)
  2. Pada **Bot response type** , pilih **AI response**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F37616417578137)

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