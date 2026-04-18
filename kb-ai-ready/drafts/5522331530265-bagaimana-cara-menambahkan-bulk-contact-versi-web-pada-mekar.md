---
title: Bagaimana Cara Menambahkan Bulk Contact Versi  Web  pada Mekari Qontak CRM
canonical_url: https://help-center.qontak.com/hc/id/articles/5522331530265-Bagaimana-Cara-Menambahkan-Bulk-Contact-Versi-Web-pada-Mekari-Qontak-CRM
article_type: task
solvability_type: tool
products:
- Qontak CRM
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- contact-crm
- add-bulk-contact
- customer-data-platform
query_examples:
- Cara Menambahkan Bulk Contact Versi  Web  pada Mekari Qontak CRM
- Bagaimana cara Menambahkan Bulk Contact Versi  Web  pada Mekari Qontak CRM?
- Langkah-langkah Menambahkan Bulk Contact Versi  Web  pada Mekari Qontak CRM di Qontak
  CRM
- How do I Menambahkan Bulk Contact Versi  Web  pada Mekari Qontak CRM?
- Mau Menambahkan Bulk Contact Versi  Web  pada Mekari Qontak CRM, caranya gimana?
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
- Akses ke versi web Qontak CRM
- Role pengguna dengan izin untuk membuat kontak
- File template Excel yang tersedia di dashboard CRM
- Data kontak dalam format Excel atau CSV
- File berukuran maksimum 25 MB dengan jumlah baris maksimum 7.000
- Catatan: Jika menggunakan Qontak One, lihat dokumentasi Customer Data Platform yang telah diperbarui

## Steps  <!-- confidence:high ✓ -->

1. Masuk ke akun Qontak CRM, kemudian pilih menu **Contacts** di navigasi utama.

2. Klik tombol **Add Contact**, lalu pilih opsi **Bulk add contacts** dari menu dropdown. Sistem akan menampilkan halaman untuk pengunggahan kontak massal.

3. Klik tombol **Download** untuk mengunduh template Excel. File template berisi kolom-kolom standar yang harus diisi.

4. Buka file template Excel. Perhatikan kolom bertanda (*) adalah kolom wajib diisi. Field unik pembeda kontak adalah email dan nomor telepon.

5. Isi kolom-kolom sesuai database Anda. Untuk kolom terkustomisasi (Status, Job Title, dll), masukkan data sesuai opsi di CRM — perhatikan ejaan, huruf besar-kecil, dan spasi harus sama persis.

6. Pada kolom **Owner**, isikan username atau email pemilik data kontak.

7. Pastikan tidak ada data duplikat dalam file.

8. Ubah format file Excel menjadi **Text**.

9. Klik **Browse a file** untuk memilih dan mengunggah file Excel yang sudah diisi.

10. Pilih file Excel data kontak Anda. Sistem akan memproses dan menampilkan notifikasi berhasil jika pengunggahan berhasil.

11. Cek progress pengunggahan di menu **Properties**, tab **Upload/Download**.## Expected Result  <!-- confidence:high ✓ -->

Setelah pengunggahan berhasil, sistem akan menampilkan notifikasi konfirmasi. Data kontak yang berhasil diunggah akan muncul di menu **Contacts** dan dapat dilihat dalam daftar kontak. Progress pengunggahan dapat dipantau di menu **Properties**, tab **Upload/Download**. Kontak yang diunggah akan terhubung ke owner sesuai username atau email yang Anda tentukan.

![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49586336116121)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49586336117785)
![Contact_Bulk__3.jpg](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36781183618073)
![Contact_Bulk_4.jpg](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36781141856665)
![Contact_Bulk_5.jpg](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36781141855513)
![09.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F26552575400089)

## Error States  <!-- confidence:medium ~ -->

- **Data gagal terunggah**: Jika ada baris data yang tidak sesuai format atau ada typo pada kolom terkustomisasi (Status, Job Title), sistem akan menolak baris tersebut. Perbaiki data dan pastikan ejaan, huruf, dan spasi sama persis dengan opsi di CRM.
- **Duplikasi data**: Jika email atau nomor telepon sudah ada, sistem akan mendeteksi duplikasi. Hapus data duplikat sebelum mengunggah.
- **Format kolom salah**: Jika format file bukan Excel atau Text, sistem mungkin tidak dapat membaca file. Konversi ke format yang didukung.
- **File terlalu besar**: Jika file lebih dari 25 MB atau lebih dari 7.000 baris, bagi menjadi beberapa file dan unggah terpisah.

## Escalation  <!-- confidence:medium ~ -->

Hubungi dukungan Qontak jika:
- File berhasil diunggah tetapi data tidak muncul di menu Contacts setelah 1 jam
- Sistem menampilkan pesan error yang tidak jelas pada saat pengunggahan
- Sebagian besar baris data gagal terunggah tanpa penjelasan yang jelas

Sediakan informasi berikut:
- ID akun Qontak CRM Anda
- Screenshot atau deskripsi error yang muncul
- Jumlah data yang diunggah dan jumlah yang gagal
- File Excel (jika memungkinkan) untuk analisis lebih lanjut