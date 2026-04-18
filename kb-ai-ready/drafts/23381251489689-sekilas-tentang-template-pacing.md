---
title: Sekilas Tentang Template Pacing
canonical_url: https://help-center.qontak.com/hc/id/articles/23381251489689-Sekilas-Tentang-Template-Pacing
article_type: concept
solvability_type: content
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- campaign-management
- marketing-campaign-manage
query_examples:
- Apa itu Template Pacing?
- Apa fungsi Template Pacing di Qontak Omnichannel?
- Penjelasan Template Pacing
- What is Template Pacing?
- Bagaimana cara kerja Template Pacing?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Definition  <!-- confidence:high ✓ -->


### Apa Itu WhatsApp Template Pacing?[](https://help-center.qontak.com/hc/id/articles/23381251489689-Sekilas-Tentang-Template-Pacing#h_01HB7ME3P58Y6TT06ZHC727T1Y)
Template Pacing merupakan proses evaluasi Campaign Message terbaru yang akan diterapkan META (WhatsApp). Template pacing nantinya akan melakukan pengecekan sensitivitas kualitas pesan terhadap penerima Campaign Message, dengan tujuan untuk menghindarkan potensi Nomor WhatsApp Anda terkena Block. Proses ini dilakukan pada Campaign Message kategori Marketing mulai 12 Oktober 2023. Pelajari FAQ seputar Template Pacing di Qontak, [di sini](https://help-center.qontak.com/hc/id/articles/5703349565209-Omnichannel-Frequently-Asked-Questions-FAQs-#h_01HB7N94KF910AK1W09JTB6VK9).
Mekanisme tersebut hanya akan **berdampak terhadap template broadcast kategori** _**Marketing**_ saja. Untuk template kategori _Utility_ dan _Authentication_ tidak akan menerapkan Template Pacing.
Mekanisme template pacing memungkinkan pelanggan memberikan feedback pada template marketing yang dibuat. Nantinya terdapat pesan campaign yang ditahan dan ini memungkinkan pelanggan untuk memberikan feedback. Meta memiliki perhitungan tersendiri untuk menilai campaign mana saja yang akan diterapkan Template Pacing.
### Bagaimana Cara Kerja Fitur Ini?[](https://help-center.qontak.com/hc/id/articles/23381251489689-Sekilas-Tentang-Template-Pacing#h_01HB7ME3P53GGGX7ZEPWRCBHP3)
Template Pacing dirancang khusus untuk kampanye pemasaran skala besar. Untuk campaign yang terpilih dilakukan Template Pacing, Meta akan mengirimkan pesan campaign pada sebagian kecil dari jumlah total penerima campaign tersebut. Berdasarkan “sampel" tersebut, Meta akan memberi penilaian berdasarkan respon-respon penerima dalam hasil akhir; _Template Quality_ status. Berdasarkan penilaian tersebut, Meta akan memutuskan apakah akan melanjutkan pengiriman pesan ke audiens yang lebih besar. 
**Contoh:**
Misalkan terdapat template pemasaran yang ditujukan ke 100,000 penerima. Template Pacing akan dimulai dengan mengirimkan pesan campaign tersebut ke segmen yang lebih kecil (misalnya, 20,000 penerima), lalu sistem Meta akan menunggu selama 30 menit untuk mengevaluasi kualitas template berdasarkan respons 20,000 penerima tersebut. Setelah itu, Meta (WhatsApp) akan memberi penilaian berdasarkan respon dari penerima-penerima campaign tersebut. Jika dinilai _Medium/High Quality_ maka broadcast kepada 80,000 penerima sisanya akan dilanjutkan.
Berikut flow dari Template Pacing.
![Untitled \(1\).png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774918179225)
**Penting**  
1. Template Pacing adalah flow terbaru dari proses broadcast, dan dapat dilihat dalam flowchart di atas yang berwarna kuning.  
2. Template Pacing akan dilakukan dari sistem Meta dan bukan Qontak.  
3. Meta yang akan menentukan apakah campaign (berikut dengan templatenya) akan melalui Template Pacing - tidak semua campaign Marketing akan melalui Template Pacing, WhatsApp (Meta) memiliki perhitungannya sendiri dan tidak di buka untuk umum.  
4. Durasi Template Pacing adalah ~30 menit, namun apabila respons penerima sudah cukup untuk WhatsApp (Meta) melakukan penilaian, tidak menutup kemungkinan hasil keluar lebih cepat.  
5. Status ‘Template Quality’ bersifat dinamis, kualitas dari template dapat berubah kapan saja sesuai dengan respon dari penerima pesan.  
6. Apabila template mendapatkan Template Quality ‘Low’ maka template tersebut akan di ‘Disable’, kami menyarankan untuk mengevaluasi kembali template Anda dan membuat template baru, karena template yang sudah ‘Disabled’ tidak dapat digunakan kembali.
**No.** | **Contoh** | **Category Template** | **Template Status** |  **Template Quality** **(****Baru****)** | **Campaign Status** | **Memenuhi syarat untuk broadcast?**  
---|---|---|---|---|---|---  
1 |  Template: Submitted but Rejected Pacing: None Campaign Broadcast: None | Marketing | Rejected | - | - | No  
2 |  Template: Submitted and Approved Pacing: None Campaign Broadcast: Not yet | Marketing | Approved | Neutral | - | Yes  
3 |  Template: Submitted and Approved Pacing: No Campaign Broadcast: Done | Marketing | Approved | Neutral | Completed | Yes  
4 |  Template: Submitted and Approved Pacing: Yes Campaign Broadcast: Done with High Quality | Marketing | Approved | High Quality | Completed | Yes  
5 |  Template: Submitted and Approved Pacing: Yes Campaign Broadcast: Done with Medium Quality | Marketing | Approved | Medium Quality | Completed | Yes  
7 |  Template: Submitted and Approved Pacing: Yes Campaign Broadcast: Done with Low Quality | Marketing | Disabled | Low Quality | Stopped (WA effect) | No  
### Rangkuman Status-status Baru[](https://help-center.qontak.com/hc/id/articles/23381251489689-Sekilas-Tentang-Template-Pacing#h_01HBAN91812B2MR9V69QF3RJYF)
**1. Definisi Status-status Baru**
**Kategori** | **Status** | **New?** | **Definition**  
---|---|---|---  
Template Status | Disabled | New | Template di non-aktifkan karena mendapatkan penilaian buruk dari WhatsApp (Meta)  
Template Quality (New) | High Quality | New | Kualitas template dinilai minim respon negatif dari penerima pesan  
Template Quality (New) | Medium Quality | New | Kualitas template mendapat respon negatif dari penerima pesan, namun belum mengkhawatirkan  
Template Quality (New) | Low Quality | New | Kualitas template mendapatkan respon negatif yang cukup banyak  
Template Quality (New) | Quality Pending | New | Template belum mendapatkan penilaian kualitas dari WhatsApp  
Campaign Status | Stopped (WA effect) | New | Pesan sudah dalam proses pengiriman namun terhenti sebagian karena terdapat penanganan khusus dari WhatsApp (Meta)  
**2. Halaman Template**![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774918180121) Pada halaman ‘Template message’ terdapat kolom status baru, yaitu kolom ‘Quality’. Kolom ini secara spesifik menggambarkan kualitas template yang kami terima berdasarkan penilaian dari sistem Meta. 
Pada Template Status, kami menambahkan status baru, yaitu ‘Disabled’, di mana status ini ditujukan untuk template yang dinonaktifkan karena melanggar ketentuan Meta atau mendapat penilaian kualitas yang rendah dari Meta (Low quality).
**3. Halaman Campaign**![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774945004185) Pada halaman campaign, kami menambahkan status baru yaitu ‘Stopped (WA effect)’. Status ini ditujukan untuk campaign yang melalui Template Pacing namun tidak memenuhi standar Meta sehingga campaign tersebut dihentikan. Namun, Anda dapat mendapatkan rincian kontak mana saja yang sudah terkirim maupun belum terkirim broadcast melalui, Campaign Detail Page.
**4. Campaign Detail Page![pasted image 0 - 2023-09-27T133154.862.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774918193689)**  
Untuk campaign yang sedang melalui fase/proses Template Pacing, nomor yang terpilih untuk dilakukan _sampling_ akan tertandai status **‘Pending - In review by WhatsApp’**.
Teruntuk campaign yang terhenti karena Template Pacing, Anda dapat mengetahui mana saja nomor penerima yang sudah berhasil terkirim pada fase Template Pacing dan mana saja yang belum terkirim dengan melihat Message Status pada halaman Campaign Detail. Spesifik untuk Template Pacing, nomor penerima yang belum terkirim akan mendapatkan **‘Failed - Template is disabled by WhatsApp. See template details for more information.’**
### Apa yang Harus Saya Lakukan Apabila Template Saya ‘Disabled’?[](https://help-center.qontak.com/hc/id/articles/23381251489689-Sekilas-Tentang-Template-Pacing#h_01HB7ME3P7YEB15NXFGQAD5913)
Template yang mendapatkan Template Quality ‘Low’ akan di non-aktifkan, atau, ‘Disabled’. Template yang di ‘Disabled’ karena mendapat respon buruk dari penerima tidak dapat digunakan kembali, lalu, apa yang harus Anda lakukan?
Meta tidak memberikan kami pedoman khusus untuk template yang dinonaktifkan, namun dapat kami pastikan WhatsApp/Meta hanya bertindak dari respon-respon penerima pesanan. Apabila penerima pesanan melakukan ‘Report’ atau ‘Block’ maka, Meta menganggapnya pesanan tersebut tidak sesuai atau mengganggu mereka. 
Karena itu, kami menghimbau Anda untuk mengevaluasi kembali pesan yang Anda kirimkan kepada kontak-kontak yang sudah anda pilih. Beberapa aspek dapat Anda kaji kembali, contoh; konten pesan, informasi yang disampaikan atau mungkin waktu pengiriman pesan tersebut yang kurang sesuai.
Untuk informasi lebih lengkap terkait peraturan WhatsApp, Anda dapat mengunjungi

## Key Attributes  <!-- confidence:high ✓ -->

• Hanya berlaku untuk template broadcast kategori Marketing
• Template Utility dan Authentication tidak menerapkan Template Pacing
• Durasi evaluasi sekitar 30 menit, dapat lebih cepat jika respons sudah cukup
• Meta mengirimkan pesan ke sampel kecil penerima (contoh: 20.000 dari 100.000 penerima)
• Penilaian didasarkan pada Template Quality status dari respons penerima
• Meta memiliki algoritma tersendiri untuk menentukan campaign mana yang melalui Template Pacing
• Proses dilakukan oleh sistem Meta, bukan Qontak
• Jika dinilai Medium/High Quality, pengiriman ke audiens sisa dilanjutkan

## Related Tasks  <!-- confidence:medium ~ -->

• Bagaimana Cara Mengatur Follow-up Templates
• Pengelolaan dan Penerapan OTP pada New Template Kategori Marketing dan Utility pada Menu Campaign (Broadcast)
• Bagaimana Cara Membuat Recipient List melalui 'Select Contact' secara Langsung