---
title: Bagaimana Cara Menambahkan Deal Bulk
canonical_url: https://help-center.qontak.com/hc/id/articles/5662051540377-Bagaimana-Cara-Menambahkan-Deal-Bulk
article_type: task
solvability_type: tool
products:
- Qontak CRM
product_surface: web
language: id
intent_tags:
- sales-pipeline-deals-tracking
- add-deal-bulk
- sales-management
query_examples:
- Cara Menambahkan Deal Bulk
- Bagaimana cara Menambahkan Deal Bulk?
- Langkah-langkah Menambahkan Deal Bulk di Qontak CRM
- How do I Menambahkan Deal Bulk?
- Mau Menambahkan Deal Bulk, caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk menambahkan Deal secara massal (bulk) di Qontak CRM, Anda membutuhkan:

1. Akun Qontak CRM aktif dengan akses login
2. Akses ke menu Deals (role Admin atau Sales disarankan)
3. Template spreadsheet dalam format CSV atau Excel yang dapat diunduh dari sistem
4. Data Deal yang siap diinput dengan memastikan tidak ada duplikasi
5. Kolom-kolom yang sudah disesuaikan dengan database CRM Anda (Status, Job Title, atau custom field lainnya)
6. Pengetahuan tentang field wajib (ditandai *) dan field custom yang harus sesuai dengan opsi di database

## Steps  <!-- confidence:high ✓ -->


Menu **Deal** pada situs sosial CRM digunakan untuk menginput database tiket dari pelanggan Anda. Untuk melakukan penambahan data pada Menu **Deal** CRM dapat dilakukan secara manual dan secara massal. Berikut langkah-langkah untuk menambahkan Deals secara massal pada Qontak versi web: 
  1. Login ke akun Qontak CRM Anda.
  2. Pilih Menu **Deals**.
  3. Klik **"Add Tickets"** dan pilih **Bulk add deals**.  
![10.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49893760535961)
  4. Unduh template **CSV** atau **Excel** yang sudah tersedia.  
![11.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49893760541593)
  5. Pada saat pengisian data menggunakan form excel ini, pastikan bahwa data yang diinput tidak ter-double. Kemudian, isilah kolom – kolom yang tersedia pada excel sesuai database yang Anda miliki.  
![Deals_Bulk_3.jpg](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774121226649)

Apabila terdapat kolom yang bertanda (*), artnya kolom tersebut wajib diisi. Sedangkan pada kolom yang terkustomisasi seperti: Status, Job Title, dll. pengisian data pada file excel harus sesuai dengan opsi yang terdapat pada database CRM. Mulai dari ejaan, besar kecil huruf, sampai penempatan spasi perlu diperhatikan harus sama persis, karena jika terdapat typo atau tidak sesuai akan menyebabkan error pada data yang diunggah.
  6. Jika data “**Deal”** pada file Excel sudah terisi semua, Anda dapat merubah format pada file Excel menjadi **“Text”**.  
![Deals_Bulk_4.jpg](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774147981209)
  7. Klik **“Browse a file”** untuk mengunggah kembali file excel “**Deal”** yang sudah terisi.  
![12.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49893760546329)
  8. Apabila muncul notifikasi sebagai berikut artinya data Deal anda sudah berhasil terunggah.  
![13.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49893760548505)
  9. Untuk melihat progres pengunggahan data, Anda bisa cek secara berkala pada menu **Properties** dan pilih tab **Upload/Download.**  
![14.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49893760550169)

Jika terdapat data yang gagal terunggah, sistem akan secara otomatis mengirimkan notifikasi ke alamat email Anda yang terdaftar akun CRM Qontak. Apabila sudah menerima email notifikasi tersebut Anda dapat melihat detail penjelasan data - data apa saja yang gagal terunggah, Silahkan periksa kembali file Anda dan perbaiki data yang salah.

## Error States  <!-- confidence:high ✓ -->

Jika terjadi kesalahan saat pengunggahan:

1. **Data Duplikasi**: Pastikan setiap baris data Deal adalah data unik dan tidak ada pengulangan.

2. **Typo atau Format Tidak Sesuai**: Jika field custom (Status, Job Title, dll) tidak sesuai dengan opsi di database CRM — baik dalam hal ejaan, besar-kecil huruf, maupun spasi — data akan mengalami error. Periksa kembali file dan perbaiki data yang salah.

3. **Kolom Wajib Kosong**: Kolom bertanda (*) harus diisi. Jika ada yang kosong, unggahan akan gagal.

4. **Notifikasi Kegagalan**: Sistem akan mengirimkan email notifikasi ke alamat email akun CRM Anda dengan detail data mana saja yang gagal. Buka email tersebut, identifikasi error, perbaiki file Excel, dan unggah kembali.

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support jika:

1. Email notifikasi kegagalan diterima namun penjelasan error tidak jelas atau ambigu
2. File Excel sudah diperbaiki sesuai petunjuk namun tetap gagal saat diunduh
3. Tombol **"Bulk add deals"** tidak muncul atau tidak dapat diklik di menu Deals
4. Sistem tidak mengirimkan notifikasi email meskipun proses unggahan selesai
5. Data Deal telah berhasil terunggah namun tidak muncul di menu Deals setelah waktu tunggu yang wajar

Siapkan informasi: screenshot error/notifikasi, file Excel yang digunakan, dan jumlah baris data yang diinput.