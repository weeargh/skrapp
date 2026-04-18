---
title: Bagaimana Cara Melakukan Bulk Edit Contact pada Omnichannel
canonical_url: https://help-center.qontak.com/hc/id/articles/38938028053529-Bagaimana-Cara-Melakukan-Bulk-Edit-Contact-pada-Omnichannel
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- contact-omnichannel
- perform-bulk-edit-contact
- customer-data-platform
query_examples:
- Cara Melakukan Bulk Edit Contact pada Omnichannel
- Bagaimana cara Melakukan Bulk Edit Contact pada Omnichannel?
- Langkah-langkah Melakukan Bulk Edit Contact pada Omnichannel di Qontak Omnichannel
- How do I Melakukan Bulk Edit Contact pada Omnichannel?
- Mau Melakukan Bulk Edit Contact pada Omnichannel, caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

- Akun Qontak Omnichannel aktif dengan akses ke menu Contacts
- Data Contact dalam format CSV file yang siap diedit
- Aplikasi atau program yang dapat membuka dan mengedit file CSV (seperti Microsoft Excel atau Google Sheets)
- Akses web browser di perangkat desktop atau laptop
- Koneksi internet yang stabil
- Minimal satu Contact sudah terdaftar di sistem Qontak Omnichannel

## Steps  <!-- confidence:high ✓ -->

1. Masuk ke akun Qontak Omnichannel, lalu buka menu **Contacts**.
2. Pilih opsi bulk edit sesuai kebutuhan:
   - **Bulk edit all contacts**: Klik tombol "Actions", kemudian pilih "Bulk edit all contacts" untuk mengedit semua data Contact.
   - **Bulk edit selected**: Centang Contact tertentu di tabel, klik tombol "Actions", lalu pilih "Bulk edit selected" untuk mengedit data Contact terpilih saja.
3. Sistem akan menampilkan halaman unduh. Klik tombol **"Download CSV file"** untuk mengunduh data Contact.
4. Buka file CSV yang telah diunduh menggunakan aplikasi spreadsheet. Lakukan pengeditan sesuai ketentuan:
   - Kolom Full name dan channel data wajib diisi.
   - Contact ID tidak boleh diedit.
   - Jangan ubah baris pertama (header).
   - Jangan ubah data pada kolom A-D.
5. Simpan file CSV setelah selesai mengedit.
6. Kembali ke halaman Qontak Omnichannel, klik tombol **"Choose file"** dan pilih file CSV yang telah diedit.
7. Klik tombol **"Upload"**. Sistem akan memproses file dan menampilkan notifikasi konfirmasi.
8. Data Contact akan tersimpan otomatis di halaman utama menu **Contacts** dengan informasi terupdate di Custom field.

## Expected Result  <!-- confidence:high ✓ -->

- Notifikasi sukses muncul mengkonfirmasi file telah terunggah.
- Data Contact yang diedit tersimpan dan terupdate otomatis di halaman Contacts.
- Custom field nama Contact menampilkan data terbaru sesuai perubahan yang dilakukan pada file CSV.
- Sistem kembali ke halaman utama menu Contacts dengan data Contact yang sudah diperbarui.

## Error States  <!-- confidence:medium ~ -->

- **File format tidak sesuai**: Pastikan file yang diunggah dalam format CSV. File dengan format lain akan ditolak sistem.
- **Header atau kolom A-D berubah**: Jika baris pertama atau kolom A-D diedit, sistem akan menampilkan pesan error. Unduh kembali file CSV dan pastikan tidak mengubah bagian tersebut.
- **Kolom Full name atau channel data kosong**: Sistem akan menolak upload dan menampilkan pesan error. Isi kedua kolom wajib sebelum mengupload ulang.
- **Contact ID diedit**: Sistem akan menampilkan pesan error karena Contact ID tidak boleh diubah. Unduh file kembali dan jangan ubah kolom Contact ID.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak jika mengalami:
- File CSV tidak dapat diunduh dari sistem Qontak Omnichannel.
- Pesan error terus muncul meskipun file sudah sesuai ketentuan pengeditan.
- Data Contact tidak tersimpan setelah upload berhasil.
- Kesulitan mengidentifikasi kolom mana yang boleh diedit.

Siapkan informasi berikut saat menghubungi support: email akun Qontak, screenshot pesan error (jika ada), dan file CSV yang bermasalah.