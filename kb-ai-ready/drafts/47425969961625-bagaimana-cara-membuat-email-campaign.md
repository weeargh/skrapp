---
title: Bagaimana Cara Membuat Email Campaign
canonical_url: https://help-center.qontak.com/hc/id/articles/47425969961625-Bagaimana-Cara-Membuat-Email-Campaign
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- email-campaign
- create-email-campaign
- marketing-campaign-manage
query_examples:
- Cara Membuat Email Campaign
- Bagaimana cara Membuat Email Campaign?
- Langkah-langkah Membuat Email Campaign di Qontak Omnichannel
- How do I Membuat Email Campaign?
- Mau Membuat Email Campaign, caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk membuat Email Campaign di Mekari Qontak, Anda harus memenuhi persyaratan berikut:

1. Langganan aktif paket Broadcast, Service Suite, Sales Suite, atau Qontak 360
2. Akses ke akun Omnichannel Mekari Qontak
3. Subdomain dan email pengirim (sender email) sudah terdaftar melalui self-integrate Email Campaign
4. Template konten email sudah dibuat di menu Campaign > Templates > Email
5. Daftar penerima (recipient list) sudah diimpor di menu Campaign > Recipient lists
6. Kuota Email Campaign harian dan bulanan Anda mencukupi untuk jadwal pengiriman

## Steps  <!-- confidence:high ✓ -->

1. Masuk ke akun Omnichannel Anda dan pilih menu Campaign.
   Sistem menampilkan halaman Campaign dengan beberapa tab pilihan.

2. Klik tab Email.
   Sistem menampilkan daftar email campaign yang sudah dibuat (jika ada).

3. Klik tombol Create campaign.
   Sistem membuka formulir Campaign setup.

4. Isi field yang diperlukan:
   - Email subject: Judul atau subjek email yang akan dikirimkan
   - Sender name: Nama pengirim email
   - Recipient list: Pilih daftar penerima yang sudah diimpor sebelumnya

5. Klik tombol Continue.
   Sistem melanjutkan ke tahap berikutnya untuk memilih template dan mengatur pengiriman.## Expected Result  <!-- confidence:high ✓ -->

Setelah mengklik tombol Continue, sistem akan menampilkan halaman berikutnya dalam proses pembuatan Email Campaign. Anda akan dapat memilih template email yang telah dibuat sebelumnya dan mengatur detail pengiriman campaign. Data yang Anda masukkan (Email subject, Sender name, dan Recipient list) tersimpan dan siap untuk tahap konfigurasi template dan jadwal pengiriman.## Error States  <!-- confidence:medium ~ -->

Kesalahan umum yang mungkin terjadi:

1. **Subdomain belum terdaftar**: Jika email pengirim tidak muncul di field Sender email, daftarkan subdomain terlebih dahulu melalui proses self-integrate Email Campaign.

2. **Recipient list kosong**: Jika tidak ada pilihan recipient list, impor daftar penerima dengan format CSV/Excel yang valid terlebih dahulu.

3. **Kuota tidak cukup**: Jika muncul pesan kuota tidak mencukupi, periksa kuota Email Campaign harian dan bulanan Anda sebelum melanjutkan.

4. **Template belum dibuat**: Pastikan Anda telah membuat minimal satu template email di menu Campaign > Templates > Email.

![rev.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F47426113314073)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52283953214361)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52283953215257)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52283982578841)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F47425969958553)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F47425950955929)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52283982579609)

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Mekari Qontak jika mengalami:

1. Email subject, Sender name, atau Recipient list tidak bisa disimpan setelah klik Continue
2. Sistem menampilkan pesan error yang tidak jelas
3. Tombol Create campaign tidak responsif atau tidak berfungsi
4. Kuota Email Campaign tidak terupdate dengan benar

Siapkan informasi berikut saat menghubungi support:
- Screenshot error message
- ID akun Omnichannel Anda
- Waktu kejadian error
- Jumlah recipient yang akan dikirimkan