---
title: Bagaimana Cara Melakukan Bulk Approval Deals
canonical_url: https://help-center.qontak.com/hc/id/articles/21395881244953-Bagaimana-Cara-Melakukan-Bulk-Approval-Deals
article_type: task
solvability_type: tool
products:
- Qontak CRM
product_surface: web
language: id
intent_tags:
- sales-pipeline-deals-tracking
- perform-bulk-approval-deals
- sales-management
query_examples:
- Cara Melakukan Bulk Approval Deals
- Bagaimana cara Melakukan Bulk Approval Deals?
- Langkah-langkah Melakukan Bulk Approval Deals di Qontak CRM
- How do I Melakukan Bulk Approval Deals?
- Mau Melakukan Bulk Approval Deals, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

1. Akun Qontak CRM aktif dengan akses login
2. Telah mengatur Approval untuk Deals di Profile Settings → menu Approval → tab Deals → Enable approval
3. Memiliki role/permission untuk mengakses dan melakukan approval pada Deals
4. Minimal satu Deal dengan status "Need approval" sudah ada di sistem
5. Akses ke menu Deals pada Qontak CRM

## Steps  <!-- confidence:high ✓ -->


Pada Qontak CRM, selain melakukan Approval Deals secara satuan, Anda juga dapat melakukannya secara massal (bulk). Berikut adalah langkah - langkah yang dapat Anda lakukan:
  1. Pada tampilan menu Deals, Anda dapat klik **“Need my approval”** untuk membuka daftar approval yang perlu Anda proses.  
![23.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49955103399321)
  2. Anda dapat memanfaatkan filter berdasarkan status di sini. Untuk memproses Approval menurut status yang perlu Anda proses approvalnya, klik pada kolom seperti gambar di bawah ini dan atur ke **Need approval.**  
![24.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49955164898457)
  3. Centang seluruh deals yang perlu Anda proses. Kemudian, klik**“Actions”.**  
![25.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49955164901145)
  4. Lalu, Anda dapat memilih untuk **Approve** (menerima) atau **Reject** (menolak) Approval tersebut.  
![bulkdeals4.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36773920069273)
  5. Maka, sebuah pop-up konfirmasi muncul. Pastikan deals yang akan Anda approve atau Reject sudah sesuai sebelum klik **“Approve”** untuk menyetujuinya.  
![bulkdeals5.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36773920074521)
  6. Maka, approval Anda diproses oleh sistem. Tetap berada pada halaman ini dan tunggu hingga proses selesai.  
![bulkdeals6.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36773920070041)
  7. Maka, Anda dapat melihat hasil proses approval tersebut. **Tanda centang hijau berarti terdapat deals yang sudah berhasil diapprove**. Sedangkan, jika terdapat **tanda silang merah** , maka**terdapat deals yang gagal diapprove**. Terdapat keterangan di bawahnya menjelaskan kenapa deal tersebut gagal diapprove. Klik **Retry approval** **untuk mengulang proses approval** atau klik **“Ok, got it”** **untuk membiarkannya** , dan menutup pop-up.  
![bulkdeals7.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36773920076825)

Demikian panduan cara melakukan approval massal pada Qontak CRM.

## Error States  <!-- confidence:medium ~ -->

Deal gagal diapprove (ditandai tanda silang merah) disertai keterangan alasan kegagalan di bawahnya. Alasan umum meliputi:
- Deal tidak memenuhi syarat approval layer yang ditetapkan
- Perubahan data Deal sejak approval diminta
- Izin akses tidak sesuai

Untuk mengatasi: Baca keterangan error, periksa konfigurasi approval layer di Profile Settings, atau hubungi admin untuk verifikasi permission.

## Escalation  <!-- confidence:medium ~ -->

Hubungi support Qontak jika:
1. Pop-up hasil approval tidak muncul setelah klik "Approve"
2. Semua Deal menunjukkan tanda silang merah tanpa keterangan yang jelas
3. Tombol "Retry approval" tidak berfungsi
4. Deals berhasil diapprove tetapi status di daftar Deals tidak berubah

Siapkan: screenshot error, daftar Deal ID yang bermasalah, dan konfigurasi approval layer Anda.