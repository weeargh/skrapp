---
title: Bagaimana Cara Submit Ticket Omnichannel ke Qontak CRM
canonical_url: https://help-center.qontak.com/hc/id/articles/21790065933465-Bagaimana-Cara-Submit-Ticket-Omnichannel-ke-Qontak-CRM
article_type: task
solvability_type: tool
products:
- Qontak CRM
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- ticket-creation-tracking
- customer-support-ticketin
query_examples:
- Cara Submit Ticket Omnichannel ke Qontak CRM
- Bagaimana cara Submit Ticket Omnichannel ke Qontak CRM?
- Langkah-langkah Submit Ticket Omnichannel ke Qontak CRM di Qontak CRM
- How do I Submit Ticket Omnichannel ke Qontak CRM?
- Mau Submit Ticket Omnichannel ke Qontak CRM, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mensubmit ticket Omnichannel ke Qontak CRM, Anda memerlukan:

• Akses ke Qontak CRM dengan peran Admin atau User
• Akses ke Qontak Omnichannel dengan peran yang sesuai
• Fitur Tickets sudah diaktifkan di kedua produk (Qontak CRM dan Qontak Omnichannel)
• Template ticket sudah dibuat pada menu Integrasi di Qontak Omnichannel
• Pipeline dan Stage sudah dikonfigurasi di Qontak CRM
• Kontak (Contact) dan Perusahaan (Company) sudah dibuat jika ingin mengasosiasikan tiket

## Steps  <!-- confidence:high ✓ -->

1. Buka Qontak Omnichannel dan navigasi ke menu **Inbox**, kemudian klik submenu **All chats**. Sistem akan menampilkan daftar pesan.

2. Pilih salah satu pesan yang ingin Anda buatkan tiket. Sistem akan membuka detail percakapan.

3. Pada **Room detail**, klik tombol **"Submit ticket"** yang berada pada bagian **Ticket**. Pop-up form akan muncul.

4. Pilih **Pipeline** yang Anda inginkan dari dropdown. Sistem akan menampilkan daftar pipeline yang tersedia.

5. Pilih **Stage** tempat ticket akan dimasukkan. Sistem akan menampilkan kolom-kolom tambahan.

6. Isi kolom-kolom berikut:
   - **Ticket name**: nama tiket
   - **Description**: deskripsi tiket
   - **Assignee**: pengguna yang bertanggung jawab
   - **Ticket priority**: tingkat prioritas
   - **Ticket Category**: kategori tiket
   - **Due date**: tenggat waktu
   - **Note**: catatan tambahan
   - **Contact Association**: kontak terkait
   - **Company Association**: perusahaan terkait
   - **Product Association**: produk terkait
   - **Task Association**: task terkait

7. Klik tombol **"Submit"**. Sistem akan memproses dan membuat ticket di Qontak CRM.

8. Notifikasi sukses akan muncul. Klik nomor ticket untuk membuka tiket di Qontak CRM.

> Screenshot: 75.png
> Image: https://help-center.qontak.com/hc/article_attachments/50911798216729

> Screenshot: 76.png
> Image: https://help-center.qontak.com/hc/article_attachments/50911841781401

> Screenshot: Screenshot
> Image: https://lh7-rt.googleusercontent.com/docsz/AD_4nXeZ-Pza-pQDLuJf66Q7Es5xXOvDehGeauk4tRpGH-exBifL46yIZPuM3aBkxnIVKSNgPuME8f6xv3uXmaYYZT63T7ZGH8dx7TlN0kmY8nUEcb297XCixZ7ky-V8rnq_W4Mz6Y9odHbcO5mY7iS1Zya6nW8?key=Jqkn8dhQ_InX_HZYbdhKWg

> Screenshot: Screenshot
> Image: https://lh7-rt.googleusercontent.com/docsz/AD_4nXfl0kQGBVkCqt_sTKFqMm15S-wy61_sXhkmMFwTg-LYHRpb2ejuJnMqDtgUWzQMznaR5RJOTSPAbbTKyA81QMx3LSEm4jk8Q_EIILPVxfJg-r9MEvSFjaPOqr6Z_KCZwxS-ReE7_GYUwu8jOHvODBad0Wg?key=Jqkn8dhQ_InX_HZYbdhKWg

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/35834581904537

> Screenshot: 77.png
> Image: https://help-center.qontak.com/hc/article_attachments/50912106053913

## Expected Result  <!-- confidence:high ✓ -->

Setelah mensubmit ticket dengan sukses:

• Sistem menampilkan notifikasi konfirmasi bahwa ticket berhasil dibuat
• Nomor ticket unik akan ditampilkan
• Ticket muncul di menu Tickets di Qontak CRM dengan status sesuai Stage yang dipilih
• Semua informasi yang diisi (nama, deskripsi, assignee, priority, kategori, due date, catatan, dan asosiasi kontak/perusahaan/produk/task) tersimpan di Qontak CRM
• User dapat membuka dan mengelola ticket di Qontak CRM melalui link yang disediakan
• Ticket dapat diakses oleh assignee untuk penanganan lebih lanjut

## Error States  <!-- confidence:medium ~ -->

Berdasarkan dokumentasi artikel, error states berikut dapat terjadi:

• **Tombol Submit ticket tidak muncul**: Fitur Tickets belum diaktifkan di Qontak Omnichannel atau Qontak CRM. Verifikasi pengaturan integrasi pada menu Integrasi di kedua produk.

• **Pipeline atau Stage tidak muncul di dropdown**: Pipeline dan Stage belum dikonfigurasi di Qontak CRM. Buat pipeline dan stage terlebih dahulu di menu Tickets → pengaturan pipeline.

• **Kolom required kosong saat submit**: Isi semua kolom yang ditandai required (biasanya Ticket name, Pipeline, dan Stage) sebelum klik Submit.

• **Ticket tidak muncul di Qontak CRM**: Periksa menu Tickets di Qontak CRM dan filter berdasarkan pipeline/stage yang dipilih.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak jika mengalami:

• Fitur Tickets tidak dapat diaktifkan di kedua produk meskipun akses sudah sesuai
• Tombol "Submit ticket" tidak muncul meski pengaturan integrasi sudah benar
• Ticket berhasil disubmit tetapi tidak muncul di Qontak CRM setelah 5 menit
• Pop-up form tidak menampilkan kolom-kolom yang seharusnya ada

Siapkan informasi berikut saat menghubungi support:
• Screenshot layar yang menunjukkan masalah
• ID workspace atau nama workspace
• Peran pengguna (Admin/User)
• Langkah yang sudah dicoba untuk mengatasi masalah
• Nomor ticket jika ada (jika berhasil disubmit)