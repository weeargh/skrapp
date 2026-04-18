---
title: Bagaimana Cara Melakukan Integrasi Fitur Comments dengan Akun Instagram
canonical_url: https://help-center.qontak.com/hc/id/articles/12263352540313-Bagaimana-Cara-Melakukan-Integrasi-Fitur-Comments-dengan-Akun-Instagram
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- multi-channel-integration
- perform-integrasi-fitur-comments-denga
- conversation-management
query_examples:
- Cara Melakukan Integrasi Fitur Comments dengan Akun Instagram
- Bagaimana cara Melakukan Integrasi Fitur Comments dengan Akun Instagram?
- Langkah-langkah Melakukan Integrasi Fitur Comments dengan Akun Instagram di Qontak
  Omnichannel
- How do I Melakukan Integrasi Fitur Comments dengan Akun Instagram?
- Mau Melakukan Integrasi Fitur Comments dengan Akun Instagram, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengintegrasikan fitur Comments dengan akun Instagram Anda di Qontak Omnichannel, Anda memerlukan:

- Role Admin di Qontak Omnichannel (hanya Admin yang dapat mengintegrasikan Instagram)
- Akun Instagram Business yang sudah aktif
- Status sebagai admin di Halaman Instagram yang akan diintegrasikan
- Fitur Comments sudah diaktifkan oleh tim support Qontak (hubungi support-qontak@mekari.com)
- Message Control Connected Tools sudah di-enable di Instagram Settings → Privacy → Messages → Connected Tools → Enable Allow Access to Messages

Tanpa Message Control diaktifkan, komentar dari Instagram tidak akan masuk ke chat panel.

## Steps  <!-- confidence:high ✓ -->

1. Login ke akun Qontak Omnichannel Anda dengan kredensial Admin.
2. Buka menu **Channel Integration** dan pilih **Instagram**.
3. Klik tombol **Add Instagram** dan pilih **Comment**.
4. Klik tombol **Continue** untuk melanjutkan — sistem akan menampilkan konfirmasi dari Facebook.
5. Klik tombol **Continue as (nama akun Anda)** pada jendela popup Facebook.
6. Pilih pengaturan impor komentar yang Anda inginkan:
   - **Import all comments**: untuk mengimpor semua komentar pada akun Instagram
   - **Only import comments that are mentioned this instagram account**: untuk mengimpor hanya komentar yang me-mention akun Instagram Anda
7. Klik tombol **Connect** — sistem akan menampilkan notifikasi "Instagram connected" jika berhasil.

## Expected Result  <!-- confidence:high ✓ -->

Integrasi berhasil ketika Anda menerima notifikasi "Instagram connected" di layar Qontak Omnichannel. Setelah itu, komentar dari Instagram akan mulai masuk ke menu **Inbox** Qontak dan dapat dikelola oleh Admin, Supervisor, dan Agent. Anda dapat melihat akun Instagram yang terintegrasi di tab **Comments** dalam menu **Channel Integration**.

## Error States  <!-- confidence:medium ~ -->

**Komentar tidak masuk ke chat panel**: Pastikan Message Control Connected Tools sudah di-enable di Instagram Settings → Privacy → Messages → Connected Tools. Jika belum diaktifkan, komentar tidak akan tersinkronisasi ke Qontak.

**Tidak dapat melakukan integrasi**: Verifikasi bahwa akun Instagram Anda adalah Akun Instagram Business dan Anda adalah admin di Halaman Instagram tersebut. Jika fitur Comments belum diaktifkan, hubungi tim support kami di support-qontak@mekari.com.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak di **support-qontak@mekari.com** jika:

- Fitur Comments belum diaktifkan di akun Anda (ini adalah fitur add-ons yang memerlukan biaya tambahan)
- Integrasi gagal meskipun semua langkah sudah dilakukan
- Komentar tidak muncul di Inbox setelah integrasi berhasil
- Anda ingin melepas integrasi Instagram Comments

Sertakan nama akun Qontak Anda dan username Instagram Business yang akan diintegrasikan.