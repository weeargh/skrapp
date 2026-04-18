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

1. Masuk ke akun Mekari Qontak One, lalu buka menu Customers.

2. Pada halaman Customers, pilih tab "Customers" dan klik "All customers".

3. Klik tombol "Add customer", kemudian pilih "Multiple customers". Sistem akan menampilkan halaman Bulk add customer.

4. Klik tombol "Download template" untuk mengunduh template pengisian data customer.

5. Pada panel Download Template, tentukan File format (XLSX) dan Layout (Default by Qontak), lalu pilih Default fields dan Custom fields sesuai kebutuhan Anda.

6. Klik tombol "Download" untuk mengunduh template dengan kolom yang telah dipilih.

7. Isi data kontak pada template yang telah diunduh, pastikan nama lengkap dan data channel terisi, serta ikuti petunjuk dalam file.

8. Klik tombol "Choose file" untuk memilih file template yang telah diisi.

9. Setelah file berhasil dipilih, klik tombol "Upload". Sistem akan menampilkan notifikasi proses unggah.

10. Tunggu hingga proses selesai. Sistem akan menampilkan notifikasi konfirmasi bahwa data telah berhasil diunggah dan data akan muncul di halaman All customers.## Expected Result  <!-- confidence:high ✓ -->

Setelah proses unggah selesai, Anda akan melihat:

• Notifikasi konfirmasi dari sistem yang menyatakan data pelanggan berhasil diunggah
• Daftar pelanggan baru muncul pada halaman All customers di Customer Data Platform
• Semua data yang diunggah dapat diakses dan dikelola melalui Customers menu
• Field wajib (Full Name, Owner, Assignee, Username, Phone Number, Email) terisi sesuai data yang diunggah

![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F53245072601369)

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