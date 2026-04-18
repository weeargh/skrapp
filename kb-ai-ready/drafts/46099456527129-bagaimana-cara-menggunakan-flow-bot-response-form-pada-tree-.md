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

1. Masuk ke akun Qontak Omnichannel, pilih menu Chatbot
2. Pilih tab Conversation
3. Pilih salah satu Conversation name yang ada
4. Klik ikon tambah pada bagian Greetings — sistem akan menampilkan pilihan Bot response type
5. Pilih WhatsApp Flow template yang telah dibuat di WhatsApp Business Manager — preview form akan ditampilkan
6. Klik Next untuk melanjutkan
7. Isikan Bot response name, Header text, Message content, Button text, dan Next action
8. Klik Save — form akan disimpan dan muncul pada halaman conversation
9. Klik Preview conversation untuk melihat tampilan form di percakapan

## Expected Result  <!-- confidence:high ✓ -->

Form Bot Response berhasil dibuat dan tersimpan. Form akan muncul pada halaman Tree Diagram di bagian Greetings. Saat preview conversation, pengguna dapat melihat form dengan Header text, Message content, dan Button text yang telah dikonfigurasi. Bot siap mengirimkan form kepada pengguna sebagai greeting awal conversation.

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