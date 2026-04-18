---
title: Bagaimana Cara Mengelola Package Usage AI Chatbot
canonical_url: https://help-center.qontak.com/hc/id/articles/28275811373977-Bagaimana-Cara-Mengelola-Package-Usage-AI-Chatbot
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- platform
- manage-package-usage-ai-chatbot
- general-platform
query_examples:
- Cara Mengelola Package Usage AI Chatbot
- Bagaimana cara Mengelola Package Usage AI Chatbot?
- Langkah-langkah Mengelola Package Usage AI Chatbot di Qontak Omnichannel
- How do I Mengelola Package Usage AI Chatbot?
- Mau Mengelola Package Usage AI Chatbot, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengelola Package Usage AI Chatbot di Qontak Omnichannel, Anda membutuhkan:

- Akun Qontak Omnichannel aktif dengan akses Admin atau Supervisor
- Paket berlangganan aktif dengan fitur AI Chatbot
- Akses ke menu Package Usage di dashboard Qontak Omnichannel
- Koneksi internet stabil untuk membuka antarmuka web Qontak
- Pengetahuan tentang struktur percakapan (Intent Classification dan Chatbot AI) untuk memahami pemakaian kuota

## Steps  <!-- confidence:high ✓ -->

1. Login ke akun Qontak Omnichannel Anda menggunakan kredensial Admin atau Supervisor.

2. Di menu utama, pilih **Package Usage**, kemudian klik tab **Chatbot AI**. Sistem akan menampilkan halaman rincian keterangan pemakaian paket Chatbot AI.

3. Lihat bagian **Initial AI dialogs** untuk melihat kuota AI awal yang didapat dan sisanya. Bagian **Extra AI dialogs** menampilkan kuota tambahan (pascabayar atau prabayar) dan sisanya.

4. Pada tabel **Chatbot AI usage**, lihat informasi lengkap pemakaian per dialog: Room ID, Channel, Account ID, Response Date, Dialog Deduction, dan AI Dialog Usage.

5. Klik **Periode Filter** untuk menyaring rentang waktu yang ditampilkan pada tabel.

6. Klik tombol **Download** untuk mengunduh tabel dalam format CSV (maksimal rentang 90 hari).

## Expected Result  <!-- confidence:high ✓ -->

Setelah mengikuti langkah-langkah, Anda akan melihat:

- Halaman Package Usage AI Chatbot dengan ringkasan kuota awal dan kuota tambahan
- Status sisa kuota AI Dialog yang tersedia
- Tabel Chatbot AI usage yang menampilkan detail lengkap setiap penggunaan dialog
- Kemampuan untuk memfilter data berdasarkan periode waktu
- File CSV siap diunduh berisi riwayat pemakaian kuota hingga 90 hari terakhir

Data ini membantu Anda memantau penggunaan dan merencanakan top up kuota jika diperlukan.

## Error States  <!-- confidence:high ✓ -->

**Kuota AI Dialog hampir habis**: Anda akan menerima banner notifikasi ketika saldo kuota mendekati batas minimum. Tindakan yang dapat dilakukan adalah melakukan top up kuota tambahan melalui menu Package Usage.

**Saldo negatif**: Apabila sisa kuota dari bulan lalu minus (negatif), Initial AI Dialog tidak akan direset sampai tagihan sudah lunas.

**Perbedaan perhitungan kuota**: Setiap 1 pertanyaan dari customer dan 1 jawaban dari Chatbot AI mengurangi 1 AI Dialog. Semua bubble message dari Chatbot AI, termasuk pesan assign dan pesan otomatis saat customer idle, tetap dihitung dan mengurangi kuota.

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support jika mengalami:

- Perbedaan perhitungan kuota AI Dialog yang tidak sesuai dengan penggunaan aktual
- Masalah akses ke menu Package Usage atau tab Chatbot AI
- Kegagalan mengunduh tabel Chatbot AI usage dalam format CSV
- Pertanyaan tentang kebijakan reset kuota pascabayar atau prabayar

Siapkan informasi berikut saat menghubungi support: Account ID, screenshot halaman Package Usage, rentang waktu masalah terjadi, dan deskripsi detail masalah yang dialami.