---
title: Bagaimana Cara Membuat dan Mengatur Custom Goal
canonical_url: https://help-center.qontak.com/hc/id/articles/23249048100121-Bagaimana-Cara-Membuat-dan-Mengatur-Custom-Goal
article_type: task
solvability_type: tool
products:
- Qontak CRM
product_surface: web
language: id
intent_tags:
- goal-setting-performance-tracking
- sales-management
query_examples:
- Cara Membuat dan Mengatur Custom Goal
- Bagaimana cara Membuat dan Mengatur Custom Goal?
- Langkah-langkah Membuat dan Mengatur Custom Goal di Qontak CRM
- How do I Membuat dan Mengatur Custom Goal?
- Mau Membuat dan Mengatur Custom Goal, caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

1. Role: Akun dengan peran Admin untuk menambahkan kontributor pada Custom Goal.
2. Akun Anda dan akun tim harus terdaftar di tim utama.
3. Jika menambahkan kontributor dari tim lain, hierarki Parent Team dan Child Team harus dikonfigurasi dengan benar.
4. Akses View Deals pengguna menentukan siapa yang dapat ditambahkan sebagai kontributor:
   - View Deals = Everything: dapat menambahkan semua pengguna organisasi
   - View Deals = Team Only: dapat menambahkan pengguna tim sendiri dan tim di bawah hierarki
   - View Deals = Owned Only: hanya dapat menambahkan diri sendiri.

## Steps  <!-- confidence:medium ~ -->

1. Buka menu **Custom Goal** di Qontak CRM.
   Sistem akan menampilkan daftar Custom Goal yang sudah dibuat.

2. Klik tombol **"Buat target"** di sudut kanan atas halaman.
   Sistem akan membuka halaman formulir pembuatan target.

3. Isi formulir data target dengan kolom: **Nama target**, **Periode target**, **Tipe target**, **Pipeline**, dan **Total target deal**.

4. Klik tombol **"Tambah kontributor"** untuk menentukan kontributor target.

5. Pilih kontributor dengan memilih kategori **Karyawan tim utama** atau **Karyawan dari tim lainnya**.
   (Opsional) Klik **"Filter"** untuk menemukan kontributor berdasarkan Tim dan Level staf, lalu klik **"Terapkan filter"**.

6. Klik tombol **"Tambah"** untuk menambahkan kontributor.

7. Klik tombol **"Simpan"** untuk menyimpan Custom Goal.
   Sistem akan menampilkan konfirmasi dan Custom Goal akan muncul di daftar Custom Goal.## Expected Result  <!-- confidence:high ✓ -->

Setelah menyimpan, Custom Goal berhasil dibuat dan muncul di menu **Custom Goal** dengan status aktif. Sistem menampilkan detail target yang berisi nama target, periode, tipe, pipeline, total target deal, dan daftar kontributor yang sudah ditambahkan. Semua kontributor yang terdaftar dapat memantau kemajuan mereka masing-masing terhadap target yang telah ditetapkan.

> Screenshot: 1.png
> Image: https://help-center.qontak.com/hc/article_attachments/25418431791641

> Screenshot: 2.png
> Image: https://help-center.qontak.com/hc/article_attachments/25417506070681

> Screenshot: 3.1.png
> Image: https://help-center.qontak.com/hc/article_attachments/25417533123481

> Screenshot: 3.png
> Image: https://help-center.qontak.com/hc/article_attachments/25418365437721

> Screenshot: 7.png
> Image: https://help-center.qontak.com/hc/article_attachments/25418391619481

> Screenshot: 8.png
> Image: https://help-center.qontak.com/hc/article_attachments/23249772028441

## Error States  <!-- confidence:medium ~ -->

1. **Tidak dapat menambahkan kontributor**: Peran akun Anda bukan Admin. Hubungi Admin akun untuk menambahkan kontributor.

2. **Kontributor dari tim lain tidak muncul**: Hierarki Parent Team dan Child Team belum dikonfigurasi. Minta Admin untuk mengatur hubungan tim terlebih dahulu.

3. **Pengguna tertentu tidak dapat dipilih**: Pengguna tidak terdaftar di tim utama atau akses View Deals mereka tidak memungkinkan. Periksa konfigurasi View Deals dan registrasi tim pengguna.

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support jika: 1) Tidak dapat mengakses menu Custom Goal meskipun memiliki peran Admin, 2) Formulir Custom Goal tidak menyimpan data meskipun sudah diisi lengkap, 3) Kontributor sudah ditambahkan namun tidak muncul di laporan progress target, atau 4) Pesan error sistem muncul saat membuat atau menyimpan target. Sediakan: screenshot halaman yang error, ID akun Qontak, dan langkah yang sudah dicoba.