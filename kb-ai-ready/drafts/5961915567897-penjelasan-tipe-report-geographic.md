---
title: Penjelasan Tipe Report Geographic
canonical_url: https://help-center.qontak.com/hc/id/articles/5961915567897-Penjelasan-Tipe-Report-Geographic
article_type: concept
solvability_type: content
products:
- Qontak CRM
product_surface: web
language: id
intent_tags:
- sales-report
- report-management
query_examples:
- Apa itu Tipe Report Geographic?
- Apa fungsi Tipe Report Geographic di Qontak CRM?
- Penjelasan Tipe Report Geographic
- What is Tipe Report Geographic?
- Bagaimana cara kerja Tipe Report Geographic?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Definition  <!-- confidence:high ✓ -->


###  **1. GPS Check-In**[](https://help-center.qontak.com/hc/id/articles/5961915567897-Penjelasan-Tipe-Report-Geographic#h_01K5E2Z3CBEPZCSBK8BXAHTF9J)
![46.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50807474730777)
Laporan GPS Check In menampilkan peta Google Maps yang **menunjukkan lokasi Check In dari User pada Tasks** yang dipilih dalam periode waktu tertentu. Lokasi Check In dapat di-klik untuk menampilkan nama User, alamat lokasi check in, dan waktu check in. Berbeda dari grafik lainnya, lokasi check in yang ditampilkan adalah untuk semua pipeline, bukan pipeline yang terpilih di filter bar.
###  **2. Customer Geolocation Map**[](https://help-center.qontak.com/hc/id/articles/5961915567897-Penjelasan-Tipe-Report-Geographic#h_01K5E2Z3CCFQ2M328N9YMA6HXC)
![47.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50807469313049)
Laporan Customer Geolocation Map menampilkan peta Google Maps dengan tambahan 2 jenis ikon yang menunjukkan lokasi alamat Contacts dan Company. Data Contacts dan Company yang akan ditampilkan alamatnya adalah Contacts dan Company yang memiliki tipe Customer pada field properties **Status** pada Menu **Contacts** dan **Type** pada Menu **Companies**.
Ikon untuk **Company berwarna jingga** sedangkan ikon untuk **Contact berwarna biru**. Jika ikon di-klik, akan tampil nama item, alamat, situs web, nomor telepon, rata-rata besaran Deal, besaran Deal terkecil, besaran Deal terbesar, dan tanggal dibuatnya item tersebut. Terdapat filter tambahan pada laporan ini sesuai seperti informasi yang tampil pada saat ikon di-klik.
###  **3. Live GPS Attendance Tracking**[](https://help-center.qontak.com/hc/id/articles/5961915567897-Penjelasan-Tipe-Report-Geographic#h_01K5E2Z3CCQCSZFTMJ9EVG0MJS)
![48.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50807506644377)
Laporan Live GPS Attendance Tracking menampilkan peta Google Maps yang menunjukkan **lokasi GPS terhitung dari user tersebut Check-In hingga user tersebut Check-Out** pada aplikasi mobile. Laporan ini akan merekam perjalanan user beserta persentase baterai gawai yang digunakan dalam bentuk titik checkpoint dan jalur berwarna biru tua sesuai dengan jalur yang dilalui oleh user aplikasi mobile tersebut.
Laporan ini mensinkronisasi setiap interval jam XX:00 yang rincian _checkpoint_ -nya dapat dicek pada tabel sebelah kiri di dalam laporan atau dengan klik titik checkpoint tersebut. Terdapat filter tambahan berupa tanggal dan user yang dapat dipilih sesuai dengan keinginan.

## Key Attributes  <!-- confidence:high ✓ -->

• GPS Check-In: menampilkan lokasi untuk semua pipeline (bukan hanya pipeline terpilih)
• Customer Geolocation Map: ikon Company berwarna jingga, ikon Contact berwarna biru; menampilkan data Company dan Contact dengan status Customer
• Live GPS Attendance Tracking: merekam jalur perjalanan berwarna biru tua, data checkpoint tersinkronisasi setiap interval jam XX:00, persentase baterai tercatat, filter berdasarkan tanggal dan user
• Semua tipe laporan berbasis peta Google Maps dengan klik lokasi untuk detail informasi

## Related Tasks  <!-- confidence:medium ~ -->

• Bagaimana Cara Mengajukan Pembuatan Mekari Insight di Qontak CRM
• Bagaimana Cara Melihat Custom Report
• Bagaimana Cara Menambahkan Ticket Reports ke Dashboard Qontak CRM