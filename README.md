# ResuTrack (Phase 1 & 2 File Ingestion Pipeline)

A robust, enterprise-focused document ingestion system engineered to safely capture, screen, and log applicant payload files via a multi-part web user interface. The system implements a defensive architecture that strictly limits inputs to authentic `.pdf` documents, checking incoming files at both the user-interface entry point and the core database validation level before any binary stream is committed to the server disk.

## 🚀 Architectural Phase Breakdown

### 🟩 Phase 1: Multi-Part Binary Ingestion
The initial phase established a functioning data streaming pipe capable of capturing physical user documents alongside relative form parameters.
* **Multi-Part Protocols:** Configured the HTML interface with `enctype="multipart/form-data"` boundaries to break binary chunks apart for network streaming.
* **In-Memory Buffer Extraction:** Leveraged Django’s global `request.FILES` dictionary to seamlessly fetch file streams out of transition memory arrays.
* **Disk Path Relocation:** Used Django's `FileField(upload_to=...)` parameters to save payloads into organized directory structures while storing URL pointer paths in database rows.

### 🟨 Phase 2 (Current): Structural File-Extension Validation Gate
The architecture was hardened to protect the host machine against arbitrary file uploads (such as executable malware scripts `.exe` or un-sanitized web shells `.php`).
* **Client-Side Interface Filtering:** Integrated standard HTML5 `accept=".pdf"` attribute hints on file fields to filter out non-compliant document formats inside the native browser window.
* **Model-Level Constraint Validation:** Developed an isolated string utility validator bound directly to the database model fields. If an adversary attempts to bypass the web interface and inject unauthorized files, the database schema instantly triggers a structural `ValidationError` and drops the write path.
* **Defensive Exception Catching:** Configured custom try-except catch loops within `views.py` to intercept structural database validation rejections gracefully and output controlled API alert responses to the user.

## 🗄️ Relational Database Schema Design (models.py)

The data structure relies on a singular, tightly structured candidate application model:

### ResuModel Table
* `name` (CharField, max_length=255): Captures the applicant's raw full text string.
* `email` (EmailField): Standard system validation for applicant electronic mail syntax.
* `resume` (FileField): Stores the disk pointer path to the resume file, locked behind the custom `validate_pdf_extension` boundary.
* `transcript` (FileField): Stores the disk pointer path to the academic transcript file, locked behind the custom `validate_pdf_extension` boundary.
* `uploaded_at` (DateTimeField): Generates an unalterable microsecond time-stamp of the exact ingestion moment via `auto_now_add=True`.

## 🛡️ Ingestion Security Matrix

The system validates file extensions across a multi-tier defense layer:

| Validation Tier | Enforcement Point | Mechanism | Primary Defensive Purpose |
| :--- | :--- | :--- | :--- |
| **Tier 1: UX Hint** | Client Browser Interface | `accept=".pdf"` HTML attribute | Filters out noise and prevents accidental wrong-file selection. |
| **Tier 2: Model Rule** | Django ORM Core | `os.path.splitext(value.name)` | Hardened backend block that drops execution if the file extension is not pure `.pdf`. |

## 💻 Tech Stack & Engineering Focus
* **Framework:** Django 5.x / Python 3.x
* **Storage Interface:** Django Object-Relational Mapping (ORM) & Local System Directories
* **Core Concepts Practiced:** Binary File Streaming Protocols (`request.FILES`), Form Encoding Rules (`multipart/form-data`), Model-level Field Constraints, Graceful Exception Handling.
