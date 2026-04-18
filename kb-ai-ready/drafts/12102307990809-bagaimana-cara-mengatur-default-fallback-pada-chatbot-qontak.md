---
title: Bagaimana Cara Mengatur Default Fallback pada Chatbot Qontak
canonical_url: https://help-center.qontak.com/hc/id/articles/12102307990809-Bagaimana-Cara-Mengatur-Default-Fallback-pada-Chatbot-Qontak
article_type: task
solvability_type: tool
products:
- Qontak Chat
product_surface: web
language: id
intent_tags:
- conversational-ai-chatbot
- configure-default-fallback
- ai-chatbot-automation
query_examples:
- Cara Mengatur Default Fallback pada Chatbot Qontak
- Bagaimana cara Mengatur Default Fallback pada Chatbot Qontak?
- Langkah-langkah Mengatur Default Fallback pada Chatbot Qontak di Qontak Chat
- How do I Mengatur Default Fallback pada Chatbot Qontak?
- Mau Mengatur Default Fallback pada Chatbot Qontak, caranya gimana?
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
2. Conversation sudah dibuat di menu Chatbot
3. Welcome Message sudah dikonfigurasi
4. User Input dan Bot Response sudah disiapkan
5. Pemahaman tentang tiga opsi Default Fallback: AI response, Send fallback message, dan Assign to agent

## Steps  <!-- confidence:high ✓ -->


Default Fallback dapat digunakan untuk memicu sistem memberikan respon, apabila chatbot tidak mengenali User Input yang diberikan oleh penanya. Anda dapat menetapkan percakapan ke agen tertentu untuk membantu merespon penanya. Berikut langkah-langkahnya:
  1. Masuk ke percakapan yang ingin Anda atur Default Fallback-nya.  
![127.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51514898536601)
  2. Klik ikon**“Setting”** untuk mengubah aturan pada Default Fallback.  
![128.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51514898538265)

Anda perlu mengatur semua Default Fallback (Default Fallback hanya muncul pada Bot Response dan untuk pengaturannya hanya berlaku pada Bot Response terkait) di setiap User Input. Apabila Default Fallback tidak diatur, maka Chatbot akan merespons dengan Bot Response sebelumnya.
  3. Maka Anda akan diarahkan ke halaman berikut.  
![129.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51514928377753)

**No.** | **Nama Tombol/Kolom** | **Deskripsi**  
---|---|---  
1 | AI response | Klik untuk mengaktifkan AI response yang telah Anda kelola sebelumnya di AI Knowledge.  
2 | Send fallback message |  Klik untuk mengaktifkan **send fallback message**. Lalu, isikan pesan tertentu untuk merespon penanya, berikut contohnya.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780920175385)  
3 | Assign to agent |  Klik untuk menugaskan Agent ke dalam percakapan ini.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780920176793)  
**- Auto****:** Sistem akan secara otomatis memilih agen yang aktif atau sedang _online_ untuk merespon percakapan, sistemnya **round robin** atau terpilih secara acak.  
**- Division** : Sistem akan menugaskan agen berdasarkan divisi yang Anda pilih di sini (pilih dari _chat panel_).  
**- Agent** : Pilih Agent yang ditugaskan untuk percakapan ini (pilih dari _chat panel_).  
  4. Klik **“Save conversation”** untuk menyimpan pengaturan fallback ini.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780920179865)

Demikian panduan cara mengatur Default Fallback pada Chatbot Qontak.

## Error States  <!-- confidence:high ✓ -->

• Default Fallback tidak disimpan: Pastikan Anda mengklik tombol Save conversation setelah mengatur opsi fallback. Tanpa menyimpan, pengaturan akan hilang.

• Chatbot merespons dengan Bot Response sebelumnya: Ini terjadi ketika Default Fallback tidak diatur pada User Input tertentu. Atur Default Fallback untuk setiap User Input agar sistem memberikan respons yang konsisten.

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support jika:

• Tombol Setting tidak muncul pada conversation
• Pengaturan Default Fallback tidak tersimpan meskipun sudah diklik Save conversation
• Chatbot tidak merespons sesuai pengaturan fallback yang sudah dikonfigurasi

Sediakan screenshot halaman pengaturan Default Fallback dan ID conversation saat menghubungi support.