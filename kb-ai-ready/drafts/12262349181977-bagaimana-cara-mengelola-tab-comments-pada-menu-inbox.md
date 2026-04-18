---
title: Bagaimana Cara Mengelola Tab Comments pada Menu Inbox
canonical_url: https://help-center.qontak.com/hc/id/articles/12262349181977-Bagaimana-Cara-Mengelola-Tab-Comments-pada-Menu-Inbox
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- inbox-inquiry-management
- manage-tab-comments
- conversation-management
query_examples:
- Cara Mengelola Tab Comments pada Menu Inbox
- Bagaimana cara Mengelola Tab Comments pada Menu Inbox?
- Langkah-langkah Mengelola Tab Comments pada Menu Inbox di Qontak Omnichannel
- How do I Mengelola Tab Comments pada Menu Inbox?
- Mau Mengelola Tab Comments pada Menu Inbox, caranya gimana?
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
- Fitur Comments sudah diaktifkan pada akun Anda (hubungi support-qontak@mekari.com jika belum aktif)
- Akun Instagram sudah terintegrasi dengan Qontak Omnichannel
- Minimal satu postingan Instagram yang memiliki komentar dari customer

## Steps  <!-- confidence:high ✓ -->

1. Buka menu **Inbox** di Qontak Omnichannel Anda, lalu pilih tab **Comments** — sistem akan menampilkan daftar room comments yang masuk.
2. Klik salah satu room comments yang ingin Anda lihat — sistem akan menampilkan detail komentar, termasuk agent yang di-assign dan opsi sorting by latest comments.
3. Di sisi kanan, periksa postingan mana yang mendapat komentar dengan klik tombol **See Post** atau nama profil Instagram Anda untuk verifikasi.
4. (Opsional) Klik tombol **Assign Agent** untuk menambahkan agent ke room comments tersebut.
5. Klik tombol **Resolve** untuk menutup room comments — sistem akan berhenti menerima komentar baru pada postingan tersebut.
6. (Jika diperlukan) Klik tombol **Reopen** untuk membuka kembali room comments yang sudah di-resolve.

> Screenshot: 28.png
> Image: https://help-center.qontak.com/hc/article_attachments/36774173109785

> Screenshot: 30.png
> Image: https://help-center.qontak.com/hc/article_attachments/36774173114137

> Screenshot: 40.png
> Image: https://help-center.qontak.com/hc/article_attachments/36774149576089

> Screenshot: 34.png
> Image: https://help-center.qontak.com/hc/article_attachments/36774173121945

> Screenshot: 35.png
> Image: https://help-center.qontak.com/hc/article_attachments/36774149566361

> Screenshot: 41.png
> Image: https://help-center.qontak.com/hc/article_attachments/36774149574809

> Screenshot: 42.png
> Image: https://help-center.qontak.com/hc/article_attachments/36774173152281

## Expected Result  <!-- confidence:high ✓ -->

Tab Comments menampilkan daftar room comments dari Instagram Anda. Setiap room comments menunjukkan: postingan yang mendapat komentar, jumlah komentar, agent yang di-assign, dan status (aktif atau resolved). Setelah klik Resolve, room comments berubah status menjadi tertutup dan tidak akan menerima komentar baru. Setelah klik Reopen, room comments kembali ke status aktif dan siap menerima komentar.

## Error States  <!-- confidence:high ✓ -->

**Fitur Comments tidak tampil di menu Inbox**: Pastikan fitur Comments sudah diaktifkan dengan menghubungi tim support kami di support-qontak@mekari.com dan verifikasi bahwa akun Instagram Anda sudah terintegrasi.

**Postingan Instagram dihapus**: Sistem akan menampilkan notifikasi pada room comments bahwa postingan telah dihapus. History komentar tetap tersimpan di room comments dan tidak akan hilang.

**Agent hilang setelah reopen**: Jika Admin membalas komentar kemudian room di-resolve dan di-reopen, Admin akan keluar otomatis. Jika Agent/SPV tidak login atau status tidak aktif saat reopen, Agent/SPV akan keluar otomatis dari room comments.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak di **support-qontak@mekari.com** dalam situasi berikut:
- Fitur Comments belum diaktifkan pada akun Anda
- Akun Instagram tidak berhasil terintegrasi dengan Qontak Omnichannel
- Komentar customer tidak muncul di tab Comments meskipun sudah ada postingan baru
- Terjadi error saat resolve atau reopen room comments

Sertakan screenshot menu Inbox tab Comments, nama akun Omnichannel, dan deskripsi masalah yang dihadapi.