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

1. Login ke akun CRM Anda melalui website www.qontak.com. Sistem akan menampilkan dashboard CRM.

2. Klik menu **Companies/Perusahaan** di navigasi utama. Halaman Companies akan terbuka.

3. Klik tombol **Add Company**, kemudian pilih opsi **Upload file**. Dialog unggah file akan tampil.

4. Unduh template Excel dari dashboard CRM dengan mengklik tombol download. File template akan tersimpan di komputer Anda.

5. Buka file Excel dan isi kolom sesuai data perusahaan Anda. Perhatikan: kolom dengan tanda (*) wajib diisi, dan data custom (Status, Job Title, dll) harus sesuai ejaan, besar-kecil huruf, dan spasi di database CRM agar tidak terjadi error.

6. Pastikan data email dan phone number (unique field) tidak terduplikasi. Ubah format file Excel menjadi **Text**.

7. Klik **Browse a file** dan pilih file Excel yang sudah terisi. Sistem akan memproses data.

8. Tunggu notifikasi sukses. Untuk melihat progress unggahan, buka menu **Properties** → tab **Upload/Download**.

## Expected Result  <!-- confidence:high ✓ -->

Setelah proses selesai, Anda akan melihat:

• Notifikasi konfirmasi bahwa data Perusahaan berhasil terunggah
• Data company baru muncul di menu **Companies/Perusahaan** dengan status updated
• Semua company yang diunggah dapat dilihat, diubah, atau dihubungkan dengan contact, deal, dan record CRM lainnya
• Progress pengunggahan dapat dipantau di menu **Properties**, tab **Upload/Download**
• Company database Anda telah bertambah sesuai jumlah data yang diunggah

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