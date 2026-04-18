---
title: Bagaimana Cara Mengatur Limit Workload pada Agents Management
canonical_url: https://help-center.qontak.com/hc/id/articles/5690685559065-Bagaimana-Cara-Mengatur-Limit-Workload-pada-Agents-Management
article_type: concept
solvability_type: content
products:
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- inquiry-assignment-escalation-agent-management
- configure-limit-workload
- customer-support-ticketin
query_examples:
- Apa itu Mengatur Limit Workload pada Agents Management?
- Apa fungsi Mengatur Limit Workload pada Agents Management di Qontak Omnichannel?
- Penjelasan Mengatur Limit Workload pada Agents Management
- What is Mengatur Limit Workload pada Agents Management?
- Bagaimana cara kerja Mengatur Limit Workload pada Agents Management?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Definition  <!-- confidence:high ✓ -->


**Agents Management** merupakan sebuah fitur Omnichannel Qontak yang terdiri dari **Division** , **Agent Allocation, Broadcast** dan **Workload** dimana hanya Admin yang bisa menambahkan atau melakukan perubahan pada fitur yang ada pada agent management.
Untuk menampilkan menu **workload** pada halaman **Agent** , Anda perlu mengikuti langkah-langkah berikut:
  1. Masuk ke akun Omnichannel Anda. 
  2. Pilih menu **Settings,** kemudian klik **Agent Management.  
**![1.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36778709551641)
  3. Selanjutnya, klik “**Workload** ” dan centang “**Enable conversation limits”**.  
![2.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36778741338905)
  4. Lalu, pilih “**Specific agents”** apabila Anda ingin mengatur **workload** untuk **agents** tertentu.   
![3.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36778741342361)

- Apabila Anda memasukkan limit sebanyak **15** , maka Agent hanya dapat menangani **15 chat** dan jika **agent** sudah memenuhi limit tersebut, maka pesan baru yang masuk akan diarahkan ke **A****gent** yang masih memiliki limit pesan dengan **status online**.  
- Apabila limit **A****gents** sudah memenuhi kapasitas, maka chat akan ditugaskan kembali ketika limit **A****gents** tidak dalam kondisi penuh.
  9. Jika semua proses sudah selesai, klik “**Save changes”**.  
![10.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36778709564185)

## Key Attributes  <!-- confidence:high ✓ -->

• Dapat diaktifkan melalui opsi "Enable conversation limits" di menu Workload
• Tersedia dua pilihan penerapan: semua agent (All agents) atau agent tertentu (Specific agents)
• Limit dapat diatur per agent atau diterapkan seragam ke semua agent yang dipilih
• Ketika agent mencapai limit, chat baru diarahkan ke agent dengan kapasitas tersedia
• Chat akan dialokasikan kembali ketika agent tidak dalam kondisi penuh
• Hanya Admin yang dapat mengubah pengaturan workload

## Related Tasks  <!-- confidence:medium ~ -->

• Bagaimana Cara Mengatur Agent Allocation pada Agents Management
• Bagaimana Cara Mengatur Broadcast pada Agents Management
• Skema Pembagian Pesan Masuk ke Agen