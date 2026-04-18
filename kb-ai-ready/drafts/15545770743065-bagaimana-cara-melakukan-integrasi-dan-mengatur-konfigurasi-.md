---
title: Bagaimana Cara Melakukan Integrasi dan Mengatur Konfigurasi Channel pada Qontak
  CRM
canonical_url: https://help-center.qontak.com/hc/id/articles/15545770743065-Bagaimana-Cara-Melakukan-Integrasi-dan-Mengatur-Konfigurasi-Channel-pada-Qontak-CRM
article_type: task
solvability_type: tool
products:
- Qontak CRM
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- multi-channel-integration
- configure-konfigurasi-channel
- conversation-management
query_examples:
- Cara Melakukan Integrasi dan Mengatur Konfigurasi Channel pada Qontak CRM
- Bagaimana cara Melakukan Integrasi dan Mengatur Konfigurasi Channel pada Qontak
  CRM?
- Langkah-langkah Melakukan Integrasi dan Mengatur Konfigurasi Channel pada Qontak
  CRM di Qontak CRM
- How do I Melakukan Integrasi dan Mengatur Konfigurasi Channel pada Qontak CRM?
- Mau Melakukan Integrasi dan Mengatur Konfigurasi Channel pada Qontak CRM, caranya
  gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk melakukan integrasi dan mengatur konfigurasi channel pada Qontak CRM, Anda memerlukan:

- Role **Owner** atau **Admin** pada akun Qontak CRM
- Akun Qontak Omnichannel yang aktif
- Token API Admin dari akun Omnichannel (user Admin tersebut juga harus berperan sebagai owner pada akun CRM)
- Akses ke menu **Properties** pada akun CRM Anda
- Setidaknya satu channel yang sudah dikonfigurasi di Omnichannel (WhatsApp, Instagram, atau channel lainnya)

## Steps  <!-- confidence:high ✓ -->


Melalui **Qontak CRM** , Anda dapat melakukan integrasi Channel pada menu **Properties.** Dalam hal ini, Anda dapat mengintegrasikan Qontak Omnichannel ke Qontak CRM. Selain itu, data pelanggan yang mengirimkan chat di Omnichannel akan otomatis tersimpan pada menu **Kontak** di CRM.

Dengan integrasi tersebut, **CRM** akan secara otomatis membuat **Deal** atau **Tiket** berdasarkan chat yang masuk ke **Omnichannel**. Isi percakapan chat juga dapat terlihat pada timeline **Deal** atau **Tiket** sehingga Anda dapat lebih mudah memahami konteks dari sebuah **Deal** atau **Tiket** tersebut. Sebelumnya, Anda perlu melakukan proses integrasi akun **Omnichannel Qontak** dengan **CRM Qontak** terlebih dahulu. Berikut adalah langkah - langkahnya.

###  **B. Cara Mengatur Konfigurasi Channel**[](https://help-center.qontak.com/hc/id/articles/15545770743065-Bagaimana-Cara-Melakukan-Integrasi-dan-Mengatur-Konfigurasi-Channel-pada-Qontak-CRM#h_01HQ2CY5H8Z0ZMY7Y3RP42537Q)
Setelah menyelesaikan proses integrasi, maka akun CRM Anda sudah berhasil terhubung dengan akun Omnichannel, namun Anda masih perlu menyelesaikan proses konfigurasi. Lanjutkan konfigurasi dengan klik tombol **“Atur konfigurasi”** seperti pada tampilan berikut.  
![4.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36773919924761)  
Lalu Anda akan melihat dua pilihan integrasi dan Anda perlu memilih salah satu di antara pilihan berikut, yaitu:
**A. Integrasikan semua channel ke satu pipeline di modul pilihan  
****![5.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36773912573337)  
**Dengan memilih opsi integrasi ini,**Deal** atau **Tiket** secara otomatis akan terbuat di **1 pipeline.** **Deal** atau **Tiket** ini berasal dari chat yang masuk ke seluruh channel di Omnichannel. Berikut adalah langkah-langkahnya:**  
**
  1. Anda dapat memilih untuk mengintegrasikan seluruh channel Anda ke modul **Deals** saja, **Tiket** saja, ataupun kedua modul.   
![6.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36773919928985)
Apabila Anda hanya ingin melakukan integrasi dengan modul **Tiket** saja, maka Anda tidak perlu mengisi kolom yang terdapat pada bagian modul **Deals**.
  2. Selanjutnya, klik **“Tindakan”** dan pilih **Ubah** untuk melengkapi kolom **CRM module**.  
![7.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36773912573977)
  3. Kemudian, pilihlah jenis **Pipeline** , **New stage** , serta **Won/Closed stage** untuk melengkapi kolom **CRM module** pada modul yang akan terintegrasi.  
![8.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36773912577561)

**B. Atur multi channel ke multi pipeline secara manual  
****![16.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36773912586137)  
** Dengan memilih opsi integrasi ini, Anda dapat menentukan agar  **Deal** atau **Tiket** yang terbuat secara otomatis di CRM hanya berasal dari chanel tertentu di Omnichannel. Selain itu, Anda juga dapat menentukan agar Deal atau Tiket tersebut dapat terbuat di pipeline yang berbeda-beda, sesuai dengan kebutuhan Anda. Berikut adalah langkah-langkahnya:**  
**
  1. Klik **“Tambah konfigurasi”**.  
![17.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36773919946137)

**Penting**  
- **ID Integrasi** dapat diperoleh dengan melakukan login ke **Qontak Omnichannel** terlebih dahulu.  
![ID Integration.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36773912595481)  
- Modul **“Deals”** mungkin namanya telah diubah oleh **Admin** di perusahaan anda (Contoh: _Kunjungan_ , _Ticket_ , _Laporan_ , dll). Pastikan Anda memilih modul yg sesuai dengan menu yg berada di sidebar.
  3. Setelah memilih **Modul CRM** , Anda dapat memilih jenis **Pipeline** , **New stage** , serta **Won/Closed stage**.  
![19.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36773912602521)

- **Deal** atau **Tiket** akan secara otomatis terbuat di **Pipeline** yang Anda pilih.  
- Pada kategori **Pipeline**. Anda dapat memilih jenis **Pipeline** berdasarkan **Feedback** , **Technical** **reports** , serta **User** **claim**.
  4. Klik **Simpan**.  
![23.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36773919979417)
  5. Lalu akan muncul notifikasi berikut. Dalam hal ini, **Deals** atau **Tiket** akan secara otomatis terbuat setiap kali terdapat chat yg masuk ke **channel** yang sudah ditentukan.  
![15.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36773912635417)
Anda dapat menambahkan sampai dengan **30 channel** berbeda sesuai dengan kebutuhan Anda dengan mengulang langkah-langkah berikut dari awal.

## Error States  <!-- confidence:medium ~ -->

Kesalahan umum yang mungkin terjadi:

- **Token API tidak valid**: Pastikan Anda menyalin token API Admin yang benar dari akun Omnichannel. Token harus dari user yang juga berperan sebagai owner pada akun CRM.
- **Koneksi gagal**: Periksa koneksi internet Anda dan pastikan akun Omnichannel dan CRM aktif serta milik organisasi yang sama.
- **Tombol Atur konfigurasi tidak muncul**: Integrasi mungkin belum sepenuhnya berhasil. Coba logout dan login kembali ke akun CRM Anda.
- **Permission denied**: Hanya user dengan role **Owner** atau **Admin** yang dapat mengakses halaman **Channel Integration**. Hubungi administrator akun jika role Anda berbeda.

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support (support-qontak@mekari.com) jika Anda mengalami:

- Token API tidak diterima oleh sistem meski sudah benar.
- Integrasi berhasil tetapi Deal atau Tiket tidak otomatis terbuat dari pesan masuk.
- Tombol atau menu integrasi tidak muncul di akun CRM Anda.
- Data pelanggan tidak tersimpan di menu **Kontak** setelah integrasi.

Sertakan screenshot halaman error, ID akun CRM dan Omnichannel Anda, serta deskripsi masalah yang dialami.