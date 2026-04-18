---
title: Bagaimana Cara Melatih Chatbot AI Berdasarkan Pertanyaan yang Tidak Dapat Dijawab
canonical_url: https://help-center.qontak.com/hc/id/articles/41100802729369-Bagaimana-Cara-Melatih-Chatbot-AI-Berdasarkan-Pertanyaan-yang-Tidak-Dapat-Dijawab
article_type: troubleshooting
solvability_type: hybrid
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- conversational-ai-chatbot
- ai-chatbot-automation
query_examples:
- Melatih Chatbot AI Berdasarkan Pertanyaan yang Tidak Dapat Dijawab tidak berhasil,
  kenapa?
- Ada masalah dengan Melatih Chatbot AI Berdasarkan Pertanyaan yang Tidak Dapat Dijawab
- Kenapa Melatih Chatbot AI Berdasarkan Pertanyaan yang Tidak Dapat Dijawab gagal?
- Error waktu Melatih Chatbot AI Berdasarkan Pertanyaan yang Tidak Dapat Dijawab
- 'How to fix: Melatih Chatbot AI Berdasarkan Pertanyaan yang Tidak Dapat Dijawab?'
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Symptom  <!-- confidence:high ✓ -->

Chatbot AI Anda tidak dapat menjawab pertanyaan tertentu dari pengguna. Pertanyaan tersebut muncul di halaman Unanswered questions dengan status Unreviewed, menunjukkan bahwa AI belum memiliki pengetahuan yang cukup untuk merespons. Pengguna mungkin menerima respons fallback (pesan default, dialihkan ke agent) alih-alih jawaban yang relevan dan informatif.## Root Cause  <!-- confidence:high ✓ -->

Chatbot AI tidak dapat menjawab karena keterbatasan basis pengetahuan (knowledge base). Pertanyaan yang baru atau tidak relevan dengan perusahaan belum ditambahkan sebagai sumber pembelajaran AI. AI mempelajari hanya dari sumber jawaban yang telah Anda tambahkan di Training sources. Tanpa sumber ini, sistem tidak dapat mencocokkan pertanyaan pengguna dengan jawaban yang sesuai.

![175.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F53791281592473)
![1.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F41100787751705)
![2.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F41100787752601)
![3.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F41100802675737)
![4.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F41100787757593)
![5.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F41100802683289)
![6.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F41100802684185)
![7.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F41100802686745)
![8.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F41100787762969)
![10.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F41100802715801)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F41100787763865)
![11.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F41100802720409)
![12.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F41100787767449)

## Solution  <!-- confidence:high ✓ -->

**Untuk pertanyaan yang dapat dijawab:**

1. Buka menu Chatbot, pilih tab Training sources, lalu klik AI resources.
2. Klik View questions untuk melihat pertanyaan yang tidak terjawab.
3. Di halaman Unanswered questions, pilih pertanyaan bertanda Unreviewed, klik Actions, lalu pilih Add as source.
4. Halaman Add as text source muncul. Isikan jawaban yang sesuai dengan pertanyaan tersebut.
5. Klik Add. Sistem menampilkan notifikasi dan AI mulai mempelajari sumber jawaban baru.

**Untuk pertanyaan tidak relevan:**

1. Di halaman Unanswered questions, klik Actions pada pertanyaan tidak relevan, lalu pilih Dismiss.
2. Status pertanyaan berubah menjadi Dismiss dan tidak ditampilkan lagi di daftar.

## Escalation  <!-- confidence:medium ~ -->

Jika setelah menambahkan sumber jawaban Chatbot AI masih tidak menjawab pertanyaan dengan benar, atau jika Anda mengalami kesalahan saat mengakses halaman Unanswered questions atau menu Training sources, hubungi tim dukungan Qontak dengan informasi berikut: nomor akun Omnichannel, nama percakapan chatbot, pertanyaan spesifik yang tidak dapat dijawab, serta sumber jawaban yang telah Anda tambahkan.