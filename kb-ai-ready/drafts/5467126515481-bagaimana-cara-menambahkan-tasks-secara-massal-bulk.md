---
title: Bagaimana Cara Menambahkan Tasks secara Massal (Bulk)
canonical_url: https://help-center.qontak.com/hc/id/articles/5467126515481-Bagaimana-Cara-Menambahkan-Tasks-secara-Massal-Bulk
article_type: task
solvability_type: tool
products:
- Qontak CRM
product_surface: web
language: id
intent_tags:
- task-management
- add-tasks-secara-massal-bulk
- operation-workflow-automa
query_examples:
- Cara Menambahkan Tasks secara Massal (Bulk)
- Bagaimana cara Menambahkan Tasks secara Massal (Bulk)?
- Langkah-langkah Menambahkan Tasks secara Massal (Bulk) di Qontak CRM
- How do I Menambahkan Tasks secara Massal (Bulk)?
- Mau Menambahkan Tasks secara Massal (Bulk), caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk menambahkan Tasks secara massal (bulk upload) di Mekari Qontak CRM, Anda memerlukan:

• Akun Mekari Qontak CRM yang aktif
• Role Admin atau Owner
• Akses ke menu Tasks dan menu Properties
• Web browser untuk mengakses www.qontak.com
• Template Excel yang akan diunduh dari dashboard CRM
• Data tasks yang siap untuk diunggah dengan format sesuai database CRM Anda

## Steps  <!-- confidence:high ✓ -->


Pada Menu **Tasks** , Anda bisa menambahkan Task dalam jumlah banyak sekaligus, atau yang biasa disebut dengan bulk upload task. Anda dapat lakukan dengan mengunduh template Excel yang telah disediakan dan melengkapi data tasks Anda, dan mengunggahnya melalui Menu **Properties**.
Untuk melakukan bulk upload tasks, ikuti langkah-langkah berikut ini:
  1. Pastikan Anda sudah login kedalam akun CRM Anda melalui website [www.qontak.com](http://www.qontak.com/) dan masuk ke menu **Task**.

3. Unduh template Excel yang sudah tersedia dalam dashboard CRM.  
![31.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56956754426777)
  4. Pada saat pengisian data mengguankan form Excel ini, **pastikan bahwa data yang diinput tidak double**. Kemudian isilah kolom yang tersedia pada Excel sesuai database yang Anda miliki.  
![bulkontak4.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36776161701529)
Apabila terdapat kolom yang bertanda **(*),** artinya kolom tersebut wajib diisi. Sedangkan pada kolom yang terkustomisasi seperti; Status, Job Title, dll. pengisian data pada file Excel harus sesuai dengan opsi yang terdapat pada database CRM. Mulai dari ejaan, besar kecil huruf, sampai penempatan spasi perlu diperhatikan harus sama persis, karena jika terdapat typo atau tidak sesuai akan menyebabkan error pada data yang diunggah.
  5. Jika data “**Task”** pada file Excel sudah terisi semua, Anda dapat merubah format pada file Excel menjadi **“Text”**.  
![bulkontak6.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36776188543513)
  6. Klik **“Browse a file”** untuk mengunggah Kembali file Excel “**Task”** yang sudah terisi.
  7. Apabila muncul notifikasi sebagai berikut artinya data Task anda sudah berhasil terunggah.  
![34.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56956754427417)
  8. Untuk melihat proses pengunggahan data, Anda dapat cek secara berkala pada menu **Properties,** tab **Upload/Download”.**  
**![33.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56956754428185)**

Jika terdapat data yang gagal terunggah, sistem akan secara otomatis mengirimkan notifikasi ke alamat email Anda yang terdaftar akun CRM Qontak. Apabila sudah menerima email notifikasi tersebut Anda dapat melihat detail penjelasan data-data apa saja yang gagal terunggah, Silahkan periksa kembali file Anda dan perbaiki data yang salah.

## Error States  <!-- confidence:high ✓ -->

Jika terdapat data yang gagal terunggah:

• Sistem akan mengirimkan email notifikasi ke alamat email akun CRM Anda yang terdaftar
• Email notifikasi berisi detail data-data mana saja yang gagal dan alasan kegagalan
• Penyebab umum gagal: typo dalam kolom kustomisasi, format data tidak sesuai database CRM, atau data double
• Solusi: Periksa file Excel Anda, perbaiki data yang salah, pastikan ejaan dan spasi persis sama dengan opsi di CRM, kemudian ulangi proses upload dari langkah 3

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Mekari Qontak jika:

• File Excel tidak dapat diunduh dari dashboard CRM
• Sistem tidak menampilkan opsi **Upload File** saat klik tombol **Add Task**
• Email notifikasi gagal diterima setelah 24 jam proses upload
• Data yang sudah diperbaiki masih tetap gagal terunggah setelah beberapa kali percobaan

Siapkan informasi berikut saat menghubungi support: screenshot error, file Excel yang bermasalah, email notifikasi gagal, dan ID akun CRM Anda