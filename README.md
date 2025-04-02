# PDF to SCORM Package Generator

This Python script allows you to convert a PDF document into a **SCORM-compliant package** (SCORM 1.2) that can be imported into most Learning Management Systems (LMS) such as Moodle, Canvas, or Blackboard.

## 🎯 Purpose

The goal of this project is to provide an **open-source, lightweight, and offline** solution to package PDF documents as SCORM content without relying on commercial tools.

## 📦 Features

- Wraps a PDF file inside a SCORM-compliant HTML viewer
- Generates a valid `imsmanifest.xml` for SCORM 1.2
- Produces a ready-to-upload `.zip` SCORM package

## 🧰 Requirements

- Python 3.6+
- Works on Linux, macOS, and Windows
- No third-party Python packages needed

## 🚀 How to Use

1. Clone or download the repository.
2. Place your PDF file (e.g., `example.pdf`) in the project folder.
3. Run the script:

```bash
python3 pdf_to_scorm.py
