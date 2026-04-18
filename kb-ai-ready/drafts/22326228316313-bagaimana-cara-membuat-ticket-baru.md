---
title: Bagaimana Cara Membuat Ticket Baru
canonical_url: https://help-center.qontak.com/hc/id/articles/22326228316313-Bagaimana-Cara-Membuat-Ticket-Baru
article_type: task
solvability_type: tool
products:
- Qontak CRM
- Qontak Chat
product_surface: web
language: id
intent_tags:
- ticket-creation-tracking
- create-ticket-baru
- customer-support-ticketin
query_examples:
- Cara Membuat Ticket Baru
- Bagaimana cara Membuat Ticket Baru?
- Langkah-langkah Membuat Ticket Baru di Qontak CRM
- How do I Membuat Ticket Baru?
- Mau Membuat Ticket Baru, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk membuat tiket baru di Qontak CRM, pastikan Anda memenuhi persyaratan berikut:

• Akses ke Qontak CRM dengan peran pengguna atau admin
• Produk Qontak CRM atau Qontak Chat sudah diaktifkan di akun Anda
• Menu Tickets tersedia dan dapat diakses
• Jika menggunakan custom fields, pastikan fields sudah dibuat terlebih dahulu melalui menu Properties - Tickets
• Data kontak client (Contact) sudah tersedia di sistem jika ingin menghubungkan tiket ke kontak tertentu

## Steps  <!-- confidence:high ✓ -->

1. Buka Qontak CRM dan navigasikan ke menu Tickets. Sistem akan menampilkan daftar tiket yang sudah ada.

2. Klik tombol "Create Ticket" di halaman Tickets. Popup Create Ticket form akan muncul.

3. Isi kolom-kolom berikut sesuai kebutuhan:
   - Ticket Stage: pilih tahapan tiket (New, Assigned, In Progress, atau Done)
   - Ticket name: masukkan nama tiket
   - Description: tambahkan deskripsi kendala (opsional)
   - Assignee: pilih pengguna atau tim yang akan menyelesaikan tiket
   - Ticket Priority: pilih tingkat urgensi (low, medium, high, atau critical)
   - Source: pilih sumber kendala (Call, Email, Chat, Other, atau Multichannel Whatsapp)
   - Due date: tentukan tenggat waktu penyelesaian
   - Contacts: pilih nama kontak client
   - Company: pilih perusahaan client
   - Products: pilih produk terkait (opsional)
   - Task: pilih task terkait (opsional)

4. Klik tombol "Create" untuk menyimpan tiket baru. Sistem akan memproses dan menampilkan konfirmasi bahwa tiket berhasil dibuat.## Expected Result  <!-- confidence:high ✓ -->

Tiket baru berhasil dibuat dan Anda akan melihat pesan konfirmasi. Tiket akan muncul dalam daftar Tickets dengan status sesuai Ticket Stage yang dipilih. Tiket dapat langsung diakses untuk ditambahkan aktivitas, catatan, atau perubahan detail lainnya. Data tiket yang Anda isi akan tersimpan dan dapat dilihat oleh assignee atau pengguna lain yang memiliki akses.

![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56811066453529)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56811070518681)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56811070519577)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56811066466969)
![72.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50827719487257)

## Error States  <!-- confidence:medium ~ -->

Tiket gagal dibuat jika:

• Kolom "Ticket name" kosong atau tidak diisi — isi nama tiket yang deskriptif
• Assignee tidak dipilih saat diperlukan — pastikan memilih pengguna atau tim di kolom Assignee
• Due date tidak valid — gunakan format tanggal yang benar sesuai sistem
• Custom fields (jika ada) belum dibuat — buat fields melalui menu Properties - Tickets terlebih dahulu
• Kontak atau perusahaan yang dipilih tidak aktif — verifikasi data kontak masih valid di menu Contacts

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support jika Anda mengalami:

• Tombol "Create Ticket" tidak muncul atau tidak responsif — sertakan screenshot halaman Tickets
• Popup Create Ticket form tidak terbuka atau terbuka dengan error message — catat error message yang ditampilkan
• Data yang diisi tidak tersimpan meskipun klik "Create" — screenshot form dan error message
• Custom fields tidak muncul di form meski sudah dibuat — verifikasi di menu Properties - Tickets

Siapkan: ID akun, screenshot masalah, daftar field yang digunakan, dan browser/device yang digunakan.