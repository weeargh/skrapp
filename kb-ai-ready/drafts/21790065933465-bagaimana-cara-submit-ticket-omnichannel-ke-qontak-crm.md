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


Setelah membuat template ticket pada menu [Integrasi](https://help-center.qontak.com/hc/id/articles/5642795619737), selanjutnya Anda dapat mensubmit ticket tersebut. Fitur pada Omnichannel ini memanfaatkan fitur Tiket di CRM yang membuat pengguna di chatpanel dapat membuat tiket di CRM. Namun fitur ini perlu diaktifkan pada kedua produk. Berikut langkah-langkahnya.
  1. Pada menu **Inbox** , lalu klik submenu **All chats**. Kemudian pilih salah satu pesan yang ingin Anda buatkan tiketnya.  
![75.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50911798216729)
  2. Pada **Room detail** , klik **“Submit ticket”** yang berada pada bagian **Ticket**.  
![76.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50911841781401)
  3. Selanjutnya, Anda akan melihat _pop up_ berikut dan pilih **Pipeline** yang Anda inginkan.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Flh7-rt.googleusercontent.com%2Fdocsz%2FAD_4nXeZ-Pza-pQDLuJf66Q7Es5xXOvDehGeauk4tRpGH-exBifL46yIZPuM3aBkxnIVKSNgPuME8f6xv3uXmaYYZT63T7ZGH8dx7TlN0kmY8nUEcb297XCixZ7ky-V8rnq_W4Mz6Y9odHbcO5mY7iS1Zya6nW8%3Fkey%3DJqkn8dhQ_InX_HZYbdhKWg)
  4. Pilih di **Stage** mana ticket tersebut akan Anda masukkan.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Flh7-rt.googleusercontent.com%2Fdocsz%2FAD_4nXfl0kQGBVkCqt_sTKFqMm15S-wy61_sXhkmMFwTg-LYHRpb2ejuJnMqDtgUWzQMznaR5RJOTSPAbbTKyA81QMx3LSEm4jk8Q_EIILPVxfJg-r9MEvSFjaPOqr6Z_KCZwxS-ReE7_GYUwu8jOHvODBad0Wg%3Fkey%3DJqkn8dhQ_InX_HZYbdhKWg)
  5. Maka akan muncul kolom lainnya seperti berikut.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F35834581904537)  
****Keterangan:  
**** **No** | **Kolom** | **Penjelasan**  
---|---|---  
1 | Ticket name | Masukkan nama tiket yang Anda inginkan.  
2 | Description | Masukkan deskripsi informasi dari tiket tersebut.  
3 | Assignee | Pilih kepada siapa tiket akan di assign.  
4 | Ticket priority | Pilih prioritas tiket tersebut.  
5 | Ticket Category | Pilih kategori atas tiket tersebut.  
6 | Due date | Tentukan tenggat waktu atas tiket tersebut.  
7 | Note | Masukkan note atau catatan (jika dibutuhkan).  
8 | Contact Association | Pilih kepada kontak mana tiket tersebut akan diasosiasikan.  
9 | Company Association | Pilih kepada perusahaan mana tiket tersebut akan diasosiasikan.  
10 | Product Association | Pilih kepada produk mana tiket tersebut akan diasosiasikan.  
11 | Task Association | Pilih kepada task mana tiket tersebut akan diasosiasikan.  
  6. Jika sudah, klik ****“** Submit**”****.**  
**
  7. Maka tiket sudah berhasil terbuat, Anda dapat klik **“nomor tiket”** untuk membuka tiket pada Qontak CRM.  
![77.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50912106053913)

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