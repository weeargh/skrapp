---
title: Bagaimana Cara Mengatur Agent Allocation pada Agents Management
canonical_url: https://help-center.qontak.com/hc/id/articles/5675423908633-Bagaimana-Cara-Mengatur-Agent-Allocation-pada-Agents-Management
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- inquiry-assignment-escalation-agent-management
- configure-agent-allocation
- customer-support-ticketin
query_examples:
- Cara Mengatur Agent Allocation pada Agents Management
- Bagaimana cara Mengatur Agent Allocation pada Agents Management?
- Langkah-langkah Mengatur Agent Allocation pada Agents Management di Qontak Omnichannel
- How do I Mengatur Agent Allocation pada Agents Management?
- Mau Mengatur Agent Allocation pada Agents Management, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.3
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengatur Agent Allocation pada Agents Management, Anda memerlukan:

• Role Admin (hanya Admin yang dapat menambahkan atau mengubah pengaturan Agent Management)
• Akun Qontak Omnichannel aktif
• Akses ke menu Settings
• Pemahaman tentang tiga mode alokasi: manual assignment oleh Supervisor, pengambilan mandiri oleh Agent melalui tombol "Get New Chat", atau distribusi otomatis

## Steps  <!-- confidence:high ✓ -->


**Agent Allocation** merupakan sebuah fitur Omnichannel Qontak pada **Agents Management** yang terdiri dari **Division** , **Agent Allocation, Broadcast** dan **Workload** di mana hanya Admin yang bisa menambahkan atau melakukan perubahan pada fitur yang ada pada agent management.
Untuk melakukan perubahan pada agent allocation, Anda perlu mengikuti langkah-langkah berikut:
  1. Masuk ke akun Omnichannel Anda. 
  2. Pilih menu **Settings,** lalu klik **Agent Management.  
![85.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50937610235929)  
**
  3. Pilih “**Agent Allocation** ” untuk melakukan pengaturan pada alokasi agent.  
![90.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50937912895385)
  4. Pada _toggle_ “**Agent can takeover unassigned chat”** apabila dicentang maka Agent dapat mengambil alih obrolan yang belum ditetapkan.  
![86.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50937849984281)
  5. Agent bisa mengambil alih _chat_ yang masuk dengan cara klik “**Get New Chat** ” pada _room_ Inbox milik Agent, jika tidak maka Agent tersebut tidak akan mendapatkan _room_ kecuali Supervisor _assign_ langsung ke Agent tersebut.  
![83.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50937856794137)
Jika 'dinonaktifkan' maka tombol “**Get New Chat”** tidak akan muncul pada room sehingga Agent tidak bisa mengambil alih obrolan.
  6. Pada toggle “**Agent can assign room to another agent”** apabila “**ON** ” maka agent tersebut bisa meng _assign_ obrolan ke room lain.  
![87.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50937849987865)
Jika _toggle_ dinonaktifkan, maka agent tidak bisa melakukan _assign_ ke Agent lain dengan karena tombol **Assign** pada Agent akan _disable_.
  7. Klik **“Assign”** untuk menambahkan Agent pada _room_.
![84.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50937849991705)
  8. Pada _toggle_ “**Auto agent allocation (AAA)”** apabila dicentang maka Agent tersebut bisa melakukan _assign_ obrolan ke room lain ketika ada pesan baru yang masuk secara otomatis ke Agent yang online, sehingga Supervisor tidak perlu untuk _assign_ ke Agent dan Agent sendiri tidak perlu untuk “**Get New Chat** ” secara manual. Jika _toggle_ dinonaktifkan, maka agent tidak bisa melakukan _assign_ otomatis.  
![88.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50937856798361)
Hanya dapat mengaktifkan CAA atau AAA, tidak keduanya.
  9. Pada _toggle_ “**Custom agent allocation (CAA)** ” apabila diaktifkan maka Agent dapat menerima permintaan _custom_ sistem oleh klien. Jika dinonaktifkan, maka Agent tidak menerima _custom_ dari klien.  
![89.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50937856799257)
Hanya dapat mengaktifkan CAA atau AAA, tidak keduanya.

## Error States  <!-- confidence:low ? -->

No common errors documented.

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support jika mengalami:

• Tombol Save tidak merespons setelah mengubah pengaturan Agent Allocation
• Toggle pengaturan tidak menyimpan perubahan meskipun sudah diklik
• Pesan error muncul saat mencoba mengaktifkan kedua mode AAA dan CAA sekaligus
• Agent tidak menerima chat meskipun sudah mengaktifkan "Agent can takeover unassigned chat"

Siapkan informasi berikut untuk Support: screenshot pengaturan Agent Allocation, ID akun Omnichannel Anda, langkah yang telah dicoba, dan pesan error (jika ada).