---
title: Bagaimana Cara Update Deal Secara Massal Versi Web
canonical_url: https://help-center.qontak.com/hc/id/articles/26436160560793-Bagaimana-Cara-Update-Deal-Secara-Massal-Versi-Web
article_type: task
solvability_type: tool
products:
- Qontak CRM
product_surface: web
language: id
intent_tags:
- sales-pipeline-deals-tracking
- sales-management
query_examples:
- Cara Update Deal Secara Massal Versi Web
- Bagaimana cara Update Deal Secara Massal Versi Web?
- Langkah-langkah Update Deal Secara Massal Versi Web di Qontak CRM
- How do I Update Deal Secara Massal Versi Web?
- Mau Update Deal Secara Massal Versi Web, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk melakukan update deal secara massal di Qontak CRM versi web, Anda membutuhkan:

1. Akun Qontak CRM aktif dengan akses login
2. Akses ke menu Deals (role Admin atau Sales disarankan)
3. Untuk update deal yang sudah ada: informasi Pipeline, Stage, dan Slug ID yang benar
4. Template spreadsheet dalam format CSV atau XLS/XLSX (dapat diunduh dari halaman Bulk update deals)
5. Data deal yang siap diperbarui dengan maksimal 3000 baris per upload

## Steps  <!-- confidence:high ✓ -->

1. Login ke akun Qontak CRM Anda.
   → Sistem akan menampilkan dashboard utama.

2. Buka menu Deals.
   → Halaman daftar Deal akan ditampilkan.

3. Klik tombol "Add Tickets" kemudian pilih "Bulk update deals".
   → Sistem akan membuka halaman Bulk update deals dengan opsi template.

4. Klik tombol "CSV template" atau "Excel template" untuk mengunduh template spreadsheet.
   → File template akan terunduh ke perangkat Anda.

5. Isi template spreadsheet dengan data yang ingin diupdate (pastikan Pipeline, Stage, dan Slug ID sesuai dengan data existing).

6. Kembali ke halaman Bulk update deals dan klik tombol "Choose file" untuk mengunggah template yang sudah diisi.
   → Dialog pemilihan file akan muncul.

7. Pilih file template dan klik tombol "Upload".
   → Sistem akan memproses dan menyimpan semua perubahan.

> Screenshot: 26.png
> Image: https://help-center.qontak.com/hc/article_attachments/49955362961433

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36776163158425

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36776163166361

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/36776163160601

## Expected Result  <!-- confidence:high ✓ -->

Setelah upload berhasil:

1. Semua deal yang diupdate akan ditampilkan di daftar Deal dengan status dan pipeline/stage yang baru.
2. Sistem akan menampilkan notifikasi konfirmasi bahwa update massal berhasil disimpan.
3. Data di spreadsheet yang Anda upload akan tersinkronisasi dengan sistem Qontak CRM.
4. Deal-deal yang diupdate dapat langsung dilihat pada menu Deals dengan perubahan yang sesuai dengan template yang diunggah.

## Error States  <!-- confidence:medium ~ -->

Kesalahan umum yang dapat terjadi:

1. **Deal tidak terupdate - Pipeline/Stage/Slug ID tidak cocok**: Pastikan Pipeline, Stage, dan Slug ID dalam template sesuai dengan data deal yang sebelumnya. Periksa ID Slug dari rincian profil deal atau data yang diunduh sebelumnya.

2. **Deal tidak terupdate - Pipeline atau Stage tidak ditemukan**: Verifikasi bahwa nama Pipeline dan Stage yang digunakan sudah ada di sistem Qontak CRM Anda.

3. **Upload gagal - Format template tidak sesuai**: Gunakan template resmi (CSV atau Excel) yang diunduh dari halaman Bulk update deals, jangan format spreadsheet custom.

4. **Upload timeout - Jumlah baris terlalu banyak**: Batas maksimal adalah 3000 baris. Jika lebih, bagi data menjadi beberapa batch upload.

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support jika:

1. Template spreadsheet sudah sesuai dengan format resmi namun upload tetap gagal
2. Pesan error tertentu muncul saat proses upload
3. Deal tidak terupdate padahal Slug ID, Pipeline, dan Stage sudah benar
4. Sistem menampilkan error code atau pesan teknis yang tidak jelas

Sediakan informasi berikut saat menghubungi support:
- Screenshot halaman error atau pesan error lengkap
- File template spreadsheet yang Anda gunakan
- ID Slug deal yang bermasalah
- Nama Pipeline dan Stage yang digunakan
- Jumlah baris data yang diunggah