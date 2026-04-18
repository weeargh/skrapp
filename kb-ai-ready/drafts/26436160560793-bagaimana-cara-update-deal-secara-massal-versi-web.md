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


Melalui Qontak CRM, setelah Anda [menambahkan deal](https://help-center.qontak.com/hc/id/articles/5659326461337), Anda dapat meng _update_ deal yang Anda lakukan baik satuan maupun secara bersamaan _(bulk)_. Kemudian, Anda dapat menempatkan satuan Deal tersebut dengan pipeline dan stage yang sesuai. 
Berikut langkah-langkah untuk meg _update_ Deal secara massal pada Web. 
  1. Login ke Akun Qontak CRM Anda.
  2. Masuk ke Menu **Deals.**
  3. Klik **“Add Tickets”** lalu pilih **Bulk update deals.**  
![26.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49955362961433)
  4. Maka, Anda akan diarahkan ke halaman berikut.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36776163158425)  
**No.** | **Nama Tombol** | **Deskripsi**  
---|---|---  
1 | CSV template | Klik untuk mengunduh template spreadsheet update massal deal dalam format CSV.  
2 | Excel template | Klik untuk mengunduh template spreadsheet update massal deal dalam format XLS atau XLSX.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36776163166361)

**Penting  
** Terdapat beberapa hal yang harus Anda ketahui sebelum mengunggah, yaitu:  
- Deals Anda tidak dapat diperbarui jika pipeline, stage, dan ID slug tidak cocok. Anda dapat menemukan ID Slug baik dalam data deals yang diunduh atau melalui URL [rincian profil deals.](https://help-center.qontak.com/hc/id/articles/6081264912025)![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36776163160601)  
- Deals Anda tidak dapat diperbarui jika pipeline dan stage tidak ditemukan.  
- Untuk memperbarui deals, pastikan Anda menggunakan template di atas.  
- Untuk memperbarui deals, pastikan ID slug cocok dengan data sebelumnya.  
- Jumlah baris mempengaruhi durasi upload. Maksimal jumlah update adalah 3000 baris.

Demikian adalah panduan meng _update_ deal secara massal melalui Qontak CRM. Selain itu, Anda dapat juga dapat menambah dan mengupdate deals massal secara bersamaan, pelajari caranya [di sini.](https://help-center.qontak.com/hc/id/articles/26437621611801)

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