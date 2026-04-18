---
title: Bagaimana Cara Menambahkan Multiple Customers pada Customer Data Platform
canonical_url: https://help-center.qontak.com/hc/id/articles/53245097521561-Bagaimana-Cara-Menambahkan-Multiple-Customers-pada-Customer-Data-Platform
article_type: task
solvability_type: tool
products:
- Mekari Qontak
product_surface: web
language: id
intent_tags:
- customer-data-platform
- add-multiple-customers
query_examples:
- Cara Menambahkan Multiple Customers pada Customer Data Platform
- Bagaimana cara Menambahkan Multiple Customers pada Customer Data Platform?
- Langkah-langkah Menambahkan Multiple Customers pada Customer Data Platform di Mekari
  Qontak
- How do I Menambahkan Multiple Customers pada Customer Data Platform?
- Mau Menambahkan Multiple Customers pada Customer Data Platform, caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk menambahkan multiple customers pada Customer Data Platform, Anda memerlukan:

• Akses ke akun Mekari Qontak One yang aktif
• Menu Customers tersedia di akun Anda
• Daftar data pelanggan yang siap ditambahkan (dalam format XLSX)
• File template yang telah diunduh dan diisi dengan data pelanggan
• Koneksi internet stabil untuk proses unggah file

Proses ini memungkinkan Anda mengimpor data pelanggan dalam jumlah besar sekaligus, bukan menambahkan satu per satu.

## Steps  <!-- confidence:high ✓ -->


9. Setelah pengguna memilih field dan format file yang diinginkan, Anda dapat klik **“Download”**. Selanjutnya, sistem kemudian akan menghasilkan file dan menampilkan _prompt_ unduhan dengan kolom yang sesuai dengan _field_ yang telah dipilih.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F53245072601369)
  10. Selanjutnya isikan data kontak pada _template_ yang telah diunduh. Untuk menghindari kegagalan saat proses unggah, ikuti petunjuk yang tertera di dalam file serta ketentuan berikut:

* Nama lengkap dan data channel wajib diisi.
  * ID pelanggan yang sudah ada tidak boleh diubah.
  * Jangan mengedit baris pertama (_header_).
  * Jangan mengubah nilai apa pun pada kolom A–D.
  * Untuk menghindari kegagalan saat proses unggah, pastikan juga mengikuti petunjuk yang terdapat di dalam file.

## Error States  <!-- confidence:high ✓ -->

Untuk menghindari kegagalan saat proses unggah, periksa hal berikut:

• Nama lengkap dan data channel harus diisi pada setiap baris data
• ID pelanggan yang sudah ada tidak boleh diubah
• Jangan mengedit baris pertama (header) pada template
• Jangan mengubah nilai pada kolom A–D
• Gunakan format file XLSX sesuai template yang diunduh
• Ikuti seluruh petunjuk yang tertera di dalam file template

Jika file gagal diunggah, periksa kembali data Anda dan pastikan semua ketentuan di atas terpenuhi sebelum mencoba unggah ulang.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Mekari Qontak jika mengalami:

• File template tidak dapat diunduh dari halaman Bulk add customer
• Proses unggah gagal meskipun semua data telah sesuai dengan ketentuan
• Notifikasi error spesifik saat unggah file
• Data tidak muncul di halaman All customers setelah proses dinyatakan berhasil

Sediakan informasi berikut saat menghubungi support: nama akun Qontak Anda, ID pelanggan (jika ada), tangkapan layar error message, dan file template yang bermasalah.