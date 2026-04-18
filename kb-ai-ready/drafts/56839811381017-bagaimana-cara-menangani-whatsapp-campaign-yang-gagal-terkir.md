---
title: Bagaimana Cara Menangani WhatsApp Campaign yang Gagal Terkirim
canonical_url: https://help-center.qontak.com/hc/id/articles/56839811381017-Bagaimana-Cara-Menangani-WhatsApp-Campaign-yang-Gagal-Terkirim
article_type: troubleshooting
solvability_type: hybrid
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- campaign
- marketing-campaign-manage
query_examples:
- Menangani WhatsApp Campaign yang Gagal Terkirim tidak berhasil, kenapa?
- Ada masalah dengan Menangani WhatsApp Campaign yang Gagal Terkirim
- Kenapa Menangani WhatsApp Campaign yang Gagal Terkirim gagal?
- Error waktu Menangani WhatsApp Campaign yang Gagal Terkirim
- 'How to fix: Menangani WhatsApp Campaign yang Gagal Terkirim?'
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Symptom  <!-- confidence:high ✓ -->


Di Mekari Qontak, Anda dapat memantau status pengiriman _campaign_ untuk setiap penerima melalui halaman _detail_**Campaign** pada bagian **Campaign Logs**.
**Penting**  
Dalam merencanakan pengiriman _campaign_ , Anda perlu memahami**batas pengiriman pesan (**_**messaging limit**_**)** yang ditetapkan oleh Meta pada level Business Portfolio Anda. Pelajari lebih lanjut [di sini](https://help-center.qontak.com/hc/id/articles/54386710521369-Messaging-Limit-WhatsApp-Business-FAQs). Selain itu, Anda juga dapat melihat informasi resmi dari Meta mengenai**Messaging Limit Meta**
Berikut adalah penjelasan setiap status pengiriman _campaign_ :
**Status** | **Keterangan** | **Saldo WhatsApp Dipotong**  
---|---|---  
Created  |  _Campaign_ berhasil dibuat di Qontak, namun belum dikirim ke META.  Status ini seharusnya hanya muncul sementara. Jika berlangsung lama, silakan hubungi  | Tidak  
Pending |  _Campaign_ telah dikirim oleh sistem Qontak ke META dan sedang menunggu META untuk diteruskan ke penerima. Berikut beberapa kondisi pesan _campaign_ belum diteruskan oleh META:  
1. [Template Pacing](https://help-center.qontak.com/hc/id/articles/23381251489689-Sekilas-Tentang-Template-Pacing)  
2. [Business Portfolio Pacing](https://help-center.qontak.com/hc/id/articles/54386710521369-Messaging-Limit-WhatsApp-Business-FAQs#h_01KFAZQ9DTH3G0EMV062GMKRYQ) | Tidak  
Sent | _Campaign_ berhasil diteruskan oleh META ke penerima, namun belum masuk ke perangkat (misalnya karena WhatsApp penerima tidak aktif). Biasanya ditandai dengan satu centang. | Tidak  
Delivered | _Campaign_ berhasil diterima oleh perangkat penerima. Biasanya ditandai dengan dua centang. | Ya, hanya dipotong satu kali per pesan (antara _delivered_ atau _read_)  
Read | _Campaign_ telah dibaca oleh penerima (dua centang biru). | Ya, hanya dipotong satu kali per pesan (antara _delivered_ atau _read_)  
Replied |  Status ini dihitung oleh sistem Qontak (bukan dari META). Jika penerima membalas dalam waktu **maksimal 30 hari** setelah _campaign_ dikirim, maka akan dianggap sebagai _replied_. Efektif per**1 Februari 2026,**_campaign_ yang dikirim ke _room_ percakapan yang masih aktif **tidak** lagi dihitung sebagai _**replied** _dalam perhitungan **reply rate** di Qontak. | Tidak  
Failed | Pengiriman _campaign_ gagal. Kegagalan dapat berasal dari sistem **Qontak** maupun **META**. Silakan lihat detail _error_ dibawah untuk mengetahui penyebab dan langkah penanganannya. | Tidak  
Pelajari lebih lanjut harga per pesan template di [sini](https://help-center.qontak.com/hc/id/articles/48430892733465-Perubahan-Harga-pada-Meta)
###  **Daftar Pesan Gagal yang Sering Ditemui**[](https://help-center.qontak.com/hc/id/articles/56839811381017-Bagaimana-Cara-Menangani-WhatsApp-Campaign-yang-Gagal-Terkirim#h_01KNV75186877A8FGKWWSH3YS2)
Pada umumnya, pesan dengan kategori**“Marketing”** memiliki aturan pengiriman yang **lebih ketat** untuk menjaga pengalaman pengguna WhatsApp, sehingga pengirimannya lebih dibatasi dibanding kategori lain seperti **Utilitas**.
Berikut beberapa aturan yang berlaku untuk pesan**Marketing** dan tidak berlaku pada kategori _template_ lainnya.
  * _engagement_) dan volume pesan yang diterima pengguna.
  * **Pembatasan pada nomor tertentu** , khususnya penerima yang termasuk dalam 
  * _marketing_.

Di bawah ini disajikan tabel berisi beberapa _error message_ yang umum terjadi pada pengiriman WhatsApp Campaign, beserta penyebab dan cara penanganannya untuk membantu Anda mengidentifikasi kendala dalam pengiriman pesan. Untuk informasi lebih lanjut, silakan merujuk pada referensi dari META 
**Error Message** | **Penyebab dan Solusi**  
---|---  
**131026 – Message**  
**Undeliverable**

**Kategori terdampak:**  
Semua kategori | Nomor penerima bukan nomor WhatsApp  
**Solusi:**  
Harap periksa apakah penerima pernah mengirimkan pesan ke nomor WABA Anda. Jika belum, Anda dapat memasukan nomor penerima ke _link_ berikut untuk memvalidasi apakah nomor tersebut merupakan nomor WhatsApp

**131049** **Meta chose not to deliver.** This message was not delivered to maintain healthy ecosystem   
engagement. **Kategori terdampak:**   
Marketing |  META menerapkan **batas penerimaan pesan marketing** untuk menjaga pengalaman pengguna WhatsApp. Limit per penerima dapat **berbeda-beda** dalam periode tertentu, yang ditetapkan berdasarkan kombinasi volume pesan di **Inbox** dan tingkat interaksi terbaru, sehingga pengguna dengan aktivitas rendah atau _engagement_ rendah akan **menerima lebih sedikit pesan.** **Solusi:**  
Jika Anda menerima pesan _error_ ini, harap tunggu **minimal 24 jam** sebelum mengirimkan ulang pesan _marketing_.  Periode pembatasan dapat berlangsung lebih lama dari **24 jam** , tergantung profil penerima. META tidak menyediakan informasi spesifik mengenai durasi pembatasan per penerima. **Pelajari lebih lanjut dengan klik****.**  
Mulai**Februari 2026** , Meta menambahkan fitur reaksi pada pesan marketing berupa **thumbs up (tertarik)** dan **thumbs down (tidak tertarik)** seperti yang terlihat pada gambar di bawah ini.

**![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56839811374233)** Penerima yang memberikan reaksi **thumbs down** akan mempengaruhi batas pengiriman pesan _marketing_ , sehingga Anda tidak dapat mengirimkan pesan _marketing_ berikutnya dalam**jangka waktu yang tidak ditentukan.** **Solusi:**  
Saat ini, Meta belum menyediakan **rekomendasi** maupun **visibilitas** terkait penerima yang memberikan reaksi tersebut, serta **penerima tidak dapat mengubah respons yang telah diberikan.** Oleh karena itu, Anda disarankan untuk mengecualikan penerima tersebut dari _campaign_ berikutnya, karena penerima menunjukkan ketidaktertarikan terhadap pesan _marketing_ yang dikirimkan sebelumnya.  
**130472**

**Kategori terdampak:**   
Marketing |  WhatsApp melakukan eksperimen pada **1%** nomor pengguna secara global. Akibatnya, nomor-nomor yang termasuk dalam eksperimen ini tidak dapat menerima pesan _broadcast_ yang dikirim menggunakan template Marketing. **Periode eksperimen ini tidak memiliki batas waktu yang pasti.** **Solusi:**  
Anda hanya dapat mengirim pesan selama **Customer Service window (CSW)** masih aktif; untuk membuka kembali CSW, minta pelanggan mengirimkan pesan terlebih dahulu ke nomor WABA Anda. **Pelajari lebih lanjut**  
**131048**

**Kategori terdampak:**   
Semua kategori |  Pesan gagal dikirim karena terdapat pembatasan jumlah pesan yang dapat dikirim dari nomor ini, yang dapat disebabkan oleh banyaknya pesan sebelumnya yang **diblokir** atau **ditandai sebagai** _**spam**_**.** **Solusi:**  
Evaluasi ulang konten pesan dan daftar penerima untuk memperbaiki penilaian atas nomor bisnis Anda.  Anda dapat melihat **status WABA** , **rating nomor WABA** , dan **kualitas template** Anda ketika mengirimkan _campaign_ di Mekari Qontak. ![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56839827316633) **Pelajari lebih lanjut tentang kualitas template****.**  
**132015**

**Kategori terdampak:**   
Semua kategori |  Jika _template_ Anda mencapai status “**Active - Low Quality”** pada WhatsApp Manager atau**“quality_score = RED”** dari respon API**,** maka _template_ akan otomatis dijeda atau _pause_ sementara untuk **menjaga kualitas nomor pengirim** , dengan durasi jeda sebagai berikut: 
  * Pelanggaran pertama: 3 jam;
  * Kedua: 6 jam;
  * Ketiga: akan dinonaktifkan.

**Solusi:**  
Anda disarankan untuk**membuat** _**template**_**baru** dengan memperbaiki konten agar mengurangi _feedback_ negatif dan meningkatkan _engagement_ , serta mengirimkan pesan secara bertahap ke jumlah penerima yang lebih kecil terlebih dahulu untuk menguji respons sebelum menjangkau audiens yang lebih luas. Pelajari lebih lanjut tentang **template pausing**  
**132016**

Template is permanently disabled due to consistent low quality and multiple pauses. It is no longer available to use. |  _Template_ telah dinonaktifkan oleh pihak WhatsApp (META) karena menerima penilaian buruk secara konsisten. Hal ini dapat terjadi karena konten dilaporkan oleh pengguna, melanggar kebijakan WhatsApp, atau sering dilaporkan sebagai _spam_. **Solusi:**  
Anda disarankan untuk**membuat** _**template**_**baru** dengan memperbaiki konten agar mengurangi _feedback_ negatif dan meningkatkan _engagement_ , serta mengirimkan pesan secara bertahap ke jumlah penerima yang lebih kecil terlebih dahulu untuk menguji respon sebelum menjangkau audiens yang lebih luas. Anda dapat mengajukan banding ke META, namun terdapat kemungkinan _template_ akan dinonaktifkan lagi pada masa mendatang karena adanya riwayat penonaktifan sebelumnya.  
**131050**

**Kategori terdampak:**   
Marketing |  Pesan _marketing_ tidak dapat dikirim karena penerima telah memilih untuk berhenti menerima pesan promosi dari bisnis Anda di WhatsApp.  Pengaturan ini dapat dilihat oleh pengguna melalui halaman profil bisnis WhatsApp. ![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56839827318553) **Solusi:**
  * Kecualikan penerima dari pengiriman campaign berikutnya karena mereka telah menolak menerima pesan promosi
  * Fokus pada penerima yang masih memberikan opt-in untuk menjaga kualitas dan performa campaign

**Tips:**  
Anda dapat mengarahkan penerima untuk mengaktifkan konfigurasi **“offers and announcements”** jika ingin menerima pesan marketing Fitur _opt-in_ akan tersedia di Mekari Qontak mulai pertengahan **Mei 2026**. **Pelajari tentang lanjut aturan META terkait opt-in**  
**132005**

**Kategori terdampak:**   
Utilitas, Marketing |  Pesan gagal dikirim karena**jumlah karakter** melebihi batas yang ditetapkan oleh Meta. Batas maksimal untuk _**template marketing**_ dan _**utility**_ adalah**1024 karakter** , **termasuk isi variabel pesan.** [**Pelajari tentang variabel pesan.**](https://help-center.qontak.com/hc/id/articles/54928838790809-Sekilas-tentang-Variabel-Template-Campaign) **Solusi:**  
Buat _template_ baru dengan pesan yang lebih **ringkas** dan **jelas**. Pesan yang lebih singkat cenderung meningkatkan kemungkinan pengguna untuk membaca dan berinteraksi.  
**There Is A Missing Required Field Or Invalid Phone Number Format During Recipient List**  
**Upload**

**Kategori terdampak:**   
Utilitas, Marketing |  Penulisan kode negara yang salah atau tidak  **Solusi:**   
Gunakan format internasional, dengan angka tanpa simbol “+”  
Karakter yang tidak valid  **Solusi:**  
Hindari penggunaan huruf, simbol, atau karakter khusus lainnya kecuali jika memang diizinkan dalam format nomor telepon.

## Solution  <!-- confidence:medium ~ -->

1. Periksa halaman Campaign Logs di detail Campaign untuk melihat error message spesifik setiap penerima.
2. Identifikasi jenis error menggunakan tabel error message umum pada artikel ini dan referensi error codes Meta.
3. Jika error terkait Messaging Limit, pahami batas pengiriman Business Portfolio Anda dan tunggu reset harian atau tingkatkan limit.
4. Jika campaign kategori Marketing, pastikan penerima telah opt-in dan Customer Service Window aktif jika diperlukan.
5. Verifikasi template WhatsApp memiliki status Connected dan rating High Quality di menu template.
6. Coba kirim ulang campaign setelah masalah diatasi atau ubah waktu pengiriman dengan opsi Send Later.

## Escalation  <!-- confidence:medium ~ -->

Jika campaign tetap gagal setelah mengikuti langkah solusi, hubungi Qontak Support dengan informasi: (1) Screenshot halaman Campaign Logs menampilkan error message lengkap; (2) Campaign ID dan nama campaign yang gagal; (3) Jumlah penerima yang gagal vs berhasil; (4) Template message ID dan nama template yang digunakan; (5) Waktu pengiriman campaign; (6) Business Portfolio name dan Business Account ID Anda di Meta.