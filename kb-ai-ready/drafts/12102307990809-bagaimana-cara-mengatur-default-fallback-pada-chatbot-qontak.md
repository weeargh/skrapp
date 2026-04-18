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

1. Buka menu Chatbot dan pilih conversation yang ingin diatur Default Fallback-nya.
   Sistem akan menampilkan daftar percakapan yang tersedia.

2. Klik ikon Setting pada conversation tersebut.
   Halaman pengaturan Default Fallback akan terbuka.

3. Pilih salah satu opsi Default Fallback:
   - AI response: Aktifkan respons AI dari AI Knowledge
   - Send fallback message: Aktifkan dan ketikkan pesan khusus untuk penanya
   - Assign to agent: Pilih Auto (acak), Division (berdasarkan divisi), atau Agent (agen spesifik)

4. Klik tombol Save conversation untuk menyimpan pengaturan.
   Sistem akan menampilkan konfirmasi bahwa pengaturan telah disimpan.## Expected Result  <!-- confidence:high ✓ -->

Default Fallback berhasil dikonfigurasi. Ketika penanya memberikan input yang tidak dikenali chatbot, sistem akan merespons sesuai pengaturan yang Anda tetapkan: mengirim respons AI, menampilkan pesan fallback custom, atau mengarahkan ke agen. Status conversation menunjukkan bahwa fallback telah diatur pada setiap Bot Response.

![127.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51514898536601)
![128.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51514898538265)
![129.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51514928377753)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780920175385)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780920176793)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780920179865)

## Error States  <!-- confidence:high ✓ -->

• Default Fallback tidak disimpan: Pastikan Anda mengklik tombol Save conversation setelah mengatur opsi fallback. Tanpa menyimpan, pengaturan akan hilang.

• Chatbot merespons dengan Bot Response sebelumnya: Ini terjadi ketika Default Fallback tidak diatur pada User Input tertentu. Atur Default Fallback untuk setiap User Input agar sistem memberikan respons yang konsisten.

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support jika:

• Tombol Setting tidak muncul pada conversation
• Pengaturan Default Fallback tidak tersimpan meskipun sudah diklik Save conversation
• Chatbot tidak merespons sesuai pengaturan fallback yang sudah dikonfigurasi

Sediakan screenshot halaman pengaturan Default Fallback dan ID conversation saat menghubungi support.