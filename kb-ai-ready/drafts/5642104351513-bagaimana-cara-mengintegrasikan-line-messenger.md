---
title: Bagaimana Cara Mengintegrasikan Line Messenger
canonical_url: https://help-center.qontak.com/hc/id/articles/5642104351513-Bagaimana-Cara-Mengintegrasikan-Line-Messenger
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- multi-channel-integration
- integrate-line-messenger
- conversation-management
query_examples:
- Cara Mengintegrasikan Line Messenger
- Bagaimana cara Mengintegrasikan Line Messenger?
- Langkah-langkah Mengintegrasikan Line Messenger di Qontak Omnichannel
- How do I Mengintegrasikan Line Messenger?
- Mau Mengintegrasikan Line Messenger, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengintegrasikan Line Messenger dengan Qontak Omnichannel, Anda memerlukan:

1. **Role Admin** di akun Qontak Omnichannel — hanya pengguna dengan role Admin yang dapat melakukan integrasi
2. **Akun Qontak Omnichannel** yang aktif
3. **Akun Line Messenger** yang sudah aktif
4. **Line Channel Token** — token yang diperlukan untuk menghubungkan akun Line dengan Qontak
5. Akses ke menu **Integrations** di Qontak Omnichannel

Jika Anda tidak memiliki role Admin, hubungi tim support kami di support-qontak@mekari.com.

## Steps  <!-- confidence:high ✓ -->

1. Masuk ke akun Qontak Omnichannel Anda.
2. Buka menu **Integrations** dan pilih **Line Messenger** dari daftar channel yang tersedia.
3. Klik tombol **Add Line Account** untuk menyambungkan akun Line. Sistem akan menampilkan form integrasi Line Messenger dengan panduan di bagian kanan.
4. Pada Chat Panel, masukkan **Line Channel Token** Anda.
5. Klik tombol **Install** untuk mengintegrasikan Line. Jika ada field yang kosong, sistem akan menampilkan pesan error "field is required".
6. Tunggu konfirmasi — jika token valid, popup akan menampilkan pesan success. Jika tidak valid, popup akan menampilkan pesan error.
7. Klik **Settings** pada nama Line untuk melihat detail informasi Line Messenger Anda.

> Screenshot: 10.png
> Image: https://help-center.qontak.com/hc/article_attachments/50771100808473

> Screenshot: line.png
> Image: https://help-center.qontak.com/hc/article_attachments/36775773552409

> Screenshot: line1.png
> Image: https://help-center.qontak.com/hc/article_attachments/36775773557273

> Screenshot: line2.png
> Image: https://help-center.qontak.com/hc/article_attachments/36775773559321

> Screenshot: line3.png
> Image: https://help-center.qontak.com/hc/article_attachments/36775763602457

> Screenshot: line4.png
> Image: https://help-center.qontak.com/hc/article_attachments/36775763599001

> Screenshot: line5.png
> Image: https://help-center.qontak.com/hc/article_attachments/36775773562521

> Screenshot: line6.png
> Image: https://help-center.qontak.com/hc/article_attachments/36775763600665

## Expected Result  <!-- confidence:high ✓ -->

Setelah integrasi berhasil, Anda akan melihat:

1. Pesan popup success yang mengkonfirmasi Line Messenger telah terhubung
2. Akun Line Messenger muncul di daftar channel pada menu **Integrations**
3. Halaman Settings menampilkan detail informasi Line Anda (Channel Name dan Channel Secret dalam kondisi disable/tidak dapat diubah)
4. **Admin, Supervisor, dan Agen** dapat mulai menggunakan Line Messenger di Inbox untuk menerima dan mengirim pesan dari pelanggan Line Anda

## Error States  <!-- confidence:medium ~ -->

**Error yang dapat terjadi:**

1. **"Field is required"** — Muncul saat Anda mengklik tombol **Install** tanpa mengisi Line Channel Token. Solusi: Pastikan Line Channel Token sudah dimasukkan dengan benar di Chat Panel sebelum mengklik **Install**.
2. **Error message pada popup** — Token Line yang Anda masukkan tidak valid atau tidak sesuai. Solusi: Verifikasi kembali Line Channel Token Anda dan pastikan Anda menggunakan token yang benar dari akun Line Anda.
3. **Integrasi gagal** — Jika sistem tidak dapat mendeteksi token. Hubungi support-qontak@mekari.com dengan screenshot error dan Channel Token ID Anda.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak di **support-qontak@mekari.com** jika Anda mengalami:

1. Pesan error yang persisten saat mengklik tombol **Install**
2. Token Line diterima tetapi integrasi tetap gagal
3. Tidak dapat mengakses menu **Integrations** (kemungkinan masalah permission/role)
4. Channel Line sudah terintegrasi tetapi pesan tidak masuk ke Inbox

Sertakan dalam laporan:
- Screenshot pesan error lengkap
- Line Channel ID/Account ID
- Email akun Qontak Omnichannel Anda
- Waktu saat error terjadi