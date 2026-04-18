---
title: Bagaimana Cara Membuat Recipient List untuk Email Campaign
canonical_url: https://help-center.qontak.com/hc/id/articles/47426266423065-Bagaimana-Cara-Membuat-Recipient-List-untuk-Email-Campaign
article_type: task
solvability_type: tool
products:
- Qontak CRM
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- email-campaign
- create-recipient-list-untuk-email-cam
- marketing-campaign-manage
query_examples:
- Cara Membuat Recipient List untuk Email Campaign
- Bagaimana cara Membuat Recipient List untuk Email Campaign?
- Langkah-langkah Membuat Recipient List untuk Email Campaign di Qontak CRM
- How do I Membuat Recipient List untuk Email Campaign?
- Mau Membuat Recipient List untuk Email Campaign, caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Anda ingin membuat Recipient list untuk Email Campaign. Sebelum memulai, pastikan Anda memiliki:

1. Akun Mekari Qontak aktif dengan langganan paket Broadcast, Service Suite, Sales Suite, atau Qontak 360
2. Akses ke menu Campaign di Qontak Omnichannel dengan peran manajemen campaign
3. File berisi data recipient (format CSV, XLS, atau XLSX) dengan ukuran maksimal 5 MB
4. Data email recipient dan nama lengkap siap untuk diunggah
5. Kuota email campaign harian yang mencukupi untuk jumlah recipient yang akan diimpor

## Steps  <!-- confidence:high ✓ -->

1. Masuk ke akun Omnichannel Anda dan pilih menu Campaign.
2. Klik tab Recipient lists. Sistem akan menampilkan daftar recipient list yang sudah ada.
3. Klik tombol Create recipient list dan pilih opsi Upload file.
4. Isikan nama Recipient list pada kolom yang tersedia. Gunakan nama unik agar mudah ditemukan saat mengirim campaign.
5. Pilih tipe data Email template dan tentukan format file (CSV, XLS, atau XLSX).
6. Unduh template yang disediakan dan isi dengan data recipient Anda. Pastikan kolom pertama berisi recipient_email_address dan kolom kedua berisi full_name tanpa mengubah nama header.
7. Unggah file dengan menyeret file ke tampilan atau klik Browse, kemudian klik Import. Sistem akan memproses data.

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/47426266416025

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/47426266416153

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/47426266416537

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/47426281632153

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/47426281632409

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/51230879965465

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/47426266419737

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/52284811708697

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/52284836572313

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/52284836572569

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/52284836574489

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/52284811710745

> Screenshot: 22.png
> Image: https://help-center.qontak.com/hc/article_attachments/52284811711001

## Expected Result  <!-- confidence:high ✓ -->

Recipient list berhasil dibuat dan data recipient terimpor. Sistem akan menampilkan status impor dan jumlah recipient yang berhasil diproses. Recipient list akan muncul di daftar Recipient lists dan siap digunakan saat membuat Email Campaign. Anda dapat memilih recipient list ini dari dropdown menu saat membuat campaign baru.

## Error States  <!-- confidence:high ✓ -->

1. **Email duplikat dalam file**: Sistem akan mengimpor hanya data email pertama dan menghapus duplikat. Cek file Anda sebelum mengimpor.
2. **Kolom kosong**: Impor gagal jika ada value kosong pada kolom yang Anda gunakan. Pastikan semua data terisi lengkap.
3. **Melebihi kuota harian**: Jika jumlah recipient melebihi kuota email harian Anda, impor akan gagal. Kurangi jumlah recipient atau tunggu pembaruan kuota.
4. **File terlalu besar**: File maksimal 5 MB. Gunakan file yang lebih kecil atau bagi data menjadi beberapa file.
5. **Impor sebelumnya masih berjalan**: Tunggu impor sebelumnya selesai sebelum mengimpor daftar recipient baru.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Mekari Qontak jika Anda mengalami:

1. Pesan error saat mengimpor recipient list yang tidak jelas atau tidak tercantum di atas
2. File berukuran di bawah 5 MB tetapi tetap ditolak sistem
3. Data recipient tidak muncul setelah impor dinyatakan berhasil
4. Kebutuhan khusus terkait format file atau custom field yang tidak standar

Siapkan screenshot error message, file yang Anda coba impor, dan ID akun Qontak Anda saat menghubungi support.