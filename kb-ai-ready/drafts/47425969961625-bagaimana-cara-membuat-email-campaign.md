---
title: Bagaimana Cara Membuat Email Campaign
canonical_url: https://help-center.qontak.com/hc/id/articles/47425969961625-Bagaimana-Cara-Membuat-Email-Campaign
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- email-campaign
- create-email-campaign
- marketing-campaign-manage
query_examples:
- Cara Membuat Email Campaign
- Bagaimana cara Membuat Email Campaign?
- Langkah-langkah Membuat Email Campaign di Qontak Omnichannel
- How do I Membuat Email Campaign?
- Mau Membuat Email Campaign, caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk membuat Email Campaign di Mekari Qontak, Anda harus memenuhi persyaratan berikut:

1. Langganan aktif paket Broadcast, Service Suite, Sales Suite, atau Qontak 360
2. Akses ke akun Omnichannel Mekari Qontak
3. Subdomain dan email pengirim (sender email) sudah terdaftar melalui self-integrate Email Campaign
4. Template konten email sudah dibuat di menu Campaign > Templates > Email
5. Daftar penerima (recipient list) sudah diimpor di menu Campaign > Recipient lists
6. Kuota Email Campaign harian dan bulanan Anda mencukupi untuk jadwal pengiriman

## Steps  <!-- confidence:high ✓ -->


Pada Mekari Qontak, Anda dapat mengelola pengiriman _campaign_ ke target audiens Anda, dari pembuatan desain _template_ , mempersiapkan daftar _recipient_ (penerima email), hingga pengiriman _campaign_.
**Penting**  
- Email Campaign hanya akan muncul pada pengguna yang berlangganan paket terbaru dari Mekari Qontak, yaitu **Broadcast, Service Suite, Sales Suite,** atau **Qontak 360**. Lihat rincian paket tersebut [di sini](https://qontak.com/harga/).  
- Pastikan kuota Email Campaign **harian** dan **bulanan** Anda cukup sebelum jadwal pengiriman Campaign. Pelajari terkait [kuota Email Campaign](https://help-center.qontak.com/hc/id/articles/50305970510745-Sekilas-tentang-Kuota-Harian-Email-Campaign).  
**  
Informasi biaya pengiriman email**  
- Setiap pengiriman email akan dikenakan tarif sebesar **Rp 21** per email. Tagihan dikirimkan pada awal bulan berikutnya antara **tanggal 1-10** sesuai dengan **jumlah kuota email yang terpakai**.  
- Jika nominal tagihan Anda di bawah **Rp 5.000,** maka penagihan akan digabungkan dengan penagihan penggunaan pada periode berikutnya.  
- Email tagihan akan dikirimkan ke alamat email yang terdaftar sebagai PIC penagihan dengan subjek **Sales Invoice #{Nomor Invoice} {Nama Perusahaan Anda}**.
Sebelum mulai mengirimkan _campaign_ , pastikan Anda telah melakukan hal berikut ini:
  1. Mendaftarkan subdomain dan email yang akan digunakan sebagai **email pengirim/****_sender email_**. Jika belum, silakan ikuti panduan [cara self integrate Email Campaign](https://help-center.qontak.com/hc/id/articles/50335729699225-Bagaimana-Cara-Melakukan-Self-Integrate-Email-Campaign) ini.
  2. [Membuat template konten email yang ingin dikirimkan. ](https://help-center.qontak.com/hc/id/articles/47426448666521-Bagaimana-Cara-Membuat-Template-untuk-Email-Campaign)_Template_ dapat Anda ubah dan buat baru ketika membuat pengiriman _campaign_.
  3. [Mengimpor daftar penerima email campaign / recipient lists.](https://help-center.qontak.com/hc/id/articles/47426266423065-Bagaimana-Cara-Membuat-Recipient-List-untuk-Email-Campaign) Kenali dan pastikan Anda memasukan daftar _recipient_ dengan alamat email yang _valid_.

**Nama Fitur** | **Penjelasan**  
---|---  
Email subject | Judul atau subjek email.  
Email sender |  Otomatis terisi dengan email yang telah terintegrasi.  Jika integrasi email telah Anda hapus, kolom ini akan kosong dan Anda tidak dapat melanjutkan pengiriman email.  
Sender name |  Nama pengirim email. **Sender name** akan otomatis terisi sesuai dengan yang Anda daftarkan pada halaman[ Integrasi Email Campaign](https://chat.qontak.com/integrations/email/campaign/sender).  Anda dapat mengubah **Sender name** sesuai kebutuhan ketika mengirimkan _campaign_.  
Recipient list |  Pilih data _recipient lists_ yang ingin Anda targetkan untuk pengiriman _campaign_. Anda tidak dapat melanjutkan ke tahap berikutnya jika **jumlah**** _recipient_** lebih besar dari **sisa kuota harian.** Pelajari terkait kuota harian dan bulanan Email Campaign [di sini.](https://help-center.qontak.com/hc/id/articles/50305970510745-Sekilas-tentang-Kuota-Harian-Email-Campaign)  
  5. Selanjutnya pada tahap **Template** , pilih _template_ yang sebelumnya telah Anda buat pada menu **Template** , atau Anda dapat klik **“Create new”** untuk membuat _template_ baru.![rev.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F47426113314073)

Perubahan yang Anda lakukan di sini tidak akan mengubah konten _template_ yang asli.
  11. Lalu Anda akan diarahkan ke tahapan **Additional setup**. Pada tahapan ini, Anda dapat klik **“Send test email”** untuk melakukan simulasi pengiriman email sebelum email tersebut dikirimkan ke _client_ Anda. Email simulasi akan dikirimkan otomatis ke alamat email Anda dengan email pengirim . Pengiriman simulasi email tidak memotong kuota harian maupun bulanan Anda.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52283953214361)
  12. Selain itu, Anda juga dapat menyimpan _template_ yang telah **diubah** dan/atau **dibuat** pada tahap sebelumnya dengan klik **“Save template”**. Apabila email telah siap untuk dikirimkan, maka klik **“Send campaign”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52283953215257)
  13. Maka Email Campaign yang telah dibuat dan sedang dikirimkan akan muncul pada halaman utama **Email** dengan status **‘Sending’**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52283982578841)
  14. Untuk dapat melihat detail aktivitas Email Campaign yang telah dikirimkan, Anda dapat klik **“Actions”** , lalu pilih **“View details”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F47425969958553)
  15. Pada halaman ini, Anda dapat memantau **Campaign performance** dan **Campaign logs**. Di bagian **Campaign performance** , Anda dapat memantau **jumlah penerima** , **Delivery rate** , **Open rate** , dan **Bounce rate**. Lalu pada bagian **Campaign logs** , Anda dapat melihat Email Campaign yang telah dikirimkan ke **Recipient list** terkait.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F47425950955929)
  16. Anda juga dapat melakukan filter status lalu klik **“Export”** untuk mengunduh daftar _campaign logs_ ke format file **.csv** sesuai status pengiriman email yang difilter.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52283982579609)

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Mekari Qontak jika mengalami:

1. Email subject, Sender name, atau Recipient list tidak bisa disimpan setelah klik Continue
2. Sistem menampilkan pesan error yang tidak jelas
3. Tombol Create campaign tidak responsif atau tidak berfungsi
4. Kuota Email Campaign tidak terupdate dengan benar

Siapkan informasi berikut saat menghubungi support:
- Screenshot error message
- ID akun Omnichannel Anda
- Waktu kejadian error
- Jumlah recipient yang akan dikirimkan