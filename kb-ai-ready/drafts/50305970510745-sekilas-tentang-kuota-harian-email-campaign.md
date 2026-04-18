---
title: Sekilas tentang Kuota Harian Email Campaign
canonical_url: https://help-center.qontak.com/hc/id/articles/50305970510745-Sekilas-tentang-Kuota-Harian-Email-Campaign
article_type: concept
solvability_type: content
products:
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- email-campaign
- marketing-campaign-manage
query_examples:
- Apa itu Kuota Harian Email Campaign?
- Apa fungsi Kuota Harian Email Campaign di Qontak Omnichannel?
- Penjelasan Kuota Harian Email Campaign
- What is Kuota Harian Email Campaign?
- Bagaimana cara kerja Kuota Harian Email Campaign?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Definition  <!-- confidence:high ✓ -->


Mulai tanggal**15 September 2025,** penerapan **Kuota Harian** untuk pengiriman Email campaign akan efektif berlaku.
Tujuan dari penerapan limit harian adalah untuk membantu Anda dalam menjaga kualitas pengiriman email dengan memulai dari jumlah yang lebih kecil. Hal ini penting dikarenakan **subdomain** dan **email sender** yang dipakai pada Email campaign adalah email baru yang didaftarkan ketika proses integrasi dengan Qontak.
**Mengapa Pengiriman Email dari Subdomain Baru Harus Dimulai dengan Jumlah Kecil?**
Penggunaan **subdomain baru** untuk pengiriman email tidak disarankan langsung dilakukan dalam jumlah besar. Hal ini dikarenakan penyedia layanan email (seperti Gmail, Yahoo, dan Outlook) menerapkan sistem penyaringan _spam_ yang ketat. 
Jika sebuah subdomain baru mengirimkan email dalam volume tinggi **tanpa memiliki reputasi pengiriman** , terdapat risiko besar email akan ditandai sebagai _spam_ , ditolak, atau bahkan menyebabkan subdomain masuk ke dalam daftar _blacklist_.
Oleh karena itu, praktik yang direkomendasikan adalah melakukan pemanasan subdomain _(domain warm-up)_ dengan cara meningkatkan volume pengiriman email secara bertahap.
**Alasan utama perlunya peningkatan bertahap:**
  1. **Membangun reputasi pengiriman.**  
Volume pengiriman kecil dan konsisten membantu penyedia layanan email menilai subdomain sebagai pengirim yang sah dan terpercaya.

### A. Perbedaan Utama Sebelum dan Sesudah Pemberlakuan Kuota Harian [](https://help-center.qontak.com/hc/id/articles/50305970510745-Sekilas-tentang-Kuota-Harian-Email-Campaign#h_01K4W4RTZ8PHVKKNM99922BDGE)
Berikut ringkasan perbedaan informasi kuota sebelum dan sesudah pemberlakuan kuota harian di Qontak.
| **Sebelum** | **Sesudah**  
---|---|---  
Tampilan | ![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50608378976921) | ![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50608378978585)  
Kuota bulanan |  Menampilkan **sisa kuota** yang dapat Anda gunakan pada **bulan berjalan.**   
Kuota akan diperbarui kembali setiap **tanggal 1 awal bulan berikutnya** , dengan skema pembayaran _**postpaid**_ berdasarkan tagihan dari tim _billing_ Qontak. |  Menampilkan **total kuota terpakai** dan **kuota dasar bulanan.**   
Misalnya, tampilan 8/80 berarti 8 kuota telah digunakan dari total 80 kuota bulanan yang tersedia.   
Jadwal pembaruan kuota dan sistem penagihan tetap sama dengan kondisi sebelumnya.  
Kuota harian | Tidak tersedia. |  Menampilkan**sisa kuota harian** yang dapat digunakan pada**hari yang sama.**   
Kuota akan diperbarui kembali setiap hari pada pukul **07.00 pagi (WIB)**.  
**Penting**  
- Setiap pengiriman email akan dikenakan tarif sebesar **Rp 21** per email. Tagihan dikirimkan pada awal bulan berikutnya antara **tanggal 1-10** sesuai dengan **jumlah kuota email yang terpakai**.  
- Jika nominal tagihan Anda di bawah **Rp 5.000,** maka penagihan akan digabungkan dengan penagihan penggunaan pada periode berikutnya.  
- Email tagihan akan dikirimkan ke alamat email yang terdaftar sebagai PIC penagihan, dengan subjek **Sales Invoice #{Nomor Invoice} {Nama Perusahaan Anda}**.  
- Pengajuan terkait kenaikan _**top up**_ kuota harian maupun bulanan tidak dikenakan biaya. Biaya tersebut hanya dikenakan sesuai **jumlah kuota Email campaign yang dipakai**.

### B. Cara Melihat Kuota Harian dan Bulanan Email Campaign[](https://help-center.qontak.com/hc/id/articles/50305970510745-Sekilas-tentang-Kuota-Harian-Email-Campaign#h_01K4W4RCCHBMMQ0VSD6XPNEV6E)
Setiap akun akan mendapatkan _default_ kuota harian sebanyak **4.000 email** , dengan kuota bulanan sebanyak **10.000 email**.
Dampak dari pemberlakukan kuota harian adalah sebagai berikut. 
  1. Jika Anda memiliki kuota harian **4.000** dan bulanan **10.000** , maka Anda hanya dapat mengirimkan email ke maksimal **4.000 recipients** pada hari yang sama. 
  2. Jika sisa kuota bulanan**lebih kecil dari pada kuota harian** (misalnya tersisa **1.000**), dan Anda belum mengirimkan email sama sekali pada hari berjalan, maka Anda hanya dapat mengirimkan email ke maksimal **1.000 recipients** pada hari tersebut.

**Penting**  
Kuota harian Anda **akan diturunkan** jika performa dari pengiriman email Anda buruk. Hal ini dapat terjadi jika email Anda banyak ditandai sebagai _spam_ dan/atau dilaporkan oleh email penerima. Harap _review_ kembali strategi pengiriman _campaign_ Anda dan tinjau ulang daftar penerima sebelum melanjutkan pengiriman _campaign_ selanjutnya. 
Jika ada peningkatan performa dalam status pengiriman email, Anda dapat melakukan pengajuan kenaikan limit melalui prosedur [di bawah ini](https://help-center.qontak.com/hc/id/articles/50305970510745-Sekilas-tentang-Kuota-Harian-Email-Campaign#h_01K4W4RCCHB9AMD9FE6VRZR6XE).
Anda dapat melihat informasi **kuota harian** dan **bulanan** email campaign pada halaman pembuatan **Campaign**. Pelajari lebih lanjut tentang [cara membuat Email Campaign](https://help-center.qontak.com/hc/id/articles/47425969961625-Bagaimana-Cara-Membuat-Email-Campaign).  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50608378980121)
Pada halaman pembuatan _campaign_ , Anda akan melihat informasi seperti di bawah ini.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50608393304089)
No. | Nama Fitur | Penjelasan  
---|---|---  
1 | Remaining daily email quota |  Menampilkan sisa **kuota** **harian** Email Campaign yang dapat digunakan pada hari yang sama.

**Penting**  
Anda dapat mengirimkan _campaign_ selama jumlah _recipient list_**tidak melebihi** sisa kuota harian. ![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50608393305241) Jika jumlah _recipient list_**melebihi** sisa kuota harian, Anda akan melihat pesan _error_ di bawah ini dan tidak dapat melanjutkan proses pengiriman _campaign_.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50608393307801)  
2 | Monthly email usage |  Menampilkan jumlah kuota Email Campaign yang telah digunakan dan akan ditagihkan setiap bulannya.   
Berikut daftar **status Email Campaign** yang akan memotong kuota email:  
**a. Pending** : pesan email telah masuk ke mail server Qontak.   
**b. Delivered** : pesan email telah diterima ke _mail server_ penerima.  
**c. Open** : pesan email telah dibuka oleh penerima.  
**Note:**  
pesan email yang masuk ke _spam_ tidak dapat terdeteksi sebagai status **‘** _**open**_**’** karena _tracker_ biasanya di-_block_ oleh _mail server_ penerima.  
**d. Bounced** : pesan email gagal diterima, misalnya karena email tidak ditemukan.  
3 | Top up quota |  Anda dapat klik **“Top up quota”** untuk diarahkan ke _channel_**WhatsApp Support Qontak** untuk pengajuan kenaikan limit kuota harian maupun bulanan.    
Anda juga dapat mengirimkan _request_ melalui email ke [di bawah ini](https://help-center.qontak.com/hc/id/articles/50305970510745-Sekilas-tentang-Kuota-Harian-Email-Campaign#h_01K4W4RCCHB9AMD9FE6VRZR6XE).  
### C. Cara Mengajukan Top up kuota untuk Email Campaign[](https://help-center.qontak.com/hc/id/articles/50305970510745-Sekilas-tentang-Kuota-Harian-Email-Campaign#h_01K4W4RCCHB9AMD9FE6VRZR6XE)
Anda dapat melakukan pengajuan penambahan kuota harian dan bulanan melalui **2x24 jam.** Penyesuaian kuota akan berlaku untuk periode berikutnya.
**Penting!**  
Sebelum melakukan pengajuan _top up_ kuota, Anda diimbau untuk memastikan beberapa hal di bawah ini:   
1. Pastikan Anda tidak memiliki banyak riwayat pengiriman email yang ditandai sebagai _spam_ dan/atau dilaporkan oleh penerima, atau Anda tidak diturunkan kuota harian oleh Qontak dalam kurun waktu minimal **1 bulan sebelumnya.**   
2. Sisa kuota telah mencapai **5%** dari kuota dasar **harian/bulanan** Anda.  
**Contoh:** Jika kuota bulanan Anda sebanyak **10.000 email** , maka Anda dapat melakukan pengajuan ketika kuota bulanan Anda tersisa **500 email.** Namun, hal ini dapat dinegosiasikan tergantung kebutuhan yang Anda lampirkan ketika melakukan pengajuan ke tim Qontak.   
3. Rencanakan pengiriman _campaign_ Anda dalam bulan berjalan agar pengajuan tidak perlu dilakukan berulang. Pengajuan penambahan kuota maksimal dapat dilakukan**2 kali** dalam **1 bulan yang sama**.
Pengajuan dapat **ditolak** dengan pertimbangan:
1. Reputasi email pengirim yang buruk.  
2. Sisa kuota email dengan kebutuhan dalam hari/bulan berjalan masih dapat terpenuhi tanpa perlu peningkatan kuota harian maupun bulanan.
Berikut contoh _template_ pengajuan penambahan kuota yang dapat Anda gunakan sebagai referensi.
**To:**

- Tipe kuota yang diajukan: **Monthly/Daily**.  
- Email pengirim: masukan alamat email pengirim yang digunakan pada email campaign  
- Sisa kuota isi sisa kuota harian/bulanan per tanggal pengajuan. Informasi ini dapat Anda cek melalui halaman [**Create Campaign**](https://help-center.qontak.com/hc/id/articles/47425969961625-Bagaimana-Cara-Membuat-Email-Campaign).  
- Tambahan kuota yang dibutuhkan: isi jumlah kuota yang ingin ditambahkan   
- Alasan penambahan kuota: lampirkan penjelasan perencanaan campaign Anda sebagai bahan pertimbangan kenaikan kuota  
---  
Jika Anda membutuhkan kenaikan **kuota harian** dan **bulanan** sekaligus, Anda dapat menggabungkan pengajuan dalam **1 email yang sama**. Namun, mohon dipastikan untuk merincikan kebutuhan masing-masing tipe kuota.

## Key Attributes  <!-- confidence:high ✓ -->

• Berlaku efektif: 15 September 2025
• Tarif: Rp 21 per email yang dikirimkan
• Penagihan: Awal bulan berikutnya (tanggal 1-10) berdasarkan kuota email terpakai
• Pembayaran minimum: Jika tagihan di bawah Rp 5.000, akan digabung dengan periode berikutnya
• Email tagihan dikirim ke alamat PIC penagihan dengan subjek Sales Invoice
• Pengajuan kenaikan kuota harian/bulanan tidak dikenakan biaya tambahan
• Mekanisme: Pemanasan subdomain (domain warm-up) dengan peningkatan volume bertahap

## Related Tasks  <!-- confidence:medium ~ -->

• Bagaimana Cara Membuat Email Campaign
• Bagaimana Cara Membuat Recipient List untuk Email Campaign
• Bagaimana Cara Membuat Template untuk Email Campaign
• Cara melakukan pengajuan peningkatan kuota email (untuk informasi detail tentang proses kenaikan kuota)