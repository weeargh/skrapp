---
title: Penjelasan Tipe Report General - CRM
canonical_url: https://help-center.qontak.com/hc/id/articles/5960894977689-Penjelasan-Tipe-Report-General-CRM
article_type: concept
solvability_type: content
products:
- Qontak CRM
- Qontak Chat
product_surface: web
language: id
intent_tags:
- sales-report
- report-management
query_examples:
- Apa itu Tipe Report General - CRM?
- Apa fungsi Tipe Report General - CRM di Qontak CRM?
- Penjelasan Tipe Report General - CRM
- What is Tipe Report General - CRM?
- Bagaimana cara kerja Tipe Report General - CRM?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Definition  <!-- confidence:high ✓ -->


**Report** dengan tipe General umumnya berisi gambaran laporan dari total keseluruhan data yang diinput oleh sales atau User ke dalam sistem CRM.
###  **1. Filter Bar**[](https://help-center.qontak.com/hc/id/articles/5960894977689-Penjelasan-Tipe-Report-General-CRM#h_01HHXVQ33PAWT9DQCMHQ6EA1KF)
Filter Bar pada Dashboard CRM dimanfaatkan untuk men-generate data sesuai dengan data yang diinput oleh **User** tertentu atau **Team** tertentu pada **Pipeline** tertentu di **Waktu** tertentu.  
![42.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50807247824665)
###  **2. Sales Performance dan Yearly Sales Comparison**[](https://help-center.qontak.com/hc/id/articles/5960894977689-Penjelasan-Tipe-Report-General-CRM#h_01HHXVQ33PTCHCG9JXWQ0NFPRW)
![43.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50807247827225)
**- Sales Performance  
** Laporan Sales Performance menampilkan **besaran data Deals (Value)** yang masuk ke Stage Won yang dikelompokkan berdasarkan periode yang terpilih dalam bentuk grafik line area. Periode grafik ini tidak mengikuti filter waktu pada filter bar, namun dapat dipilih sesuai dengan periode khusus yaitu Daily (harian), Weekly (mingguan), dan Monthly (Bulanan).
Jika ujung kursor diarahkan ke garis pada grafik tersebut maka muncul informasi total **besarnya Deal (Value)** dalam satu periode. Total besar Deal dikonversikan ke mata uang _default_ yang dipilih oleh User.
**- Yearly Sales Comparison  
** Laporan Yearly Sales Comparison menampilkan total **besaran Deals (Value)** yang masuk ke Stage Won yang dikelompokkan berdasarkan tahun dalam bentuk histogram. Periode grafik ini tidak mengikuti filter waktu pada filter bar, namun memiliki periode khusus yaitu dari awal tahun hingga bulan saat grafik ditampilkan. Contoh apabila grafik ditampilkan bulan Mei 2018, maka periode nya adalah dari 1 Januari hingga bulan Mei tiap tahunnya.
Jika ujung kursor diarahkan ke bar pada grafik tersebut maka muncul informasi periode dan total besaran Deal pada periode tersebut. Total besar Deal dikonversikan ke mata uang default yang dipilih user.
###  **3. Deals Won dan Summary Report**[](https://help-center.qontak.com/hc/id/articles/5960894977689-Penjelasan-Tipe-Report-General-CRM#h_01HHXVQ33PJF01JCTVVQB0Z09B)
**![3.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F5960935421977)  
-****Deals Won  
** Laporan Deals Won menampilkan data Deals yang dikelompokkan berdasarkan User pembuat Deal dan periodenya dalam bentuk grafik line. Data Deals yang masuk ke grafik ini hanya yang berada pada stage Won. Periode grafik ini tidak mengikuti filter waktu pada filter bar, namun memiliki periode sendiri yaitu Daily (harian), Weekly (mingguan), dan Monthly (Bulanan). Kemunculan item pada grafik ini mengacu pada waktu di mana Deal tersebut dipindah ke stage Won.   
**Contoh:** Deal 1 dibuat pada tanggal 9 September 2018 lalu diubah ke stage Won pada tanggal 18 September 2018, maka Deal tersebut akan ditampilkan pada grafik untuk periode tanggal 18 September 2018.
Jika ujung kursor diarahkan ke titik dari grafik tersebut maka akan muncul informasi nama user, periode, dan jumlah Deal yang berada di stage Won. User pada grafik dapat ditampilkan dan disembunyikan dengan klik nama user tersebut di bagian bawah grafik.
**- Summary Report  
** Summary Report menampilkan perubahan-perubahan yang dilakukan oleh User atau Team yang terpilih di filter bar pada menu Dashboard CRM. Perubahan-perubahan yang dicatat adalah **Create (pembuatan), Update (pembaruan), dan Delete (penghapusan)**. Item-item yang akan tercatat perubahannya adalah User, Deal, Task, Company, Contact, Note, Meeting, Ticket, Pipeline, Target, Email, Properties, Product, dan Stage.
Item-item pada Summary Report diurutkan berdasarkan waktu pencatatan perubahan. Item-item yang tampil dibatasi 100 item terakhir.
Jika salah satu baris memiliki informasi yang terlalu panjang sehingga terpotong, maka isi dari baris tersebut dapat dimunculkan informasi lengkapnya dengan mengarahkan ujung kursor ke baris tersebut.
###  **4. Deals by Stage dan Sources**[](https://help-center.qontak.com/hc/id/articles/5960894977689-Penjelasan-Tipe-Report-General-CRM#h_01HHXVQ33PSMETKGKE58P79JQZ)
**![4.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F5960950065177)**
**- Deals by Stage  
** Laporan Deals by Stage menampilkan data Deals yang dikelompokkan berdasarkan Stage dengan grafik yang ditampilkan berbentuk corong.
Jika kursor diarahkan ke salah satu kelompok dari grafik tersebut maka muncul informasi jumlah Deal, total besar Deal dan persentase-nya terhadap keseluruhan grafik. Persentase dihitung berdasarkan **jumlah banyaknya Deal (Count)** , bukan total **besar Deal (Value)**.
**- Sources  
** Laporan Sources menampilkan data yang dikelompokkan berdasarkan isi dari field properties **Source/Sumber** pada Menu**Contacts, Companies, dan Deals** dengan grafik yang ditampilkan berbentuk pie chart. Jika ada Contact, Company, atau Deal yang **tidak memiliki Source** , maka akan dikelompokkan sebagai **“Undefined Source”**.
Grafik Source untuk data Deals memiliki filter tambahan yaitu Stage.
Jika kursor diarahkan ke salah satu kelompok dari pie chart tersebut maka muncul informasi jumlah item dan persentase-nya terhadap keseluruhan grafik.
###  **5. Lost Reasons dan Tasks**[](https://help-center.qontak.com/hc/id/articles/5960894977689-Penjelasan-Tipe-Report-General-CRM#h_01HHXVQ33Q4EH0W1XWFT94TVMH)
**![5.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F5960943631001)**
**-****Lost Reasons  
** Laporan Lost Reasons menampilkan data yang dikelompokkan berdasarkan isi dari field properties **Lost Reason** pada Menu **Deals** dengan grafik yang ditampilkan berbentuk pie chart. Jika ada Deal yang **tidak memiliki Lost Reason** , maka akan dikelompokkan sebagai **“Undefined Lost Reason”**. Deal yang masuk ke grafik ini adalah Deal yang berada di stage Lost.
Jika kursor diarahkan ke salah satu kelompok dari pie chart tersebut maka akan muncul informasi jumlah item Deal dan persentase-nya terhadap keseluruhan grafik.
**- Tasks  
** Laporan Tasks menampilkan ringkasan data Tasks dalam bentuk tabel. Informasi Task yang ditampilkan adalah **nama Task** , **Item yang terasosiasi** dengan Task tersebut (Contact, Company, Deal), **Status Task** tersebut, **Priority** dari **Task** tersebut, dan **Due Date** -nya. Due date yang ditampilkan pada laporan tersebut apabila field properties **Start Due Date** pada **Task** terisi.
Data Task ditampilkan dalam bentuk tabel dapat di-scroll ke bawah dengan data yang paling atas adalah data yang paling baru diedit atau dibuat.
###  **6. Weighted Average Deals by Stage dan Deals Pipeline Conversion**[](https://help-center.qontak.com/hc/id/articles/5960894977689-Penjelasan-Tipe-Report-General-CRM#h_01HHXVQ33Q71F60C6CCN8RQH8Y)
**![6.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F5960958029209)**
**- Weighted Average Deals by Stage  
** Laporan Weighted Average Deals By Stage menampilkan data Deals yang dikelompokkan berdasarkan Stage dan nilai dari stage tersebut dengan grafik yang ditampilkan berbentuk pie chart. Nilai dari setiap stage pada suatu pipeline ini dapat ditentukan oleh User dengan role Admin pada Menu**Properties - Deals - Edit Pipeline**.
Jika kursor diarahkan ke salah satu kelompok dari pie chart tersebut maka muncul informasi total besar Deal dan persentase-nya terhadap keseluruhan grafik. Persentase dihitung berdasarkan total besar Deal.
**- Deals Pipeline Conversion  
** Laporan Deals Pipeline Conversion menampilkan jumlah deal yang terkonversi dari stage satu ke stage selanjutnya dengan grafik yang ditampilkan berbentuk grafik proses.
Jika kursor diarahkan ke salah satu kelompok dari grafik proses tersebut maka muncul informasi berupa jumlah deal dan persentase-nya.
###  **7. Cumulative Daily Sales Performance by Month**[](https://help-center.qontak.com/hc/id/articles/5960894977689-Penjelasan-Tipe-Report-General-CRM#h_01HHXVQ33QZFEQA2AAKHS8T7Y8)
**![7.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F5960950551577)**
Laporan Cumulative Daily Sales Performance by Month menampilkan besaran deal yang masuk di stage Won secara akumulatif selama 1 bulan dengan grafik yang ditampilkan berbentuk line area.
Jika kursor diarahkan ke garis pada grafik tersebut maka muncul informasi total besarnya Deal dalam suatu tanggal.

## Key Attributes  <!-- confidence:high ✓ -->

• Filter Bar: Memfilter data berdasarkan User tertentu, Team tertentu, Pipeline tertentu, dan Waktu tertentu
• Sales Performance: Grafik line area yang menunjukkan besaran Deal (Value) yang masuk ke stage Won dengan periode Daily, Weekly, atau Monthly
• Yearly Sales Comparison: Histogram yang membandingkan total Deal (Value) per tahun dari awal tahun hingga bulan saat ini
• Deals Won: Grafik line yang menampilkan data Deals per User pembuat Deal dengan periode Daily, Weekly, atau Monthly
• Summary Report: Tabel data Deals yang dapat dikelompokkan berdasarkan User pembuat Deal dan periode
• Konversi mata uang: Semua nilai Deal otomatis dikonversi ke mata uang default pengguna

## Related Tasks  <!-- confidence:high ✓ -->

• Bagaimana Cara Mengajukan Pembuatan Mekari Insight di Qontak CRM
• Bagaimana Cara Melihat Custom Report
• Bagaimana Cara Menambahkan Ticket Reports ke Dashboard Qontak CRM