---
title: Bagaimana Cara Ekspor Report List of Conversations
canonical_url: https://help-center.qontak.com/hc/id/articles/19020437193113-Bagaimana-Cara-Ekspor-Report-List-of-Conversations
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- report-builder
- report-management
query_examples:
- Cara Ekspor Report List of Conversations
- Bagaimana cara Ekspor Report List of Conversations?
- Langkah-langkah Ekspor Report List of Conversations di Qontak Omnichannel
- How do I Ekspor Report List of Conversations?
- Mau Ekspor Report List of Conversations, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:medium ~ -->

Untuk mengekspor Report List of Conversations, Anda memerlukan:
• Akun Qontak Omnichannel aktif dengan kredensial login
• Akses ke menu Reports (umumnya memerlukan izin admin atau reporting)
• Minimal satu percakapan telah terjadi dalam sistem untuk periode yang ingin diekspor
• Data percakapan tersedia di channel yang dipilih

## Steps  <!-- confidence:high ✓ -->

1. Buka Qontak Omnichannel dan login dengan akun Anda → Sistem menampilkan dashboard utama
2. Klik menu **Report** di navigasi utama → Halaman Reports terbuka
3. Pilih tab **General** → Sistem menampilkan laporan umum dengan berbagai tabel
4. Scroll ke bagian bawah halaman hingga menemukan tabel **List of Conversations** → Tabel menampilkan daftar percakapan
5. Klik ikon **Download** pada tabel **List of Conversations** → Halaman ekspor terbuka
6. Klik tombol **Export** → Kartu List of Conversation ditampilkan
7. Pada kartu **List of Conversation**, klik tombol **Export** → Halaman filter ekspor muncul
8. Pilih **Periode** dan **Channel** sesuai kebutuhan, lalu klik **Export** → Proses ekspor dimulai
9. Tunggu hingga halaman menampilkan status ekspor dengan informasi **File Name**, **Exporter**, **Export Date**, dan **Status** → Ekspor sedang diproses atau telah selesai

> Screenshot: 62.png
> Image: https://help-center.qontak.com/hc/article_attachments/50809474876185

> Screenshot: 63.png
> Image: https://help-center.qontak.com/hc/article_attachments/50809446007449

## Expected Result  <!-- confidence:high ✓ -->

Setelah ekspor berhasil:
• Halaman menampilkan status **Completed** dengan detail file (nama file, pengekspor, tanggal ekspor)
• Email notifikasi dikirim ke alamat email terdaftar akun Anda berisi link download file laporan
• File laporan dapat diunduh dan dibuka dalam format CSV untuk analisis lebih lanjut
• Data List of Conversations mencakup semua percakapan sesuai periode dan channel yang dipilih

## Error States  <!-- confidence:medium ~ -->

Status ekspor yang mungkin terjadi:
• **In Progress**: Ekspor masih dalam proses pengunduhan. Tunggu beberapa saat sampai status berubah menjadi Completed
• **Failed/Gagal**: Jika ekspor gagal, periksa kembali pilihan Periode dan Channel, pastikan data tersedia, kemudian ulangi proses ekspor dari langkah 5

Jika email notifikasi tidak diterima setelah status Completed, periksa folder spam atau hubungi tim support Qontak.

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support jika:
• Tombol Download atau Export tidak muncul di halaman Reports → General
• Proses ekspor terus menunjukkan status **In Progress** lebih dari 30 menit
• Email notifikasi ekspor tidak diterima setelah status Completed
• File laporan rusak atau tidak dapat dibuka

Siapkan informasi:
• Screenshot halaman error atau status ekspor
• Account ID / Email akun Qontak
• Periode dan channel yang dipilih untuk ekspor
• Waktu ekspor dilakukan