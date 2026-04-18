---
title: Bagaimana Cara Menangani WhatsApp Campaign yang Gagal Terkirim
canonical_url: https://help-center.qontak.com/hc/id/articles/56839811381017-Bagaimana-Cara-Menangani-WhatsApp-Campaign-yang-Gagal-Terkirim
article_type: troubleshooting
solvability_type: hybrid
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- campaign
- marketing-campaign-manage
query_examples:
- Menangani WhatsApp Campaign yang Gagal Terkirim tidak berhasil, kenapa?
- Ada masalah dengan Menangani WhatsApp Campaign yang Gagal Terkirim
- Kenapa Menangani WhatsApp Campaign yang Gagal Terkirim gagal?
- Error waktu Menangani WhatsApp Campaign yang Gagal Terkirim
- 'How to fix: Menangani WhatsApp Campaign yang Gagal Terkirim?'
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Symptom  <!-- confidence:high ✓ -->

Pesan WhatsApp Campaign Anda tidak berhasil terkirim kepada penerima. Anda dapat melihat status pengiriman yang gagal pada halaman detail Campaign di bagian Campaign Logs. Pesan mungkin menampilkan status error tertentu atau tidak masuk ke dalam daftar pesan yang berhasil dikirim, meskipun campaign sudah dijalankan.

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/56839811374233

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/56839827316633

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/56839827318553

## Root Cause  <!-- confidence:high ✓ -->

Pengiriman WhatsApp Campaign gagal dapat disebabkan oleh beberapa faktor: (1) Messaging Limit pada Business Portfolio Anda sudah mencapai batas harian; (2) Pesan kategori Marketing memiliki aturan pengiriman lebih ketat, termasuk pembatasan per penerima berdasarkan engagement level, kebutuhan opt-in, atau penerima terdaftar dalam eksperimen Meta tanpa Customer Service Window aktif; (3) Error khusus dari Meta seperti template issue, nomor penerima invalid, atau quality rating template rendah.

## Solution  <!-- confidence:medium ~ -->

1. Periksa halaman Campaign Logs di detail Campaign untuk melihat error message spesifik setiap penerima.
2. Identifikasi jenis error menggunakan tabel error message umum pada artikel ini dan referensi error codes Meta.
3. Jika error terkait Messaging Limit, pahami batas pengiriman Business Portfolio Anda dan tunggu reset harian atau tingkatkan limit.
4. Jika campaign kategori Marketing, pastikan penerima telah opt-in dan Customer Service Window aktif jika diperlukan.
5. Verifikasi template WhatsApp memiliki status Connected dan rating High Quality di menu template.
6. Coba kirim ulang campaign setelah masalah diatasi atau ubah waktu pengiriman dengan opsi Send Later.

## Escalation  <!-- confidence:medium ~ -->

Jika campaign tetap gagal setelah mengikuti langkah solusi, hubungi Qontak Support dengan informasi: (1) Screenshot halaman Campaign Logs menampilkan error message lengkap; (2) Campaign ID dan nama campaign yang gagal; (3) Jumlah penerima yang gagal vs berhasil; (4) Template message ID dan nama template yang digunakan; (5) Waktu pengiriman campaign; (6) Business Portfolio name dan Business Account ID Anda di Meta.