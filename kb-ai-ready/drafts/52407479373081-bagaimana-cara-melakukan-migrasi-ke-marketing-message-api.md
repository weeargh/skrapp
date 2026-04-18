---
title: Bagaimana Cara Melakukan Migrasi ke Marketing Message API
canonical_url: https://help-center.qontak.com/hc/id/articles/52407479373081-Bagaimana-Cara-Melakukan-Migrasi-ke-Marketing-Message-API
article_type: task
solvability_type: tool
products:
- Qontak Chat
product_surface: api
language: id
intent_tags:
- multi-channel-integration
- perform-migrasi
- conversation-management
query_examples:
- Cara Melakukan Migrasi ke Marketing Message API
- Bagaimana cara Melakukan Migrasi ke Marketing Message API?
- Langkah-langkah Melakukan Migrasi ke Marketing Message API di Qontak Chat
- How do I Melakukan Migrasi ke Marketing Message API?
- Mau Melakukan Migrasi ke Marketing Message API, caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.3
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk melakukan migrasi ke Marketing Message API (MM API), Anda memerlukan:

- Role Admin pada akun Qontak Omnichannel
- Akun Qontak Omnichannel yang aktif
- WhatsApp Business Account (WABA) yang sudah terdaftar dan terintegrasi dengan Qontak
- Akses ke menu Channel Integration di Qontak Omnichannel
- Template pesan marketing yang sudah tersimpan di WABA Anda
- Data riwayat pengiriman pesan (untuk benchmarking performa template)

Catatan: Mulai 20 Agustus 2025, semua WABA baru otomatis menggunakan MM API.

## Steps  <!-- confidence:medium ~ -->

1. Masuk ke akun Qontak Omnichannel dengan role Admin dan buka menu **Channel Integration**.

2. Pilih **WhatsApp** dari daftar channel yang tersedia untuk melihat akun WABA Anda.

3. Identifikasi akun yang masih menggunakan Cloud API (sistem akan menampilkan label "Cloud API" pada akun tersebut).

4. Klik tombol **Migrate to MM API** pada akun yang dipilih.

5. Sistem akan menampilkan konfirmasi perubahan dan ringkasan keuntungan MM API (optimasi otomatis, benchmarking template, peningkatan efisiensi hingga 7%).

6. Klik tombol **Confirm Migration** untuk menyelesaikan proses migrasi.

7. Tunggu hingga status akun berubah menjadi "Marketing Message API" atau "MM API Active".

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/52816180307481

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/52816159733913

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/52816159737625

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/52816180317081

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/52816159747097

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/52816180322969

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/52816159755161

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/52816159757337

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/52816159760281

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/52816180334873

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/52816180336921

## Expected Result  <!-- confidence:medium ~ -->

Setelah migrasi berhasil:

- Akun WhatsApp Anda akan menampilkan status "Marketing Message API Active" atau "MM API" di menu Channel Integration
- Sistem pengiriman pesan marketing otomatis beralih ke MM API
- Anda dapat mengakses fitur Benchmarking Template Pesan di dashboard kampanye marketing
- Laporan pengiriman akan menampilkan data optimasi otomatis dan tingkat keterlibatan pesan
- Batas pengiriman pesan akan menyesuaikan dinamis berdasarkan performa template

## Error States  <!-- confidence:low ? -->

Kemungkinan masalah migrasi dan solusinya:

**Tombol "Migrate to MM API" tidak muncul:** Akun Anda sudah menggunakan MM API atau memerlukan verifikasi tambahan dari Meta. Hubungi support-qontak@mekari.com.

**Migrasi gagal atau terhenti:** Koneksi Internet putus atau WABA Anda belum sepenuhnya terverifikasi di Meta Business Manager. Coba lagi atau hubungi support Qontak.

**Template pesan tidak tersinkronisasi setelah migrasi:** Refresh halaman atau tunggu 5-10 menit untuk sinkronisasi otomatis. Jika masih bermasalah, hubungi support.

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support jika:

- Migrasi gagal berulang kali setelah mencoba langkah-langkah di atas
- Tombol "Migrate to MM API" tidak tersedia di Channel Integration
- Template pesan hilang atau tidak tersinkronisasi setelah migrasi
- Pengiriman pesan marketing masih mengalami gangguan 24 jam setelah migrasi

Sediakan informasi berikut saat menghubungi support:
- ID akun Qontak Omnichannel
- Nomor WhatsApp Business Account (WABA)
- Screenshot menu Channel Integration
- Pesan error lengkap (jika ada)