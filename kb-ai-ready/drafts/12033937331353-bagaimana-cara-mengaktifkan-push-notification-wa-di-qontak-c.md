---
title: Bagaimana Cara Mengaktifkan Push Notification WA di Qontak CRM
canonical_url: https://help-center.qontak.com/hc/id/articles/12033937331353-Bagaimana-Cara-Mengaktifkan-Push-Notification-WA-di-Qontak-CRM
article_type: task
solvability_type: tool
products:
- Qontak CRM
- Qontak Omnichannel
- Qontak Chat
product_surface: mobile
language: id
intent_tags:
- goal-setting-performance-tracking
- enable-push-notification-wa
- sales-management
query_examples:
- Cara Mengaktifkan Push Notification WA di Qontak CRM
- Bagaimana cara Mengaktifkan Push Notification WA di Qontak CRM?
- Langkah-langkah Mengaktifkan Push Notification WA di Qontak CRM di Qontak CRM
- How do I Mengaktifkan Push Notification WA di Qontak CRM?
- Mau Mengaktifkan Push Notification WA di Qontak CRM, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Sebelum mengaktifkan push notification WhatsApp di Qontak CRM, pastikan Anda memiliki:

1. **Akun Chat Panel** dengan akses broadcast yang sudah terdaftar
2. **Saldo MCC (Mekari Credit Center)** tersedia untuk melakukan broadcast
3. **Nomor pengirim WhatsApp** yang telah disetujui oleh WhatsApp
4. **Template pesan** yang telah disetujui oleh WhatsApp
5. **Nomor tujuan penerima** dengan format lengkap kode negara (contoh: +62)
6. **API Token Chat Panel** untuk menghubungkan akun ke CRM
7. Akses ke menu **Properties** di Qontak CRM

## Steps  <!-- confidence:high ✓ -->


Pada Qontak CRM, Anda bisa mengaktifkan**push notification** untuk mendapatkan notifikasi di Whatsapp. Pada fitur ini, Anda bisa mengirimkan pesan otomatis dengan _trigger_ dari CRM seperti **deal date** , **deal creation** , **deal moving** , **idle deal** atau **birthday**. Berikut langkah-langkahnya.
**Penting**  
Untuk mengaktifkan fitur ini, ada beberapa yang harus Anda perhatikan seperti:  
1. Harus memiliki **Akun Chat Panel** yang memiliki akses untuk melakukan broadcast.  
2. Harus memiliki**saldo MCC** yang tersedia untuk melakukan broadcast.  
3. Pengirim WhatsApp harus disetujui oleh WhatsApp.  
4. Pesan template harus disetujui oleh WhatsApp.  
5. Nomor tujuan harus diawali dengan kode negara.
Sebelumnya Anda dapat mempelajari tentang:  
[**[Fitur] Aplikasi CRM Mekari Qontak untuk Tingkatkan Performa Bisnis 75%**](https://qontak.com/fitur/aplikasi-crm/?utm_source=ecosystem&utm_medium=qontak+%28help+center%29)
###  A. Cara Mendaftarkan akun Chat Panel ke CRM[](https://help-center.qontak.com/hc/id/articles/12033937331353-Bagaimana-Cara-Mengaktifkan-Push-Notification-WA-di-Qontak-CRM#h_01HEQ23D3X6W2VPNYTM31ZPFTQ)
  1. Masuk ke menu **Properties** lalu pilih **WhatsApp Notification.  
**
  2. Lalu klik tombol **“Create push notification”.  
****![1.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50564561987993)**
  3. Kemudian Anda akan diarahkan ke halaman berikut. Isikan **Omnichannel API token** seperti yang terlihat pada gambar berikut.  
![1.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780203075609)

###  B. Cara Membuat Push Notification [](https://help-center.qontak.com/hc/id/articles/12033937331353-Bagaimana-Cara-Mengaktifkan-Push-Notification-WA-di-Qontak-CRM#h_01HEQ23D3YQSK2VX1NCYF9C706)
  1. Klik tombol **“Create push notification”**.  
![Image_004.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780194340761)

1. a. **Feature Name** : **Deal****  
****![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52108728697241)**
**No** | **Nama Fitur** | **Penjelasan**  
---|---|---  
1 | **Feature: Deal** | Menampilkan jenis **_Feature_** yang sedang dipilih. Pada contoh gambar di atas, jenis **_Feature_** yang dipilih adalah **Deal**.  
2 | **Pipeline** | Menampilkan pilihan **Pipeline** yang tersedia. Pelajari [di sini](https://help-center.qontak.com/hc/id/articles/42009600870169-Bagaimana-Cara-Membuat-Pipeline-Deal-Baru-pada-Qontak-CRM) lebih lanjut terkait cara membuat **Deals Pipeline**.  
3 | **Trigger** |  Menentukan **kapan notifikasi akan dikirim** , berdasarkan kondisi tertentu pada _Feature_ (contoh pada gambar adalah _Deal_).

Terdapat dua jenis _trigger_ yang bisa digunakan  a. **By action** : notifikasi dikirim **berdasarkan tindakan atau aktivitas tertentu** , misalnya ketika _Deal_ baru dibuat (_Deal is created_) atau berpindah tahap. Pada tipe **By action** , notifikasi akan dikirim ketika terjadi suatu aktivitas atau perubahan status pada _Feature_ yang dipilih.  
Beberapa contoh _action trigger_ yang tersedia antara lain:  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52108728699417)
     * **Deal is created** : notifikasi dikirim saat _Deal_ baru dibuat.
     * **Deal is on stage** : notifikasi dikirim ketika _Deal_ berpindah ke tahap tertentu dalam _pipeline_.
     * **Deal is inactive for** : notifikasi dikirim jika _Deal_ tidak mengalami aktivitas selama jangka waktu tertentu.
- Jika pengguna memilih **Deal is on stage** pada bagian _Trigger_ , maka akan muncul kolom tambahan bernama **Stage**. Kolom ini digunakan untuk menentukan **tahap tertentu dalam Pipeline** yang akan menjadi pemicu pengiriman notifikasi.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52108739156505)  
- **Stage** : digunakan untuk menentukan tahap tertentu di Pipeline yang ingin dipantau tingkat aktivitasnya.  
- **Inactive duration** : digunakan untuk menentukan berapa lama _Deal_ tidak aktif (dalam hitungan hari) sebelum notifikasi dikirim. Contohnya, jika dipilih _Stage: Qualified_ dan _Inactive duration: 7 days_ , maka _push notification_ akan dikirim **jika Deal di tahap Qualified tidak mengalami aktivitas selama 7 hari berturut-turut**. **  
**b.**By date** : notifikasi dikirim **berdasarkan tanggal yang terhubung dengan data tertentu** , misalnya sehari sebelum tanggal _closing deal_ atau pada tanggal jatuh tempo.  
Beberapa contoh _trigger_ by date yang tersedia antara lain:  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52108739156633) Anda dapat melakukan penyesuaian (_custom_) pada seluruh _trigger_ yang memiliki tipe data **Date** atau memilih _trigger_ yang telah disediakan oleh sistem. **  
****  
** - **Deal Expected Close / Order** : notifikasi dikirim pada atau sebelum tanggal perkiraan _deal close/order_. **- Deal Expire Date** : notifikasi dikirim saat mendekati tanggal kadaluarsa _deal_.  
- **Deal Start Date** : notifikasi dikirim pada tanggal mulai _deal_. ![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52108728706201)

Jika pengguna memilih **By date** pada bagian _Trigger_ , maka setelah menentukan jenis tanggal acuan (misalnya **Deal Expected Close / Order**), akan muncul kolom tambahan **Send notification at (hours)**. Kolom ini berfungsi untuk menentukan **waktu pengiriman notifikasi** berdasarkan jam tertentu pada tanggal yang sudah dipilih.

` b. **Feature Name: Ticket**
**![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52108728707609)**
**No** | **Nama Fitur** | **Penjelasan**  
---|---|---  
1 | **Feature: Ticket** | Menampilkan jenis **_Feature_** yang sedang dipilih. Pada contoh gambar di atas, jenis **_Feature_** yang dipilih adalah **Ticket**.  
2 | **Pipeline** | Menampilkan pilihan **Pipeline** yang tersedia.   
3 | **Trigger** |  a. **By action** : notifikasi dikirim **berdasarkan tindakan atau aktivitas tertentu** , misalnya ketika _Ticket_ baru dibuat (_Ticket is created_) atau berpindah tahap. Pada tipe **By action** , notifikasi akan dikirim ketika terjadi suatu aktivitas atau perubahan status pada _Feature_ yang dipilih.  
Beberapa contoh _action trigger_ yang tersedia antara lain:  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52108728707865)
     * **Ticket is created** : notifikasi dikirim saat _Ticket_ baru dibuat.
     * **Ticket is on stage** : notifikasi dikirim ketika _Ticket_ berpindah ke tahap tertentu dalam _pipeline_.
     * **Ticket is inactive for** : notifikasi dikirim jika _Ticket_ tidak mengalami aktivitas selama jangka waktu tertentu.
- Jika pengguna memilih **Ticket is on stage** pada bagian _Trigger_ , maka akan muncul kolom tambahan bernama **Stage**. Kolom ini digunakan untuk menentukan **tahap tertentu dalam Pipeline** yang akan menjadi pemicu pengiriman notifikasi.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52108728709529)   
- **Stage** : digunakan untuk menentukan tahap tertentu di Pipeline yang ingin dipantau tingkat aktivitasnya.  
- **Inactive duration** : digunakan untuk menentukan berapa lama _Ticket_ tidak aktif (dalam hitungan hari) sebelum notifikasi dikirim.

Contohnya, jika dipilih _Stage: Assigned_ dan _Inactive duration: 7 days_ , maka _push notification_ akan dikirim **jika Ticket di tahap Assigned tidak mengalami aktivitas selama 7 hari berturut-turut**. **  
**b.**By date** : notifikasi dikirim **berdasarkan tanggal yang terhubung dengan data tertentu** , misalnya sehari sebelum tanggal _closing ticket_ atau pada tanggal jatuh tempo.  
Beberapa contoh _trigger_ by date yang tersedia antara lain:  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52108728710681) Anda dapat melakukan penyesuaian (_custom_) pada seluruh _trigger_ yang memiliki tipe data **Date** atau memilih _trigger_ yang telah disediakan oleh sistem.**  
****  
****Ticket Due Date** : Artinya, sistem akan mengirimkan _push notification_ **pada waktu yang ditentukan** (melalui kolom _Send notification at (hours)_) untuk mengingatkan bahwa tiket akan segera jatuh tempo, atau sudah mencapai tanggal jatuh tempo. ![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52108739164313)

Jika pengguna memilih **By date** pada bagian _Trigger_ , maka setelah menentukan jenis tanggal acuan (misalnya **Ticket Due Date**), akan muncul kolom tambahan **Send notification at (hours)**. Kolom ini berfungsi untuk menentukan **waktu pengiriman notifikasi** berdasarkan jam tertentu pada tanggal yang sudah dipilih.  
**  
**c.**Feature Name: Contact****  
****![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52108739165977)**
**No** | **Nama Fitur** | **Penjelasan**  
---|---|---  
1 | **Feature: Contact** | Menampilkan jenis **_Feature_** yang sedang dipilih. Pada contoh gambar di atas, jenis **_Feature_** yang dipilih adalah **Contact**.  
2 | **Trigger** |  **By date** : notifikasi dikirim **berdasarkan tanggal yang terhubung dengan data tertentu**. Beberapa contoh _trigger_ by date yang tersedia antara lain:  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52108728713753) Anda dapat melakukan penyesuaian (_custom_) pada seluruh _trigger_ yang memiliki tipe data **Date** atau memilih _trigger_ yang telah disediakan oleh sistem.**

** - **Contact Date Of Birth** : notifikasi dikirim berdasarkan **tanggal lahir kontak** , misalnya untuk mengirim ucapan ulang tahun atau promo khusus.  
- **Contact Tanggal** : notifikasi dikirim berdasarkan **tanggal khusus lain yang disimpan di field “Tanggal”** pada data kontak, misalnya tanggal bergabung, tanggal _reminder follow-u_ p, dan sebagainya. ![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52108739170457)

Jika pengguna memilih **By date** pada bagian _Trigger_ , maka setelah menentukan jenis tanggal acuan (misalnya **Contact Date Of Birth**), akan muncul kolom tambahan **Send notification at (hours)**. Kolom ini berfungsi untuk menentukan **waktu pengiriman notifikasi** berdasarkan jam tertentu pada tanggal yang sudah dipilih.  
**  
**d.**Feature Name** : **Company****  
**
**No** | **Nama Fitur** | **Penjelasan**  
---|---|---  
1 | **Feature: Contact** | Menampilkan jenis **_Feature_** yang sedang dipilih. Pada contoh gambar di atas, jenis **_Feature_** yang dipilih adalah **Company**.  
2 | **Trigger** |  **By date** : notifikasi dikirim **berdasarkan tanggal yang terhubung dengan data tertentu**.

Anda dapat melakukan penyesuaian (_custom_) pada seluruh _trigger_ yang memiliki tipe data Date atau memilih _trigger_ yang telah disediakan oleh sistem.****  
**  
** Jika pengguna memilih By date pada bagian _Trigger_ , maka setelah menentukan jenis tanggal acuan, akan muncul kolom tambahan Send notification at (hours). Kolom ini berfungsi untuk menentukan **waktu pengiriman notifikasi** berdasarkan jam tertentu pada tanggal yang sudah dipilih.  
  5. Klik **“Continue”** untuk melanjutkan.  
![mceclip1.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780194356633)

Adapun _format file_ dan _maximum size_ sebagai berikut:  
- **Image** : .jpg, .jpeg, .png, dengan maksimum size 20 mb.  
- **Video** : .mp4, .avi dengan maksimum size 50 mb.  
- **Dokumen** : .pdf dengan maksimum size 10 mb.
  9. _Preview_ dari _template_ pesan akan dimunculkan seperti berikut.  
![Image_019.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780194346649)
  10. Pada _template_ di atas terdapat variabel yang dalam hal ini, Anda dapat menentukan isi _template_ tersebut dengan memilihnya di bagian **Variable mapping**. Tentukan variablenya pada bagian **Select mapping feature** dan **Field**.**  
![1.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F40188290246297)  
**
  11. Kemudian terdapat kolom **Dynamic Link**. Kolom ini hanya terdapat pada _template_ yang berisikan variable dynamic URL dan memungkinkan Anda untuk membuat URL yang dapat disesuaikan secara dinamis berdasarkan modul dan _field_ yang dipilih. Anda dapat memilih **modul**(contoh: **Deal** dan **Associated Ticket**) dan _field_ (contoh: **Name** dan **ID**) yang akan secara otomatis membentuk URL.  
![2.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F40188290251033)

Berikut contoh alur penerapan **Dynamic Link** :  
Seorang pengguna Qontak CRM mengatur **Dynamic Link** untuk mengirim template pesan yang disertai URL agar pelanggan mereka dapat dengan mudah mengakses URL untuk memantau status pesanan.  
Pengguna akan memilih Modul **"Associated Ticket"** dan Kolom **"Ticket ID"**. Kemudian sistem akan secara otomatis membuat template URL seperti ini: 
  12. Pilih penerima pesan pada bagian **WhatsApp sender**.  
![mceclip2.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780194358297)

Nomor yang muncul merupakan nomor Whatsapp yang disetujui oleh WhatsApp dari Chat Panel berdasarkan akun yang terdaftar.
  13. Tentukan penerima dengan memilih pada kolom **Recipient field** , pilih fitur dan kolom yang Anda inginkan pada bagian **Feature** dan **Field**.  
![Image_022.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780194348697)

## Escalation  <!-- confidence:medium ~ -->

Hubungi **Qontak Support** jika Anda mengalami:

1. **API Token tetap error** setelah refresh halaman dan generate ulang token
2. **Saldo MCC hilang** atau tidak tersimpan dengan benar
3. **Template WhatsApp ditolak tanpa alasan jelas** — siapkan screenshot template dan pesan error dari WhatsApp
4. **Push notification tidak terkirim** meskipun status Connected dan trigger terpenuhi — siapkan:
   - Screenshot menu Properties WhatsApp Notification
   - ID Contact/Deal yang seharusnya menerima notifikasi
   - Waktu pengiriman yang diharapkan
   - Screenshot saldo MCC saat ini
5. **Akses Chat Panel hilang** atau akun tidak bisa login

Siapkan informasi: User ID, Workspace ID, dan detail error yang ditampilkan sistem.