---
title: Panduan Menyusun Prompt dan Instruksi Chatbot AI yang Efektif
canonical_url: https://help-center.qontak.com/hc/id/articles/55092256923545-Panduan-Menyusun-Prompt-dan-Instruksi-Chatbot-AI-yang-Efektif
article_type: concept
solvability_type: content
products:
- Qontak Chat
product_surface: web
language: id
intent_tags:
- conversational-ai-chatbot
- ai-chatbot-automation
query_examples:
- Apa itu Menyusun Prompt dan Instruksi Chatbot AI yang Efektif?
- Apa fungsi Menyusun Prompt dan Instruksi Chatbot AI yang Efektif di Qontak Chat?
- Penjelasan Menyusun Prompt dan Instruksi Chatbot AI yang Efektif
- What is Menyusun Prompt dan Instruksi Chatbot AI yang Efektif?
- Bagaimana cara kerja Menyusun Prompt dan Instruksi Chatbot AI yang Efektif?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.9
---

## Definition  <!-- confidence:high ✓ -->


Chatbot AI akan bekerja lebih optimal jika diberikan instruksi yang jelas dan terstruktur. Panduan ini menjelaskan cara menyusun _prompt_ dan instruksi **Chatbot AI** agar sesuai dengan kebutuhan operasional, _brand voice_ , serta alur layanan pelanggan.
Dengan mengikuti panduan ini, Anda dapat memastikan _chatbot_ memberikan jawaban yang konsisten dan mengetahui kapan harus meneruskan percakapan ke Agent manusia. 
### A. Memahami Konsep Dasarnya[](https://help-center.qontak.com/hc/id/articles/55092256923545-Panduan-Menyusun-Prompt-dan-Instruksi-Chatbot-AI-yang-Efektif#h_01KH6EJMGPVMA8WH04CB2F866K)
Untuk membuat _chatbot_ yang mengikuti aturan,**Custom Prompt** perlu diperlakukan sebagai **Standard Operating Procedure (SOP)** bagi karyawan baru.
**Knowledge Base** berfungsi menyediakan informasi atau fakta (bagian **“apa”**), sedangkan **Custom Prompt** memberikan arahan tentang **cara bersikap, cara menjawab, dan cara menangani skenario tertentu** (bagian **“bagaimana”**).
Struktur _prompt_ yang baik terdiri dari **tiga elemen utama** yang diberikan kepada AI:
  1. **Knowledge Base** : dokumen yang berisi informasi faktual, seperti pertanyaan yang sering diajukan (FAQ) dan daftar produk.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55092284943001)
  2. **Custom Prompt:** Pengaturan gaya komunikasi dan cara berinteraksi.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55092256916889)

### B. Komponen Struktur Prompt yang Baik[](https://help-center.qontak.com/hc/id/articles/55092256923545-Panduan-Menyusun-Prompt-dan-Instruksi-Chatbot-AI-yang-Efektif#h_01KH6EJMH5EMTC59SCZ41RR895)
Saat mengkonfigurasi AI, Anda perlu mendefinisikan beberapa komponen berikut agar perilakunya konsisten.
####  **1. Identity**[](https://help-center.qontak.com/hc/id/articles/55092256923545-Panduan-Menyusun-Prompt-dan-Instruksi-Chatbot-AI-yang-Efektif#h_01KH6EJMH6SWZ1DG894VH3PW8M)
Tentukan siapa _chatbot_ tersebut. Ini membantu AI tetap “berperan” dengan benar.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55092256917017)
  * **Nama:** Berikan nama khusus untuk chatbot (misalnya: _MinBos_ , _MekaBot_ , _Usman_).
  * **Peran:** Tentukan jabatan atau fungsi chatbot (misalnya: _Customer Service Agent_ , _Sales Representative_ , _Virtual Assistant_).
  * **Cara Menyapa Pelanggan:** Tentukan secara jelas bagaimana chatbot harus menyapa pelanggan agar sesuai dengan _brand voice_ (misalnya menggunakan “Kakak” alih-alih “Anda”, atau menyebut pelanggan sebagai “Mekarians”).

####  **2. Gaya Bahasa (Tone of Voice)**[](https://help-center.qontak.com/hc/id/articles/55092256923545-Panduan-Menyusun-Prompt-dan-Instruksi-Chatbot-AI-yang-Efektif#h_01KH6EJMHEN2J2P880DFZPF13J)
Pilih gaya bahasa yang sesuai dengan identitas _brand_. Berdasarkan referensi umum, beberapa _tone_ yang sering digunakan antara lain:  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55092284943513)
  * **Santai dan conversational:** Terasa ringan dan mudah didekati.
  * **Profesional dan formal:** Sopan dan berorientasi bisnis.
  * **Empatik dan ramah:** Menunjukkan kepedulian dan koneksi personal.
  * **Playful dan fun:** Menghibur dan menyenangkan.

####  **3. Tujuan dan Perilaku Operasional**[](https://help-center.qontak.com/hc/id/articles/55092256923545-Panduan-Menyusun-Prompt-dan-Instruksi-Chatbot-AI-yang-Efektif#h_01KH6ETJGS8SCQV572VTAH2PKF)
Bagian ini adalah inti dari instruksi AI—ibarat “otak” dari operasionalnya. Tulis dengan logika yang jelas dan terstruktur.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55092284943897)
  1. **Tulis Instruksi Secara Spesifik dan Jelas**  
Jangan berasumsi AI bisa memahami aturan tersirat. Jelaskan seolah-olah Anda sedang mengajari anak usia 5 tahun.  
- **Prompt kurang baik:** “Kasih diskon kalau belinya banyak.”  
- **Prompt yang baik:** “Jika pelanggan membeli 12–59 pcs, berikan diskon 5%. Jika membeli 100 pcs atau lebih, berikan diskon 15%.”

1. **Definisikan Skenario ‘If–Then’**  
Berikan logika yang harus diikuti AI untuk menangani kasus yang lebih kompleks.  
**Contoh:** “Diskon hanya berlaku JIKA DAN HANYA JIKA produk adalah jersey custom DAN pelanggan membayar penuh di awal. Jika pembayaran menggunakan Down Payment (DP), maka diskon tidak berlaku.”

1. **Tentukan Batasan untuk Mencegah Halusinasi**  
Jelaskan secara eksplisit apa yang tidak boleh dilakukan AI. Jika suatu produk punya nama panggilan yang umum digunakan pelanggan (misalnya “Qontak” untuk “Mekari Qontak”), instruksikan AI untuk mengenalinya agar tidak terjadi kebingungan.

###  **C. Merancang Aturan Human Handover**[](https://help-center.qontak.com/hc/id/articles/55092256923545-Panduan-Menyusun-Prompt-dan-Instruksi-Chatbot-AI-yang-Efektif#h_01KH6ETJGVGXQD5GC8F9KNDGXS)
Anda perlu menentukan aturan yang jelas kapan AI harus berhenti merespons dan mengalihkan chat ke agen manusia. Ini sangat penting untuk menjaga kepuasan pelanggan.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F55092284944281)
Beberapa kondisi umum yang perlu dimasukkan:
  1. **Penanganan Komplain:** Jika pelanggan terlihat marah, menggunakan huruf kapital/kata kasar, atau melaporkan kesalahan tagihan.
  2. **Penutupan Penjualan:** Jika pelanggan ingin negosiasi deal khusus atau memesan dalam jumlah besar/grup.
  3. **Pertanyaan yang Tidak Diketahui:** Jika AI gagal memahami pertanyaan setelah dua kali percobaan, atau jika informasinya tidak tersedia di Knowledge Base.
  4. **Kata Kunci Tertentu:** Jika pengguna mengetik “CS”, “Admin”, “Agent”, atau “Orang”.

###  **D. Ringkasan Best Practices**[](https://help-center.qontak.com/hc/id/articles/55092256923545-Panduan-Menyusun-Prompt-dan-Instruksi-Chatbot-AI-yang-Efektif#h_01KH6ETJGWGMYJNBQHKVEQ6YX4)
  * **Iterasi:** _Prompting_ bukan pekerjaan sekali jadi. Lakukan pengujian, amati jawaban AI, lalu perbaiki instruksinya secara berkala.
  * **Kontekstual:** Jika Knowledge Base berisi media (gambar/video), sertakan deskripsi teks di prompt atau KB agar AI memahami konteksnya.
  * **Hindari Ambiguitas:** Jangan biarkan aturan terbuka untuk interpretasi. Jika diskon hanya berlaku untuk produk tertentu, sebutkan daftarnya. Jika layanan hanya tersedia _offline,_ jelaskan secara eksplisit.

## Related Tasks  <!-- confidence:high ✓ -->

• Bagaimana Cara Mengatur Default Fallback pada Chatbot Qontak
• Bagaimana Cara Mempublish Chatbot
• Bagaimana Cara Melakukan Pengaturan Tambahan pada Bot Response