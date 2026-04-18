---
title: Bagaimana Cara Membuat, Menghapus, dan Menduplikasi Ticket Layout pada Mekari
  Qontak CRM
canonical_url: https://help-center.qontak.com/hc/id/articles/55153890680089-Bagaimana-Cara-Membuat-Menghapus-dan-Menduplikasi-Ticket-Layout-pada-Mekari-Qontak-CRM
article_type: task
solvability_type: tool
products:
- Qontak CRM
product_surface: web
language: id
intent_tags:
- ticket-creation-tracking
- create-menghapus
- customer-support-ticketin
query_examples:
- Cara Membuat, Menghapus, dan Menduplikasi Ticket Layout pada Mekari Qontak CRM
- Bagaimana cara Membuat, Menghapus, dan Menduplikasi Ticket Layout pada Mekari Qontak
  CRM?
- Langkah-langkah Membuat, Menghapus, dan Menduplikasi Ticket Layout pada Mekari Qontak
  CRM di Qontak CRM
- How do I Membuat, Menghapus, dan Menduplikasi Ticket Layout pada Mekari Qontak CRM?
- Mau Membuat, Menghapus, dan Menduplikasi Ticket Layout pada Mekari Qontak CRM, caranya
  gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.3
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk membuat, menghapus, dan menduplikasi Ticket Layout pada Mekari Qontak CRM, Anda memerlukan:

• Akses ke Qontak CRM dengan peran Administrator atau pengguna dengan izin mengelola Properties
• Menu Tickets sudah tersedia dan aktif di workspace Anda
• Pipeline dan Stage sudah dikonfigurasi di Qontak CRM
• Pemahaman tentang field-field yang relevan dengan proses penanganan Ticket di tim Anda
• Izin untuk membuat dan menghapus layout (hanya Administrator yang dapat melakukan operasi ini)

## Steps  <!-- confidence:high ✓ -->


Pengaturan layout kolom pada halaman pembuatan **Ticket** berperan penting dalam membantu tim bekerja lebih efisien dan terfokus. Tanpa pengaturan yang tepat, Agent dapat dihadapkan pada banyak kolom yang tidak relevan, sehingga proses penanganan _ticket_ menjadi lebih lambat, rawan kesalahan pengisian, serta berisiko menampilkan informasi yang seharusnya tidak diakses oleh pihak tertentu.
Untuk menjawab kebutuhan tersebut, **Mekari Qontak** menyediakan fitur **Ticket Layout** yang memungkinkan penyesuaian tampilan kolom Ticket berdasarkan kebutuhan dan peran masing-masing tim. Dengan fitur ini, setiap tim hanya dapat melihat dan mengelola kolom yang sesuai dengan tanggung jawabnya dalam proses penanganan Ticket.
Fitur ini dapat diakses melalui tab **Layout** pada halaman **Ticket** di menu **Properties**. Pada tab ini, Anda dapat membuat layout baru, melakukan perubahan pada layout yang sudah ada, hingga menghapus layout yang tidak lagi digunakan. Layout yang telah dibuat juga dapat diterapkan sesuai kebutuhan operasional dalam pengelolaan Ticket.
Untuk memahami cara penggunaan fitur ini secara lebih _detail_ , silakan simak penjelasan pada langkah-langkah berikut.
**Penting**  
- Untuk saat ini, fitur pengelolaan **Layout** , baik dari sisi **penambahan field** dan pengaturan **required/optional** hanya berlaku pada kolom terkait **About Ticket**. Sementara, kolom-kolom terkait **Associated companies** dan **Associated contacts** hanya dapat diatur dari sisi pengaturan **required/optional**.  
- Untuk kolom terkait **Product Association** dapat dikelola melalui menu **Properties** tepatnya di halaman [Settings](https://app.qontak.com/crm/properties/settings).
###  **A. Cara Membuat Layout Baru**[](https://help-center.qontak.com/hc/id/articles/55153890680089-Bagaimana-Cara-Membuat-Menghapus-dan-Menduplikasi-Ticket-Layout-pada-Mekari-Qontak-CRM#h_01KHBBWBW3HD2TDWZBN382JH6F)
  1. Masuk ke akun **CRM** Anda kemudian pilih menu **Properties**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55153890649753)
  2. Lalu klik tab **“Layouts”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55153907379097)
  3. Pada halaman **Layout** , klik **“Create layout”** , lalu pilih **“Ticket”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55153907379609)
  4. Selanjutnya Anda akan diarahkan ke halaman berikut. Pada _step_**Fill details** , isikan kolom **Layout name** , **Pipeline** , dan **Teams**. Kemudian klik **“Continue”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55153907382041)
Pada bagian **Teams** , Anda dapat memilih tim spesifik atau **All teams**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55153907382297)
  5. Kemudian akan muncul halaman pengelolaan Layout seperti berikut. Atur dan kelola setiap _field_ yang ingin Anda munculkan pada halaman pembuatan **Deals**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55153890659097)

**No.** | **Nama Fitur** | **Penjelasan**  
---|---|---  
1 | **Available fields** | Berisikan _fields_ yang tersedia dan belum ditambahkan ke area _layout_.

2 | **Search field name** | Kolom untuk mencari nama _field_ yang telah dibuat.  
3 | **Filter** |  Filter untuk memudahkan Anda dalam mencari nama _field_.  
Anda dapat menyaring data tersebut berdasarkan:  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55153907383833)  
**Keterangan:**
  * **All creators** digunakan untuk filter data berdasarkan semua _creator_. 
  * **Created by Qontak** digunakan untuk menyaring data berdasarkan _field_ yang telah dibuat oleh sistem Qontak.
  * **Created by user** digunakan untuk menyaring data berdasarkan _field_ yang telah dibuat oleh _user_.

4 | **Create field** | Klik tombol tersebut untuk menambahkan _field_ baru. Secara otomatis, Anda akan diarahkan ke halaman pembuatan _field_ berikut.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55153907384217)  
5 | **Ticket layout** | Area untuk menyusun _field_ yang sudah ditambahkan.  
6 | **Ikon ‘titik enam’** | Klik ikon berikut untuk memudahkan Anda dalam memindahkan susunan _layout_.   
7 | **Ikon ‘titik tiga’** |  Berisikan pilihan sebagai berikut:  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55153907384985)  
**Keterangan:**
  * **Edit property:** Mengedit _field_.
  * **Set as required:** Menjadikan _field_**wajib** untuk diisi.
  * **Send to top:** Memindahkan _field_ ke posisi urutan atas.
  * **Send to bottom:** Memindahkan _field_ ke posisi urutan terbawah.
  * **Takeout property:** Menghapus _field_. Apabila Anda menghapus salah satu _field_ , maka _field_ yang terhapus akan kembali pada kotak **Available fields**.

9 | **Select field** | Klik tombol ini untuk menambah _field_ yang tersedia pada **Available fields**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55153907387289)  
10 | **Preview** | Klik tombol tersebut untuk melihat tampilan yang akan muncul pada halaman **Customers**.  
Contoh **Preview** yang akan terlihat:  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55153907388185)  
  1. Selanjutnya Layout yang telah dibuat akan muncul pada halaman berikut.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55153890668825)

###  **B. Cara Menghapus Layout yang Telah Dibuat**[](https://help-center.qontak.com/hc/id/articles/55153890680089-Bagaimana-Cara-Membuat-Menghapus-dan-Menduplikasi-Ticket-Layout-pada-Mekari-Qontak-CRM#h_01KHBBWBYGXXZSESP0HRZESQH7)
Berikut merupakan langkah-langkah yang dapat Anda ikuti.
  1. Pada data Layout yang akan Anda hapus, klik **“Actions”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55153907390489)
  2. Lalu pilih **“Delete”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55153907391257)
  3. Kemudian akan muncul kotak informasi seperti berikut. Klik **“Delete”** untuk melanjutkan.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55153907391513)
  4. Maka akan muncul notifikasi berikut yang menyatakan bahwa **Layout** telah berhasil terhapus.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55153890670489)

###  **C. Cara Melakukan Duplikat pada Layout**[](https://help-center.qontak.com/hc/id/articles/55153890680089-Bagaimana-Cara-Membuat-Menghapus-dan-Menduplikasi-Ticket-Layout-pada-Mekari-Qontak-CRM#h_01KHBBWBYR2JNAYT7E25V46VD5)
Berikut merupakan langkah-langkah yang dapat Anda ikuti.
  1. Klik **“Actions”** pada salah satu **Layout** , lalu pilih **Duplicate**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55153890671129)
  2. Selanjutnya Anda akan diarahkan ke halaman **Create ticket Layout**. Dalam hal ini, **Pipeline tidak boleh** memiliki **Layout name** yang sama dengan yang diduplikasi. Jadi, Anda perlu mengubah **Layout name** yang akan diduplikasi. Kemudian ulangi langkah yang sama dalam pembuatan **Ticket Layout** dengan menentukan **Pipeline** dan **Team**. Lalu klik **“Continue”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55153907397657)
  3. Atur kembali **Ticket layout** sesuai dengan keinginan Anda.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55153890671769)
  4. Maka data yang diduplikasi akan kembali muncul pada halaman berikut.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55153907400089)

Demikian penjelasan terkait cara membuat, menghapus, dan menduplikasi Ticket Layout. Selanjutnya pelajari terkait cara mengelola Ticket Properties [di sini](https://help-center.qontak.com/hc/id/articles/22324045918233).

## Error States  <!-- confidence:low ? -->

No common errors documented.

## Escalation  <!-- confidence:medium ~ -->

Jika Anda mengalami masalah saat membuat, menghapus, atau menduplikasi Ticket Layout, hubungi Qontak Support dengan informasi berikut:

• ID workspace dan nama akun CRM Anda
• Nama layout yang bermasalah
• Screenshot halaman Properties - Layouts yang menunjukkan kondisi masalah
• Peran pengguna Anda dalam workspace
• Deskripsi langkah yang sudah Anda coba

Jika layout tidak muncul setelah dibuat, pastikan Anda memiliki izin Administrator dan pipeline/stage telah dikonfigurasi dengan benar di Qontak CRM.