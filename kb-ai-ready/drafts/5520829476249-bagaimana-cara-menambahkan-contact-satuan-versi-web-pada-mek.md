---
title: Bagaimana Cara Menambahkan Contact Satuan Versi Web pada Mekari Qontak CRM
canonical_url: https://help-center.qontak.com/hc/id/articles/5520829476249-Bagaimana-Cara-Menambahkan-Contact-Satuan-Versi-Web-pada-Mekari-Qontak-CRM
article_type: task
solvability_type: tool
products:
- Qontak CRM
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- contact-crm
- add-contact-satuan
- customer-data-platform
query_examples:
- Cara Menambahkan Contact Satuan Versi Web pada Mekari Qontak CRM
- Bagaimana cara Menambahkan Contact Satuan Versi Web pada Mekari Qontak CRM?
- Langkah-langkah Menambahkan Contact Satuan Versi Web pada Mekari Qontak CRM di Qontak
  CRM
- How do I Menambahkan Contact Satuan Versi Web pada Mekari Qontak CRM?
- Mau Menambahkan Contact Satuan Versi Web pada Mekari Qontak CRM, caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

- Akun Qontak CRM aktif dengan akses ke menu Contacts
- Akses ke versi web Qontak CRM melalui browser
- Role pengguna dengan izin untuk membuat kontak baru
- Informasi kontak yang akan ditambahkan (nama, email, nomor telepon, dll)
- Jika menggunakan Qontak One, lihat dokumentasi Customer Data Platform yang telah diperbarui
- Catatan: Kontak yang dibuat di Qontak CRM akan otomatis tersinkronisasi ke Qontak Omnichannel jika kedua produk berlangganan sejak Q2 2024

## Steps  <!-- confidence:high ✓ -->

1. Masuk ke akun Qontak CRM, kemudian buka menu **Contacts** dari navigasi utama. Halaman daftar kontak akan ditampilkan.

2. Klik tombol **Add contact**, lalu pilih opsi **Single Contact** dari menu dropdown. Form pembuatan kontak satuan akan terbuka.

3. Isi kolom informasi kontak seperti nama, jabatan, email, nomor telepon, dan alamat. Kolom bertanda bintang (*) wajib diisi. Sistem memvalidasi setiap input.

4. (Opsional) Di kolom **Tickets**, ketikkan nama tiket yang ingin Anda hubungkan dengan kontak ini, lalu klik **Update Contact**. Tiket akan tautkan secara otomatis ke kontak.

5. (Opsional) Pada kolom **Perusahaan**, pilih Primary Company kontak (maksimal 1 perusahaan) atau klik **atau buat perusahaan** untuk menambah perusahaan baru. Untuk menambah perusahaan tambahan, klik **Additional Companies** (maksimal 5 perusahaan).

6. (Opsional) Pada panel kanan, gunakan kolom **Notes**, **Task**, **Panggilan**, **Email**, **Dokumen**, dan **Rapat** untuk menambah catatan atau informasi lainnya.

7. Klik **Buat Kontak** untuk menyimpan. Atau klik **Buat dan lanjutkan menambahkan** untuk menyimpan dan menambah kontak lainnya sekaligus.## Expected Result  <!-- confidence:high ✓ -->

Kontak satuan berhasil dibuat dan tersimpan. Sistem akan menampilkan pesan konfirmasi, dan kontak baru muncul dalam daftar kontak di menu **Contacts** dengan semua informasi yang dimasukkan (nama, email, nomor telepon, perusahaan, tiket, dan catatan) terlihat dan dapat dicari. Jika pengguna berlangganan Qontak Omnichannel, kontak juga secara otomatis tersinkronisasi ke Omnichannel tanpa perlu membuat ulang.

![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49586043440025)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F23735374085657)
![1.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F39653244319257)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F23735105423129)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F23735375580569)

## Error States  <!-- confidence:medium ~ -->

- **Kolom wajib kosong**: Jika kolom bertanda bintang (*) tidak diisi, tombol **Buat Kontak** tidak aktif atau sistem menampilkan pesan "Harap isi semua field wajib". Solusi: Isi semua kolom yang ditandai bintang sebelum menyimpan.
- **File perusahaan tidak ditemukan**: Jika Primary Company atau Additional Companies tidak muncul di dropdown, periksa apakah perusahaan sudah dibuat di menu **Companies**. Gunakan opsi **atau buat perusahaan** untuk menambah perusahaan baru.
- **Tiket tidak terhubung**: Jika tiket tidak tautkan setelah klik **Update Contact**, pastikan nama tiket ketik dengan benar sesuai yang ada di sistem.

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support jika:
- Tombol **Buat Kontak** tetap tidak aktif meski semua field wajib sudah diisi
- Kontak tidak muncul di daftar setelah disimpan
- Kontak tidak tersinkronisasi ke Qontak Omnichannel meski kedua produk berlangganan
- Saat menghubungi, sertakan: ID akun Qontak, tangkapan layar form kontak, browser yang digunakan, dan langkah tepat yang diambil sebelum error terjadi.