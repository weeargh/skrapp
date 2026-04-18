---
title: Bagaimana Cara Mengelola User Input dan Bot Response pada Chatbot
canonical_url: https://help-center.qontak.com/hc/id/articles/12263090746137-Bagaimana-Cara-Mengelola-User-Input-dan-Bot-Response-pada-Chatbot
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- conversational-ai-chatbot
- manage-user-input
- ai-chatbot-automation
query_examples:
- Cara Mengelola User Input dan Bot Response pada Chatbot
- Bagaimana cara Mengelola User Input dan Bot Response pada Chatbot?
- Langkah-langkah Mengelola User Input dan Bot Response pada Chatbot di Qontak Omnichannel
- How do I Mengelola User Input dan Bot Response pada Chatbot?
- Mau Mengelola User Input dan Bot Response pada Chatbot, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Sebelum mengelola User Input dan Bot Response pada Chatbot, pastikan Anda memiliki:

1. Akses ke Qontak Omnichannel atau Qontak Chat dengan izin pembuatan chatbot
2. Conversation yang sudah dibuat di menu Chatbot
3. Welcome Message sudah dikonfigurasi sebelumnya
4. Pemahaman tentang struktur percakapan chatbot dalam bentuk Tree Diagram

## Steps  <!-- confidence:high ✓ -->


Terdapat **3 Input Type** yang dapat Anda pilih yaitu:  
![120.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51040302976025)  
**Keterangan:**  
- **All types:** Bot akan menerima semua jenis input dari pengguna, baik berupa teks maupun gambar. Cocok digunakan bila percakapan tidak dibatasi oleh format tertentu.  
- **Image:** Bot hanya menerima input berupa gambar yang dikirimkan pengguna. Biasanya dipakai untuk kasus penggunaan yang membutuhkan bukti visual, misalnya foto produk.  
- **Text:** Bot hanya menerima input berupa teks. Digunakan saat chatbot memang membutuhkan jawaban tertulis dari pengguna, misalnya nama, email, atau pertanyaan terbuka.
  4. Apabila Anda memilih **Input Type** berupa **Text** , maka Anda dapat menentukan **Input handling** yang berfungsi untuk menentukan bagaimana bot memperlakukan jawaban atau input yang diberikan pengguna. Terdapat **dua opsi** yang dapat Anda pilih yaitu **Specific user input** atau bot hanya akan merespons kalau input dari pengguna sesuai dengan kata/kalimat yang sudah ditentukan di kolom _User input_ dan **Save user input to variable** atau opsi yang digunakan untuk menyimpan seluruh jawaban yang diberikan oleh pengguna ke dalam sebuah variabel.  
**![121.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51040281074201)**
User Input dapat dibuat beberapa kali, dengan cara klik **“+”** lalu **“User input”** sesuai dengan jumlah user input yang ingin Anda buat.  
**Keterangan:**  
- **Save user input to variable:** Digunakan untuk menangkap user input sebagai variabel. Variabel dapat digunakan lagi di Bot Response yang mana akan menampilkan nilai variabel tersebut. Klik [di sini](https://help-center.qontak.com/hc/id/articles/12263090746137) untuk fungsi lebih lengkapnya.  
- **Trigger text:** Fitur **add-ons** yang juga tersedia untuk**AI package subscriber** ini memperbolehkan Anda untuk mengetikkan kata-kata trigger dari customer di sini agar sistem dukungan AI mengalihkan percakapan ini untuk lompat ke lajur percakapan lainnya. **Kata-kata** yang telah Anda**Enter** akan masuk ke dalam **daftar di bawah**. Anda dapat klik **“Generate similiar text”** untuk mendapatkan kata-kata usulan AI.
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774149609625)
  5. Jika sudah sesuai, klik “**Save”** untuk menyimpan user input.  
![122.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51040281077785)
  6. User input pun terbuat. Klik **ikon “+”** dan Anda dapat pilih salah satu tipe bot response sesuai dengan user input yang dimasukkan oleh penanya. Terdapat 3 tipe bot response, yaitu **Texts, Buttons,** dan **Lists.** Saat ini dengan adanya fitur + ini, chatbot dapat mengirimkan multiple bubble messages sesuai dengan chatbot flownya.  
![124.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51132823692313)
Untuk mempelajari pengaturan bot response lainnya, mengenai **Additional settings, API Integration** dan**Qontak CRM** , pelajari [di sini](https://help-center.qontak.com/hc/id/articles/12128813400857-Bagaimana-Cara-Melakukan-Pengaturan-Tambahan-pada-Bot-Response).
    1. **Text messages**  
Text adalah respon bot yang isinya berupa pesan teks panjang guna menjelaskan sesuatu (pesan default).  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774149638809)  
Anda dapat mengatur Bot response settings dengan cara seperti berikut:  
1. Isi **Bot response name.**  
2. Lengkapi **Message content,** untuk mengisikan pesan defaut yang ingin disampaikan kepada penanya  
3. Masukkan lampiran file pada bagian **Add attachment**. Lalu, klik **Browse file**. Jumlah maksimal file yang dapat Anda unggah adalah 10 file dan maksimum ukuran file yang dapat diunggah adalah 64 MB. Jenis file yang bisa dapat diunggah adalah Image (.jpeg, .jpg, .png, dan .gif), Video (.mkv, .mov, and .mp4), dan Document (.pdf, .xlsx, .docx, .pptx , .xls, .csv, .s20, dan .cdr). Jika user melampirkan lebih dari 5 file, maka hanya 5 file pertama yang akan ditampilkan. Gunakan tombol **“-”** di samping file untuk menghapusnya. Jika sudah terunggah, pilih**“Save”.**  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774173180313)  
4. Masukkan **Conversation tags,** apabila diperlukan. Tag ini berguna untuk mengelompokkan percakapan berdasarkan tag yang Anda pilih. Klik [di sini](https://help-center.qontak.com/hc/id/articles/5662312564889) untuk mengetahui cara menambahkan tag.  
5. Pilih **Additional settings** untuk menentukan penyelesaian percakapan. Pelajari selengkapnya [di sini](https://help-center.qontak.com/hc/id/articles/12128813400857).  
6. Klik **Send purchase event** untuk mengirimkan purchase event pada setiap Conversation tag, dimana chatbot akan mengirimkan suatu event ke chatpanel untuk diteruskan ke Meta, agar report ads yang memakai CTWA (click to chat WhatsApp ads) dapat menjadi lebih informatif.  
7. Klik **“Save”** jika sudah selesai mengatur bot response.
    2. **Buttons**  
Bot dapat mengajukan pertanyaan sederhana yang memerlukan Jawaban Ya atau Tidak (atau kasus pilihan dengan klik tombol lainnya) dari penanya dan memilih respon berdasarkan jawaban tersebut.  
Hanya tersedia untuk Channel WhatsApp.  
Contoh Kasus:  
Bot akan mengajukan pertanyaan sederhana dengan jawaban ya atau tidak. Jika ya maka akan masuk ke pertanyaan lain dan tidak akan kembali ke menu utama.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774149640729)  
Anda dapat mengatur Bot response settings dengan cara seperti berikut:  
1. Isi **Bot response name.**  
2. Pilih jenis Konten Header (Teks, Gambar, Video, atau Dokumen) pada **Header content type.** Apabila Anda Text, maka kolom yang muncul adalah Header text, namun apabila Anda gambar, video atau dokumen, maka kolom yang muncul adalah **Choose file** attachment.  
3. Lengkapi **Message content,** untuk pesan perintah, untuk memilih pilihan button yang tersedia.  
4. Tambahkan Button pada bagian **Button content type** dengan klik**“Add button”**. WhatsApp menyediakan maksimal 3 Button yang dapat dibuat dalam 1 bubble. Anda juga dapat mengatur urutan tombol hanya dengan menggeser naik turun ikon **“Titik enam”.** Anda dapat memasukkan nama button (maks. 20 Karakter).  
5. Masukkan **Conversation tags** , apabila diperlukan. Tag ini berguna untuk mengelompokkan percakapan berdasarkan tag yang Anda pilih. Klik [di sini](https://help-center.qontak.com/hc/id/articles/5662312564889) untuk mengetahui cara menambahkan tag.  
6. Pilih **Additional settings** untuk menentukan penyelesaian percakapan. Pelajari selengkapnya [di sini](https://help-center.qontak.com/hc/id/articles/12128813400857).  
7. Klik **Send purchase event** untuk mengirimkan purchase event pada setiap Conversation tag, dimana chatbot akan mengirimkan suatu event ke chatpanel untuk diteruskan ke Meta, agar report ads yang memakai CTWA (click to chat WhatsApp ads) dapat menjadi lebih informatif.  
8. Klik **“Save”** jika sudah selesai mengatur bot response.
    3. **Lists**  
Jenis pesan ini menawarkan cara yang lebih sederhana dan lebih konsisten bagi user untuk membuat pilihan saat berinteraksi dengan bot.  
Hanya tersedia untuk Channel WhatsApp.  
Contoh Kasus:  
Bot akan menunjukkan daftar produk yang dapat dipilih user. Jika Anda memilih List, maka Bot response default akan muncul sesuai dengan pilihan yang telah dipilih oleh penanya.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774173228057)  
Anda dapat mengatur Bot response settings dengan cara seperti berikut:  
1. Isi **Bot response name.**  
2. Seperti Button, Anda harus perlu mengisikan kolom**Header** , tetapi bedanya terdapat pada List, tipe header tersedia hanya dalam bentuk text.  
3. Lengkapi**Message content** , untuk pesan perintah, untuk memilih pilihan button yang tersedia.  
4. Lengkapi nama tombol pada **Button text**. Tombol di sini berfungsi untuk memunculkan opsi-opsi yang telah Anda siapkan untuk dipilih oleh penanya.  
5. Lengkapi opsi-opsi yang dapat dipilih oleh penanya. Anda dapat menyediakan maksimal 3 item atau opsi pada list. Maksimum karakter pada setiap item atau opsi adalah 24 karakter. Centang **"Reply all answers with one bot response"** jika Anda ingin membuat respon dari bot menjadi 1 respon saja (semua jawaban akan masuk ke 1 respons bot).  
7. Lengkapi informasi List name dan**List description** nya. Anda juga dapat mengatur urutan list hanya dengan menggeser naik turun ikon **“Titik enam”**. Atau, apabila Anda ingin menghapus salah satu list, klik ikon **“-”**.  
8. Masukkan **Conversation tag** , apabila diperlukan. Tag ini berguna untuk mengelompokkan percakapan berdasarkan tag yang Anda pilih. Klik [di sini](https://help-center.qontak.com/hc/id/articles/5662312564889) untuk mengetahui cara menambahkan tag.  
9. Pilih**Additional settings** untuk menentukan penyelesaian percakapan. Pelajari selengkapnya [di sini](https://help-center.qontak.com/hc/id/articles/12128813400857).  
10. Klik **Send purchase event** untuk mengirimkan purchase event pada setiap Conversation tag, dimana chatbot akan mengirimkan suatu event ke chatpanel untuk diteruskan ke Meta, agar report ads yang memakai CTWA (click to chat WhatsApp ads) dapat menjadi lebih informatif.  
11. Klik **“Save”** jika sudah selesai mengatur bot response.
    4. **Form**  
Form merupakan jenis _Bot response_ dalam alur (tree diagram) dimana chatbot mengirim _template_ formulir (form) yang telah dibuat melalui _WhatsApp flow template_ (dari WhatsApp Business Manager) kepada pengguna, agar pengguna dapat mengisi data/formulir, kemudian alur dilanjutkan berdasarkan entri (input) dari form tersebut. Pelajari lebih lanjut terkait **Form** [di sini](https://help-center.qontak.com/hc/id/articles/46099456527129-Bagaimana-Cara-Menggunakan-Flow-Bot-Response-Form-pada-Tree-Diagram).

5. **Branch**  
Branch adalah salah satu tipe Bot response di diagram pohon (flow) chatbot, yang berfungsi untuk mengarahkan kondisi berdasarkan respons API (atau hasil dari integrasi API) dan memilih tanggapan (_response_) yang sesuai dengan kondisi tersebut. Pelajari lebih lanjut terkait **Branch**[di sini](https://help-center.qontak.com/hc/id/articles/44801510839577-Bagaimana-Cara-Mengarahkan-Bot-Response-Branch-sebagai-Greetings).

6. **AI response**  
Jenis pesan ini mengandalkan response AI yang Anda atur sedemikian rupa.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774173228697)  
1. Isikan nama bot response AI ini di kolom**Bot response name.**  
2. Untuk mempermudah pencarian percakapan yang menggunakan bot response ini, tambahkan **Conversation tags** bila perlu.  
3. Klik **Send purchase event** untuk mengirimkan purchase event pada setiap Conversation tag, dimana chatbot akan mengirimkan suatu event ke chatpanel untuk diteruskan ke Meta, agar report ads yang memakai CTWA (click to chat WhatsApp ads) dapat menjadi lebih informatif.  
4. Klik **Select specific sources** untuk memilih Knowledge source yang telah dibuat.  
5. Klik**“Save”** jika sudah selesai mengatur bot response.
    7. **Reuse bot response**  
Apabila Anda ingin menggunakan kembali respons bot yang sudah ada/telah dibuat sebelumnya, Anda dapat klik**“Reuse bot response”**. Setelah itu, akan muncul pop up Reuse existing bot response, seperti ini. Klik **Select Bot Response** dan pilih yang respons Anda inginkan, kemudian klik **“Reuse”**. Maka Respon Bot yang muncul akan sesuai dengan response bot yang telah Anda pilih.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774173181849)

### B. Set as Default Delete Single Block, dan Delete with Children [](https://help-center.qontak.com/hc/id/articles/12263090746137-Bagaimana-Cara-Mengelola-User-Input-dan-Bot-Response-pada-Chatbot#h_01J5Q1GDJC6BYGWQBZGHPRX6S0)
  1. Apabila ingin menghapus User input, Anda dapat klik ikon **“Titik tiga”**. Kemudian, akan muncul pilihan **Set as default, Delete single block** , **Delete with children,** dan**Delete.**  
**![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774173233817)**
  2. **Pilih Set as default** apabila Anda ingin menonaktifkan Default Fallback yang mana setiap jawaban yang diinput oleh penanya di chat akan dipindahkan ke Bot Response berikutnya. Jadi, alur percakapan tidak terjebak pada respon tersebut berulang kali.

Karena bot dapat mengenali "Didi" sebagai Nama, Anda harus mengatur User Input tersebut sebagai User Input Default sehingga Bot akan pindah ke pertanyaan lain. Jika tidak, Bot akan memicu Default Fallback.
  3. Pilih **Delete Single Block** , apabila Anda hanya ingin menghapus User Input dan Bot Response tertentu saja (Apabila Anda telah membuat user input lain pada bagian bawahnya, itu tidak akan terhapus).

Berikut tampilan **sebelum** Anda mengklik Delete Single Block (User input Sunscreen, Toner, dan Clay Mask berada di bawah User input 2.)  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774173236633)  
Apabila Anda klik**“Delete Single Block”** pada user input 2, maka User input Sunscreen, Toner, dan Clay Mask akan naik menggantikan posisi User input 2.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774149645977)
  4. Pilih **Delete with children** , apabila Anda ingin menghapus semua User input dan Bot Response di bawahnya (semua user input yang berada di bawah user input yang Anda hapus, akan ikut terhapus juga).

### C. Membuat Variable Input[](https://help-center.qontak.com/hc/id/articles/12263090746137-Bagaimana-Cara-Mengelola-User-Input-dan-Bot-Response-pada-Chatbot#h_01J5Q1GDJDKMHVN9E9704GCYQ1)
Variabel Input digunakan untuk menangkap user input sebagai variabel. Variabel dapat digunakan lagi di dalam Bot Response yang mana akan menampilkan nilai variabel tersebut.
**Contoh Kasus:**  
Anda ingin merekap jawaban di akhir percakapan. Rekapnya adalah Respon Bot.  
Bot: Sebutkan Nama Anda  
User: Wahyu   
Bot: sesuai umur anda  
User: 27   
Bot: Baik, silakkan cek kembali data Anda  
Nama: Wahyu  
Umur: 27
Berikut cara membuat variable input:
  1. Buat User input terlebih dahulu, lalu centang**Set user input to variable.**  
**![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774149655961)**
  2. Setelah itu, Anda dapat memasukkan atau membuat Nama Variabel atau tag baru. Tindakan ini akan menyimpan teks yang dimasukkan penanya pada chat room sebagai entitas sehingga dapat digunakan lagi dalam respons bot dengan variabel yang memuatnya.   
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774173246745)
  3. Kemudian pada bagian klik kolom bot response content.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774173240857)
  4. Kemudian akan muncul tampilan **Bot response setting.** Untuk Menggunakan Entitas yang telah dibuat di Bot Response, ketik **“{{}}”** di Bot Response **Message Content**. Kemudian, pilih**ENTITY.**  
**![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774149667609)**
  5. Pilih entity yang ingin Anda tampilkan.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774149663385)
  6. Setelah memilih entity, maka entity akan ditampilkan di Respon Bot Content seperti berikut.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774173243929)

- Cara ini dapat Anda lakukan berulang kali dan simpanlah sebagai _entity_ secara satu per satu. Maka, Anda dapat menampilkan semua entity yang telah dibuat, jadi Anda tidak perlu membuat entity yang sama berulang kali.  
- Agar Bot dapat mengenali jawaban user tanpa diblokir oleh fallback default, **gunakan user input default**. Sehingga, Bot dapat menangkap jawabannya dan menyimpannya sebagai entity (tidak mengenalinya sebagai fallback default).
Demikian adalah cara mengelola **user input** dan**bot response** pada chatbot Mekari Qontak Omnichannel. Selanjutnya pelajari terkait cara melihat Bot Performance pada Reports [di sini](https://help-center.qontak.com/hc/id/articles/13642682801177-Bagaimana-Cara-Melihat-Bot-Performance-pada-Reports).

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak jika Anda mengalami:

- Fitur Trigger text (AI package subscriber) tidak berfungsi dengan baik
- Variabel yang disimpan tidak muncul di Bot Response meskipun sudah dikonfigurasi
- Conversation mengalami error saat menyimpan User Input atau Bot Response

Siapkan informasi berikut saat menghubungi support:
- Screenshot konfigurasi User Input dan Bot Response
- Nama Conversation yang bermasalah
- Langkah spesifik yang menghasilkan error
- Tipe input dan handling yang Anda gunakan