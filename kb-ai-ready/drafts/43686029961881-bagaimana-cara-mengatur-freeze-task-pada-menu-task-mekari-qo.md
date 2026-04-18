---
title: Bagaimana Cara Mengatur Freeze Task pada Menu Task Mekari Qontak CRM
canonical_url: https://help-center.qontak.com/hc/id/articles/43686029961881-Bagaimana-Cara-Mengatur-Freeze-Task-pada-Menu-Task-Mekari-Qontak-CRM
article_type: task
solvability_type: tool
products:
- Qontak CRM
product_surface: web
language: id
intent_tags:
- task-management
- configure-freeze-task
- operation-workflow-automa
query_examples:
- Cara Mengatur Freeze Task pada Menu Task Mekari Qontak CRM
- Bagaimana cara Mengatur Freeze Task pada Menu Task Mekari Qontak CRM?
- Langkah-langkah Mengatur Freeze Task pada Menu Task Mekari Qontak CRM di Qontak
  CRM
- How do I Mengatur Freeze Task pada Menu Task Mekari Qontak CRM?
- Mau Mengatur Freeze Task pada Menu Task Mekari Qontak CRM, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengatur Freeze Task pada menu Task Mekari Qontak CRM, Anda memerlukan:

• Akun Mekari Qontak CRM yang aktif
• Role Admin atau Owner (hanya role ini yang dapat mengaktifkan, menonaktifkan, dan mengedit Freeze Task Settings)
• Akses ke menu Properties
• Tab Task tersedia di dalam menu Properties
• Pemahaman tentang jenis Trigger yang ingin digunakan (misalnya Task status atau tanggal jatuh tempo)

## Steps  <!-- confidence:high ✓ -->


Kini terdapat fitur **Freeze Task** pada menu **Task** yang dapat membentuk aturan _workflow_ dengan cara membekukan **Task** yang sebelumnya telah ditetapkan. Hal ini bertujuan untuk mendukung tim dalam mematuhi alur kerja dan standar yang berlaku. Sebelum dapat mengatur **Freeze Task** , Anda perlu mengaktifkannya terlebih dahulu pada **Task Settings** yang dapat diakses melalui menu **Properties**. Untuk itu pada penjelasan di bawah ini, Anda akan mempelajari mulai dari mengaktifkan hingga mengelola **Freeze Task** pada **Task**. Simak langkah-langkah berikut ini. 
### A. Cara Mengaktifkan Freeze Task[](https://help-center.qontak.com/hc/id/articles/43686029961881-Bagaimana-Cara-Mengatur-Freeze-Task-pada-Menu-Task-Mekari-Qontak-CRM#h_01JMEYSB065VH0ZWGSZNFBF3ZJ)
  1. Masuk ke akun Mekari Qontak CRM Anda, lalu pilih menu **Properties**.
  2. Kemudian pilih tab **Task**.  
![29.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F53150081079833)
  3. Selanjutnya klik **“Frozen task settings”**.  
![35.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F53150081082265)
  4. Lalu Anda akan diarahkan ke tampilan berikut. Aktifkan toggle **Frozen task** , lalu pilih jenis **Trigger** pada saat melakukan **Freeze Task**. Sebagai contoh, pada tampilan ini **Trigger options** yang dipilih adalah **Task status**. Maka tentukan jenis status pada Task.  
![36.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F53150081083417)
Hanya **Admin/Owner** yang dapat mengaktifkan pengaturan **Freeze Task** (baik dengan melampaui tanggal jatuh tempo mulai atau status).
  5. Jika semua data telah terisi, klik **“Save changes”**.  
![37.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F53150053419929)
  6. Lalu akan muncul _pop up_ informasi berikut yang menyatakan apabila Anda mengaktifkan **Freeze Task** , maka pengaturan sistem akan membatasi **task updates** sampai **unfrozen** dan akan diaplikasikan ke seluruh **Task** , baik **Task** baru maupun yang sudah ada dalam kurun waktu **15 menit**. Klik **“Enable”** untuk melanjutkan.  
![38.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F53150053421593)
  7. Apabila Anda ingin menonaktifkannya, Anda dapat kembali ke tampilan **‘Freeze Task Settings’** , lalu non aktifkan toggle **‘Enable frozen task’**.  
![39.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F53150081086617)
Hanya **Admin/Owner** yang dapat menonaktifkan pengaturan **Freeze Task**.
  8. Lalu akan muncul _pop up_ informasi berikut yang menyatakan apabila Anda menonaktifkan **Freeze Task** , maka **task updates** akan diperbolehkan dan akan diaplikasikan ke seluruh **Task** , baik **Task** baru maupun yang sudah ada dalam kurun waktu **15 menit**. Klik **“Disable”** untuk melanjutkan.  
![40.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F53150081087513)
  9. Selain itu, Anda sebagai peran **Admin/Owner** juga dapat melakukan edit kembali pada **Freeze Task Settings** dengan kembali pada tampilan tersebut dan melakukan edit.

### B. Implementasi Freeze Task pada Menu Task[](https://help-center.qontak.com/hc/id/articles/43686029961881-Bagaimana-Cara-Mengatur-Freeze-Task-pada-Menu-Task-Mekari-Qontak-CRM#h_01JMEYSB064WYPRA19HWV2Z0ZS)
Setelah Anda mengaktifkan Freeze Task, maka tampilan yang akan muncul adalah seperti berikut.

**B. Tampilan pada halaman ‘Edit Task’**  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F43686029955353)
- Pada tampilan berikut, Task telah mengalami **Freeze** dikarenakan sudah mencapai kriteria tenggat waktunya. Dalam hal ini, apabila Anda merupakan peran **member** , maka Anda **tidak dapat** mengedit data apapun yang terdapat di dalamnya.  
- Hal ini juga berlaku pada tampilan **Task** versi**Mobile CRM**.
Apabila Anda merupakan peran **Admin/Owner** , maka tampilan yang terlihat adalah seperti berikut.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F43686029955993)
- Pada tampilan berikut, Task telah mengalami **Freeze** dikarenakan sudah mencapai tenggat waktunya. Dalam hal ini, apabila Anda merupakan peran **Admin/owner** , maka Anda **dapat** mengedit data apapun yang terdapat di dalamnya, kecuali data **Reporter**.  
- Hal ini juga berlaku pada tampilan **Task** versi**Mobile CRM**.
Demikian penjelasan mengenai Freeze Task pada Qontak CRM.

## Error States  <!-- confidence:high ✓ -->

No common errors documented.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Mekari Qontak jika mengalami:

• Pengaturan Freeze Task tidak tersimpan setelah mengklik **"Save changes"**
• Popup konfirmasi tidak muncul saat mengklik **"Enable"** atau **"Disable"**
• Freeze Task tidak diterapkan ke Task setelah 15 menit
• Pesan error muncul saat mengakses **Frozen task settings**
• Role Admin/Owner tidak dapat mengakses fitur ini

Siapkan informasi: nama akun, screenshot halaman **Frozen task settings**, dan daftar Task yang terpengaruh untuk membantu diagnosis.