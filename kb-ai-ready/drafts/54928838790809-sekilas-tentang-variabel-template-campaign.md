---
title: Sekilas tentang Variabel Template Campaign
canonical_url: https://help-center.qontak.com/hc/id/articles/54928838790809-Sekilas-tentang-Variabel-Template-Campaign
article_type: concept
solvability_type: content
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: api
language: id
intent_tags:
- campaign-management
- marketing-campaign-manage
query_examples:
- Apa itu Variabel Template Campaign?
- Apa fungsi Variabel Template Campaign di Qontak Omnichannel?
- Penjelasan Variabel Template Campaign
- What is Variabel Template Campaign?
- Bagaimana cara kerja Variabel Template Campaign?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Definition  <!-- confidence:high ✓ -->

Variabel Template Campaign adalah fitur pada Mekari Qontak yang memungkinkan Anda menampilkan data unik untuk setiap penerima dalam kampanye WhatsApp (WABA) atau Email. Variabel menggunakan format placeholder numerik berurutan seperti {{1}}, {{2}}, {{3}} yang akan diganti dengan data aktual saat kampanye dikirim. Fitur ini membuat konten template lebih personal dan interaktif dengan menampilkan informasi spesifik seperti nama pelanggan, nomor invoice, tanggal jatuh tempo, atau kode voucher untuk setiap penerima.

## Why It Matters  <!-- confidence:high ✓ -->

Menggunakan variabel dalam template campaign meningkatkan tingkat engagement pelanggan karena pesan terasa lebih personal dan relevan. Dengan menampilkan data spesifik seperti nama, nomor pesanan, atau jadwal pengiriman, Anda dapat membangun kepercayaan dan respons yang lebih baik dari audiens. Variabel juga menghemat waktu pembuatan kampanye karena Anda hanya perlu membuat satu template yang dapat digunakan untuk ribuan penerima dengan data berbeda-beda.

## Key Attributes  <!-- confidence:high ✓ -->

• Format placeholder menggunakan angka berurutan tanpa tanda lain ({{1}}, {{2}}, {{3}}, bukan {{1}}, {{2}}, {{4}})
• Placeholder tidak boleh ditempatkan di akhir body message
• Urutan variabel harus konsisten sesuai data yang akan dipetakan
• Tidak ada batasan jumlah variabel, namun disarankan tidak berlebihan
• Konten variabel sebaiknya ringkas untuk menghindari pesan gagal dikirim (khususnya WhatsApp)
• Setiap variabel harus memiliki definisi data yang jelas sebelum kampanye dikirim
• Pesan error "Translation text too long" menunjukkan total karakter melebihi limit

## Related Tasks  <!-- confidence:medium ~ -->

• Bagaimana Cara Mengatur Follow-up Templates — untuk membuat template balasan pesan otomatis dengan variabel
• Sekilas Tentang Template Pacing — untuk memahami evaluasi otomatis Meta terhadap kualitas template campaign sebelum pengiriman
• Pengelolaan dan Penerapan OTP pada New Template Kategori Marketing dan Utility pada Menu Campaign (Broadcast) — untuk menerapkan verifikasi keamanan pada template dengan variabel