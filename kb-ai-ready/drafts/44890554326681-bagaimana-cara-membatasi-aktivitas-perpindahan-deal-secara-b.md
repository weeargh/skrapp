---
title: Bagaimana Cara Membatasi Aktivitas Perpindahan Deal secara Backward pada Mekari
  Qontak CRM
canonical_url: https://help-center.qontak.com/hc/id/articles/44890554326681-Bagaimana-Cara-Membatasi-Aktivitas-Perpindahan-Deal-secara-Backward-pada-Mekari-Qontak-CRM
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
- Cara Membatasi Aktivitas Perpindahan Deal secara Backward pada Mekari Qontak CRM
- Bagaimana cara Membatasi Aktivitas Perpindahan Deal secara Backward pada Mekari
  Qontak CRM?
- Langkah-langkah Membatasi Aktivitas Perpindahan Deal secara Backward pada Mekari
  Qontak CRM di Qontak CRM
- How do I Membatasi Aktivitas Perpindahan Deal secara Backward pada Mekari Qontak
  CRM?
- Mau Membatasi Aktivitas Perpindahan Deal secara Backward pada Mekari Qontak CRM,
  caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.3
---

## Prerequisites  <!-- confidence:high ✓ -->

1. Akun Qontak CRM aktif dengan akses login
2. Role Admin atau Owner (fitur ini hanya dapat diakses oleh Admin/Owner)
3. Minimal satu Pipeline sudah dibuat di menu Properties → tab Deals
4. Akses ke menu Properties dengan izin untuk mengedit Pipeline
5. Memahami urutan tahap (stage order) yang berlaku pada Pipeline Anda

## Steps  <!-- confidence:high ✓ -->


Dalam sistem yang ada, fitur **‘Rotten time’** tersedia untuk mengidentifikasi transaksi yang terhambat pada tahap tertentu setelah batas waktu yang ditentukan. Namun nyatanya, agent telah menemukan solusi untuk melewati fungsi ini yaitu dengan ‘sengaja’ memindahkan transaksi ke tahap sebelumnya dan kemudian segera kembali ke tahap berikutnya, kemudian mereka menyetel ulang penghitung **‘Rotten time’**. Manipulasi ini membuat fitur **Rotten time** menjadi tidak efektif.

Untuk mengatasi hal tersebut, kami menghadirkan fitur **Restrict moving forward Deal stage** berupa toggle yang apabila Anda aktifkan akan mencegah **Deal** dipindahkan ke tahap dengan urutan tahap yang lebih rendah. Pada penjelasan di bawah ini, Anda akan mempelajari mulai dari cara mengaktifkan hingga mengimplementasikan pembatasan aktivitas perpindahan Deals secara _backward_. Berikut langkah-langkahnya.
**Penting**   
Fitur ini hanya dapat diakses oleh**Admin/Owner**.
  1. Pada akun Qontak CRM Anda, masuk ke menu **Properties**.
  2. Kemudian pilih tab **“Deals”**.  
![3.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49955575707289)
  3. Kemudian klik tab **"Pipelines"**.  
![27.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49955568259737)
  4. Lalu pada salah satu **“Pipeline”** klik **“Edit”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F44890554311961)
  5. Selanjutnya Anda akan diarahkan ke halaman berikut. Centang toggle **“Deal stage cannot move backwards”** apabila Anda ingin menerapkannya.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F44890563352857)

**Stage order** tersebut berasal dari edit order pada menu **Properties** di bagian tab **Deals**. Berikut langkah-langkahnya:  
1. Masuk ke menu **Properties** , lalu pilih tab **Deals**.  
2. Kemudian pada tabel **Pipeline list** , klik ikon **‘Change Stage Order’**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F44890563354905)  
3. Kemudian Anda dapat kelola urutan _stage_ tersebut dengan klik **ikon titik enam** , lalu pindahkan urutan **Pipeline** sesuai dengan yang Anda inginkan.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F44890554315545)
  6. Kemudian klik **“Save Pipeline”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F44890563357081)
  7. Lalu akan muncul _pop up_ informasi berikut yang menyatakan bahwa pembatasan pemindahan _stage_ pada Deals akan berlaku untuk seluruh Deal baik yang sudah ada, maupun Deal baru pada pipeline yang telah Anda aktifkan pembatasan Dealsnya. Klik **“Restrict”** untuk melanjutkan.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F44890554319513)
  8. Kemudian, apabila Anda beralih ke menu **Deals** , pada **pipeline** yang telah dibatasi perpindahannya, akan muncul notifikasi berikut. Dalam hal ini, peran lain **tidak dapat** memindahkan Deals ke _stage_ yang lebih rendah.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F44890554321433)
  9. Selain itu, apabila Anda klik salah satu **Deal** , akan muncul informasi berikut yang juga menandakan bahwa peran lain **tidak dapat** memindahkan Deals ke stage yang lebih rendah.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F44890563367065)
  10. Pembatasan ini juga akan berlaku pada Deals di Mobile Apps.

Demikian penjelasan terkait fitur Deals cannot Move Backwards. Selanjutnya, pelajari juga terkait cara membuat Conditional Formatting pada Deals [di sini](https://help-center.qontak.com/hc/id/articles/32845659060377).

## Error States  <!-- confidence:low ? -->

No common errors documented.

## Escalation  <!-- confidence:medium ~ -->

Jika toggle **Deal stage cannot move backwards** tidak muncul atau tidak responsif setelah Anda membuka halaman edit Pipeline:
1. Verifikasi bahwa Anda login dengan role Admin atau Owner.
2. Refresh halaman browser dan coba kembali.
3. Jika masalah persisten, catat informasi berikut sebelum menghubungi Qontak Support:
   - Nama Pipeline yang bermasalah
   - ID akun Qontak CRM Anda
   - Screenshot halaman edit Pipeline
   - Browser dan versi yang digunakan