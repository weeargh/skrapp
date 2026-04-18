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

1. Siapkan template Excel dengan data yang perlu diisi otomatis (contoh: Quotation Number, Company, Name, Email, Address, Quotation Item, Unit Price, Quantity, Months, Total). Sistem akan menggunakan template ini sebagai dasar pembuatan dokumen.

2. Buka menu **Properties** dan pastikan semua field properties yang sesuai dengan template sudah dibuat di tab yang tepat (Deals/Companies/Contacts/Tasks). Sistem akan menampilkan Default Variable ID untuk setiap field yang dibuat.

3. Catat semua Variable ID dari field properties yang telah dibuat. Anda akan membutuhkan ID-ID ini untuk mengisi template Excel.

4. Buka template Excel dan isi cell-cell dengan Variable ID yang sesuai dengan field properties di CRM. Pastikan penempatan Variable ID sesuai dengan data yang ingin ditampilkan di dokumen akhir.

5. Simpan file template Excel setelah selesai menambahkan semua Variable ID.

6. Buka menu **Document** di Qontak CRM. Sistem akan menampilkan halaman manajemen template dokumen.

7. Klik tombol **Upload Template**. Sistem akan membuka dialog unggah file.

8. Ketik nama template pada bagian **File Name**. Klik tombol **Browse a file** untuk memilih file template Excel dari perangkat Anda. Sistem akan menampilkan daftar file yang tersedia.

9. Pilih file template Excel yang telah disiapkan. Klik tombol **Create Template** untuk mengunggah file tersebut ke sistem CRM.

10. Sistem akan memproses file dan menampilkan notifikasi bahwa template berhasil terupload. Template Anda sekarang tersedia di menu Document dan siap digunakan untuk membuat dokumen otomatis.

> Screenshot: 1.png
> Image: https://help-center.qontak.com/hc/article_attachments/36772398808985

> Screenshot: 29.png
> Image: https://help-center.qontak.com/hc/article_attachments/50802006513177

> Screenshot: 30.png
> Image: https://help-center.qontak.com/hc/article_attachments/50801979073177

> Screenshot: 4.png
> Image: https://help-center.qontak.com/hc/article_attachments/36772391258265

> Screenshot: 5.png
> Image: https://help-center.qontak.com/hc/article_attachments/36772391262745

> Screenshot: 31.png
> Image: https://help-center.qontak.com/hc/article_attachments/50803410084761

> Screenshot: 32.png
> Image: https://help-center.qontak.com/hc/article_attachments/50803410090777

> Screenshot: mceclip5.png
> Image: https://help-center.qontak.com/hc/article_attachments/36772391270169

> Screenshot: 33.png
> Image: https://help-center.qontak.com/hc/article_attachments/50803388337049

> Screenshot: 9.png
> Image: https://help-center.qontak.com/hc/article_attachments/36772391264665

## Expected Result  <!-- confidence:high ✓ -->

Setelah template berhasil diupload, Anda akan melihat:

• Pesan konfirmasi bahwa template telah berhasil diupload ke sistem CRM
• Template muncul dalam daftar template yang tersedia di menu **Document**
• Template dapat dipilih saat membuat dokumen otomatis di menu **Deals** atau **Tiket**
• Sistem siap mengisi Variable ID pada template dengan data dari CRM sesuai dengan informasi yang ada di Deal atau Tiket

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