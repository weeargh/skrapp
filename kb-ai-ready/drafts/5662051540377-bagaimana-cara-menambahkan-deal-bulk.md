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

1. Login ke akun Qontak CRM Anda.
   → Dashboard utama Qontak CRM akan ditampilkan.

2. Buka menu **Deals**.
   → Halaman daftar Deal akan ditampilkan.

3. Klik tombol **"Add Tickets"** kemudian pilih **"Bulk add deals"**.
   → Halaman penambahan Deal massal akan terbuka dengan opsi template.

4. Unduh template **CSV** atau **Excel**.
   → File template akan terunduh ke perangkat Anda.

5. Isi semua kolom pada file Excel sesuai data Deal Anda, pastikan tidak ada duplikasi data dan kolom bertanda (*) harus diisi. Untuk kolom custom (Status, Job Title, dll), data harus sesuai persis dengan opsi di database CRM termasuk ejaan, besar-kecil huruf, dan spasi.

6. Ubah format file Excel menjadi **"Text"**.
   → Format file berhasil diubah.

7. Klik tombol **"Browse a file"** untuk mengunggah file Excel Deal yang sudah lengkap.
   → Dialog pemilihan file akan terbuka, pilih file Excel Anda.

8. Tunggu notifikasi keberhasilan unggahan.
   → Pesan konfirmasi akan muncul bahwa data Deal berhasil terunggah.

9. Periksa progres pengunggahan di menu **Properties** → tab **Upload/Download**.
   → Status proses unggahan akan ditampilkan.

## Expected Result  <!-- confidence:high ✓ -->

Setelah berhasil menambahkan Deal secara massal, Anda akan melihat:

1. Notifikasi konfirmasi bahwa data Deal berhasil terunggah ke sistem
2. Daftar Deal baru akan tersedia di menu **Deals** dengan status sesuai data yang diinput
3. Progress pengunggahan dapat dipantau di menu **Properties** → tab **Upload/Download**
4. Semua Deal yang diinput dapat dilihat, diedit, dan dikelola melalui menu **Deals** seperti Deal yang ditambahkan secara manual

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