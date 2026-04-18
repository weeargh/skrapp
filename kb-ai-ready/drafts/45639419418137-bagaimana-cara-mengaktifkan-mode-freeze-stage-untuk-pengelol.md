---
title: Bagaimana Cara Mengaktifkan Mode ‘Freeze Stage’ untuk Pengelolaan Deals
canonical_url: https://help-center.qontak.com/hc/id/articles/45639419418137-Bagaimana-Cara-Mengaktifkan-Mode-Freeze-Stage-untuk-Pengelolaan-Deals
article_type: task
solvability_type: tool
products:
- Qontak CRM
product_surface: web
language: id
intent_tags:
- sales-pipeline-deals-tracking
- enable-mode-freeze-stage-untuk-pengel
- sales-management
query_examples:
- Cara Mengaktifkan Mode ‘Freeze Stage’ untuk Pengelolaan Deals
- Bagaimana cara Mengaktifkan Mode ‘Freeze Stage’ untuk Pengelolaan Deals?
- Langkah-langkah Mengaktifkan Mode ‘Freeze Stage’ untuk Pengelolaan Deals di Qontak
  CRM
- How do I Mengaktifkan Mode ‘Freeze Stage’ untuk Pengelolaan Deals?
- Mau Mengaktifkan Mode ‘Freeze Stage’ untuk Pengelolaan Deals, caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.3
---

## Prerequisites  <!-- confidence:high ✓ -->

1. Akun Qontak CRM aktif dengan akses login
2. Role Admin (hanya Admin yang dapat mengatur Freeze Stage)
3. Minimal satu Pipeline sudah dibuat di menu Deals
4. Akses ke menu Properties dengan permission untuk mengedit Pipeline
5. Deals yang ingin difungsikan dengan Freeze Stage sudah ada di sistem

## Steps  <!-- confidence:high ✓ -->


Apabila Anda mengaktifkan mode ‘Freeze Stage’ pada pengaturan Deals, maka deals tidak dapat diubah jika dipindahkan ke stage tertentu. Sebagai contoh, jika deal dipindah ke stage **Done/Won** , maka deals tersebut sudah tidak dapat diedit kembali. Dalam hal ini, hanya peran **Admin** yang dapat mengatur ‘Freeze Stage’ pada Deals. Hal ini bertujuan untuk memastikan adanya integritas data dan mencegah modifikasi yang tidak diinginkan. Untuk lebih jelasnya, simak langkah-langkah mengaktifkan mode ‘Freeze Stage’ pada Deals.
  1. Masuk ke akun **CRM** Anda, lalu pilih menu **Properties**.
  2. Kemudian klik tab **‘Deals’**.  
![3.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49955802316313)
  3. Kemudian klik tab **"Pipelines"**.  
![27.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49955802331033)
  4. Klik ikon **‘Edit’** pada salah satu **Pipeline** yang telah dibuat.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F45639407498649)
  5. Lalu centang **‘Freeze Stage’** kemudian klik **“Save pipeline”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F45639419402265)
  6. Selanjutnya, masuk ke menu utama **Deals** , lalu pilih **Pipeline** yang telah diaktifkan mode **‘Freeze Stage’**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F45639419403417)
  7. Di sini, Anda akan melihat status **Deals** dalam kondisi **‘Freeze Stage’**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F45639407518233)
  8. Klik salah satu **Deals** untuk melihat detailnya. Kemudian pada saat Anda mencari salah satu **Deal** , maka akan terlihat Deal lain yang juga mengalami ‘Freeze’. Dalam hal ini, Deal yang mengalami ‘freeze’ tersebut tidak dapat ditambahkan. Hal ini dikarenakan data pada Deal akan ikut mengalami perubahan.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F45639419413657)

Demikian cara mengaktifkan mode ‘Freeze Stage’ pada Deals. Selanjutnya, pelajari juga [cara membuat Pipeline Deal baru pada Qontak CRM](https://help-center.qontak.com/hc/id/articles/42009600870169-Bagaimana-Cara-Membuat-Pipeline-Deal-Baru-pada-Qontak-CRM).

## Error States  <!-- confidence:low ? -->

No common errors documented.

## Escalation  <!-- confidence:medium ~ -->

Jika Anda mengalami kesulitan mengakses menu Properties atau tidak melihat opsi Freeze Stage:
1. Verifikasi role Anda adalah Admin di Qontak CRM
2. Pastikan akun sudah memiliki permission untuk mengakses Profile Settings
3. Refresh browser dan login kembali
4. Hubungi tim support Qontak dengan menyertakan: screenshot error, nama akun CRM, dan daftar Pipeline yang bermasalah.