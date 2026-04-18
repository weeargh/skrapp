---
title: Bagaimana Cara Melakukan Auto Resolve
canonical_url: https://help-center.qontak.com/hc/id/articles/6167066294041-Bagaimana-Cara-Melakukan-Auto-Resolve
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- platform
- perform-auto-resolve
- general-platform
query_examples:
- Cara Melakukan Auto Resolve
- Bagaimana cara Melakukan Auto Resolve?
- Langkah-langkah Melakukan Auto Resolve di Qontak Omnichannel
- How do I Melakukan Auto Resolve?
- Mau Melakukan Auto Resolve, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengatur Auto Resolve pada chat di Qontak Omnichannel, Anda membutuhkan:

- Akun Qontak Omnichannel aktif dengan akses Admin
- Akses ke menu Setting dan tab Inbox
- Koneksi internet stabil untuk membuka web Qontak Omnichannel
- Setidaknya satu channel aktif (jika ingin mengatur Auto Resolve untuk channel tertentu)
- Pengetahuan tentang periode inaktivitas percakapan yang diinginkan

## Steps  <!-- confidence:high ✓ -->

1. Login ke akun Qontak Omnichannel Anda dengan kredensial Admin. Dashboard akan ditampilkan.

2. Buka menu **Setting** dan pilih tab **Inbox**. Sistem akan menampilkan opsi pengaturan inbox.

3. Pilih tab **Auto Resolve**. Halaman konfigurasi Auto Resolve akan ditampilkan.

4. Centang **Enable auto-resolve for messages** untuk mengaktifkan auto-resolve pesan, atau **Enable auto-resolve for comments** untuk komentar.

5. Pilih opsi **All channel** (untuk semua channel) atau **Specific channels** (untuk channel tertentu).

6. Jika memilih **All channel**, atur **Inactivity period** (periode tidak aktif percakapan). Jika memilih **Specific channels**, klik **Select channel** dan centang channel yang diinginkan, lalu klik **Done**.

7. Atur **Inactivity period** sesuai kebutuhan Anda.

8. (Opsional) Tambahkan atau cari tag untuk diterapkan ke semua auto-resolved rooms.

9. Klik **Save changes** untuk menyimpan pengaturan Auto Resolve. Sistem akan menyimpan konfigurasi dan menampilkan notifikasi konfirmasi.## Expected Result  <!-- confidence:high ✓ -->

Setelah berhasil menyimpan pengaturan Auto Resolve, fitur akan aktif dan berfungsi sesuai konfigurasi yang telah ditentukan. Chat dari customer akan secara otomatis ter-resolve setelah periode inaktivitas yang telah Anda atur tercapai. Jika Anda menambahkan tag pada Auto Resolve, tag tersebut akan diterapkan ke semua room yang ter-resolve otomatis. Pengaturan akan berlaku untuk channel yang dipilih dan dapat diedit atau dihapus kapan saja melalui menu **Auto Resolve**.

![1.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F26947322330521)
![2.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36777848118169)
![NEW.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36777834109209)
![NEW.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F26947313528985)
![G.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36777834112153)

## Error States  <!-- confidence:medium ~ -->

- Jika Anda menghapus tag dari menu Tag setelah menerapkannya pada Auto Resolve, tag akan terhapus dari pengaturan namun tetap tersisa di room lama yang sudah ter-resolve.

- Jika room tidak ter-resolve setelah periode inaktivitas berakhir, periksa apakah Agent baru saja mengirim pesan. Room tidak akan ter-resolve sampai Agent tidak lagi mengirim pesan dalam jangka waktu yang ditentukan (asalkan pesan terakhir dari customer masih dalam rentang waktu yang ditentukan).

- Jika Anda ingin mengatur channel spesifik tetapi tidak melihat channel tersebut di daftar, pastikan channel sudah aktif dan terhubung dengan akun Qontak Anda.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak jika Anda mengalami:

- Tombol **Save changes** tidak merespons atau pengaturan tidak tersimpan setelah klik save
- Tab **Auto Resolve** tidak tampil di menu Setting → Inbox
- Fitur Auto Resolve tidak berfungsi meskipun sudah diaktifkan dan periode inaktivitas sudah tercapai
- Error message muncul saat mengatur Inactivity period atau memilih channel

Sediakan informasi: screenshot halaman error, nama channel yang bermasalah, browser yang digunakan, dan account ID Qontak Anda.