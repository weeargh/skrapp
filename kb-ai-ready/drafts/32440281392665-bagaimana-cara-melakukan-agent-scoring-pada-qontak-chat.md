---
title: Bagaimana Cara Melakukan Agent Scoring pada Qontak Chat
canonical_url: https://help-center.qontak.com/hc/id/articles/32440281392665-Bagaimana-Cara-Melakukan-Agent-Scoring-pada-Qontak-Chat
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- agent-performance-and-quality-assurance
- perform-agent-scoring
- customer-support-ticketin
query_examples:
- Cara Melakukan Agent Scoring pada Qontak Chat
- Bagaimana cara Melakukan Agent Scoring pada Qontak Chat?
- Langkah-langkah Melakukan Agent Scoring pada Qontak Chat di Qontak Omnichannel
- How do I Melakukan Agent Scoring pada Qontak Chat?
- Mau Melakukan Agent Scoring pada Qontak Chat, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk melakukan Agent Scoring pada Qontak Chat, Anda memerlukan:

• Akun Qontak Omnichannel aktif dengan role supervisor, manager, atau admin
• Akses ke menu Settings dan Scorecard
• Pemahaman tentang parameter penilaian kinerja agen
• Belum ada Scorecard yang dibuat sebelumnya (jika membuat baru)

Proses ini memerlukan dua tahap utama: membuat Scorecard beserta parameter penilaian, kemudian melakukan penilaian terhadap agen pada ruang percakapan.

## Steps  <!-- confidence:high ✓ -->

**Membuat Scorecard:**

1. Login ke akun Omnichannel dan pilih menu Settings → Klik Scorecard.
2. Pada tab Scorecard, klik tombol Create scorecard.
3. Isi kolom Scorecard name (wajib) dan Description → Klik Add parameter.
4. Pilih maksimum 12 parameter penilaian atau buat parameter baru via Create parameter.
5. Isi Parameter name, Description, dan aktifkan toggle jika ingin menyertakan alasan 'bad rating' → Klik Save.
6. Klik Select untuk parameter yang dipilih.
7. Tambahkan bobot penilaian per parameter (total harus 100%) atau klik Distribute equal weight.
8. Klik Save untuk menyimpan Scorecard.

Sistem akan menampilkan parameter yang telah dibuat pada halaman Scorecard.

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/50941930028313

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/44411253824665

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36774529389977

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36774535941657

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36774535942681

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/50941930030233

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/50941921107737

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/50941930034969

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36774529406873

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36774529408537

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36774535948697

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36774535961881

## Expected Result  <!-- confidence:high ✓ -->

Setelah menyelesaikan proses pembuatan Scorecard:

• Scorecard baru muncul di halaman Scorecard dengan nama dan daftar parameter yang telah dikonfigurasi
• Setiap parameter menampilkan bobot penilaian yang telah ditentukan
• Parameter menjadi tersedia untuk digunakan dalam penilaian kinerja agen pada ruang percakapan
• Supervisor/manager/admin dapat langsung mengakses Scorecard ini untuk melakukan Agent Scoring
• Data Scorecard dapat dilihat di laporan Service Quality Score Report untuk analisis kinerja agen

## Error States  <!-- confidence:medium ~ -->

Kemungkinan masalah yang dapat terjadi:

• **Scorecard name kosong**: Sistem tidak akan menyimpan. Isi kolom Scorecard name terlebih dahulu.
• **Bobot parameter tidak 100%**: Klik Save akan terblokir. Sesuaikan bobot sehingga total mencapai 100%.
• **Parameter tidak dipilih**: Tambahkan minimal satu parameter dengan klik Add parameter sebelum menyimpan.
• **Alasan 'bad rating' tidak tersimpan**: Pastikan toggle untuk alasan sudah diaktifkan sebelum mengisi kolom alasan.

Jika masalah persisten, refresh halaman Settings dan coba kembali.

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support jika mengalami:

• Tombol Create scorecard atau Add parameter tidak berfungsi
• Scorecard tidak tersimpan meskipun semua kolom wajib sudah diisi
• Tidak dapat mengakses menu Settings → Scorecard
• Parameter yang telah dibuat hilang atau tidak muncul di halaman Scorecard

Siapkan informasi berikut saat menghubungi support:
• Screenshot halaman error
• Nama akun Omnichannel
• Daftar langkah yang sudah dicoba
• Browser dan versi yang digunakan