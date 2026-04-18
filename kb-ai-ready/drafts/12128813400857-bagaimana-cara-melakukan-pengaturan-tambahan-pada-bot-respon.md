---
title: Bagaimana Cara Melakukan Pengaturan Tambahan pada Bot Response
canonical_url: https://help-center.qontak.com/hc/id/articles/12128813400857-Bagaimana-Cara-Melakukan-Pengaturan-Tambahan-pada-Bot-Response
article_type: task
solvability_type: tool
products:
- Qontak CRM
- Qontak Chat
product_surface: api
language: id
intent_tags:
- conversational-ai-chatbot
- perform-pengaturan-tambahan
- ai-chatbot-automation
query_examples:
- Cara Melakukan Pengaturan Tambahan pada Bot Response
- Bagaimana cara Melakukan Pengaturan Tambahan pada Bot Response?
- Langkah-langkah Melakukan Pengaturan Tambahan pada Bot Response di Qontak CRM
- How do I Melakukan Pengaturan Tambahan pada Bot Response?
- Mau Melakukan Pengaturan Tambahan pada Bot Response, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.3
---

## Prerequisites  <!-- confidence:high ✓ -->

1. Akses ke Qontak Omnichannel atau Qontak Chat dengan izin manajemen chatbot
2. Conversation sudah dibuat di menu Chatbot
3. Welcome Message sudah dikonfigurasi
4. User Input dan Bot Response sudah diatur
5. Minimal satu Bot Response telah dibuat untuk dikonfigurasi Additional Settings

## Steps  <!-- confidence:high ✓ -->

1. Buka menu Chatbot dan pilih conversation yang ingin dikonfigurasi.
2. Klik salah satu Bot Response yang ingin Anda atur pengaturan tambahannya.
3. Sidebar Bot Response Settings akan terbuka pada tab General. Sistem menampilkan 3 pilihan Additional Settings: Default, Resolve Conversation, dan Assign Conversation.
4. Pilih opsi sesuai kebutuhan:
   - **Default**: Gunakan pengaturan default dari Settings Menu Chatbot
   - **Resolve Conversation**: Bot menutup percakapan otomatis. Isi Closing Message dan (opsional) centang Set user idle time untuk menentukan waktu tunggu
   - **Assign Conversation**: Tugaskan agen dengan tipe Auto, Division, atau Agent. (Opsional) centang Set user idle time
5. Klik tombol Save untuk menyimpan pengaturan.

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36780203082265

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36780203086873

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36780203089177

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36780203083033

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36780194384153

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36780194381721

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36780194385817

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36780203094297

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36780203092633

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36780203095833

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36780194390425

## Expected Result  <!-- confidence:medium ~ -->

Pengaturan tambahan Bot Response berhasil disimpan. Sistem menampilkan notifikasi konfirmasi atau kembali ke tampilan Bot Response dengan status pengaturan yang telah diperbarui. Bot Response akan berfungsi sesuai pengaturan Additional Settings yang dipilih (penutupan otomatis percakapan atau penugasan agen).

## Error States  <!-- confidence:low ? -->

No common errors documented.

## Escalation  <!-- confidence:medium ~ -->

Jika pengaturan Additional Settings tidak tersimpan atau Bot Response tidak berfungsi sesuai konfigurasi:
1. Verifikasi bahwa conversation status adalah 'Unpublished' atau 'Published'
2. Pastikan minimal satu User Input telah dikonfigurasi sebelum Bot Response
3. Hubungi support Qontak dengan menyertakan: screenshot pengaturan, nama conversation, dan deskripsi masalah yang dihadapi