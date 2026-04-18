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

1. Buka menu **Deals** pada Qontak CRM. Sistem akan menampilkan daftar semua Deals.
2. Klik tombol **"Need my approval"**. Sistem akan menampilkan daftar approval Deals yang perlu Anda proses.
3. (Opsional) Gunakan filter status dengan mengklik kolom filter dan atur ke **"Need approval"** untuk melihat hanya Deals yang memerlukan persetujuan.
4. Centang checkbox pada setiap Deal yang ingin Anda approve atau reject secara massal.
5. Klik tombol **"Actions"**. Menu aksi akan muncul.
6. Pilih **"Approve"** (untuk menerima) atau **"Reject"** (untuk menolak). Pop-up konfirmasi akan muncul menampilkan daftar Deals yang dipilih.
7. Verifikasi Deals di pop-up konfirmasi sudah sesuai, kemudian klik **"Approve"**. Sistem akan memproses approval.
8. Tunggu hingga proses selesai. Hasil approval akan ditampilkan dengan indikator: tanda centang hijau (berhasil) atau tanda silang merah (gagal).
9. Baca keterangan jika ada Deal gagal. Klik **"Retry approval"** untuk mengulang atau **"Ok, got it"** untuk menutup pop-up.

## Expected Result  <!-- confidence:high ✓ -->

Setelah proses selesai, Anda melihat status approval untuk setiap Deal:
- **Tanda centang hijau**: Deal berhasil diapprove dan statusnya berubah menjadi "Approved"
- **Tanda silang merah**: Deal gagal diapprove dengan keterangan alasan kegagalan

Deal yang berhasil diapprove akan hilang dari daftar "Need my approval" dan muncul di daftar Deals dengan status diperbarui.

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