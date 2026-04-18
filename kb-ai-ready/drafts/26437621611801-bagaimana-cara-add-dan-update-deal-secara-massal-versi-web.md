---
title: Bagaimana Cara Add dan Update Deal Secara Massal Versi Web
canonical_url: https://help-center.qontak.com/hc/id/articles/26437621611801-Bagaimana-Cara-Add-dan-Update-Deal-Secara-Massal-Versi-Web
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
- Cara Add dan Update Deal Secara Massal Versi Web
- Bagaimana cara Add dan Update Deal Secara Massal Versi Web?
- Langkah-langkah Add dan Update Deal Secara Massal Versi Web di Qontak CRM
- How do I Add dan Update Deal Secara Massal Versi Web?
- Mau Add dan Update Deal Secara Massal Versi Web, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk menambah dan meng-update deal secara massal di Qontak CRM versi Web, Anda memerlukan:

1. Akun Qontak CRM aktif dengan akses login
2. Permission untuk mengakses menu Deals
3. Deals yang sudah ada di sistem (jika melakukan update)
4. Software spreadsheet (Excel, Google Sheets, atau editor CSV)
5. Nama pipeline, nama stage, dan ID slug deal yang ingin diupdate
6. Untuk update deals: ID slug harus cocok dengan data existing deal

## Steps  <!-- confidence:high ✓ -->


Melalui Qontak CRM, Anda dapat menambah dan meng _update_ deal yang Anda lakukan secara bersamaan _(bulk)_ dalam satu template spreadsheet. Sehingga, Anda tidak perlu [melakukannya secara satuan.](https://help-center.qontak.com/hc/id/articles/5659326461337)
Berikut langkah-langkah untuk menambah dan meng _update_ Deal secara massal pada Web. 
  1. Login ke Akun Qontak CRM Anda.
  2. Masuk ke Menu **Deals.**
  3. Klik **“Add Tickets”** lalu pilih **Bulk add & update deals**.  
![15.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49894160178841)
  4. Maka, Anda akan diarahkan ke halaman berikut.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36766092762009)  
**No.** | **Nama Tombol** | **Deskripsi**  
---|---|---  
1 | CSV template | Klik untuk mengunduh template spreadsheet Bulk add & update deal dalam format CSV.  
2 | Excel template | Klik untuk mengunduh template spreadsheet Bulk add & update deal dalam format XLS atau XLSX.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36766092764313)  
  5. Setelah mengisi template spreadsheet, Anda dapat kembali ke halaman **Bulk update deals** , lalu klik **“Choose file”** untuk mengunggah template spreadsheet tersebut. Pastikan untuk membaca kotak penting di bawah.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36766092748313)

**Penting**  
Terdapat beberapa hal yang harus Anda ketahui sebelum mengunggah, yaitu:  
- Untuk deals baru, Anda tidak perlu mengisi Slug ID.  
- Untuk update Deals, Anda wajib mengisi pipeline, stage, dan ID slug dengan benar agar data dapat diunggah. Anda dapat menemukan ID Slug baik dalam data deals yang diunduh atau melalui URL [rincian profil deals.](https://help-center.qontak.com/hc/id/articles/6081264912025)  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36766139563161)  
- Deals Anda tidak dapat diperbarui jika alur dan tahapan tidak ditemukan.  
- Untuk memperbarui deals, pastikan Anda menggunakan template di atas.  
- Untuk memperbarui deals, pastikan ID slug cocok dengan data sebelumnya.  
- Jumlah baris mempengaruhi durasi upload. Maksimal jumlah update adalah 3000 baris.

Demikian panduan add dan update deals melalui Qontak CRM versi Web.

## Error States  <!-- confidence:medium ~ -->

Deals gagal diunggah jika:

- **Pipeline atau stage tidak ditemukan**: Pastikan nama pipeline dan stage dalam spreadsheet cocok dengan pipeline dan stage yang ada di sistem Qontak CRM Anda.
- **ID slug tidak valid untuk update**: Jika melakukan update, pastikan ID slug cocok dengan data deals existing. Anda dapat menemukan ID slug dari URL rincian profil deals atau dari data deals yang diunduh sebelumnya.
- **Slug ID diisi untuk deals baru**: Deals baru tidak memerlukan Slug ID; kosongkan kolom ini.
- **Format file tidak didukung**: Upload hanya menerima file CSV atau Excel (XLS/XLSX).
- **Jumlah baris melebihi batas**: Maksimal 3000 baris per upload; kurangi jumlah data jika diperlukan.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak jika:

- File berhasil diunggah tetapi deals tidak muncul di menu **Deals** setelah menunggu beberapa menit.
- Pesan error muncul saat upload tanpa deskripsi yang jelas.
- Permission untuk mengakses menu **Deals** atau fitur **Bulk add & update deals** tidak tersedia meskipun akun sudah login.
- Kesalahan pipeline atau stage tidak terselesaikan setelah verifikasi ulang.

Saat menghubungi support, siapkan: screenshot halaman error, screenshot template spreadsheet yang diunggah, ID akun Qontak CRM, dan deskripsi masalah spesifik.