---
title: Bagaimana Penerapan WhatsApp Username dan BSUID pada Identitas Pelanggan di
  Qontak
canonical_url: https://help-center.qontak.com/hc/id/articles/56342149872921-Bagaimana-Penerapan-WhatsApp-Username-dan-BSUID-pada-Identitas-Pelanggan-di-Qontak
article_type: task
solvability_type: tool
products:
- Qontak CRM
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- bsuid
- general-platform
query_examples:
- Cara WhatsApp Username dan BSUID pada Identitas Pelanggan di Qontak
- Bagaimana cara WhatsApp Username dan BSUID pada Identitas Pelanggan di Qontak?
- Langkah-langkah WhatsApp Username dan BSUID pada Identitas Pelanggan di Qontak di
  Qontak CRM
- How do I WhatsApp Username dan BSUID pada Identitas Pelanggan di Qontak?
- Mau WhatsApp Username dan BSUID pada Identitas Pelanggan di Qontak, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.3
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk memahami penerapan BSUID pada identitas pelanggan di Qontak, Anda memerlukan:

• Akses ke akun Qontak CRM, Qontak Omnichannel, atau Qontak Chat
• Integrasi WhatsApp Business Account yang aktif melalui WhatsApp Cloud API
• Pemahaman bahwa fitur BSUID akan diterapkan mulai 1 Juni 2026
• Tidak ada persiapan teknis khusus yang diperlukan dari pengguna — perubahan akan diterapkan oleh sistem Qontak secara otomatis

## Steps  <!-- confidence:high ✓ -->


Meta menghadirkan fitur **WhatsApp Username** yang memungkinkan pengguna WhatsApp berinteraksi dengan bisnis tanpa menampilkan nomor telepon mereka. Dengan adanya perubahan ini, **nomor telepon tidak lagi selalu tersedia sebagai identitas utama pelanggan** , karena Anda dapat memilih untuk menyembunyikannya.
**Penting**  
Penerapan fitur BSUID akan dimulai pada**1 Juni 2026**.
Untuk menyesuaikan dengan perubahan tersebut, akan diterapkan **Business-Scoped User ID (BSUID)** sebagai identitas utama pelanggan dalam sistem.
**Business-Scoped User ID (BSUID)** adalah **ID unik yang diberikan oleh WhatsApp untuk mengidentifikasi setiap pengguna dalam konteks bisnis tertentu**. ID ini tetap konsisten meskipun pengguna menggunakan username atau menyembunyikan nomor telepon mereka. Dengan menggunakan BSUID, Qontak dapat memastikan bahwa **riwayat percakapan pelanggan tetap tersimpan, atribusi lead tetap akurat, serta fitur messaging seperti service message dan balasan dari iklan WhatsApp tetap berjalan tanpa gangguan**.
Sebagai bagian dari penerapan ini, beberapa halaman di Qontak akan mengalami penyesuaian, termasuk **Inbox, Contact, Report, serta WhatsApp Notification pada CRM**.
### A. Simulasi Penerapan BSUID[](https://help-center.qontak.com/hc/id/articles/56342149872921-Bagaimana-Penerapan-WhatsApp-Username-dan-BSUID-pada-Identitas-Pelanggan-di-Qontak#h_01KMJ97HK00ERQZCVRGQ4NE5F5)
Untuk mendukung perubahan sistem identifikasi pengguna, WhatsApp akan memperkenalkan **identitas pelanggan baru** sebagai pengganti nomor telepon pada kondisi tertentu, seiring dengan peluncuran fitur **username**.
Ke depannya, nomor telepon tidak selalu dibagikan kepada bisnis. Sebagai gantinya, WhatsApp menyediakan **Business-Scoped User ID (BSUID)** , yaitu identitas unik yang digunakan oleh bisnis melalui **WhatsApp Cloud API** untuk mengidentifikasi pengguna.
Berikut gambaran mekanisme identifikasi pengguna oleh bisnis di WhatsApp saat ini serta **setelah perubahan diterapkan**.
  1. **Kondisi saat ini (**_**Today**_**)**  
Bisnis mengidentifikasi pengguna menggunakan **nomor telepon** yang dibagikan oleh pengguna saat berinteraksi di WhatsApp.
  2. **Kondisi setelah perubahan diterapkan – pengguna tanpa username**  
Jika pengguna tidak menggunakan **username** , bisnis tetap dapat mengidentifikasi pengguna melalui **nomor telepon**. Pada beberapa implementasi, **Business-Scoped User ID (BSUID)** juga dapat tersedia sebagai identitas tambahan.
  3. **Kondisi setelah perubahan diterapkan – pengguna menggunakan username**  
Jika pengguna menggunakan **username** , nomor telepon tidak lagi selalu dibagikan kepada bisnis. Dalam kondisi ini, pengguna akan diidentifikasi menggunakan **Business-Scoped User ID (BSUID)** sebagai identitas utama.

Dengan demikian, **BSUID** akan menjadi pengenal unik pengguna di sisi bisnis, sehingga proses identifikasi, integrasi sistem, dan penyimpanan data pengguna tetap dapat berjalan meskipun nomor telepon tidak tersedia. 
**Penting**  
Dalam beberapa kondisi, nomor telepon pengguna masih dapat dibagikan kepada bisnis, seperti ketika pengguna **belum menggunakan username** atau ketika telah terdapat riwayat interaksi sebelumnya antara pengguna dan bisnis. Dalam kasus interaksi sebelumnya, nomor telepon pengguna masih dapat diterima oleh bisnis hingga **30 hari sejak interaksi terakhir**.
Setelah **BSUID** dirilis oleh Meta, nomor telepon pengguna masih dapat diterima oleh bisnis dalam periode tertentu. Hal ini berlaku hingga **30 hari sejak pertama kali pengguna mengirimkan pesan kepada bisnis setelah BSUID dirilis**.
Berikut gambaran alurnya:
  1. **Meta merilis BSUID**  
Perubahan sistem identifikasi pengguna mulai diterapkan oleh Meta, kemudian akan diikuti oleh Qontak.
  2. **Customer mengirim pesan ke bisnis**  
Ketika customer mengirim pesan setelah BSUID dirilis, interaksi tersebut akan dihitung sebagai **awal periode 30 hari**.
  3. **Customer menyembunyikan nomor telepon**  
Meskipun customer memilih untuk menyembunyikan nomor telepon, bisnis masih dapat menerima nomor telepon tersebut selama periode 30 hari sejak interaksi pertama.
  4. **Setelah 30 hari**  
Jika customer tetap menggunakan username dan menyembunyikan nomor telepon, maka bisnis **tidak lagi menerima nomor telepon pengguna**.

### B. Perbandingan Sistem Sebelum dan Sesudah Penerapan BSUID[](https://help-center.qontak.com/hc/id/articles/56342149872921-Bagaimana-Penerapan-WhatsApp-Username-dan-BSUID-pada-Identitas-Pelanggan-di-Qontak#h_01KMJ97HKY52X31EHAMHQAWCGA)
**Aspek** | **Kondisi saat ini** | **Setelah BSUID diterapkan**  
---|---|---  
Identifikasi pengguna | Bisnis mengenali pengguna melalui **nomor telepon**. | Pengguna diidentifikasi menggunakan **BSUID** dan dapat dikaitkan dengan **username**.  
Pencarian pengguna | Pencarian dilakukan menggunakan **nomor telepon**. | Pencarian dapat dilakukan menggunakan **BSUID** atau **username**.  
Akses nomor telepon |  **Nomor telepon selalu terlihat** oleh bisnis. |  **Nomor telepon tidak selalu terlihat** dan hanya dapat dibagikan dalam kondisi tertentu oleh pengguna.  
Setelah penerapan BSUID, identitas utama pengguna dalam integrasi API berubah dari **nomor telepon (wa_id)** menjadi **BSUID (user_id)**. Nomor telepon hanya menjadi informasi tambahan dan tidak selalu tersedia.
### C. Halaman Mekari Qontak yang Terdampak oleh Penerapan BSUID[](https://help-center.qontak.com/hc/id/articles/56342149872921-Bagaimana-Penerapan-WhatsApp-Username-dan-BSUID-pada-Identitas-Pelanggan-di-Qontak#h_01KMJ97HMEHRQT8QAH3P5M3ERF)
Penerapan **Business-Scoped User ID (BSUID)** juga membawa perubahan pada tampilan dan mekanisme identifikasi pengguna di beberapa halaman **Mekari Qontak** , khususnya pada **Contact Card** dan **Inbox**.
**Penting**  
Tidak terdapat perubahan pada halaman Campaign setelah penerapan BSUID. Hal ini karena aktivitas _broadcast_ tetap memerlukan nomor telepon sebagai tujuan pengiriman pesan, sehingga laporan broadcast tetap menampilkan nomor telepon.
Sebelumnya, identifikasi pengguna sepenuhnya bergantung pada **nomor telepon** , sehingga nomor telepon selalu terlihat dan digunakan sebagai dasar pencarian pengguna. Setelah BSUID diterapkan, sistem akan menggunakan **BSUID sebagai identifier utama di sisi** _**backend**_ , sementara _**username**_**dapat ditampilkan sebagai identitas pengguna**. Dalam kondisi tertentu, nomor telepon tidak selalu tersedia sehingga pengguna dapat membagikan nomor telepon melalui fitur **Request Phone** pada percakapan.
**1. Halaman Inbox**
**Tabel 1. Perbandingan tampilan Inbox sebelum dan setelah penerapan BSUID**
**Sebelum** | **Sesudah**  
---|---  
**![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56342180208665)**  
|  **![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56342180209433)** Tampilan pada halaman Inbox setelah BSUID diterapkan (nomor telepon tidak dimunculkan)   
|  **![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56342180210073)** Tampilan nomor telepon pengguna yang berhasil dibagikan setelah pengguna menyetujui permintaan berbagi nomor telepon.   
|  **![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56342149845657)** Tampilan pada halaman Inbox [Customer Data Platform] setelah BSUID diterapkan (nomor telepon tidak dimunculkan)   
|  **![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56342149849113)** Tampilan nomor telepon pengguna yang berhasil dibagikan setelah pengguna menyetujui permintaan berbagi nomor telepon.  
Untuk melakukan pengajuan permintaan nomor telepon pengguna, Anda dapat mengikuti langkah-langkah berikut:
  1. Masuk ke akun Qontak Anda, lalu pilih menu **“Inbox”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56342149849881)
  2. Kemudian klik tab **“Assigned to me”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56342180219161)
  3. Lalu klik salah satu _room chat_.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56342149852441)
  4. Kemudian klik ikon **‘tambah’** berikut. Lalu pilih **“Phone number request”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56342180221849)
  5. Maka sistem akan menampilkan permintaan berbagi nomor telepon pada kolom percakapan. Klik **“Send”** untuk melanjutkan.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56342180224665)
  6. Kemudian, permintaan berbagi nomor telepon berhasil dikirim dan akan ditampilkan pada kolom percakapan dengan status _**Requested**_. Selanjutnya, silakan menunggu respon dari customer Anda.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56342180225817)
  7. Sebagai tambahan informasi, berikut tampilan permintaan pengajuan yang akan muncul pada halaman WhatsApp milik _customer_ Anda.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56342180226329)
  8. Apabila customer menyetujui permintaan berbagi nomor telepon, maka nomor telepon akan ditampilkan pada halaman Inbox seperti pada tampilan berikut.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56342149858969)

**2. Halaman Contact**
**Tabel 2. Perbandingan tampilan Contact Detail sebelum dan setelah penerapan BSUID**
**Sebelum** | **Sesudah**  
---|---  
**![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56342180229785)**| **![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56342149859353)**  
**3. Halaman Report**
Seluruh laporan pada **Chat** , **Package Usage** , dan **Voice** juga akan menampilkan _username_ serta nomor telepon pengguna.
**![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56342149860377)**
**4. Halaman Create Push Notification [CRM]**
Penerapan **BSUID** juga dapat mempengaruhi penggunaan fitur **WhatsApp Notification** pada CRM. Fitur ini tetap memerlukan **nomor telepon** sebagai tujuan pengiriman pesan.
Jika data pengguna **tidak memiliki nomor telepon** , maka sistem tidak dapat mengirimkan notifikasi WhatsApp. Dalam kondisi tersebut, sistem akan menampilkan **informasi atau catatan pada sistem** yang menunjukkan bahwa notifikasi tidak dapat dikirim karena nomor telepon tidak tersedia.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56342149862041)
Notifikasi WhatsApp pada CRM hanya dapat dikirimkan jika data pengguna memiliki nomor telepon yang tersedia.
### D. Perubahan Data Flow setelah Penerapan BSUID[](https://help-center.qontak.com/hc/id/articles/56342149872921-Bagaimana-Penerapan-WhatsApp-Username-dan-BSUID-pada-Identitas-Pelanggan-di-Qontak#h_01KMJ97HPGYFY5N9JJJVSNCYC5)
Setelah penerapan **Business-Scoped User ID (BSUID)** , sistem akan menggunakan **BSUID sebagai identifier utama** untuk mengidentifikasi pengguna. Sebelumnya, sistem menggunakan **nomor telepon sebagai primary key** dalam proses pencarian dan pencocokan data pengguna.
Dengan perubahan ini, BSUID menjadi **identitas unik dan permanen** yang digunakan oleh sistem, sementara nomor telepon berperan sebagai informasi tambahan yang dapat digunakan apabila tersedia.
Perbandingan perubahan tersebut dapat dilihat pada tabel berikut.
**Aspek** | **Sebelum BSUID** | **Sesudah BSUID**  
---|---|---  
Primary identifier | Nomor telepon digunakan sebagai **primary key** dalam _database_. |  **BSUID digunakan sebagai primary key** dan menjadi _identifier_ utama pengguna.  
Pencocokan kontak (Contact matching) | Pencocokan data pengguna dilakukan berdasarkan **nomor telepon**. | Sistem dapat mencocokkan data menggunakan **BSUID maupun nomor telepon** jika tersedia.  
Data historis | Penggabungan data historis menggunakan **nomor telepon**. | Data historis akan disesuaikan melalui proses _mapping_ antara BSUID dan nomor telepon.  
### E. Perubahan API setelah Penerapan BSUID[](https://help-center.qontak.com/hc/id/articles/56342149872921-Bagaimana-Penerapan-WhatsApp-Username-dan-BSUID-pada-Identitas-Pelanggan-di-Qontak#h_01KMJ97HPXF8B955Q19WPD41E5)
Penerapan **Business-Scoped User ID (BSUID)** juga membawa perubahan pada mekanisme integrasi **API WhatsApp**. Sebelumnya, pengiriman pesan dan identifikasi pengguna melalui API sepenuhnya menggunakan **nomor telepon** sebagai _identifier_ utama.
Setelah BSUID diterapkan, sistem dapat menggunakan **BSUID atau username** sebagai _identifier_ pengguna. Nomor telepon masih dapat digunakan, namun tidak lagi menjadi satu-satunya _identifier_ dalam proses integrasi API.
**Penting**  
Informasi **payload API** akan segera tersedia dalam dokumentasi teknis.
###  1. **Perbandingan Endpoint API Sebelum dan Sesudah BSUID**[](https://help-center.qontak.com/hc/id/articles/56342149872921-Bagaimana-Penerapan-WhatsApp-Username-dan-BSUID-pada-Identitas-Pelanggan-di-Qontak#h_01KMJ9MGAYXE5MVN5D59AG12FV)
**Aspek** | **Sebelum BSUID** | **Sesudah BSUID**  
---|---|---  
Endpoint |  POST /api/v1/messages/  
whatsapp/send   
{ "phone_number": "6281234567890", // MANDATORY "message": "Hello World", "channel_id": "xxx-xxx-xxx" } |  **POST /api/v1/messages/**  
**whatsapp/send**   
{ "bsuid": "BSUID_123456789", // RECOMMENDED "username": "user_wa_handle", "phone_number": "6281234567890", "message": "Hello World", "channel_id": "xxx-xxx-xxx" }  
###    
2. **Dampak Perubahan API dan Tindakan yang Diperlukan**[](https://help-center.qontak.com/hc/id/articles/56342149872921-Bagaimana-Penerapan-WhatsApp-Username-dan-BSUID-pada-Identitas-Pelanggan-di-Qontak#h_01KMJ9N5K1VQBKBGTBWBBF2151)
**Endpoint** | **Tingkat Dampak** | **Tindakan yang Diperlukan**  
---|---|---  
Send Message API | Medium | Pembaruan Opsional  
Contact API | Medium | Pembaruan Opsional  
Webhook Payload | Low | Perlu Ditinjau  
Conversation API | Medium | Pembaruan Opsional  
**Urutan Prioritas Parameter**
  1. **bsuid** – prioritas tertinggi, direkomendasikan untuk integrasi baru.
  2. **username** – opsi sekunder.
  3. **phone_number** – digunakan pada integrasi yang sudah ada.

###  **3. Perubahan Webhook setelah Penerapan BSUID** [](https://help-center.qontak.com/hc/id/articles/56342149872921-Bagaimana-Penerapan-WhatsApp-Username-dan-BSUID-pada-Identitas-Pelanggan-di-Qontak#h_01KMJ97HQR0EAAG82B4SSB0YKD)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56342180233241)
(Field Baru pada Webhook Incoming Message)

## Error States  <!-- confidence:low ? -->

No common errors documented.

## Escalation  <!-- confidence:medium ~ -->

Jika Anda mengalami masalah terkait penerapan BSUID atau melihat inkonsistensi data pada identitas pelanggan, hubungi tim dukungan Qontak dengan informasi:

• ID akun Qontak Anda
• Nomor atau username pelanggan yang bermasalah
• Screenshot halaman yang menampilkan masalah (Inbox, Contact, atau Report)
• Waktu kejadian masalah
• Deskripsi perilaku yang tidak sesuai dengan ekspektasi