---
title: Bagaimana Cara Self Integration Tokopedia Chat
canonical_url: https://help-center.qontak.com/hc/id/articles/16320068291353-Bagaimana-Cara-Self-Integration-Tokopedia-Chat
article_type: task
solvability_type: tool
products:
- Qontak CRM
- Qontak Omnichannel
product_surface: mobile
language: id
intent_tags:
- multi-channel-integration
- conversation-management
query_examples:
- Cara Self Integration Tokopedia Chat
- Bagaimana cara Self Integration Tokopedia Chat?
- Langkah-langkah Self Integration Tokopedia Chat di Qontak CRM
- How do I Self Integration Tokopedia Chat?
- Mau Self Integration Tokopedia Chat, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk melakukan Self Integration Tokopedia Chat di Qontak Omnichannel, Anda memerlukan:

- Role Admin di akun Qontak Omnichannel
- Akun Seller aktif di Tokopedia
- Akses ke halaman App Management Tokopedia Developer Console
- Developer Console Tokopedia yang sudah terdaftar dan diapprove oleh pihak Tokopedia (proses persetujuan maksimal 3x24 jam)
- API Credential dari Tokopedia Developer Console
- Akses ke menu Integration > submenu Tokopedia di Qontak Omnichannel

## Steps  <!-- confidence:medium ~ -->

1. Buka akun Seller Tokopedia Anda dan buat Developer Console Tokopedia dengan mengisi kolom Company Name, PIC Contacts Name, Contacts Number, Business Registration Certificate (SIUP), Company Profile, Company Website URL, Type of Member (pilih Seller), dan System (pilih InHouse). Tunggu approval dari Tokopedia maksimal 3x24 jam.

2. Masuk ke akun Qontak Omnichannel dengan role Admin.

3. Navigasikan ke menu Integration dan pilih submenu Tokopedia.

4. Klik tombol "Book consultation" untuk mendapatkan API Credential dan bimbingan langsung dari tim Qontak.

5. Masukkan API Credential dari Tokopedia Developer Console ke dalam form yang disediakan.

6. Klik tombol Konfirmasi atau Submit untuk menyelesaikan proses Self Integration.

7. Sistem akan menampilkan notifikasi bahwa Tokopedia Chat berhasil terintegrasi.

## Expected Result  <!-- confidence:medium ~ -->

Setelah Self Integration Tokopedia Chat berhasil, Anda akan melihat:

- Tokopedia Chat muncul di daftar Channel Integration Qontak Omnichannel dengan status "Connected"
- Pesan pelanggan dari Tokopedia akan mulai masuk ke Chatpanel Qontak Omnichannel
- Anda dapat mengelola percakapan Tokopedia Chat langsung dari dashboard Qontak Omnichannel
- Notifikasi konfirmasi sukses ditampilkan di layar

## Error States  <!-- confidence:medium ~ -->

Kemungkinan masalah dan solusinya:

- **Developer Console Tokopedia belum diapprove**: Tunggu maksimal 3x24 jam untuk persetujuan dari Tokopedia. Periksa email terdaftar di Developer Console untuk notifikasi approval.

- **API Credential tidak valid atau salah**: Verifikasi kembali API Credential dari App Management Tokopedia Developer Console dan pastikan Anda menyalin dengan benar.

- **Akun Tokopedia bukan tipe Seller**: Pastikan Anda menggunakan akun Seller Tokopedia, bukan akun Buyer.

- **Integrasi gagal**: Hubungi tim Qontak Support melalui opsi "Book consultation" di submenu Tokopedia untuk mendapatkan bantuan langsung.

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support jika Anda mengalami:

- Developer Console Tokopedia tidak mendapat approval setelah 3x24 jam
- API Credential tidak diterima sistem Qontak Omnichannel
- Integrasi Tokopedia Chat gagal setelah mengikuti semua langkah
- Pesan pelanggan tidak masuk ke Chatpanel meskipun integrasi menunjukkan status Connected

Siapkan informasi berikut saat menghubungi support:
- Screenshot menu Integration > Tokopedia di Qontak Omnichannel
- Email terdaftar di Tokopedia Developer Console
- Nama Seller Shop Tokopedia Anda
- Pesan error lengkap (jika ada)