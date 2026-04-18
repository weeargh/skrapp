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


Pada Mekari Qontak, Anda dapat mengirimkan _campaign_ melalui 2 (dua) jenis media, yaitu:  
1. WhatsApp (WABA)
2. Email _(No-reply address)_
Sebelum menggunakan fitur campaign, pastikan integrasi _channel_ telah dilakukan.  
[Pelajari cara melakukan integrasi ke WhatsApp API](https://help-center.qontak.com/hc/id/articles/12055228468633-Bagaimana-Cara-Mengintegrasikan-Qontak-dengan-WhatsApp-API)  
[Pelajari cara melakukan integrasi ke Email ](https://help-center.qontak.com/hc/id/articles/50335729699225-Bagaimana-Cara-Melakukan-Self-Integrate-Email-Campaign)
Mekari Qontak menyediakan fitur **Variabel** untuk membuat konten template lebih interaktif dan personal. Variabel memungkinkan Anda menampilkan data yang berbeda untuk setiap penerima, seperti:
  * Nama pelanggan
  * Nomor invoice
  * Tanggal jatuh tempo
  * Nominal tagihan
  * Rekomendasi nama produk atau jasa
  * Jadwal booking
  * Kode voucher
  * Informasi spesifik lainnya

Contoh penggunaan pada template WhatsApp atau Email:
Halo {{1}}, 
Kami menginformasikan bahwa pesanan dengan nomor {{2}} sedang dalam proses pengiriman dan akan tiba sebelum {{3}} di alamat yang telah Anda daftarkan. 
Silakan lakukan konfirmasi pembayaran sebesar {{4}} melalui metode yang tersedia agar pesanan dapat segera diproses oleh tim kami.
**Keterangan:**
  * {{1}} = Nama pelanggan
  * {{2}} = Nomor pesanan
  * {{3}} = Estimasi tanggal pengiriman
  * {{4}} = Nominal pembayaran

**Penting**  
Qontak tidak membatasi jumlah variabel dalam satu template. Namun, untuk media WhatsApp (WABA), Anda disarankan agar **jumlah variabel tidak berlebihan** dan **isi variabel tidak terlalu panjang** untuk mengurangi risiko pesan gagal dikirim akibat text terlalu panjang**.** Hal ini dapat Anda lihat melalui pesan error: “Translation text too long” pada halaman _**Campaign Logs**_.

Gunakan variabel seperlunya dan utamakan kejelasan informasi untuk performa _campaign_ yang lebih optimal.
###  2. Memetakan Kolom Header Data Recipient ke Variable Template[](https://help-center.qontak.com/hc/id/articles/54928838790809-Sekilas-tentang-Variabel-Template-Campaign#h_01KN45WDTHT71MCMPFQGVBKWVB)
Anda dapat memetakan variabel pada proses **pembuatan campaign.** Opsi **variabel mapping** akan muncul jika Anda memilih template yang memiliki variabel. Lalu, Anda dapat memilih kolom header pada _**recipient lists**_ yang telah Anda pilih untuk dipetakan ke masing-masing variabel.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56554820108313)
Saat campaign dikirim, sistem akan secara otomatis menggantikan setiap variabel dengan data yang tersedia pada **recipient list** , berdasarkan kolom yang telah Anda petakan untuk masing-masing variabel.

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