---
title: Bagaimana Cara Mengintegrasikan Qontak dengan WhatsApp API
canonical_url: https://help-center.qontak.com/hc/id/articles/12055228468633-Bagaimana-Cara-Mengintegrasikan-Qontak-dengan-WhatsApp-API
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: api
language: id
intent_tags:
- multi-channel-integration
- integrate-qontak-dengan-whatsapp-api
- conversation-management
query_examples:
- Cara Mengintegrasikan Qontak dengan WhatsApp API
- Bagaimana cara Mengintegrasikan Qontak dengan WhatsApp API?
- Langkah-langkah Mengintegrasikan Qontak dengan WhatsApp API di Qontak Omnichannel
- How do I Mengintegrasikan Qontak dengan WhatsApp API?
- Mau Mengintegrasikan Qontak dengan WhatsApp API, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.3
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengintegrasikan Qontak dengan WhatsApp API, Anda memerlukan:

1. **Role Admin** pada akun Qontak Omnichannel
2. **Akun Qontak Omnichannel** yang aktif
3. **Facebook Business Manager** (atau Meta Business Account) — dapat dibuat otomatis jika belum ada
4. **WhatsApp Business Account (WABA)** — akan diverifikasi melalui Facebook Business Manager
5. Akses ke menu **Channel Integration** di Qontak Omnichannel

Jika Anda belum memiliki Meta Business Account dan WhatsApp Business Profile, sistem Qontak akan secara otomatis mendeteksi dan mengarahkan Anda untuk membuatnya.

## Steps  <!-- confidence:high ✓ -->

**Untuk pengguna yang belum memiliki Meta Business Account:**

1. Buka akun Qontak Omnichannel dan masuk ke menu **Channel Integration**
2. Pilih **WhatsApp** dari daftar channel yang tersedia
3. Klik tombol **Tambah WhatsApp** atau **Add WhatsApp**
4. Sistem akan mendeteksi Anda belum memiliki Meta Business Account
5. Klik tombol untuk membuat **Meta Business Account** baru
6. Ikuti alur pembuatan akun Meta dan WhatsApp Business Profile sesuai instruksi di layar
7. Verifikasi nomor telepon dan informasi bisnis Anda
8. Sistem akan menampilkan pesan konfirmasi integrasi berhasil

**Untuk pengguna yang sudah memiliki Meta Business Account:**

1. Buka menu **Channel Integration** → pilih **WhatsApp**
2. Klik tombol **Tambah WhatsApp**
3. Pilih **WhatsApp Business Account (WABA)** yang sudah terverifikasi dari dropdown
4. Klik tombol **Hubungkan** atau **Connect**
5. Sistem akan memproses integrasi dan menampilkan notifikasi "WhatsApp Terhubung"

> Screenshot: 1.png
> Image: https://help-center.qontak.com/hc/article_attachments/53356189359001

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/53356160571929

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/53356189407129

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/53356189408793

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/53356189367833

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/53356160525593

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/53356160575769

## Expected Result  <!-- confidence:high ✓ -->

Setelah integrasi berhasil:

1. **Notifikasi Konfirmasi**: Sistem menampilkan pesan "WhatsApp Terhubung" atau "WhatsApp Connected"
2. **Akun Muncul di Channel Integration**: WhatsApp Business Account Anda muncul dalam daftar channel yang terintegrasi
3. **Siap Menerima Pesan**: Akun Qontak Omnichannel Anda siap menerima dan mengirim pesan WhatsApp
4. **Mulai 20 Agustus 2025**: WABA baru akan otomatis terintegrasi dengan Marketing Messages API (MM API) untuk pengiriman campaign marketing

## Error States  <!-- confidence:low ? -->

No common errors documented.

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support (support-qontak@mekari.com) jika Anda mengalami:

1. **Integrasi gagal** meskipun Meta Business Account sudah terverifikasi — sertakan screenshot error dan nama akun Meta Business Manager Anda
2. **WABA tidak muncul** di dropdown pilihan akun — berikan informasi ID WhatsApp Business Account dan screenshot halaman Facebook Business Manager
3. **Pesan "Akun tidak terverifikasi"** — pastikan Meta Business Account sudah selesai verifikasi di Facebook Business Manager sebelum integrasi
4. **Marketing Messages API (MM API) tidak aktif** untuk akun lama — hubungi support dengan nomor WhatsApp Business Account Anda untuk bantuan migrasi manual