---
title: Bagaimana Cara Membuat Conditional Formatting untuk Deals Properties
canonical_url: https://help-center.qontak.com/hc/id/articles/32845659060377-Bagaimana-Cara-Membuat-Conditional-Formatting-untuk-Deals-Properties
article_type: task
solvability_type: tool
products:
- Qontak CRM
product_surface: web
language: id
intent_tags:
- sales-pipeline-deals-tracking
- create-conditional-formatting-untuk-d
- sales-management
query_examples:
- Cara Membuat Conditional Formatting untuk Deals Properties
- Bagaimana cara Membuat Conditional Formatting untuk Deals Properties?
- Langkah-langkah Membuat Conditional Formatting untuk Deals Properties di Qontak
  CRM
- How do I Membuat Conditional Formatting untuk Deals Properties?
- Mau Membuat Conditional Formatting untuk Deals Properties, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk membuat Conditional Formatting untuk Deals Properties, Anda memerlukan:

1. Akun Qontak CRM aktif dengan akses login
2. Akses ke menu Properties di CRM
3. Permission/role untuk mengelola Deals Properties
4. Minimal satu Parent property (properti induk) yang sudah tersedia di sistem Deals

Catatan: Fitur Conditional format (Format bersyarat) hanya berlaku untuk Deals dan Website.

## Steps  <!-- confidence:high ✓ -->

1. Buka akun CRM Anda, lalu pilih menu **Properties**. Sistem akan menampilkan daftar properties yang tersedia.

2. Klik tab **Deals**. Halaman akan menampilkan semua properties yang terkait dengan Deals.

3. Klik ikon segitiga ke bawah, lalu pilih **Add conditional property**. Form pembuatan properti bersyarat akan terbuka.

4. Pilih **Parent property** (properti induk). Dropdown akan menampilkan daftar properti yang dapat dijadikan induk.

5. Pilih **Child property** (properti cabang) untuk Parent property yang telah dipilih. Anda dapat memilih kategori dengan opsi **All options** (semua kategori) atau **Selected options only** (kategori tertentu). Sistem akan memvalidasi bahwa setiap opsi Parent property telah dipetakan ke Child property.

6. Klik **Save**. Conditional format akan disimpan dan ditampilkan di bagian Conditional properties.

7. Conditional format yang telah dibuat siap digunakan saat pembuatan Deals.## Expected Result  <!-- confidence:high ✓ -->

Setelah berhasil membuat Conditional format:

1. Conditional format akan terlihat di bagian **Conditional properties** dengan struktur Parent property dan Child property yang telah Anda konfigurasi.

2. Format bersyarat ini akan tersedia untuk diterapkan saat Anda membuat Deal baru di menu Deals.

3. Sistem akan memastikan bahwa setiap kategori yang ditetapkan sebagai properti induk atau cabang tidak dapat digunakan kembali untuk role yang sama dalam conditional formatting yang sama.

![3.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49889924033689)
![8.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49889924034713)
![3.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36776190278425)
![4.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36776163410073)
![5.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36776190282137)
![9.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49889987003801)
![6.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36776190286873)

## Error States  <!-- confidence:high ✓ -->

Error status akan muncul ketika:

1. **Opsi Parent property yang belum dipetakan** – Jika ada opsi properti induk yang belum memiliki Child property yang terhubung, status 'error' akan muncul setelah Anda klik **Simpan**. Solusi: Pastikan setiap opsi Parent property telah dipetakan ke minimal satu Child property sebelum menyimpan.

2. **Kategori sudah digunakan** – Kategori yang telah ditetapkan sebagai properti induk tidak dapat ditetapkan sebagai properti induk atau cabang lagi dalam conditional formatting yang sama. Kategori yang ditetapkan sebagai properti cabang juga tidak dapat digunakan sebagai cabang lagi, namun masih dapat dijadikan properti induk untuk conditional formatting berikutnya.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak jika:

1. Conditional format tidak muncul di bagian Conditional properties setelah klik **Save**
2. Sistem menampilkan error message yang tidak jelas saat menyimpan conditional format
3. Child property tidak tersedia untuk dipilih meskipun Parent property sudah dipilih
4. Conditional format tidak dapat diterapkan saat membuat Deal baru

Saat menghubungi support, sertakan: screenshot halaman Properties, daftar Parent dan Child property yang Anda gunakan, dan error message lengkap jika ada.