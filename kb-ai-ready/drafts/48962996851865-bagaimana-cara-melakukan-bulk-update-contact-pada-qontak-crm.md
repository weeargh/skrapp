---
title: Bagaimana Cara Melakukan Bulk Update Contact pada Qontak CRM
canonical_url: https://help-center.qontak.com/hc/id/articles/48962996851865-Bagaimana-Cara-Melakukan-Bulk-Update-Contact-pada-Qontak-CRM
article_type: task
solvability_type: tool
products:
- Qontak CRM
product_surface: web
language: id
intent_tags:
- contact-crm
- perform-bulk-update-contact
- customer-data-platform
query_examples:
- Cara Melakukan Bulk Update Contact pada Qontak CRM
- Bagaimana cara Melakukan Bulk Update Contact pada Qontak CRM?
- Langkah-langkah Melakukan Bulk Update Contact pada Qontak CRM di Qontak CRM
- How do I Melakukan Bulk Update Contact pada Qontak CRM?
- Mau Melakukan Bulk Update Contact pada Qontak CRM, caranya gimana?
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
- Role pengguna dengan izin untuk melakukan bulk update kontak
- Data kontak dalam format file (CSV/Excel) yang telah diunduh dari Qontak CRM atau disiapkan sesuai template
- File berukuran maksimum 25 MB dengan jumlah baris maksimum 7.000
- Catatan: Jika menggunakan Qontak One, lihat dokumentasi Customer Data Platform yang telah diperbarui

## Steps  <!-- confidence:high ✓ -->

1. Masuk ke akun Qontak CRM, kemudian pilih menu **Contacts** di navigasi utama.

2. Klik tombol **Add Contact**, lalu pilih opsi **Bulk update contacts** dari menu dropdown. Sistem akan menampilkan halaman Bulk Update Contacts.

3. Klik tombol **Download** untuk mengunduh data kontak yang sudah tersimpan di Qontak CRM sebagai template awal.

4. Pada halaman Download, pilih **Download all with details** untuk mengunduh seluruh data kontak dengan informasi lengkap dalam format file.

5. Buka file yang telah diunduh menggunakan aplikasi spreadsheet. Edit data kontak sesuai kebutuhan:
   - Jangan ubah kolom bertanda "(Do Not Modify)"
   - Hapus kolom yang tidak perlu diperbarui
   - Tambahkan kontak baru di baris kosong tanpa mengisi kolom Slug-ID
   - Catatan: Kolom "Address (Google Map)" dan kolom tipe "media" tidak dapat diperbarui langsung via spreadsheet

6. Simpan file yang telah diedit, kemudian kembali ke halaman Bulk Update Contacts di Qontak CRM.

7. Klik tombol **Choose file** untuk memilih file kontak yang telah diedit, pastikan semua data sudah benar, lalu klik **Upload**. Sistem akan memproses file dan menampilkan notifikasi bahwa upload sedang berjalan.

8. Pantau progress pembaruan kontak di halaman Bulk Update Contacts atau melalui notifikasi yang muncul di halaman utama Contacts, notifikasi Qontak, email, atau submenu Upload/Download di menu Properties.

## Expected Result  <!-- confidence:high ✓ -->

Setelah upload berhasil, sistem menampilkan notifikasi konfirmasi bahwa data kontak telah terunggah. Anda akan menerima notifikasi di beberapa tempat:

1. Halaman utama menu Contacts
2. Panel notifikasi Qontak (ikon bel)
3. Email akun Qontak Anda
4. Submenu Upload/Download (akses via menu Properties)

Data kontak yang di-upload akan diperbarui atau ditambahkan ke sistem sesuai dengan informasi yang dikirimkan. Progress pembaruan dapat dipantau secara real-time di halaman Bulk Update Contacts.

## Error States  <!-- confidence:medium ~ -->

- **File terlalu besar (>25 MB)**: Kurangi jumlah baris dalam file atau pisahkan menjadi beberapa file terpisah, maksimum 7.000 baris per file.

- **Format file tidak valid**: Pastikan file menggunakan format yang didukung (CSV atau Excel) dan mengikuti template yang diunduh dari Qontak CRM.

- **Slug-ID tidak ditemukan**: Jika memperbarui kontak yang sudah ada, pastikan kolom Slug-ID pada spreadsheet sesuai dengan Slug-ID kontak di sistem.

- **Asosiasi data gagal (Deals, Companies, Tickets)**: Pastikan Slug-ID untuk asosiasi data sudah benar. Sistem hanya mengenali Slug-ID sebagai pengenal, dan Secondary Companies tidak dapat diperbarui.

- **Upload gagal tanpa pesan jelas**: Periksa kembali format kolom dan pastikan tidak ada karakter khusus yang tidak valid di data.

## Escalation  <!-- confidence:medium ~ -->

Jika mengalami masalah yang tidak dapat diselesaikan, hubungi tim support Qontak dengan menyertakan informasi berikut:

- ID akun atau email Qontak Anda
- Screenshot halaman error atau notifikasi kegagalan upload
- File sample atau nama file yang bermasalah (tanpa data sensitif)
- Jumlah baris dan ukuran file yang di-upload
- Langkah-langkah spesifik yang telah dicoba sebelumnya

Tim support dapat diakses melalui menu bantuan di dashboard Qontak CRM atau situs help center Mekari Qontak.