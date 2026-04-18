---
title: Bagaimana Penggunaan WhatsApp Call pada Mekari Qontak
canonical_url: https://help-center.qontak.com/hc/id/articles/55020336751769-Bagaimana-Penggunaan-WhatsApp-Call-pada-Mekari-Qontak
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- whatsapp-call
- call-voice
query_examples:
- Cara WhatsApp Call pada Mekari Qontak
- Bagaimana cara WhatsApp Call pada Mekari Qontak?
- Langkah-langkah WhatsApp Call pada Mekari Qontak di Qontak Omnichannel
- How do I WhatsApp Call pada Mekari Qontak?
- Mau WhatsApp Call pada Mekari Qontak, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk menggunakan WhatsApp Call pada Mekari Qontak, Anda memerlukan:

• Akun Mekari Qontak yang sudah aktif dengan produk Qontak Omnichannel atau Qontak Chat
• Nomor WhatsApp bisnis yang sudah terdaftar dan terverifikasi di Mekari Qontak
• Percakapan aktif dengan pelanggan (marketing, utility, authentication, service, atau free entry point) sebelum mengirim permintaan izin panggilan outbound
• Saldo kredit yang mencukupi untuk panggilan outbound (panggilan inbound tidak dikenakan biaya)
• Izin dari pelanggan untuk melakukan panggilan keluar

## Steps  <!-- confidence:high ✓ -->


**Manfaat penggunaan WhatsApp Call:**
  * Menggabungkan layanan panggilan dan pesan dalam satu platform untuk kemudahan operasional.
  * Proses penyelesaian masalah pelanggan menjadi lebih efisien.
  * Sistem komunikasi terpadu memastikan pelayanan kepada pelanggan berjalan lebih efektif.
  * Khusus untuk **Tim Sales** , Tindak lanjut dilakukan tepat waktu sehingga peluang konversi prospek meningkat.

Untuk mewujudkan manfaat tersebut, WhatsApp Call dilengkapi dengan **berbagai kemampuan utama** yang memudahkan panggilan _inbound_(masuk) dan _outbound_ (keluar), serta integrasi dengan sistem otomatis, yaitu:
  * **Inbound & Outbound Call**: Terima panggilan masuk dari pelanggan atau melakukan panggilan keluar langsung dari _platform_.
  * **Permintaan izin panggilan keluar** : Sebelum melakukan panggilan keluar (Outbound), pelanggan perlu mengirimkan permintaan untuk menelepon dan dari sisi _customer_ jika sudah mengizinkan maka panggilan keluar baru dapat dilakukan. 
  * **Panggilan langsung dari Qontak Omnichannel** setelah mendapat persetujuan pelanggan.

**Penting**  
Berikut ketentuan biaya untuk **WhatsApp Call**  
- Panggilan yang diprakarsai oleh pelanggan tidak dikenakan biaya.  
- Panggilan yang diprakarsai oleh bisnis akan dikenakan biaya, sesuai dengan kode negara pelanggan, durasi panggilan, dan volume panggilan.  
- Mekari Qontak menerapkan penagihan per menit. Jika durasi panggilan melewati satu menit pertama, biaya akan dibulatkan ke menit berikutnya. Pelajari [di sini](https://help-center.qontak.com/hc/id/articles/49348680186009-Simulasi-Harga-pada-Penggunaan-WhatsApp-Call) selengkapnya.
Di bawah ini, Anda akan mempelajari bagian-bagian dari WhatsApp Call yang terdiri dari**Inbound Call, Outbound Call, Ring Group,** dan **WhatsApp Call di Mobile App Qontak Omnichannel**.
### A. FAQ Kebijakan Meta dan Mekari Qontak[](https://help-center.qontak.com/hc/id/articles/55020336751769-Bagaimana-Penggunaan-WhatsApp-Call-pada-Mekari-Qontak#h_01KH0W072DWAY1WY4E08Q4CB8V)
  1. **Apakah bisnis harus memiliki percakapan yang sedang aktif untuk mengirim permintaan izin panggilan?**  
Ya. Permintaan izin panggilan hanya dapat dikirim jika terdapat percakapan yang sedang aktif, baik itu percakapan **marketing, utility, authentication, service** , maupun **free entry point**. Jika pelanggan menyetujui permintaan izin tersebut, maka **customer service window** akan terbuka, sehingga bisnis dapat mengirim pesan bebas selama **24 jam**.
  2. **Berapa kali permintaan izin panggilan dapat dikirim?**  
Bisnis dapat mengirim maksimal **1 permintaan izin dalam 24 jam** dan **2 permintaan izin dalam 7 hari**. Batas ini akan **di-**_**reset**_ ketika terjadi panggilan yang terhubung antara bisnis dan pelanggan, baik panggilan tersebut diprakarsai oleh pelanggan maupun oleh bisnis.
  3. **Apa yang terjadi jika bisnis melewatkan panggilan?**  
Jika pelanggan melakukan panggilan ke bisnis namun tidak terjawab, panggilan tersebut dapat diatur untuk memicu **alur permintaan izin yang sama seperti panggilan yang diprakarsai oleh bisnis**.
Mekanisme ini **bukan** _**callback**_**otomatis**. Silakan hubungi tim kami jika ingin mengaktifkan otomatisasi.
  4. **Bagaimana bisnis mengetahui bahwa pelanggan menyetujui permintaan izin panggilan?**  
Keputusan pelanggan baik menyetujui maupun menolak, akan dikirimkan ke bisnis dan dapat dilihat pada _chat room_ di bagian pojok kanan atas. Di bawah **Nama Pelanggan**. 
  5. **Apakah pelanggan dapat mengubah keputusan izin panggilan?**  
Ya. Pelanggan dapat **mengubah atau memperbarui** keputusan izin panggilan kapan saja. Selain itu, pelanggan dapat memilih untuk **menyetujui, menolak, atau tidak merespons** permintaan izin panggilan.

### B. Cara Mengaktifkan WhatsApp Call[](https://help-center.qontak.com/hc/id/articles/55020336751769-Bagaimana-Penggunaan-WhatsApp-Call-pada-Mekari-Qontak#h_01KH0W13RJ3XVNXWDK6479W1VN)
_Role_ Admin dapat mengakses menu **WhatsApp Integration Settings** dan tab baru bernama **“Call”**. Apabila Anda merupakan peran tersebut, Anda dapat mengaktifkan _inbound_ dan _outbound call_ sesuai kebutuhan. Berikut langkah-langkahnya.
  1. Masuk ke akun Qontak Anda, lalu pilih menu **“Integrations”**. Hanya _**admin**_ yang bisa melakukan konfigurasi disini.
  2. Kemudian klik tab **“Call”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55020500651545)
  3. Lalu pada halaman berikut, klik **“Configure”** pada akun WhatsApp yang telah terintegrasi.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55020500652569)
  4. Pilih untuk _inbound_), keluar (_outbound_), atau keduanya.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55020500654873)
  5. Berikut tampilan yang akan muncul pada _room chat_ WhatsApp jika _inbound_ diaktifkan. Dalam hal ini, akan muncul ikon _phone handle_.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55020500656025)
  6. Berikut tampilan yang akan muncul pada _room chat_ WhatsApp jika _inbound_ dinonaktifkan. Dalam hal ini, ikon _phone handle_ tidak akan muncul.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55020500656793)
  7. Berikut tampilan yang akan muncul pada _room chat_ WhatsApp jika _outbound_ diaktifkan. Dalam hal ini, akan muncul tombol permintaan izin panggilan beserta status izin panggilan.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55020536488985)

* **Apakah perubahan ini mempengaruhi biaya WhatsApp Call?**  
Tidak. Model penagihan tetap sama. Fitur ini hanya memberikan kontrol atas jenis panggilan yang aktif pada akun Anda. Panggilan keluar tetap dikenakan biaya per menit.
  * **Apakah saya bisa mengatur pengaturan yang berbeda untuk setiap Agent?**  
Pada rilis awal ini, pengaturan berlaku untuk seluruh nomor WhatsApp. Pengaturan per Agent akan dipertimbangkan sebagai pengembangan di tahap selanjutnya.
  * **Apakah saya perlu melakukan verifikasi ulang akun WhatsApp untuk menggunakan fitur ini?**  
Tidak. Fitur ini merupakan peningkatan pada platform Qontak dan tidak memerlukan proses verifikasi ulang dengan Meta.

### C. Inbound Call[](https://help-center.qontak.com/hc/id/articles/55020336751769-Bagaimana-Penggunaan-WhatsApp-Call-pada-Mekari-Qontak#h_01KH0W78P21HYW5RD0M8E9FJY9)
WhatsApp Call Inbound merupakan sebuah pesan atau panggilan yang masuk ke _platform_ Mekari Qontak dari customer berupa pertanyaan, keluhan, permintaan informasi, atau pesan apapun yang dikirimkan customer kepada Anda. Dalam hal ini, Anda juga dapat mengirimkan pesan pemicu untuk memberi waktu bagi customer melakukan panggilan. Anda juga dapat menerima panggilan apapun selama masih dalam sesi 24 jam dari pesan pemicu dikirimkan.
### 1. Ketentuan Inbound Call[](https://help-center.qontak.com/hc/id/articles/55020336751769-Bagaimana-Penggunaan-WhatsApp-Call-pada-Mekari-Qontak#h_01KH0W78P4FSV62HA0RMYQ609Y)
Berikut adalah ketentuan terkait **inbound call** :
  1. Saat ini, Agent dapat menerima panggilan masuk melalui **web** dan **mobile**.
  2. Untuk Agent yang menerima panggilan masuk melalui web, disarankan menggunakan **Inbox versi V2**.
  3. Dari sisi pengguna Mekari, **panggilan masuk tidak dikenakan biaya**.
  4. Panggilan masuk dapat muncul di halaman utama Omnichannel, namun kami menyarankan agar Agent dapat selalu membuka halaman Inbox karena biasanya Agent akan banyak aktif di halaman tersebut. 
  5. Untuk dapat menerima _inbound call_ ataupun melakukan _outbound call_ , pastikan perangkat baik itu laptop, PC, ataupun _mobile phone_ sudah terkoneksi dengan _speaker_ dan _microphone_. Pastikan juga sudah ‘allow permission’ terutama di _browser_ laptop atau PC agar bisa menerima _inbound call_. 
  6. Disarankan pada pengaturan _browser_ agar diaktifkan seluruh pengaturan seperti pada gambar di bawah ini.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55021551747609)
Pengaturan ini dapat anda lakukan di sebelah URL field di _browser_ masing-masing dengan klik ikon berikut:![rev 16.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55021551749913)

Sebagai bagian dari ketentuan tersebut, panggilan masuk dapat diterima oleh Agent melalui mekanisme yang berbeda, tergantung pada pengaturan yang digunakan. Terdapat **dua mekanisme panggilan masuk (inbound call)** yang dapat diterima oleh Agent:
  * Panggilan masuk dengan pembuatan _room_.
  * Panggilan masuk tanpa pembuatan _room_(menggunakan **ring group**).

Dalam kondisi tertentu, Meta dapat menerapkan pembatasan pada panggilan masuk jika tingkat jawaban Agent dinilai rendah. Untuk menjaga kualitas komunikasi dan mencegah terjadinya pembatasan tersebut, bisnis perlu memastikan kesiapan sistem dan Agent dalam menangani panggilan masuk secara konsisten.
Berikut adalah aturan dan solusi dari Meta terkait pembatasan panggilan masuk akibat tingkat jawaban yang rendah.
  1. **Komitmen:** Pastikan terdapat agent yang available dalam menangani panggilan secara konsisten.
  2. **Optimasi Ring Group:** Aktifkan Ring Group di akun anda agar agar Agent tetap dapat menerima panggilan masuk, meskipun belum ada _chat room_ yang dibuat. 
  3. **[WAJIB] Notifikasi Browser Selalu Aktif:** Pastikan notifikasi _browser_ dan pengaturan audio selalu dalam kondisi aktif untuk mencegah panggilan atau interaksi terlewat.

Selain mekanisme panggilan masuk, terdapat perilaku lain pada fitur komunikasi yang perlu diperhatikan oleh Agent, salah satunya terkait penggunaan **voice note**. **Customer** dapat meninggalkan **pesan suara (voicemail)** untuk Agent apabila terjadi salah satu dari kondisi berikut:
  * Customer menolak panggilan sebelum panggilan tersambung.
  * Agent menolak panggilan sebelum panggilan tersambung.

### D. Outbound Call[](https://help-center.qontak.com/hc/id/articles/55020336751769-Bagaimana-Penggunaan-WhatsApp-Call-pada-Mekari-Qontak#h_01KH0XARCKHWCHYXDWM8Z546VW)
WhatsApp Call Outbound merupakan sistem panggilan yang dilakukan kepada customer melalui Mekari Qontak. Biasanya panggilan ini berupa penjelasan informasi sebuah produk, promosi, atau pemberian solusi atas kendala yang terjadi. Tujuannya adalah untuk mengelola dan merespon interaksi yang masuk dari customer. 
### 1. Alur dan Ketentuan Outbound Call[](https://help-center.qontak.com/hc/id/articles/55020336751769-Bagaimana-Penggunaan-WhatsApp-Call-pada-Mekari-Qontak#h_01KH0XARCPTDXY135ZGN5RH832)
Untuk melakukan **panggilan keluar (outbound call)** melalui WhatsApp Call, sistem menerapkan alur dan ketentuan tertentu, mulai dari pengecekan percakapan aktif, pengiriman permintaan izin panggilan, hingga panggilan dapat dilakukan setelah pelanggan memberikan persetujuan. Berikut adalah alur pengiriman dan pengelolaan permintaan izin panggilan keluar:
**1. Ketersediaan Percakapan Aktif**  
Sistem akan memeriksa apakah terdapat percakapan aktif dengan jenis Marketing, Utility, Authentication, Service, atau Free Entry Point sebelum mengirimkan permintaan izin panggilan.
**2. Pemeriksaan Batas Permintaan**  
Sebelum permintaan izin dikirim, sistem akan memeriksa batas pengiriman maksimal **1 permintaan dalam 24 jam** dan **2 permintaan dalam 7 hari**.
**3. Pengiriman Permintaan Izin Panggilan**  
Apabila batas permintaan belum tercapai dan terdapat percakapan aktif, sistem akan mengirimkan permintaan izin panggilan kepada customer.
**4. Kondisi Chat Room**  
Apabila _chat room_ telah diselesaikan, berlaku ketentuan berikut:
  * Jika customer tidak memberikan respon, permintaan izin akan ditutup secara otomatis.
  * Jika customer membalas setelah chat room diselesaikan, sistem akan mengizinkan pengiriman permintaan izin baru, sesuai dengan batas yang berlaku.

**5. Panggilan Setelah Persetujuan**  
Setelah customer menyetujui permintaan izin panggilan maka:
  * Sistem akan mengizinkan bisnis untuk melakukan panggilan keluar.
  * Setelah panggilan berhasil tersambung, batas permintaan izin (1 permintaan dalam 24 jam dan 2 permintaan dalam 7 hari) akan di-_reset_.
Untuk melakukan panggilan keluar (outbound call), pengguna perlu memastikan saldo _voice_ mencukupi. Batas minimum saldo untuk melakukan panggilan adalah **Rp50.000**.

**6. Masa Berlaku Permintaan Izin**  
Permintaan izin panggilan akan kadaluarsa secara otomatis apabila terjadi salah satu kondisi berikut:
  * Tidak ada respons dari customer selama **72 jam**.
  * Terjadi panggilan yang berhasil tersambung.
  * Customer menyetujui permintaan baru atau _chat room_ diselesaikan.

**7. Jenis Izin Panggilan**
Terdapat tiga opsi izin panggilan yang dapat dipilih oleh customer, yaitu:
  * Izin permanen.
  * Izin sementara diberikan selama**7 hari kalender (168 jam)**. Dihitung sebagai jumlah detik dalam sehari dikalikan 7, terhitung sejak persetujuan pengguna.
  * Jangan Izinkan.

Selain alur dan ketentuan pelaksanaan _outbound call_ sebagaimana dijelaskan di atas, terdapat **batasan tertentu yang perlu diperhatikan** untuk memastikan kepatuhan dan efektivitas penggunaan fitur ini, di antaranya:
  1. **Batas Volume Panggilan (Call Volume Limit)**. Agent dibatasi maksimal **10 panggilan keluar yang berhasil tersambung** dalam periode **24 jam** ke nomor tersebut.
  2. **Ketergantungan Saldo (Balance Dependency)**. Panggilan keluar bergantung pada saldo yang tersedia. Minimal saldo yang perlu ada adalah **Rp 50.000**. Apabila saldo habis, panggilan akan dihentikan secara otomatis, dan Agent tidak dapat melakukan panggilan lanjutan kepada customer. Lihat informasi mengenai tarif [di sini](https://help-center.qontak.com/hc/id/articles/49348680186009-Simulasi-Harga-pada-Penggunaan-WhatsApp-Call).
  3. **Panggilan Tidak Dijawab atau Ditolak oleh Customer**.  
- **2 (dua) kali berturut-turut panggilan tidak dijawab** , sistem akan menampilkan pesan untuk **mempertimbangkan kembali izin panggilan yang telah disetujui**.  
- **4 (empat) kali berturut-turut panggilan tidak dijawab** , izin panggilan yang telah disetujui akan **dicabut secara otomatis oleh sistem**.

**FAQ seputar Outbound Call**
  1. **Apakah kalau telepon ke negara di luar Indonesia maka tarif akan menyesuaikan dengan negara yang dituju ?**  
Betul, tarif outbound call akan disesuaikan dengan negara yang dituju. Informasi mengenai tarif per menit sesuai dengan negara yang dituju dapat dilihat pada _link_[ berikut](https://help-center.qontak.com/hc/id/articles/49348680186009-Simulasi-Harga-pada-Penggunaan-WhatsApp-Call).
  2. **Apakah batasan 10** _**outgoing calls**_**per 24 jam dihitung hanya untuk panggilan yang berhasil terjawab, atau termasuk seluruh percobaan panggilan?**  
Iya, ini akan dihitung kalau dari sisi bisnis saat akan menelepon itu tersambung dengan _users_. 
  3. **Berapa minimum top up balance untuk Voice Balance?**   
Jumlah minimum _top up balance_ untuk Voice Balance adalah Rp 50.000. 
  4. **Bagaimana caranya setting Callback permission?**

1. Masuk ke **Meta Business Suite/Manager** Anda.
  2. Kemudian buka menu **Pengaturan Bisnis (**_**Business Settings**_**)**.
  3. Di panel navigasi kiri, cari dan pilih Akun WhatsApp (_WhatsApp Accounts_) di bawah Akun (_Accounts_).
  4. Pilih Nomor Telepon (_Phone Numbers_) yang ingin Anda atur fitur panggilannya.
  5. Buka ikon **‘settings’**(biasanya ikon roda gigi) di sebelah nomor telepon Anda atau klik nomornya. Lalu cari tab atau bagian yang berlabel Panggilan (_Calls_) atau Pengaturan Panggilan (_Call Settings_).
  6. Di dalam bagian _Calls_ tersebut, Anda akan menemukan pengaturan terkait panggilan, termasuk opsi untuk mengaktifkan atau menonaktifkan fitur seperti:  
- **Allow Voice Calls** (Izinkan Panggilan Suara)  
- **Display Call Buttons** (Tampilkan Tombol Panggilan)  
- **Callback Permission:** Meta menyediakan opsi konfigurasi di sini yang memungkinkan Anda menentukan apakah izin panggilan balik sementara (_temporary call permission_) harus diberikan secara otomatis ketika pengguna menelepon bisnis Anda (_User-Initiated Call_). Opsi ini biasanya berlabel terkait **izin panggilan balik otomatis** atau **permintaan izin panggilan setelah panggilan masuk**.

### 2. Cara Melakukan Pengajuan Panggilan untuk WhatsApp Call Outbound[](https://help-center.qontak.com/hc/id/articles/55020336751769-Bagaimana-Penggunaan-WhatsApp-Call-pada-Mekari-Qontak#h_01KH0XARHVGGGV8NTQJQ0RZB2F)
Sebelum dapat mengelola WhatsApp Call Outbound, Anda perlu melakukan pengajuan panggilan terlebih dahulu guna memastikan ketersediaan customer dalam melakukan panggilan tersebut. Berikut langkah-langkahnya.
  1. Masuk ke akun Omnichannel Anda dengan _role_ Agent. 
  2. Lalu pilih menu **“Inbox”**.  
![rev 17.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55021551758617)
  3. Kemudian klik tab **“Assigned to me”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55021529150105)
  4. Kemudian pilih salah satu _room chat_.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55021529151513)
  5. Selanjutnya pada kolom _type_ , klik **ikon ‘call’** berikut untuk melakukan pengajuan panggilan.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55021529152665)
  6. Kemudian akan muncul informasi berikut yang menyatakan bahwa pengajuan panggilan akan berakhir dalam kurun waktu **72 jam** sejak pengajuan tersebut dikirim. Selanjutnya, buatlah **caption** pada kolom tersebut dan klik **“Send”** untuk mengirimkan panggilan.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55021551767833)
  7. Lalu chat tersebut akan terkirim ke room chat seperti pada tampilan berikut.   
![rev 21.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55021529155609)
  8. Untuk melihat apakah customer sudah memberikan respon atas permintaan call request maka anda perlu merefresh halaman room. Jika customer sudah memberikan permission maka di pojok kanan atas pada bagian bawah nomor telepon maka akan muncul section untuk melihat call permission status dan call attempts, serta tombol call.   
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55021551769625)  
- Untuk saat ini, hanya **1 pengajuan** dalam **24 jam** dan **2 pengajuan** dalam **7 hari**. Jika batas terlampaui, pengajuan **tidak boleh dikirim**.  
- Jika customer **tidak membalas** , maka pengajuan akan ditutup secara otomatis.  
- Jika customer membalas setelah **room chat** terselesaikan (resolved), maka sistem akan mengizinkan permintaan izin lain berdasarkan batasan.  
- Sistem akan secara otomatis mengakhiri permintaan izin setelah:  
1. **72 jam** tidak ada respon.  
2. Panggilan tersambung.  
3. Customer memberikan permintaan baru atau menyelesaikan **room chat**.  
- **1 agent** hanya dapat menerima **1 panggilan** saja. Apabila terdapat panggilan lain yang masuk pada saat agent tersebut sedang menerima panggilan, maka secara otomatis panggilan tersebut akan diarahkan dan tersambung ke semua **room chat**. 
  9. Namun, apabila customer menolak untuk memberikan izin panggilan, maka status tersebut akan hilang di pojok kanan atas tampilan _chat room_.   
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55021551771161)

### 3. Bagaimana Cara Melakukan Panggilan WhatsApp Call Outbound pada Mekari Qontak[](https://help-center.qontak.com/hc/id/articles/55020336751769-Bagaimana-Penggunaan-WhatsApp-Call-pada-Mekari-Qontak#h_01KH0XARK3JQ456V4GKR8K4GSJ)
Pada tahapan berikut, Anda akan mempelajari cara melakukan panggilan WhatsApp Call Outbound pada Mekari Qontak. Berikut penjelasannya.
**Penting**  
WhatsApp Call Outbound memiliki kuota pemakaian yang dinamakan **‘Voice balance’**. Harap perhatikan selalu kuota pemakaian tersebut. Apabila kuota habis, silahkan hubungi **Admin** Anda untuk melakukan **Top-up**.
  1. Masuk ke akun Omnichannel Anda dengan _role_ Agent.
  2. Lalu pilih menu **“Inbox”**.  
![rev 17.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55021551758617)
  3. Kemudian klik tab **“Assigned to me”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55021529150105)
  4. Kemudian pilih salah satu _room chat_.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55021529151513)
  5. Setelah Anda mendapatkan persetujuan untuk melakukan pengajuan panggilan, maka selanjutnya klik **ikon ‘call’** berikut.![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55021529160345)
Apabila **‘Voice balance’** telah habis, harap hubungi **Admin** Anda untuk melakukan **Top-up**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55021551774873)
  6. Berikut adalah tampilan ketika panggilan sedang berlangsung.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55021551776537)  
- Anda dapat klik **“Mute”** atau **“Unmute”** suara Anda dengan klik **ikon microphone** berikut.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55021529166361)  
- Di sini juga terdapat informasi mengenai pengaturan **Microphone**. Klik **ikon dropdown** berikut untuk melihatnya.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55021529167129)  
- Selain itu, Anda juga dapat memindahkan posisi **widget call** , dengan klik **ikon titik enam** berikut.
  7. Berikut adalah tampilan apabila panggilan tidak terjawab.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55021551779865)
  8. Berikut adalah tampilan apabila panggilan ditolak.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55021529170457)

### E. Ring Group[](https://help-center.qontak.com/hc/id/articles/55020336751769-Bagaimana-Penggunaan-WhatsApp-Call-pada-Mekari-Qontak#h_01KH0XS4X0YZA0QSYP89EK0WWT)
**Ring Group** adalah konfigurasi yang mengelompokkan Agent dan menentukan strategi pendistribusian panggilan masuk, termasuk bagaimana notifikasi panggilan diberikan dan Agent mana yang berhak menerima panggilan tersebut. Dengan adanya Ring Group, sistem dapat memastikan setiap panggilan masuk ditangani secara efisien, tanpa bergantung pada satu Agent atau chat room tertentu. 
Agar bisnis dapat menerima panggilan telepon (inbound call) dari customer tanpa perlu adanya chat room terlebih dahulu maka kami menyarankan bisnis agar bisa untuk membuat ring group. JIka bisnis tidak membuat ring group maka jika terdapat customer yang ingin menelepon bisnis langsung dengan tidak ada chat terlebih dahulu maka call widget tidak akan muncul di sisi agent. 
Terdapat dua Mekanisme Ring Group, yaitu:
  * **Ring to All** (Notifikasi ke seluruh Agent)  
Panggilan masuk akan diberitahukan secara bersamaan kepada seluruh Agent yang tersedia. Agent yang menjawab terlebih dahulu akan menerima panggilan tersebut.
  * **Round Robin** (Distribusi panggilan secara bergiliran)  
Panggilan masuk akan didistribusikan ke Agent secara bergiliran sesuai urutan yang telah ditentukan, sehingga beban kerja Agent dapat lebih merata.

Berikut perbedaan dua mekanisme Ring Group.
**Aspek** | **Ring to All** | **Round Robin**  
---|---|---  
**Konsep** | Seluruh Agent yang tersedia akan menerima panggilan masuk secara bersamaan. | Panggilan masuk didistribusikan secara berurutan kepada agen yang sedang online. Jika ada panggilan baru, panggilan akan diarahkan ke agen online berikutnya.  
**Ketergantungan Status Online/Offline** | Tidak bergantung pada status Agent. | Status Agent(_online/offline_) menjadi faktor utama. Panggilan hanya diarahkan ke Agent yang berstatus _online_ , dan panggilan selanjutnya didistribusikan ke Agent _online_ lain yang tersedia.  
Cara melakukan _setup_ pada Ring Group:
  1. Masuk ke akun Qontak Anda, lalu pilih menu **“Settings”**.
  2. Lalu klik tab **“Call”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55021529171737)
Hanya peran **Supervisor** dan **Admin** yang dapat mengakses menu **Call**.
  3. Kemudian klik **“Create group”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55021529173529)
  4. Lalu tentukan **Group name** , **Connected account** , mode **Ring Group** , dan **Group member**. Kemudian klik **“Save”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55021551790105)
Untuk **Ring mode** , Anda dapat memilih:

Setelah disimpan, **Ring Group** akan aktif. Panggilan masuk berikutnya pada channel WhatsApp yang telah dikonfigurasi akan dialokasikan kepada Agent yang telah Anda pilih. 
Berikut limitasi dari penggunaan Ring Group:
  1. **Satu Ring Group untuk Satu Agen dalam Satu Akun** : Jika seorang agen sudah tergabung dalam Ring Group A, maka agen tersebut tidak dapat dimasukkan ke dalam Ring Group lainnya.
  2. **Waktu Dering 30 Detik** : Jika tidak ada agen dalam Ring Group yang menjawab panggilan masuk dalam waktu 30–60 detik, panggilan akan terputus secara otomatis dan dicatat sebagai **“Unanswered”** pada log **Call Activity**.
  3. **Fokus Channel WhatsApp** : Konfigurasi ini saat ini hanya tersedia untuk panggilan masuk WhatsApp yang diinisiasi tanpa pembuatan _chat room_.
  4. **Berbeda dengan Division** : Ring Group berfungsi mirip dengan _division_ , namun memiliki aturan yang berbeda dengan _division_ pada fitur Chat.

**Skema contoh panggilan dengan ada** _**room**_**terlebih dahulu dan tidak ada room**
**Contoh 1**  
Seorang customer **terlebih dahulu mengirimkan pesan** ke nomor bisnis Anda. Namun, pada saat itu _chat room_ belum memiliki **Agent** yang di-_assign_(ditugaskan). Ketika customer kemudian melakukan panggilan secara langsung dan belum dibuat pengaturan **Ring Group** , maka **inbound call** tersebut**tidak dapat diterima oleh Agent**.
**Contoh 2**  
Seorang customer **tidak mengirimkan pesan terlebih dahulu** ke nomor bisnis Anda. Di sisi lain, pengaturan **Ring Group** juga belum ada. Ketika customer tersebut melakukan panggilan langsung ke nomor bisnis Anda, maka **inbound call** tidak dapat diterima oleh Agent Anda.
**Contoh 3**  
Seorang customer mengirimkan pesan terlebih dahulu ke nomor bisnis Anda, dan _chat room_ masih dalam kondisi aktif dengan **Agent** yang sudah di-_assign_(ditugaskan). Saat customer tersebut melakukan panggilan langsung dan belum terdapat pengaturan **Ring Group** , maka **inbound call** akan diterima oleh Agent yang sedang menangani chat dari customer tersebut.
**Contoh 4**  
Seorang customer mengirimkan pesan terlebih dahulu ke nomor bisnis Anda, dan _chat room_ masih dalam kondisi aktif dengan Agent yang sudah di-_assign_(ditugaskan). Ketika customer tersebut menelpon langsung dan pengaturan **Ring group** sudah dibuat, maka **inbound call** tetap akan diterima oleh Agent yang menangani _chat_ tersebut. Hal ini dikarenakan customer masih terhubung dengan _chat room_ aktif yang sudah memiliki Agent penanggung jawab.
**Contoh 5**  
Seorang customer mengirimkan pesan terlebih dahulu ke nomor bisnis Anda, dan _chat room_ dalam kondisi sudah di-_resolve_ (diselesaikan) dengan Agent yang sudah di-_assign_ pada _chat room_ tersebut. Ketika customer menelpon langsung dan sudah terdapat pengaturan **Ring Group** yang dibuat, maka **inbound call** akan diterima oleh Agent yang tergabung dalam **Ring Group**. 
**FAQ seputar Ring Group**
  1. Ring Group sudah ada untuk Agent A dan agent lain. Jika satu customer masih memiliki percakapan aktif dengan Agent A, lalu kemudian customer tersebut menelepon maka apa yang terjadi?   
**Inbound call hanya akan masuk ke agent A. Ring Group tidak akan aktif. Call widget hanya akan muncul ke agent A.** Hal ini karena jika masih terdapat chat room aktif maka panggilan masuk akan didahulukan kepada agent yang diassign kepada customer tersebut. 
  2. Ring Group sudah ada untuk agent A dan Agent lain. Jika satu customer sudah tidak memiliki percakapan aktif dengan agent A (_room resolved_), lalu kemudian customer tersebut menelepon maka apa yang terjadi ?   
**Ring Group akan aktif. Call widget akan muncul ke seluruh member yang ada di settingan Ring Group.**
  3. Jika terdapat incoming call dan masuk ke ring group tetapi kemudian tidak diangkat oleh agent (reject atau didiamkan selama 30 - 60 detik), maka apa yang terjadi ?   
**Di Call Activity, akan muncul status “unanswered” tapi nama Agent akan N/A.**
  4. Ketika seluruh member di Roundrobin masih offline, dan terdapat _incoming call_ yang masuk lagi maka apa yang terjadi ?   
- Jika terdapat _ring to all_ , maka itu yang dijadikan _callback_.   
- Jika tidak terdapat _ring to all_ , maka _call_ tidak akan masuk.
  5. Pada mekanisme **Round Robin** , misalnya terdapat Agent A dan Agent B. Ketika ada _incoming call_ , panggilan akan diarahkan terlebih dahulu ke Agent A, kemudian ke Agent B. Distribusi ini hanya mempertimbangkan status _online_ Agent, tanpa memperhatikan apakah panggilan diangkat atau ditolak. 
  6. Pada mekanisme **Round Robin** , jika terdapat _incoming call_ dan Agent A masih sedang on call, maka _incoming call_ berikutnya akan dialihkan ke Agent B.
  7. Kalau ada _room open_ dan sudah ada _assignee_ maka ketika ada _incoming call_ masuk akan ringing ke assignee tersebut. Tidak melalui _ring group_.

Jika customer memiliki _ring group round robin_ dan _ring to all_ maka ketika terdapat _incoming call_ akan masuk ke _round robin_ terlebih dahulu. Jika tidak ada yang _online_ statusnya maka akan dilempar ke _ring to all_.
### F. WhatsApp Call pada Aplikasi Mobile[](https://help-center.qontak.com/hc/id/articles/55020336751769-Bagaimana-Penggunaan-WhatsApp-Call-pada-Mekari-Qontak#h_01KH0XYF5TR23TRCMQRWZKZ8KD)
Aplikasi **Qontak Chat mobile** versi terbaru menghadirkan kemampuan **WhatsApp Call** secara penuh bagi Agent:
  * Agent kini dapat menerima panggilan masuk **WhatsApp**.
  * Kemampuan menerima panggilan masuk tetap didukung meskipun panggilan tersebut dialokasikan melalui pengaturan **Ring Group**.

**Berikut tampilan WhatsApp Call pada aplikasi Mobile.**
---|---  
### G. Report Activity[](https://help-center.qontak.com/hc/id/articles/55020336751769-Bagaimana-Penggunaan-WhatsApp-Call-pada-Mekari-Qontak#h_01KH0XYF65SW8VRJ7TRFK5FBYP)
_Role_ Supervisor dan Admin dapat mengakses laporan aktivitas panggilan dengan mengikuti langkah-langkah sederhana berikut:
  1. Buka menu **Report** pada akun Qontak Anda.
  2. Pilih **“Call Activity”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55021551805465)
  3. Lalu Anda akan diarahkan ke tampilan berikut.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55021551806873)
Laporan ini mengelompokkan hasil panggilan ke dalam dua status utama yaitu:  
- **Answered:** Panggilan berhasil terhubung dan ditangani oleh Agent.  
- **Unanswered:** Panggilan tidak terhubung atau tidak selesai. Hal ini mencakup kondisi ketika Agent menolak panggilan, Customer mengakhiri panggilan sebelum terhubung, atau panggilan melewati batas waktu pada platform/sistem (Meta Time Out) 30-60 detik.

## Error States  <!-- confidence:high ✓ -->

Situasi yang dapat menghambat penggunaan WhatsApp Call:

• Tidak ada percakapan aktif: Permintaan izin panggilan hanya dapat dikirim jika terdapat percakapan aktif dengan pelanggan. Jika belum ada percakapan, mulai percakapan melalui marketing, utility, authentication, atau service message terlebih dahulu
• Batas permintaan izin tercapai: Hanya dapat mengirim maksimal 1 permintaan izin dalam 24 jam dan 2 permintaan dalam 7 hari. Tunggu hingga periode reset atau hingga terjadi panggilan yang terhubung untuk mengirim permintaan baru
• Saldo kredit tidak cukup: Panggilan outbound memerlukan saldo kredit. Periksa dan isi saldo kredit akun Qontak Anda
• Pelanggan menolak permintaan izin: Jika ditolak, Anda tidak dapat melakukan panggilan outbound hingga pelanggan memberikan izin ulang

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim dukungan Mekari Qontak jika mengalami:

• Panggilan tidak dapat terhubung meskipun sudah mendapat persetujuan pelanggan
• Permintaan izin panggilan tidak dapat dikirim padahal percakapan sudah aktif
• Biaya panggilan tidak sesuai dengan durasi atau perhitungan tidak jelas
• Fitur WhatsApp Call tidak muncul di Qontak Omnichannel atau Qontak Chat

Siapkan informasi berikut saat menghubungi support: ID akun Qontak, nomor telepon pelanggan, waktu panggilan terjadi atau permintaan izin dikirim, dan tangkapan layar (screenshot) menunjukkan masalah yang terjadi