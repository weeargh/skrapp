---
title: Bagaimana Cara Membuat Template Message Campaign (Broadcast)
canonical_url: https://help-center.qontak.com/hc/id/articles/5496892203929-Bagaimana-Cara-Membuat-Template-Message-Campaign-Broadcast
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- campaign-management
- create-template-message-campaign-broa
- marketing-campaign-manage
query_examples:
- Cara Membuat Template Message Campaign (Broadcast)
- Bagaimana cara Membuat Template Message Campaign (Broadcast)?
- Langkah-langkah Membuat Template Message Campaign (Broadcast) di Qontak Omnichannel
- How do I Membuat Template Message Campaign (Broadcast)?
- Mau Membuat Template Message Campaign (Broadcast), caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Anda memerlukan akun Qontak Omnichannel aktif dengan role Admin atau user yang memiliki akses ke menu Campaign (Broadcast). Koneksi internet stabil diperlukan. Tidak ada batasan plan tier khusus untuk membuat template message campaign. Sebelum membuat template, pastikan Anda sudah memahami kategori template yang tersedia di Qontak, terutama jika menggunakan template kategori Marketing yang menerapkan Template Pacing sejak 12 Oktober 2023.

## Steps  <!-- confidence:high ✓ -->

1. Masuk ke akun Qontak Omnichannel Anda. Sistem akan menampilkan dashboard utama.
2. Buka menu Campaign (Broadcast), kemudian klik tab Templates. Daftar template yang ada akan muncul.
3. Klik tombol Create template, lalu pilih Campaign template. Form pembuatan template akan ditampilkan.
4. Isi kolom Template name dengan huruf kecil tanpa spasi dan pastikan tidak sama dengan template yang sudah ada—jika duplikat, sistem akan menolak. Pilih bahasa di kolom Template languages.
5. Di kolom Enter the text for your message, tulis pesan dengan maksimal 1024 karakter. Anda dapat menggunakan format bold, italics, strikethrough, atau menambahkan variabel dengan tombol + Add Variable untuk personalisasi (nama pelanggan, produk, URL, dll).
6. Opsional: Tambahkan media (Image, Video, Document) di Sample Media Content sebagai banner pesan.
7. Opsional: Tambahkan Interactive Message berupa Quick Reply atau Call To Action (Phone).
8. Verifikasi preview pesan di panel kanan.
9. Klik tombol Submit. Sistem akan memproses dan menyimpan template.

## Expected Result  <!-- confidence:high ✓ -->

Setelah klik tombol Submit, template message campaign berhasil dibuat. Sistem akan menampilkan pesan konfirmasi dan template baru akan muncul dalam daftar Templates di menu Campaign (Broadcast). Anda dapat langsung menggunakan template ini untuk membuat broadcast campaign ke banyak konsumen sekaligus. Template akan tersimpan dengan nama yang Anda tentukan dan siap digunakan untuk pengiriman pesan siaran.

## Error States  <!-- confidence:medium ~ -->

1. Template name duplikat: Jika nama template sama dengan yang sudah ada, sistem menampilkan pesan error dan pembuatan template gagal. Solusi: Gunakan nama template yang unik dan belum pernah dibuat sebelumnya.
2. Format template name tidak valid: Jika menggunakan huruf kapital atau spasi, sistem akan menolak. Solusi: Pastikan hanya menggunakan huruf kecil tanpa spasi.
3. Koneksi terputus saat submit: Form akan menampilkan error timeout. Solusi: Periksa koneksi internet dan ulangi proses submit dengan klik tombol Submit kembali.
4. Karakter pesan melebihi batas: Jika pesan lebih dari 1024 karakter, tombol Submit tidak dapat diklik. Solusi: Kurangi jumlah karakter pesan.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak jika Anda mengalami: 1) Template tidak tersimpan meskipun sudah klik Submit dan tidak ada pesan error; 2) Tombol Create template tidak muncul di menu Templates meskipun memiliki akses Admin; 3) Pesan error spesifik yang tidak tersebutkan di atas. Siapkan informasi: screenshot form yang mengalami masalah, nama template yang dibuat, account ID Qontak Anda, dan deskripsi langkah yang sudah dilakukan sebelum error muncul.