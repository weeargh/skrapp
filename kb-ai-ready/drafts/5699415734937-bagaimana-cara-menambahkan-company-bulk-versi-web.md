---
title: Bagaimana Cara Menambahkan Company Bulk Versi Web
canonical_url: https://help-center.qontak.com/hc/id/articles/5699415734937-Bagaimana-Cara-Menambahkan-Company-Bulk-Versi-Web
article_type: task
solvability_type: tool
products:
- Qontak CRM
product_surface: web
language: id
intent_tags:
- company-module
- add-company-bulk
- customer-data-platform
query_examples:
- Cara Menambahkan Company Bulk Versi Web
- Bagaimana cara Menambahkan Company Bulk Versi Web?
- Langkah-langkah Menambahkan Company Bulk Versi Web di Qontak CRM
- How do I Menambahkan Company Bulk Versi Web?
- Mau Menambahkan Company Bulk Versi Web, caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Sebelum menambahkan company secara bulk, pastikan Anda memenuhi persyaratan berikut:

• Akun Qontak CRM aktif dan sudah login melalui website www.qontak.com
• Akses ke menu **Companies/Perusahaan** di dashboard web
• File Excel template yang telah diunduh dari CRM dashboard
• Data perusahaan yang sudah disiapkan dengan informasi lengkap (nama perusahaan, email, nomor telepon, dan data lainnya sesuai kebutuhan)
• Koneksi internet stabil dan web browser yang didukung
• Hak akses untuk menambahkan data company ke dalam database CRM

## Steps  <!-- confidence:high ✓ -->


Menu **Company/Perusahaan** adalah sebuah menu yang digunakan untuk membuat **database company** baik yang berstatus sebagai **customer** , **partner** , atau yang lainnya. Untuk menambahkan data company, Anda dapat menambahkan satu per satu maupun secara masif. Pada panduan kali ini, kami akan menginfokan cara menambah company secara masif dengan CRM Qontak.
  1. Pastikan Anda sudah login kedalam akun CRM Anda melalui website [www.qontak.com.](http://www.qontak.com/)
  2. Masuk ke menu **Perusahaan/Companies,** Kemudian klik**"Add Company****”** dan pilih “**Upload file”**.  
![01.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36781141978393)
  3. Unduh template Excel yang sudah tersedia dalam Dashboard CRM.  
![1.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49114476804121)
  4. Perlu diperhatikan bahwa _unique field_ yang menjadi pembeda antara data “**Perusahaan”** satu dengan yang lainnya adalah pada bagian email dan phone number.
  5. Pada saat pengisian data mengguankan form Excel ini, pastikan bahwa data yang diinput tidak ter-double. Kemudian, isilah kolom – kolom yang tersedia pada Excel sesuai database yang Anda miliki.
  6. Apabila terdapat kolom yang bertanda **(*),** artinya kolom tersebut wajib diisi. Sedangkan pada kolom yang terkustomisasi seperti; Status, Job Title, dll. pengisian data pada file Excel harus sesuai dengan opsi yang terdapat pada database CRM. Mulai dari ejaan, besar kecil huruf, sampai penempatan spasi perlu diperhatikan harus sama persis, karena jika terdapat typo atau tidak sesuai akan menyebabkan error pada data yang diunggah.  
![Company_Bulk_3.jpg](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36781183692185)
  7. Jika data “**Perusahaan”** pada file Excel sudah terisi semua, Anda dapat merubah format pada file Excel menjadi **“Text”**.  
![Company_Bulk_4.jpg](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36781183691161)
  8. Klik **“Browse a file”** untuk mengunggah Kembali file Excel “**Perusahaan”** yang sudah terisi.  
![2.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49114530713241)

Jika terdapat data yang gagal terunggah, sistem akan secara otomatis mengirimkan notifikasi ke alamat email Anda yang terdaftar akun CRM Qontak. Apabila sudah menerima email notifikasi tersebut Anda dapat melihat detail penjelasan data - data apa saja yang gagal terunggah, Silahkan periksa kembali file Anda dan perbaiki data yang salah.

## Error States  <!-- confidence:medium ~ -->

Jika data gagal terunggah, periksa hal berikut:

• **Data terduplikasi**: Email atau phone number sudah ada di database. Hapus duplikat dari file Excel.
• **Format data tidak sesuai**: Data custom (Status, Job Title, dll) tidak cocok dengan opsi di database CRM. Pastikan ejaan, kapitalisasi, dan spasi sama persis.
• **Kolom wajib isi kosong**: Isi semua kolom bertanda (*) sebelum unggah.
• **Format file salah**: Pastikan file Excel sudah diubah menjadi format **Text** sebelum diunggah.

Sistem akan mengirimkan notifikasi otomatis ke alamat email terdaftar Anda jika ada data yang gagal beserta detail error.

## Escalation  <!-- confidence:medium ~ -->

Hubungi dukungan Qontak jika:

• Data terus gagal terunggah meskipun sudah mengikuti semua langkah dan format sudah benar
• Menerima pesan error yang tidak jelas atau berbeda dari error states yang dijelaskan
• Progress unggahan tidak bergerak atau stuck di menu **Properties** → **Upload/Download**
• Template Excel tidak dapat diunduh dari dashboard CRM

Saat menghubungi support, siapkan: tangkapan layar (screenshot) error message, file Excel yang diupload, dan email akun CRM Anda untuk investigasi lebih lanjut.