---
title: Bagaimana Cara Menambahkan Product Bulk
canonical_url: https://help-center.qontak.com/hc/id/articles/5498134807705-Bagaimana-Cara-Menambahkan-Product-Bulk
article_type: task
solvability_type: tool
products:
- Qontak CRM
product_surface: web
language: id
intent_tags:
- products
- add-product-bulk
- sales-management
query_examples:
- Cara Menambahkan Product Bulk
- Bagaimana cara Menambahkan Product Bulk?
- Langkah-langkah Menambahkan Product Bulk di Qontak CRM
- How do I Menambahkan Product Bulk?
- Mau Menambahkan Product Bulk, caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk menambahkan produk secara bulk (unggah file) di Qontak CRM, Anda membutuhkan:

- Akun Qontak CRM aktif dengan modul Products tersedia
- Akses ke menu Products dengan izin admin atau management
- Login berhasil ke Qontak versi Web melalui www.qontak.com
- Template Excel tersedia di dashboard CRM (disediakan sistem)
- File Excel sudah disiapkan dengan data produk yang akan diunggah
- Akses ke menu Properties - Upload/Download untuk memantau progres pengunggahan

## Steps  <!-- confidence:high ✓ -->

1. Login ke akun CRM Anda melalui www.qontak.com
   → Sistem menampilkan dashboard CRM

2. Klik menu **Products** di panel navigasi
   → Sistem membuka halaman daftar produk

3. Klik tombol **+ Tambah Product** dan pilih **Unggah File**
   → Pop-up unduh template muncul

4. Unduh template Excel yang tersedia
   → File template Excel terunduh ke perangkat Anda

5. Buka file Excel dan isi kolom-kolom:
   - Kolom bertanda (*) wajib diisi
   - Pastikan data tidak duplikat
   - Untuk kolom kustomisasi (Status, dll), isi sesuai opsi di database CRM
   - Perhatikan ejaan, kapitalisasi, dan spasi harus persis sama
   → Data terisi lengkap di file Excel

6. Ubah format file Excel menjadi **Text**
   → Format file berubah ke teks

7. Klik **Browse a file** untuk memilih file Excel yang sudah diisi
   → Dialog pemilihan file terbuka

8. Pilih file Excel Product dan konfirmasi unggahan
   → Sistem memproses file dan menampilkan notifikasi sukses

9. Pantau progres pengunggahan di menu **Properties** → **Upload/Download**
   → Status pengunggahan ditampilkan secara real-time## Expected Result  <!-- confidence:high ✓ -->

Setelah unggahan selesai, Anda akan menerima notifikasi bahwa data produk berhasil terunggah. Semua produk dari file Excel akan tersimpan dalam database Products Qontak CRM dan dapat langsung digunakan untuk transaksi atau referensi. Data produk akan muncul dalam daftar Products dengan semua informasi (nama, harga, kategori) tersimpan dan dapat diakses.

![3.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F5498042250265)
![1.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49112216742297)
![6.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774222759449)
![7.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774249495449)
![2.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49112185432473)
![9.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774222766873)
![11.2.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774222768793)

## Error States  <!-- confidence:high ✓ -->

Jika terdapat data yang gagal terunggah:

- **Penyebab umum:** Typo pada nama field, ejaan tidak sesuai, spasi tidak sama, atau nilai tidak sesuai opsi di database CRM
- **Apa yang terjadi:** Sistem akan mengirimkan notifikasi email ke alamat email akun CRM Anda dengan detail data yang gagal
- **Cara memperbaiki:** Periksa file Excel Anda, identifikasi data yang salah (gunakan detail dari email notifikasi), perbaiki kesalahan, dan unggah kembali file yang sudah diperbaiki
- **Format file:** Pastikan file sudah dikonversi ke format Text sebelum unggahan

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak jika:

- Notifikasi email tidak muncul meskipun unggahan selesai
- File Excel tidak bisa diunduh dari dashboard
- Tombol **Browse a file** tidak responsif saat diklik
- Semua data gagal terunggah berulang kali setelah perbaikan
- File Excel tidak bisa dikonversi ke format Text

Siapkan informasi berikut saat menghubungi support: username akun CRM, nama file Excel yang diunggah, screenshot notifikasi error (jika ada), dan riwayat email notifikasi gagal unggah.