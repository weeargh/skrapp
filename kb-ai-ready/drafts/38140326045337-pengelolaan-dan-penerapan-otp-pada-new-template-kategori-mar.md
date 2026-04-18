---
title: Pengelolaan dan Penerapan OTP pada New Template Kategori Marketing dan Utility
  pada Menu Campaign (Broadcast)
canonical_url: https://help-center.qontak.com/hc/id/articles/38140326045337-Pengelolaan-dan-Penerapan-OTP-pada-New-Template-Kategori-Marketing-dan-Utility-pada-Menu-Campaign-Broadcast
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- campaign-management
- marketing-campaign-manage
query_examples:
- Cara Pengelolaan dan Penerapan OTP pada New Template Kategori Marketing dan Utility
  pada Menu Campaign (Broadcast)
- Bagaimana cara Pengelolaan dan Penerapan OTP pada New Template Kategori Marketing
  dan Utility pada Menu Campaign (Broadcast)?
- Langkah-langkah Pengelolaan dan Penerapan OTP pada New Template Kategori Marketing
  dan Utility pada Menu Campaign (Broadcast) di Qontak Omnichannel
- How do I Pengelolaan dan Penerapan OTP pada New Template Kategori Marketing dan
  Utility pada Menu Campaign (Broadcast)?
- Mau Pengelolaan dan Penerapan OTP pada New Template Kategori Marketing dan Utility
  pada Menu Campaign (Broadcast), caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Anda memerlukan akun Qontak Omnichannel aktif dengan peran Admin. Alamat email yang terdaftar pada akun Anda harus valid dan mampu menerima email, karena kode OTP akan dikirimkan melalui email untuk verifikasi identitas. Pastikan Anda memiliki akses penuh ke menu Settings dan Campaign untuk mengelola toggle OTP serta membuat template baru.

## Steps  <!-- confidence:high ✓ -->

**Mengelola OTP pada Security Settings:**
1. Masuk ke akun Qontak Omnichannel Anda.
2. Buka menu Settings, lalu pilih Security.
3. Cari toggle OTP Authentication untuk Broadcast Template dan klik untuk mengaktifkan atau menonaktifkan.
4. Tekan tombol Enable atau Disable pada pop-up konfirmasi yang muncul.
5. Sistem akan mengirimkan kode OTP ke email Anda.
6. Salin kode OTP dari email dan masukkan pada kolom verifikasi.
7. Klik tombol Verify untuk menyelesaikan proses.

**Menerapkan OTP pada New Template:**
1. Buka menu Campaign, lalu pilih Templates.
2. Klik tombol Add New Template untuk membuat template baru dengan kategori Marketing atau Utility.
3. Template creation akan meminta kode OTP jika toggle sudah diaktifkan di Security Settings.## Expected Result  <!-- confidence:high ✓ -->

Setelah mengaktifkan toggle di Settings, sistem menampilkan notifikasi sukses yang mengonfirmasi OTP Authentication telah diaktifkan untuk Broadcast Template. Ketika Anda membuat New Template pada menu Campaign → Templates dengan kategori Marketing atau Utility, sistem akan meminta verifikasi OTP sebelum template dapat disimpan. Jika toggle dinonaktifkan, permintaan OTP tidak akan muncul saat pembuatan template.

![1.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F43690885861913)
![2.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F38140325979033)
![3.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F38140325981721)
![4.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F38140325987097)
![5.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F38140325989273)
![6.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F38140363885977)
![7.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F38140363888281)
![8.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F38140363889305)
![9.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F38140489769241)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F38140309112217)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F38140326015001)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F38140309126169)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F38140309129113)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F38140326033177)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F38140326036761)

## Error States  <!-- confidence:medium ~ -->

**Email tidak menerima kode OTP:** Periksa folder spam atau inbox email Anda. Pastikan alamat email pada akun Qontak valid dan dapat menerima email masuk. Tunggu beberapa menit dan minta pengiriman ulang kode OTP jika diperlukan.

**Kode OTP salah atau kadaluarsa:** Kode OTP memiliki masa berlaku terbatas. Jika kode sudah kadaluarsa, minta pengiriman kode OTP baru melalui email. Masukkan kode yang paling baru diterima.

**Toggle tidak dapat diubah:** Pastikan Anda login sebagai Admin dan memiliki akses penuh ke menu Settings Security.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak jika email OTP tidak pernah sampai meskipun Anda telah menunggu dan memeriksa spam folder, atau jika toggle OTP pada Security Settings tidak berfungsi dengan baik. Sertakan screenshot halaman Security, informasi email terdaftar pada akun, dan waktu saat Anda mencoba mengaktifkan OTP. Tim support dapat membantu memeriksa konfigurasi email dan toggle system Anda.