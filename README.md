# 📁 ResuTrack: Automated Multi-File Media System

An independent, intermediate-level Django backend utility designed to handle binary multimedia file streams (`FILE` multi-part requests) instead of standard text inputs. This standalone application mimics a corporate human resource ingestion portal, allowing job applicants to upload their **Resume** and **Academic Transcript** simultaneously. The system manages automated physical disk writing, isolates media assets into secure directories, and records relational pointer paths.

---

## 🎯 Architectural Purpose & Scope

The core objective of ResuTrack is to transition from basic string processing (text data fields) into **Binary Media Stream Ingestion**. This application serves as a direct engineering foundation for file-vault management systems, mapping out how files cross the HTTP web layer and settle into physical server storage hardware.

### ⚙️ Core System Functionality
1. **Multi-Part File Ingestion:** Processes complex HTML forms utilizing `enctype="multipart/form-data"` protocols to accept text and binary assets simultaneously.
2. **Automated Disk Storage Serialization:** Intercepts uploaded assets via the hidden `request.FILES` dictionary layer, generates isolated storage directories (`resumes/` and `transcripts/`) on the server disk, and commits the files safely.
3. **Relational Path Pointer Mapping:** To ensure high performance, the heavy file asset is never injected directly into the SQL database rows. Instead, the local operating system path string URL is recorded inside the database column as a lightweight pointer reference.
4. **Class-Based Views (CBVs):** Built using high-level, object-oriented Django layout structures (`CreateView` and `ListView`) to replace traditional function loops, complying with modern corporate development paradigms.

---

## 🗄️ Database Architecture Schema (`submissions/models.py`)

The application maps its persistence criteria inside a single, dedicated data model class named `ApplicantSubmission` using the following column fields:

* 👤 `name` (`models.CharField(max_length=100)`) — Captures the legal name of the applicant.
* 📧 `email` (`models.EmailField()`) — Captures the candidate's verified contact address.
* 📄 `resume` (`models.FileField(upload_to='resumes/')`) — Handles the binary resume document stream and automatically routes it to the local media directory tree.
* 🎓 `transcript` (`models.FileField(upload_to='transcripts/')`) — Handles the academic grade record transcript document file stream independently.
* ⏱️ `uploaded_at` (`models.DateTimeField(auto_now_add=True)`) — Precision system server timestamp tracking when the upload transaction occurred.

---

## 🚀 System Pipeline Advantages

* **FYP Code Foundation:** Establishes the core multi-file ingestion, file parsing, and system persistence models required to safely manage encrypted file uploads inside the **Digital Vault (Final Year Project)**.
* **Modular Separation:** Enforces strict data separation rules, ensuring distinct types of documents (resumes vs. transcripts) are structured into separate folders on the storage disk.
* **Enterprise Object Patterns:** Elevates software design literacy by introducing Class-Based View inheritance hooks, shrinking boilerplate code drastically while magnifying baseline security parameters.

---

## ⚠️ System Limitations (Phase 1 Baseline)

* **No Extensions Validation:** The baseline system accepts any incoming raw file format (e.g., `.png`, `.jpg`, `.txt`) as long as it passes the file field assignment boundary. *(Extension validation filtering to restrict inputs strictly to `.pdf` formats will be introduced in the Phase 2 update).*
* **Local Hard Disk Dependency:** Assets are stored natively within the host machine's local disk environment. The project is not integrated with remote distributed cloud storage layers (such as AWS S3 or Azure Blob Storage) in this phase.
* **Public Ingestion Access:** Lacks an active user profile account management shield or authentication guard layer. Any client hitting the route can execute a file upload submission transaction.
