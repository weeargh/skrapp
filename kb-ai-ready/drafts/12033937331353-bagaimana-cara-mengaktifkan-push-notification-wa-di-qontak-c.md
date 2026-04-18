---
title: Bagaimana Cara Mengaktifkan Push Notification WA di Qontak CRM
canonical_url: https://help-center.qontak.com/hc/id/articles/12033937331353-Bagaimana-Cara-Mengaktifkan-Push-Notification-WA-di-Qontak-CRM
article_type: task
solvability_type: tool
products:
- Qontak CRM
- Qontak Omnichannel
- Qontak Chat
product_surface: mobile
language: id
intent_tags:
- goal-setting-performance-tracking
- enable-push-notification-wa
- sales-management
query_examples:
- Cara Mengaktifkan Push Notification WA di Qontak CRM
- Bagaimana cara Mengaktifkan Push Notification WA di Qontak CRM?
- Langkah-langkah Mengaktifkan Push Notification WA di Qontak CRM di Qontak CRM
- How do I Mengaktifkan Push Notification WA di Qontak CRM?
- Mau Mengaktifkan Push Notification WA di Qontak CRM, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Sebelum mengaktifkan push notification WhatsApp di Qontak CRM, pastikan Anda memiliki:

1. **Akun Chat Panel** dengan akses broadcast yang sudah terdaftar
2. **Saldo MCC (Mekari Credit Center)** tersedia untuk melakukan broadcast
3. **Nomor pengirim WhatsApp** yang telah disetujui oleh WhatsApp
4. **Template pesan** yang telah disetujui oleh WhatsApp
5. **Nomor tujuan penerima** dengan format lengkap kode negara (contoh: +62)
6. **API Token Chat Panel** untuk menghubungkan akun ke CRM
7. Akses ke menu **Properties** di Qontak CRM

## Steps  <!-- confidence:high ✓ -->

**Langkah 1: Mendaftarkan Akun Chat Panel ke CRM**
1. Buka Qontak CRM dan masuk ke menu **Properties**
2. Pilih **WhatsApp Notification**
3. Klik tombol **"Create push notification"** → Sistem menampilkan form pendaftaran
4. Pada bagian **Omnichannel API token**, masukkan token API dari Chat Panel (klik "See API Token" dalam Chat Panel)
5. Klik tombol konfirmasi → Status berubah menjadi **Connected**

**Langkah 2: Membuat Push Notification**
1. Klik tombol **"Create push notification"** → Halaman pengaturan fitur terbuka
2. Pilih fitur di bagian **Feature settings** (Deal, Ticket, Contact, atau Company)
3. Klik **"Continue"** → Sistem mengarahkan ke bagian **Template message settings**
4. Pilih template pesan yang telah disetujui WhatsApp (berisi teks atau media)
5. Tentukan trigger otomatis (deal date, deal creation, deal moving, idle deal, atau birthday)
6. Klik **"Save"** → Push notification siap digunakan

## Expected Result  <!-- confidence:high ✓ -->

Setelah mengikuti semua langkah, Anda akan melihat:

1. **Status Akun**: Menampilkan "Connected" pada menu **WhatsApp Notification** di Properties
2. **Push Notification Aktif**: Sistem mulai mengirimkan notifikasi WhatsApp otomatis berdasarkan trigger yang dipilih
3. **Konfirmasi Penyimpanan**: Pesan sukses muncul setelah klik "Save"
4. **Template Terdaftar**: Template pesan tampil dalam daftar push notification yang sedang berjalan
5. **Notifikasi Terkirim**: Pesan WhatsApp otomatis dikirim ke nomor tujuan sesuai trigger (contoh: saat deal dibuat atau tanggal ulang tahun contact)

## Error States  <!-- confidence:medium ~ -->

**Masalah Umum dan Solusi:**

1. **"API Token tidak valid"** → Pastikan Anda login ke Chat Panel sebelum copy token, dan token sudah di-generate terbaru
2. **"Saldo MCC tidak cukup"** → Tambahkan saldo MCC di akun Anda sebelum mengaktifkan broadcast
3. **"Nomor pengirim tidak disetujui WhatsApp"** → Daftarkan nomor pengirim melalui WhatsApp Business Manager terlebih dahulu
4. **"Template pesan ditolak WhatsApp"** → Pastikan template mengikuti panduan WhatsApp (tidak ada link mencurigakan, format sesuai)
5. **"Nomor tujuan tidak valid"** → Gunakan format lengkap dengan kode negara (contoh: +62812xxxx, bukan 0812xxxx)
6. **Status tetap "Disconnected"** → Refresh halaman atau coba generate API Token baru di Chat Panel

## Escalation  <!-- confidence:medium ~ -->

Hubungi **Qontak Support** jika Anda mengalami:

1. **API Token tetap error** setelah refresh halaman dan generate ulang token
2. **Saldo MCC hilang** atau tidak tersimpan dengan benar
3. **Template WhatsApp ditolak tanpa alasan jelas** — siapkan screenshot template dan pesan error dari WhatsApp
4. **Push notification tidak terkirim** meskipun status Connected dan trigger terpenuhi — siapkan:
   - Screenshot menu Properties WhatsApp Notification
   - ID Contact/Deal yang seharusnya menerima notifikasi
   - Waktu pengiriman yang diharapkan
   - Screenshot saldo MCC saat ini
5. **Akses Chat Panel hilang** atau akun tidak bisa login

Siapkan informasi: User ID, Workspace ID, dan detail error yang ditampilkan sistem.