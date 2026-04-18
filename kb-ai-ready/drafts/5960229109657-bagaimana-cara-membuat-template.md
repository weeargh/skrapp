---
title: Bagaimana Cara Membuat Template
canonical_url: https://help-center.qontak.com/hc/id/articles/5960229109657-Bagaimana-Cara-Membuat-Template
article_type: task
solvability_type: tool
products:
- Qontak CRM
product_surface: mobile
language: id
intent_tags:
- documents
- create-template
- sales-management
query_examples:
- Cara Membuat Template
- Bagaimana cara Membuat Template?
- Langkah-langkah Membuat Template di Qontak CRM
- How do I Membuat Template?
- Mau Membuat Template, caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Anda ingin membuat template dokumen otomatis di Qontak CRM menggunakan fitur Document Generator. Sebelum memulai, pastikan:

• Anda memiliki Role **Admin** di Qontak CRM (hanya Admin yang dapat membuat template)
• Anda telah menyiapkan template dalam format Excel dengan layout dan struktur yang sesuai kebutuhan
• Semua field properties yang akan digunakan sebagai Variable ID telah dibuat di menu **Properties** (untuk tab Deals, Companies, Contacts, atau Tasks sesuai kebutuhan)
• Anda memiliki akses ke menu **Document** di aplikasi CRM Qontak
• File template Excel sudah tersimpan di perangkat Anda

## Steps  <!-- confidence:high ✓ -->


Pada umumnya fitur document generator pada Aplikasi CRM Qontak dimanfaatkan untuk memudahkan User CRM dalam membuat suatu dokumen secara otomatis, contoh dokumen yang umumnya dibuat dengan fitur ini adalah dokumen penawaran harga ataupun invoice. Hanya User CRM dengan Role **Admin** yang dapat membuat template ini.
Sebelumnya Anda dapat mempelajari tentang:  
[**[Fitur] Aplikasi CRM Mekari Qontak untuk Tingkatkan Performa Bisnis 75%**](https://qontak.com/fitur/aplikasi-crm/?utm_source=ecosystem&utm_medium=qontak+%28help+center%29)
Jika Anda telah memiliki format penawaran harga tersendiri dan ingin memanfaatkan fitur ini, maka dapat mengupload template penawaran harga dengan langkah-langkah sebagai berikut:
  1. **Template** yang akan diupload untuk menggunakan document generator harus **dibuat dalam bentuk Excel** agar sistem nantinya dapat mengisi data pada template yang ada sesuai dengan data yang di input dalam CRM. Langkah pertama yang perlu dilakukan adalah mempersiapkan template dari penawaran harga tersebut beserta pengaturan layout pada Excel tersebut.  
![1.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36772398808985)
  2. Sebagai contoh pada template tersebut terdapat data yang perlu diisi secara otomatis dari sistem CRM seperti Quotation Number, Company, Name, Email, Address, Quotation Item, Unit Price, Quantity, Months, dan Total. Oleh karena itu, sebelumnya harus dipastikan kita sudah membuat **field properties** pada semua Menu sesuai dengan template yang telah disiapkan. Pastikan properties tersebut dibuat di Menu **Properties,** lalu pilih ingin membuat/mengedit properties di tab apa (Deals/Companies/Contacts/Tasks) seperti gambar berikut.  
![29.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50802006513177)
  3. Selanjutnya, mengisi _cell-cell_ pada _template_ Excel sesuai dengan **Default Variable ID List** yang ada pada field properties CRM yang telah ada dan kita tambahkan agar nantinya sistem dapat mengisi data secara otomatis pada _template_ tersebut sesuai dengan data yang di input dalam CRM.  
![30.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50801979073177)
  4. Kemudian lakukan copy-paste **Variable ID** tersebut ke dalam cell pada template Excel yang telah disiapkan sebelumnya.  
![4.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36772391258265)
  5. Setelah selesai melakukan copy-paste **Variable ID** ke template Excel yang telah disiapkan sesuai dengan field properties yang ada di CRM, kurang lebih akan berbentuk sebagai berikut.  
![5.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36772391262745)
  6. Lalu, pilih Menu **Document** untuk mengunggah _template_ yang telah kita buat dalam format Excel ke sistem CRM, sehingga nantinya sistem dapat membuat dokumen secara otomatis.   
![31.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50803410084761)
  7. Pilih **Template** dan klik **"Upload Template".  
![32.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50803410090777)  
**
  8. Lalu ketik nama template tersebut pada bagian **File Name**. Klik **"****Browse a file"** untuk memilih _template_ yang telah kita buat dari penyimpanan perangkat. Setelah memilih _template_ dari penyimpanan perangkat, klik "**Create Template"** untuk mengunggah _file_ tersebut.**  
![mceclip5.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36772391270169)  
**
  9. Berikut adalah tampilan apabila file template yang kita pilih berhasil terupload ke sistem CRM.  
![33.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50803388337049)
  10. Untuk melakukan pengecekan format pada _template_ tersebut dapat meng-klik tombol **Preview** yang nantinya akan diarahkan secara otomatis ke tab baru pada _browser_ dan terbuka halaman **Google Sheet**.  
![9.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36772391264665)
Perubahan template di menu Templates oleh satu User akan berpengaruh ke semua User CRM dalam organisasi tersebut.

## Error States  <!-- confidence:medium ~ -->

Format template tidak sesuai: Pastikan template dibuat dalam format Excel (.xlsx atau .xls). Sistem CRM Qontak hanya menerima file dalam format Excel untuk fitur Document Generator.

Variable ID tidak terisi dengan data: Verifikasi bahwa semua Variable ID yang digunakan di template Excel sesuai persis dengan Default Variable ID dari field properties yang ada di CRM. Perbedaan karakter atau penulikan akan menyebabkan cell tetap kosong saat dokumen dibuat.

Field properties belum lengkap: Jika ada data yang perlu ditampilkan di dokumen namun tidak ada Variable ID di CRM, Anda harus membuat field properties terlebih dahulu di menu **Properties** sebelum upload template.

File tidak ditemukan saat browse: Pastikan file template Excel tersimpan dengan benar di perangkat dan coba refresh browser sebelum mencoba upload ulang.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim dukungan Qontak jika mengalami:

• Template sudah diupload tetapi dokumen otomatis tidak terbuat atau data tidak terisi dengan benar — siapkan screenshot template Excel dengan Variable ID dan daftar field properties yang dibuat
• Sistem menampilkan pesan error saat upload template — catat pesan error lengkap dan tipe/ukuran file template
• Tidak dapat mengakses menu **Document** meskipun memiliki Role Admin — verifikasi Role Anda di pengaturan akun dan screenshot halaman yang bermasalah
• Template hilang atau tidak muncul di daftar template setelah diupload

Sediakan informasi: nama akun Qontak, email pengguna, deskripsi masalah, screenshot yang relevan, dan waktu kejadian masalah.