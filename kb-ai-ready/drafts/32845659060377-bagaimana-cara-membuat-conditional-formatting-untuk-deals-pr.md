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


Mekari Qontak menghadirkan sebuah fitur yang akan memudahkan Anda dalam menyiapkan **Deals Properties** dengan **format bersyarat**. Fitur **Conditional format (Format bersyarat)** ini akan membantu Anda dalam mengurangi kesalahan yang mungkin terjadi pada saat mengatur format properti berdasarkan kebutuhan bisnis Anda. Simak penjelasannya pada langkah-langkah berikut.
**Penting**  
**Conditional format** (Format bersyarat) hanya berlaku untuk **Deals** dan **Website**.
  1. Masuk ke akun **CRM** Anda, lalu pilih menu **Properties**.
  2. Kemudian pilih tab **“Deals”**.  
![3.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49889924033689)
  3. Selanjutnya klik **'ikon segitiga ke bawah'** ,**“Add conditional property”** untuk membuat properti bersyarat baru pada **Deals**.  
![8.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49889924034713)
  4. Kemudian pada halaman berikut, pilih **Parent property (properti induk)** terlebih dahulu.  
![3.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36776190278425)
  5. Pilih juga **Child property (properti cabang)** untuk**Parent property (properti induk)** yang tersedia. Anda dapat memilih kategori untuk setiap pilihan **Child property**. Pilih **All options** untuk semua kategori atau pilih **Selected options only** untuk pilihan kategori tertentu.  
![4.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36776163410073)
- Setelah suatu kategori ditetapkan sebagai **induk** , kategori tersebut tidak dapat ditetapkan sebagai **induk** atau **cabang** lagi.   
- Apabila suatu kategori telah ditetapkan sebagai **properti cabang** , maka kategori tersebut tidak dapat ditetapkan sebagai **properti cabang** lagi. Namun, kategori tersebut masih dapat ditetapkan sebagai **properti induk** untuk **Conditional formatting** yang akan datang.   
- Jika ada opsi properti induk yang belum dipetakan ke properti cabang, maka status **‘error’** akan muncul setelah pengguna klik **“Simpan”**.
  6. Lalu klik **“Save”**.  
![5.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36776190282137)
  7. Kemudian **Conditional format** akan terlihat pada bagian **Conditional properties** seperti pada tampilan berikut.  
![9.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49889987003801)
  8. **Conditional format (Format bersyarat)** yang telah dibuat tersebut dapat diterapkan pada saat pembuatan **Deals**.  
![6.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36776190286873)

Demikian cara membuat **Conditional format (Format bersyarat)** untuk pembuatan **Deals**. Pelajari juga terkait[ overview menu deals](https://help-center.qontak.com/hc/id/articles/6081264912025-Overview-Menu-Deals) dan [cara menambahkan Deal satuan versi web](https://help-center.qontak.com/hc/id/articles/5659326461337-Bagaimana-Cara-Menambahkan-Deal-Satuan-Versi-Web).

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