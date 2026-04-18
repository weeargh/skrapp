---
title: Bagaimana Cara Mengelola Kebijakan SLA di CRM Qontak
canonical_url: https://help-center.qontak.com/hc/id/articles/37014086336665-Bagaimana-Cara-Mengelola-Kebijakan-SLA-di-CRM-Qontak
article_type: task
solvability_type: tool
products:
- Qontak CRM
product_surface: web
language: id
intent_tags:
- sla-management-countdown
- manage-kebijakan-sla
- customer-support-ticketin
query_examples:
- Cara Mengelola Kebijakan SLA di CRM Qontak
- Bagaimana cara Mengelola Kebijakan SLA di CRM Qontak?
- Langkah-langkah Mengelola Kebijakan SLA di CRM Qontak di Qontak CRM
- How do I Mengelola Kebijakan SLA di CRM Qontak?
- Mau Mengelola Kebijakan SLA di CRM Qontak, caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengelola kebijakan SLA di CRM Qontak, Anda membutuhkan:

- **User role**: Admin atau Owner
- **Service plan**: Ultimate atau Enterprise tier
- **Produk**: Mekari Qontak CRM
- **Modul**: Ticket Module harus aktif
- **Pengaturan sebelumnya**: Minimal satu kebijakan SLA telah diterapkan melalui menu Properties > SLA Management > Create Policy

## Steps  <!-- confidence:high ✓ -->

1. Buka halaman **Tickets** di CRM Qontak. Sistem akan menampilkan daftar tiket dalam format tabel dengan kolom **SLA Target**.

2. Lihat kolom **SLA Target** pada tabel. Status SLA akan otomatis muncul setelah Anda memilih Assignee pada tiket tersebut.

3. Arahkan kursor ke kolom **SLA Target** untuk melihat detail status SLA yang sedang berjalan (Not Started, On Going, Breach Risk, atau Completed).

4. Klik tombol **Filter** untuk memunculkan tiket berdasarkan progress SLA tertentu.

5. Pada kolom **SLA Target**, pilih status yang ingin ditampilkan, kemudian klik **Apply Filter**. Sistem akan menampilkan tiket yang sesuai dengan filter.

6. Centang tiket yang ingin dilihat SLA-nya, lalu klik **Download** untuk mengunduh data tiket dalam format file. Kolom **SLA Target** dan **Resolution Time** akan tersedia di file yang diunduh.

## Expected Result  <!-- confidence:high ✓ -->

Setelah menyelesaikan langkah-langkah di atas, Anda akan berhasil mengelola kebijakan SLA dengan hasil berikut:

- Kolom **SLA Target** menampilkan status SLA untuk setiap tiket
- Filter SLA berfungsi dan menampilkan hanya tiket sesuai status yang dipilih
- File yang diunduh berisi kolom **SLA Target** dan **Resolution Time** untuk analisis
- Status SLA terlihat jelas dengan indikator visual (warna kuning untuk Breach Risk)

## Error States  <!-- confidence:medium ~ -->

**Kolom SLA Target tidak muncul**: Pastikan Assignee telah dipilih pada tiket. SLA Target hanya muncul setelah tiket di-assign ke user tertentu.

**Status SLA menampilkan "Blank"**: Berarti tidak ada SLA yang di-assign pada tiket tersebut. Terapkan kebijakan SLA terlebih dahulu melalui menu Properties > SLA Management.

**Filter tidak menampilkan hasil**: Verifikasi bahwa tiket Anda sesuai dengan kondisi kebijakan SLA yang telah diterapkan (Pipeline, Field conditions yang cocok).

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support jika mengalami masalah berikut:

- SLA Target tetap tidak muncul meski Assignee sudah dipilih
- Filter SLA tidak berfungsi atau hasil tidak sesuai harapan
- File yang diunduh tidak menampilkan kolom SLA Target dan Resolution Time
- Kebijakan SLA tidak apply ke tiket meskipun kondisi sudah sesuai

Siapkan informasi: ID tiket, nama Pipeline, screenshot halaman Tickets, dan deskripsi kebijakan SLA yang diterapkan.