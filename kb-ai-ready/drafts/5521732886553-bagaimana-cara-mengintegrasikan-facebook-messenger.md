---
title: Bagaimana Cara Mengintegrasikan Facebook Messenger
canonical_url: https://help-center.qontak.com/hc/id/articles/5521732886553-Bagaimana-Cara-Mengintegrasikan-Facebook-Messenger
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- multi-channel-integration
- integrate-facebook-messenger
- conversation-management
query_examples:
- Cara Mengintegrasikan Facebook Messenger
- Bagaimana cara Mengintegrasikan Facebook Messenger?
- Langkah-langkah Mengintegrasikan Facebook Messenger di Qontak Omnichannel
- How do I Mengintegrasikan Facebook Messenger?
- Mau Mengintegrasikan Facebook Messenger, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengintegrasikan Facebook Messenger dengan Qontak Omnichannel, Anda memerlukan:

1. **Role Admin** pada akun Qontak Omnichannel — hanya Admin yang dapat melakukan integrasi
2. **Akun Qontak Omnichannel** yang aktif
3. **Akun Facebook** yang aktif
4. **Status sebagai admin** pada Halaman Facebook yang akan diintegrasikan
5. Akses ke menu **Channel Integrations** di Qontak Omnichannel

Jika Anda tidak memiliki role Admin, hubungi tim support kami di support-qontak@mekari.com.

## Steps  <!-- confidence:high ✓ -->

1. Masuk ke akun Qontak Omnichannel dengan kredensial Admin Anda.
2. Buka menu **Channel Integrations**, kemudian pilih **Facebook Messenger**.
3. Klik tombol **Add Facebook Messenger**. Sistem akan menampilkan form integrasi Facebook Messenger.
4. Klik **Connect with Facebook**. Sistem akan membuka tab baru dengan halaman login Facebook.
5. Masukkan username dan password Facebook Anda, kemudian klik **Log In**.
6. Ikuti instruksi popup Facebook dan pastikan Anda adalah admin pada Halaman Facebook yang akan diintegrasikan.
7. Pilih **Halaman Facebook** yang ingin diintegrasikan.
8. Klik **Simpan Perubahan**. Sistem akan menyelesaikan integrasi.
9. Facebook Messenger sekarang terhubung — mulai berkomunikasi dengan pelanggan di halaman **Inbox**.

## Expected Result  <!-- confidence:high ✓ -->

Setelah integrasi berhasil:

1. Facebook Messenger muncul di daftar channel yang terintegrasi pada menu **Channel Integrations**
2. Pesan dari pelanggan Facebook Messenger akan masuk ke panel **Inbox**
3. **Admin, Supervisor, dan Agen** dapat melihat dan merespons pesan Facebook Messenger di Inbox
4. Anda dapat mengirim dan menerima pesan langsung dari Facebook Messenger tanpa meninggalkan Qontak Omnichannel
5. Status channel akan menunjukkan **Connected**

## Error States  <!-- confidence:medium ~ -->

**Masalah: Tidak dapat mengklik tombol Add Facebook Messenger**
- Penyebab: Akun Anda tidak memiliki role Admin
- Solusi: Hubungi administrator Qontak Anda untuk meningkatkan role ke Admin

**Masalah: Login Facebook gagal atau popup tertutup**
- Penyebab: Kredensial Facebook salah atau koneksi terputus
- Solusi: Ulangi langkah 4-5, pastikan Anda login dengan akun yang merupakan admin di Halaman Facebook

**Masalah: Halaman Facebook tidak muncul di pilihan**
- Penyebab: Anda bukan admin di Halaman Facebook tersebut
- Solusi: Minta akses admin pada Halaman Facebook, lalu coba integrasi kembali

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak di **support-qontak@mekari.com** jika:

1. Tombol **Add Facebook Messenger** tidak muncul meskipun Anda memiliki role Admin
2. Popup Facebook tidak terbuka atau terus tertutup saat klik **Connect with Facebook**
3. Integrasi selesai tetapi pesan Facebook tidak masuk ke Inbox
4. Channel menunjukkan status **Disconnected** tanpa sebab yang jelas

Sertakan informasi berikut dalam laporan:
- Email akun Qontak Anda
- Nama Halaman Facebook yang diintegrasikan
- Screenshot halaman **Channel Integrations** Anda
- Deskripsi masalah dan kapan pertama kali terjadi