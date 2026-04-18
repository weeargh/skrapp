---
title: Bagaimana Cara Menggunakan Flow Bot Response Form pada Tree Diagram
canonical_url: https://help-center.qontak.com/hc/id/articles/46099456527129-Bagaimana-Cara-Menggunakan-Flow-Bot-Response-Form-pada-Tree-Diagram
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- conversational-ai-chatbot
- use-flow-bot-response-form
- ai-chatbot-automation
query_examples:
- Cara Menggunakan Flow Bot Response Form pada Tree Diagram
- Bagaimana cara Menggunakan Flow Bot Response Form pada Tree Diagram?
- Langkah-langkah Menggunakan Flow Bot Response Form pada Tree Diagram di Qontak Omnichannel
- How do I Menggunakan Flow Bot Response Form pada Tree Diagram?
- Mau Menggunakan Flow Bot Response Form pada Tree Diagram, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

1. Akses ke Qontak Omnichannel atau Qontak Chat dengan izin pembuatan chatbot
2. Conversation sudah dibuat di menu Chatbot
3. WhatsApp Flow template sudah dibuat di WhatsApp Business Manager
4. Pengguna memiliki akses untuk mengedit conversation yang dipilih

## Steps  <!-- confidence:high ✓ -->


### B. Cara Membuat Respons Form dalam Diagram Pohon (tidak dalam salam[](https://help-center.qontak.com/hc/id/articles/46099456527129-Bagaimana-Cara-Menggunakan-Flow-Bot-Response-Form-pada-Tree-Diagram#h_01JSGWPR6CBFV0N2YAW5C8ACCE)
  1. Pada diagram pohon berikut, klik **ikon tambah** , lalu pilih **Form**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F46099456518937)
  2. Lalu tentukan **WhatsApp flow template** yang sebelumnya telah dibuat pada halaman WhatsApp Business Manager. Di sini Anda akan melihat pratinjau terkait _form_ yang telah dibuat. Klik **“Next”** untuk melanjutkan.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F46099456508057)
  3. Pada tahap selanjutnya, isikan **Bot response name** , **Header text** , **Message content** , **Button text** , dan **Next action**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F46099495618585)
  4. Selanjutnya klik **“Save”** untuk menyimpan.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F46099456509977)
  5. Maka Form yang telah dibuat akan muncul pada halaman berikut.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F46099495628313)

### C. Cara Mengkonfigurasi Bot Respon Berikutnya[](https://help-center.qontak.com/hc/id/articles/46099456527129-Bagaimana-Cara-Menggunakan-Flow-Bot-Response-Form-pada-Tree-Diagram#h_01JSGWPR6CPX9VFPHYP847RTWB)
  1. Klik bagian **Response** berikut.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F46099456519961)
  2. Lalu pada tab **General** , tentukan **Bot response name** , **Message content** , **Add variable (opsional)** , Attachment (opsional), Conversation tags (opsional), dan Additional settings (opsional). Anda juga dapat centang _toggle_ tersebut untuk mengirimkan _event_ pembelian bila ada. Apabila keseluruhan data telah terisi, klik **“Save”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F46099456521241)

## Error States  <!-- confidence:medium ~ -->

• WhatsApp Flow template tidak muncul: Pastikan template sudah dibuat dan tersimpan di WhatsApp Business Manager
• Form tidak muncul di preview: Verifikasi semua field (Bot response name, Header text, Message content, Button text) sudah diisi dengan benar
• Next action tidak berfungsi: Pastikan Bot Response atau User Input tujuan sudah dikonfigurasi di conversation

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support jika:
• WhatsApp Flow template tidak terdeteksi meskipun sudah dibuat di WhatsApp Business Manager
• Form tidak dapat dikirimkan ke pengguna setelah publish
• Preview conversation menampilkan error saat membuka form
Sertakan screenshot dari Tree Diagram, nama conversation, dan ID WhatsApp Business Account Anda