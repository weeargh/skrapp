---
title: Bagaimana Cara Menambahkan Tasks secara Massal (Bulk)
canonical_url: https://help-center.qontak.com/hc/id/articles/5467126515481-Bagaimana-Cara-Menambahkan-Tasks-secara-Massal-Bulk
article_type: task
solvability_type: tool
products:
- Qontak CRM
product_surface: web
language: id
intent_tags:
- task-management
- add-tasks-secara-massal-bulk
- operation-workflow-automa
query_examples:
- Cara Menambahkan Tasks secara Massal (Bulk)
- Bagaimana cara Menambahkan Tasks secara Massal (Bulk)?
- Langkah-langkah Menambahkan Tasks secara Massal (Bulk) di Qontak CRM
- How do I Menambahkan Tasks secara Massal (Bulk)?
- Mau Menambahkan Tasks secara Massal (Bulk), caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk menambahkan Tasks secara massal (bulk upload) di Mekari Qontak CRM, Anda memerlukan:

• Akun Mekari Qontak CRM yang aktif
• Role Admin atau Owner
• Akses ke menu Tasks dan menu Properties
• Web browser untuk mengakses www.qontak.com
• Template Excel yang akan diunduh dari dashboard CRM
• Data tasks yang siap untuk diunggah dengan format sesuai database CRM Anda

## Steps  <!-- confidence:high ✓ -->

1. Login ke akun CRM Anda di www.qontak.com dan buka menu **Tasks**. Sistem akan menampilkan daftar tasks yang ada.

2. Klik tombol **Add Task**, kemudian pilih opsi **Upload File**. Halaman upload file akan terbuka.

3. Klik tombol **Browse a file** untuk mengunduh template Excel yang sudah tersedia. File template akan terunduh ke perangkat Anda.

4. Buka file Excel dan isi kolom-kolom yang tersedia sesuai data tasks Anda. Kolom bertanda (*) wajib diisi. Untuk kolom kustomisasi (Status, Job Title, dll), gunakan data yang persis sama dengan opsi di database CRM Anda — perhatikan ejaan, besar-kecil huruf, dan spasi.

5. Pastikan tidak ada data yang double. Ubah format file Excel menjadi "Text" sebelum mengunggah.

6. Klik tombol **Browse a file** kembali untuk mengunggah file Excel yang sudah terisi lengkap. Sistem akan memproses file Anda.

7. Tunggu notifikasi konfirmasi bahwa data tasks telah berhasil terunggah. Sistem akan menampilkan pesan sukses di dashboard.

8. Untuk memantau proses pengunggahan, buka menu **Properties**, kemudian klik tab **Upload/Download**. Anda dapat melihat status upload secara berkala.

> Screenshot: 31.png
> Image: https://help-center.qontak.com/hc/article_attachments/56956754426777

> Screenshot: bulkontak4.png
> Image: https://help-center.qontak.com/hc/article_attachments/36776161701529

> Screenshot: bulkontak6.png
> Image: https://help-center.qontak.com/hc/article_attachments/36776188543513

> Screenshot: 34.png
> Image: https://help-center.qontak.com/hc/article_attachments/56956754427417

> Screenshot: 33.png
> Image: https://help-center.qontak.com/hc/article_attachments/56956754428185

## Expected Result  <!-- confidence:high ✓ -->

Setelah bulk upload tasks berhasil:

• Notifikasi konfirmasi muncul di dashboard bahwa data tasks telah terunggah
• Semua tasks baru tampil di menu **Tasks** dengan data yang sesuai file Excel Anda
• Status upload dapat dilihat di menu **Properties**, tab **Upload/Download**
• Activity log menampilkan catatan upload tasks massal
• Setiap task dapat diedit atau dihapus melalui menu Tasks seperti task individual

## Error States  <!-- confidence:high ✓ -->

Jika terdapat data yang gagal terunggah:

• Sistem akan mengirimkan email notifikasi ke alamat email akun CRM Anda yang terdaftar
• Email notifikasi berisi detail data-data mana saja yang gagal dan alasan kegagalan
• Penyebab umum gagal: typo dalam kolom kustomisasi, format data tidak sesuai database CRM, atau data double
• Solusi: Periksa file Excel Anda, perbaiki data yang salah, pastikan ejaan dan spasi persis sama dengan opsi di CRM, kemudian ulangi proses upload dari langkah 3

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Mekari Qontak jika:

• File Excel tidak dapat diunduh dari dashboard CRM
• Sistem tidak menampilkan opsi **Upload File** saat klik tombol **Add Task**
• Email notifikasi gagal diterima setelah 24 jam proses upload
• Data yang sudah diperbaiki masih tetap gagal terunggah setelah beberapa kali percobaan

Siapkan informasi berikut saat menghubungi support: screenshot error, file Excel yang bermasalah, email notifikasi gagal, dan ID akun CRM Anda