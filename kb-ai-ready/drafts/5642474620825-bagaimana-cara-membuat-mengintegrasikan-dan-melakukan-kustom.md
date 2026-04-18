---
title: Bagaimana cara Membuat, Mengintegrasikan dan Melakukan Kustomisasi Qontak Web
  Chat
canonical_url: https://help-center.qontak.com/hc/id/articles/5642474620825-Bagaimana-cara-Membuat-Mengintegrasikan-dan-Melakukan-Kustomisasi-Qontak-Web-Chat
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- multi-channel-integration
- create-mengintegrasikan
- conversation-management
query_examples:
- Cara Membuat, Mengintegrasikan dan Melakukan Kustomisasi Qontak Web Chat
- Bagaimana cara Membuat, Mengintegrasikan dan Melakukan Kustomisasi Qontak Web Chat?
- Langkah-langkah Membuat, Mengintegrasikan dan Melakukan Kustomisasi Qontak Web Chat
  di Qontak Omnichannel
- How do I Membuat, Mengintegrasikan dan Melakukan Kustomisasi Qontak Web Chat?
- Mau Membuat, Mengintegrasikan dan Melakukan Kustomisasi Qontak Web Chat, caranya
  gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk membuat, mengintegrasikan, dan melakukan kustomisasi Qontak Web Chat, Anda memerlukan:

- **Role Admin** pada akun Qontak Omnichannel (hanya pengguna dengan role Admin yang dapat melakukan integrasi)
- **Akun Qontak Omnichannel** yang aktif
- **Akses ke menu Channel Integration** di dashboard Qontak Omnichannel
- **Domain website** tempat Anda akan menempatkan Web Chat widget
- **Logo dan palet warna** (opsional) untuk kustomisasi tampilan widget

Jika Anda tidak memiliki role Admin, hubungi tim support kami di support-qontak@mekari.com untuk mendapatkan akses yang diperlukan.

## Steps  <!-- confidence:high ✓ -->

**Membuat Widget Web Chat Baru:**

1. Buka menu **Channel Integration** dan pilih **Web Chat**.
2. Klik tombol **Add widget**.
3. Isi kolom **Widget name** (nama widget) dan **Domain** (domain website Anda).
4. Klik tombol **Connect**. Sistem akan memproses data Anda.
5. Jika berhasil, pop-up **Widget Created** akan muncul sebagai konfirmasi. Klik **OK** untuk menutupnya.

**Mengelola Isi dan Tampilan Widget:**

6. Pada daftar widget, klik **Action** pada widget yang ingin dikelola.
7. Pilih **Set up widget**.
8. Di halaman Widget setup, Anda dapat melihat Widget status, Widget ID, Widget name, Domain, dan Embed code. Gunakan tombol **Copy** untuk menyalin Widget ID atau Embed code.
9. Pada bagian **Widget appearance**, unggah logo dan tentukan warna-warna widget sesuai preferensi Anda.

> Screenshot: 1.png
> Image: https://help-center.qontak.com/hc/article_attachments/49062472998425

> Screenshot: Connect_webchat.png
> Image: https://help-center.qontak.com/hc/article_attachments/36772398702233

> Screenshot: Stage.png
> Image: https://help-center.qontak.com/hc/article_attachments/36772398727193

> Screenshot: Widget_setup.png
> Image: https://help-center.qontak.com/hc/article_attachments/36772398732697

> Screenshot: Widget_appearance.png
> Image: https://help-center.qontak.com/hc/article_attachments/36772391182617

> Screenshot: Widget_content.png
> Image: https://help-center.qontak.com/hc/article_attachments/36772391181337

> Screenshot: Widget_preview.png
> Image: https://help-center.qontak.com/hc/article_attachments/36772398731673

> Screenshot: Delete1.png
> Image: https://help-center.qontak.com/hc/article_attachments/36772391165849

## Expected Result  <!-- confidence:high ✓ -->

Setelah berhasil menyelesaikan langkah-langkah di atas, Anda akan mendapatkan:

- **Widget Created**: Pop-up konfirmasi menunjukkan widget telah berhasil dibuat
- **Widget ID**: Nomor identifikasi unik yang dapat disalin untuk referensi
- **Embed code**: Kode siap pakai yang dapat ditambahkan ke website Anda
- **Widget setup page**: Halaman manajemen lengkap dengan kontrol status koneksi (toggle on/off), informasi widget, dan pengaturan tampilan
- **Kustomisasi aktif**: Logo dan warna widget sudah diterapkan sesuai desain yang Anda tentukan

Widget Web Chat Anda siap dipasang dan digunakan di website.

## Error States  <!-- confidence:high ✓ -->

**Error Input Data:**

Jika data yang Anda masukkan tidak sesuai atau salah, pop-up **Error** akan muncul dengan penjelasan ketidaksesuaian. Kemungkinan penyebab:

- **Domain tidak valid**: Pastikan format domain benar (contoh: www.example.com)
- **Widget name kosong**: Isi kolom Widget name dengan nama yang deskriptif
- **Domain sudah terdaftar**: Gunakan domain berbeda yang belum terintegrasi
- **Format domain tidak sesuai**: Periksa kembali penulisan domain tanpa spasi atau karakter khusus

Koreksi data sesuai pesan error, lalu coba **Connect** kembali.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak di **support-qontak@mekari.com** jika:

- Anda tidak memiliki **role Admin** dan membutuhkan akses integrasi
- Pop-up **Error** terus muncul meskipun data sudah dikoreksi
- **Widget** tidak muncul di website setelah kode embed dipasang
- **Embed code** tidak berfungsi atau tidak merespons
- Terjadi masalah teknis pada halaman **Widget setup** atau **Widget appearance**

Sertakan informasi berikut dalam laporan:
- Nama widget dan domain yang digunakan
- Screenshot error atau pop-up yang muncul
- Langkah-langkah yang telah Anda coba
- Browser dan versi yang Anda gunakan