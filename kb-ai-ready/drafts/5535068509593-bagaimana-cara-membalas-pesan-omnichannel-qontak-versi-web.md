---
title: Bagaimana Cara Membalas Pesan Omnichannel Qontak versi Web
canonical_url: https://help-center.qontak.com/hc/id/articles/5535068509593-Bagaimana-Cara-Membalas-Pesan-Omnichannel-Qontak-versi-Web
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- inbox-inquiry-management
- conversation-management
query_examples:
- Cara Membalas Pesan Omnichannel Qontak versi Web
- Bagaimana cara Membalas Pesan Omnichannel Qontak versi Web?
- Langkah-langkah Membalas Pesan Omnichannel Qontak versi Web di Qontak Omnichannel
- How do I Membalas Pesan Omnichannel Qontak versi Web?
- Mau Membalas Pesan Omnichannel Qontak versi Web, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

- Akun Qontak Omnichannel aktif dengan akses ke menu Inbox
- Role Agent atau Admin untuk membalas pesan
- Minimal satu room chat dengan pesan masuk yang memiliki status Unassigned atau Assigned
- Koneksi internet stabil

## Steps  <!-- confidence:high ✓ -->

1. Masuk ke akun Qontak Omnichannel Anda — sistem menampilkan dashboard utama.
2. Klik menu **Inbox** — sistem menampilkan daftar semua room chat yang masuk.
3. Buka salah satu pesan dengan status Unassigned atau Assigned — sistem menampilkan detail percakapan dan riwayat pesan.
4. Ketikkan balasan Anda di kolom input pesan sesuai dengan pertanyaan atau keluhan customer.
5. Klik tombol **Kirim** — pesan balasan Anda terkirim ke customer.## Expected Result  <!-- confidence:medium ~ -->

Pesan balasan Anda berhasil dikirim dan muncul di dalam room chat dengan timestamp. Status pesan akan menunjukkan bahwa pesan telah terkirim. Customer akan menerima notifikasi balasan Anda melalui channel yang mereka gunakan (WhatsApp, Instagram, atau channel lainnya yang terintegrasi dengan Qontak Omnichannel).

![170.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F53788099058841)

## Error States  <!-- confidence:medium ~ -->

- **Pesan tidak bisa dibalas**: Pastikan status room chat adalah Unassigned atau Assigned. Room dengan status Resolved atau Closed tidak dapat dibalas.
- **Tombol Kirim tidak aktif**: Periksa apakah Anda sudah mengetikkan pesan di kolom input. Kolom tidak boleh kosong.
- **Pesan gagal terkirim**: Verifikasi koneksi internet Anda stabil dan channel yang terintegrasi masih aktif.

## Escalation  <!-- confidence:medium ~ -->

Jika pesan tidak terkirim meskipun sudah mengikuti semua langkah, hubungi support-qontak@mekari.com dengan informasi berikut: ID room chat, screenshot error atau pesan yang gagal, nama channel yang digunakan, dan waktu kejadian. Tim support akan membantu menganalisis masalah integrasi channel atau permission akun Anda.