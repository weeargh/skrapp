---
title: Bagaimana Cara Mengatur Freeze Task pada Menu Task Mekari Qontak CRM
canonical_url: https://help-center.qontak.com/hc/id/articles/43686029961881-Bagaimana-Cara-Mengatur-Freeze-Task-pada-Menu-Task-Mekari-Qontak-CRM
article_type: task
solvability_type: tool
products:
- Qontak CRM
product_surface: web
language: id
intent_tags:
- task-management
- configure-freeze-task
- operation-workflow-automa
query_examples:
- Cara Mengatur Freeze Task pada Menu Task Mekari Qontak CRM
- Bagaimana cara Mengatur Freeze Task pada Menu Task Mekari Qontak CRM?
- Langkah-langkah Mengatur Freeze Task pada Menu Task Mekari Qontak CRM di Qontak
  CRM
- How do I Mengatur Freeze Task pada Menu Task Mekari Qontak CRM?
- Mau Mengatur Freeze Task pada Menu Task Mekari Qontak CRM, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengatur Freeze Task pada menu Task Mekari Qontak CRM, Anda memerlukan:

• Akun Mekari Qontak CRM yang aktif
• Role Admin atau Owner (hanya role ini yang dapat mengaktifkan, menonaktifkan, dan mengedit Freeze Task Settings)
• Akses ke menu Properties
• Tab Task tersedia di dalam menu Properties
• Pemahaman tentang jenis Trigger yang ingin digunakan (misalnya Task status atau tanggal jatuh tempo)

## Steps  <!-- confidence:high ✓ -->

1. Masuk ke akun Mekari Qontak CRM Anda, lalu buka menu **Properties**.
2. Pilih tab **Task** — sistem akan menampilkan daftar pengaturan Task.
3. Klik **"Frozen task settings"** — Anda akan diarahkan ke halaman pengaturan Freeze Task.
4. Aktifkan toggle **Frozen task**, kemudian pilih jenis Trigger (contoh: **Task status**).
5. Tentukan kondisi spesifik sesuai Trigger yang dipilih — sistem akan menampilkan opsi yang relevan.
6. Klik **"Save changes"** — popup konfirmasi akan muncul.
7. Klik **"Enable"** untuk mengaktifkan Freeze Task — pengaturan akan diterapkan ke seluruh Task dalam 15 menit.

**Untuk menonaktifkan:**
8. Kembali ke **Frozen task settings**, lalu nonaktifkan toggle **Frozen task**.
9. Klik **"Disable"** pada popup konfirmasi — pengaturan akan dinonaktifkan dalam 15 menit.

> Screenshot: 29.png
> Image: https://help-center.qontak.com/hc/article_attachments/53150081079833

> Screenshot: 35.png
> Image: https://help-center.qontak.com/hc/article_attachments/53150081082265

> Screenshot: 36.png
> Image: https://help-center.qontak.com/hc/article_attachments/53150081083417

> Screenshot: 37.png
> Image: https://help-center.qontak.com/hc/article_attachments/53150053419929

> Screenshot: 38.png
> Image: https://help-center.qontak.com/hc/article_attachments/53150053421593

> Screenshot: 39.png
> Image: https://help-center.qontak.com/hc/article_attachments/53150081086617

> Screenshot: 40.png
> Image: https://help-center.qontak.com/hc/article_attachments/53150081087513

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/43686029955353

> Screenshot: Screenshot
> Image: https://help-center.qontak.com/hc/article_attachments/43686029955993

## Expected Result  <!-- confidence:high ✓ -->

• Pengaturan Freeze Task berhasil disimpan dengan pesan konfirmasi popup
• Toggle **Frozen task** menampilkan status aktif atau nonaktif sesuai pilihan Anda
• Sistem menerapkan pengaturan ke semua Task (baru dan yang sudah ada) dalam kurun waktu 15 menit
• Ketika aktif, task updates akan dibatasi sampai Task di-unfreeze
• Ketika nonaktif, task updates akan diizinkan kembali
• Admin/Owner dapat kembali ke **Frozen task settings** kapan saja untuk melakukan edit ulang

## Error States  <!-- confidence:high ✓ -->

No common errors documented.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Mekari Qontak jika mengalami:

• Pengaturan Freeze Task tidak tersimpan setelah mengklik **"Save changes"**
• Popup konfirmasi tidak muncul saat mengklik **"Enable"** atau **"Disable"**
• Freeze Task tidak diterapkan ke Task setelah 15 menit
• Pesan error muncul saat mengakses **Frozen task settings**
• Role Admin/Owner tidak dapat mengakses fitur ini

Siapkan informasi: nama akun, screenshot halaman **Frozen task settings**, dan daftar Task yang terpengaruh untuk membantu diagnosis.