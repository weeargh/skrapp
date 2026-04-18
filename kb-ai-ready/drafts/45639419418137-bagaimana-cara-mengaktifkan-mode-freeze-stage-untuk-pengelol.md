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

1. Login ke akun Qontak CRM, lalu buka menu **Properties**.
2. Klik tab **Deals**. Sistem menampilkan daftar pengaturan Deals.
3. Klik tab **Pipelines**. Sistem menampilkan daftar semua Pipeline yang telah dibuat.
4. Klik ikon **Edit** pada Pipeline yang ingin diaktifkan Freeze Stage. Form edit Pipeline terbuka.
5. Centang checkbox **Freeze Stage** di dalam form. Opsi Freeze Stage menjadi aktif.
6. Klik tombol **Save pipeline**. Sistem menyimpan pengaturan dan kembali ke daftar Pipelines.
7. Buka menu utama **Deals** dan pilih Pipeline yang telah diaktifkan Freeze Stage. Deals dalam Pipeline ditampilkan dengan status Freeze Stage.
8. Klik salah satu Deal untuk lihat detailnya. Deal yang dalam status Freeze Stage tidak dapat diedit atau dipindahkan ke stage lain.

> Screenshot: 3.png
> Image: https://help-center.qontak.com/hc/article_attachments/49955802316313

> Screenshot: 27.png
> Image: https://help-center.qontak.com/hc/article_attachments/49955802331033

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/45639407498649

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/45639419402265

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/45639419403417

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/45639407518233

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/45639419413657

## Expected Result  <!-- confidence:high ✓ -->

Setelah mengaktifkan Freeze Stage pada Pipeline, Deals yang berada di stage yang dikonfigurasi dengan Freeze Stage akan terkunci dan tidak dapat diedit atau dimodifikasi. Sistem menampilkan status Freeze Stage pada setiap Deal yang terdampak. Hanya Admin yang dapat mengubah pengaturan Freeze Stage kembali. Data integritas Deal terjaga karena tidak ada modifikasi yang tidak diinginkan setelah Deal mencapai stage final (misalnya Done/Won).

## Error States  <!-- confidence:low ? -->

No common errors documented.

## Escalation  <!-- confidence:medium ~ -->

Jika Anda mengalami kesulitan mengakses menu Properties atau tidak melihat opsi Freeze Stage:
1. Verifikasi role Anda adalah Admin di Qontak CRM
2. Pastikan akun sudah memiliki permission untuk mengakses Profile Settings
3. Refresh browser dan login kembali
4. Hubungi tim support Qontak dengan menyertakan: screenshot error, nama akun CRM, dan daftar Pipeline yang bermasalah.