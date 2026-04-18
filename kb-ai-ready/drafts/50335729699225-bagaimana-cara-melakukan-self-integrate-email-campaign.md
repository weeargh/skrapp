---
title: Bagaimana Cara Melakukan Self Integrate Email Campaign
canonical_url: https://help-center.qontak.com/hc/id/articles/50335729699225-Bagaimana-Cara-Melakukan-Self-Integrate-Email-Campaign
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
product_surface: mobile
language: id
intent_tags:
- email-campaign
- perform-self-integrate-email-campaign
- marketing-campaign-manage
query_examples:
- Cara Melakukan Self Integrate Email Campaign
- Bagaimana cara Melakukan Self Integrate Email Campaign?
- Langkah-langkah Melakukan Self Integrate Email Campaign di Qontak Omnichannel
- How do I Melakukan Self Integrate Email Campaign?
- Mau Melakukan Self Integrate Email Campaign, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Anda ingin melakukan self integrate email campaign di Mekari Qontak. Sebelum memulai, pastikan Anda memenuhi persyaratan berikut:

1. Langganan aktif paket Broadcast, Service Suite, Sales Suite, atau Qontak 360
2. Akses ke akun Qontak Omnichannel dengan peran Admin (hanya Admin yang dapat melakukan konfigurasi Email Campaign)
3. Subdomain eksklusif yang tidak digunakan pada layanan email lain
4. Akses ke domain manager (aplikasi eksternal tempat mengelola domain Anda)
5. Belum memiliki subdomain dan email sender yang terintegrasi dengan Qontak

## Steps  <!-- confidence:high ✓ -->

1. Masuk ke akun Qontak Omnichannel Anda, lalu pilih menu **Integrations**. Sistem menampilkan halaman Integrations.

2. Klik submenu **Email**, kemudian pilih **Campaign**. Sistem menampilkan halaman Integrasi Email Campaign.

3. Klik tab **Subdomain** untuk melanjutkan. Sistem menampilkan opsi untuk menambahkan subdomain baru.

4. Klik tombol **Add subdomain**. Sistem membuka pop-up formulir penambahan subdomain.

5. Isikan subdomain pada kolom yang tersedia, lalu klik tombol **Add**. Sistem menampilkan DNS Records yang diperlukan untuk konfigurasi domain.

6. Salin nilai DNS Records (MX Record, CNAME, SPF, DKIM) dari halaman Qontak.

7. Buka domain manager akun domain Anda (penyedia domain eksternal), lalu masukkan DNS Records yang telah disalin.

8. Kembali ke halaman Integrations Email Campaign di Qontak, lalu klik tombol **Verify** pada subdomain yang baru ditambahkan. Sistem memverifikasi konfigurasi DNS.

9. Tunggu hingga status subdomain berubah menjadi **Verified**. Sistem menampilkan subdomain yang telah diverifikasi dan memungkinkan pembuatan email sender.## Expected Result  <!-- confidence:high ✓ -->

Setelah proses self integrate selesai, Anda akan melihat:

1. Subdomain dengan status **Verified** di tab Subdomain halaman Integrations Email Campaign
2. Tab **Email Sender** menjadi aktif dan dapat diakses
3. Anda dapat membuat alamat email pengirim (email sender) baru
4. Email Campaign siap untuk digunakan sesuai dengan panduan membuat Email Campaign

Proses ini memungkinkan Anda mengirimkan Email Campaign menggunakan subdomain dan email sender yang telah terintegrasi.

![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982346649)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982348953)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931941037593)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982360345)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982364313)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982364953)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982365849)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982366873)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982367897)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931941044633)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931941046425)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982371865)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931941049113)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931941049881)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931941050521)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982376089)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982397977)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982399385)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931941080729)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982401689)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982403097)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982406041)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931941093529)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982411417)

## Error States  <!-- confidence:medium ~ -->

**Verifikasi DNS gagal:**
Jika tombol Verify menampilkan status gagal, pastikan:
- Semua DNS Records (MX Record, CNAME, SPF, DKIM) telah dikonfigurasi dengan benar pada domain manager
- Nilai DNS Records yang dimasukkan sama persis dengan yang ditampilkan di Qontak (termasuk titik akhir)
- Propagasi DNS telah selesai (dapat memakan waktu hingga 48 jam)
- Tunggu beberapa saat, lalu coba verifikasi kembali

**Subdomain tidak dapat ditambahkan:**
Pastikan subdomain yang digunakan bersifat eksklusif dan tidak digunakan pada layanan email lain. Satu akun Qontak hanya dapat mengintegrasikan 1 subdomain dengan 1 email sender.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim dukungan Qontak jika:

1. Status verifikasi subdomain tetap gagal setelah 48 jam dan semua DNS Records sudah dikonfigurasi dengan benar
2. Pesan error spesifik muncul saat menambahkan atau memverifikasi subdomain
3. Anda tidak dapat mengakses tab Integrations atau Email Campaign
4. Subdomain yang diverifikasi tidak muncul di halaman Email Campaign

Siapkan informasi berikut saat menghubungi support:
- Screenshot halaman Integrations Email Campaign menunjukkan status subdomain
- Nama subdomain yang ditambahkan
- Nama penyedia domain (domain manager)
- ID akun Qontak Anda