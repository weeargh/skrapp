---
title: Bagaimana Cara Membuat Expense
canonical_url: https://help-center.qontak.com/hc/id/articles/26986963484441-Bagaimana-Cara-Membuat-Expense
article_type: task
solvability_type: tool
products:
- Qontak CRM
product_surface: web
language: id
intent_tags:
- workflow-automation
- create-expense
- operation-workflow-automa
query_examples:
- Cara Membuat Expense
- Bagaimana cara Membuat Expense?
- Langkah-langkah Membuat Expense di Qontak CRM
- How do I Membuat Expense?
- Mau Membuat Expense, caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk membuat expense di Mekari Qontak CRM, Anda memerlukan:
- Akses ke Mekari Qontak CRM Dashboard
- Akun Mekari Qontak yang aktif
- Peran pengguna dengan akses ke menu Expense
- (Opsional) Data kontak, perusahaan, atau deal yang sudah terdaftar di CRM jika ingin mengaitkan expense

## Steps  <!-- confidence:high ✓ -->

1. Buka Dashboard Mekari Qontak CRM dan klik menu **Expense**. Sistem akan menampilkan halaman daftar expense.
2. Klik tombol **Add Expense**. Halaman form pembuatan expense akan terbuka.
3. Isi semua informasi expense:
   - **Expense date**: Masukkan tanggal pembuatan expense
   - **Expenses amount**: Masukkan jumlah dan pilih mata uang
   - **Associated contact**: (Opsional) Pilih kontak jika expense terkait dengan kontak tertentu
   - **Associated company**: (Opsional) Pilih perusahaan kontak
   - **Associated deal**: (Opsional) Pilih deal jika expense terkait dengan deal tertentu
   - **Category**: Pilih kategori expense yang sesuai
   - **Description**: (Opsional) Tambahkan deskripsi expense
   - **Upload photos/images**: (Opsional) Unggah bukti pembayaran
4. Klik tombol **Submit**. Data expense akan tersimpan dan sistem akan menampilkan konfirmasi penyimpanan.

> Screenshot: 52.png
> Image: https://help-center.qontak.com/hc/article_attachments/53149356184985

> Screenshot: 53.png
> Image: https://help-center.qontak.com/hc/article_attachments/53149356187545

## Expected Result  <!-- confidence:high ✓ -->

Expense berhasil dibuat dan tersimpan. Sistem menampilkan pesan konfirmasi sukses. Data expense kini muncul di daftar menu Expense dengan informasi lengkap (tanggal, jumlah, kategori, kontak/deal terkait jika ada). Expense dapat dievaluasi dan dilacak oleh perusahaan sesuai kebutuhan bisnis.

## Error States  <!-- confidence:medium ~ -->

- **Form tidak lengkap**: Pastikan field wajib seperti Expense date dan Expenses amount telah diisi sebelum klik Submit
- **Mata uang tidak sesuai**: Pilih mata uang dengan benar di field Expenses amount sebelum memasukkan jumlah
- **File upload gagal**: Gunakan format gambar standar (JPG, PNG) dengan ukuran di bawah batas maksimal yang ditentukan sistem
- **Kontak/Deal tidak muncul di dropdown**: Pastikan kontak atau deal sudah terdaftar di CRM sebelum mengaitkannya

## Escalation  <!-- confidence:medium ~ -->

Jika expense gagal tersimpan atau menu Expense tidak dapat diakses:
1. Verifikasi bahwa pengguna Anda memiliki izin akses ke menu Expense (hubungi admin CRM Anda)
2. Hapus cache browser dan coba lagi
3. Pastikan koneksi internet stabil
4. Jika masalah berlanjut, hubungi Mekari Qontak Support dengan menyertakan: screenshot error, nama pengguna, ID akun Qontak, dan deskripsi masalah yang dialami