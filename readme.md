
# 📄 **Django Resume Generator – Resume Builder System**

Live Demo: **[https://gourav2907.pythonanywhere.com/](https://gourav2907.pythonanywhere.com/)** <br>
Author: **Gourav Verma**

---

## ⭐ **Project Overview**

**Django Resume Generator** is a web-based Resume Builder application where users can enter their personal, educational, and professional details through a form and download a beautifully designed resume as a **PDF**.
All generated resumes are stored in a database and can be managed through the Resume List page where users can also **Download** or **Delete** profiles.

The project is fully deployed on **PythonAnywhere** and uses **wkhtmltopdf** for PDF generation.

---

## 🚀 **Features**

* ✨ Create professional resumes with a simple form
* 📄 Download resume as PDF
* 🗂 Resume List page
* ❌ Delete resume entry
* 🎨 Clean, responsive UI using Bootstrap
* 🧩 Template inheritance for efficient design
* 📁 SQLite3 as lightweight backend database
* ☁️ Live production deployment on PythonAnywhere
* ⚡ Fast PDF generation using wkhtmltopdf

---

## 🌐 **Live Demo**

🔗 **[https://gourav2907.pythonanywhere.com/](https://gourav2907.pythonanywhere.com/)**

---

## 🛠 **Tech Stack**

**Frontend**

* HTML
* CSS
* Bootstrap

**Backend**

* Python
* Django

**Database**

* SQLite3
* MySQL (optional)
* PostgreSQL (optional)

**PDF Generator**

* wkhtmltopdf
* pdfkit

**Deployment**

* PythonAnywhere

**Version Control**

* Git
* GitHub

---

## 📁 **Project Structure**

```
Resume_Generator/
│
├── mysite/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── pdf/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │     └── pdf/
│   │           ├── base.html
│   │           ├── resume.html
│   │           ├── list.html
│
├── db.sqlite3
├── requirements.txt
└── README.md
```

---

## ⚙️ **Installation Guide (Local Setup)**

### 1️⃣ Clone the repo

```bash
git clone https://github.com/Gouravverma7/Resume_generator.git
cd django_Cv_generator
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Linux/Mac
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Migrate database

```bash
python manage.py migrate
```

### 5️⃣ Run server

```bash
python manage.py runserver
```

Now open:
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🧪 **How PDF Generation Works**

We use **pdfkit** + **wkhtmltopdf**:

```python
pdf = pdfkit.from_string(html, False)
response = HttpResponse(pdf, content_type='application/pdf')
```

Make sure `wkhtmltopdf` is installed on your system.

---

## ☁️ **Deployment Guide (PythonAnywhere)**

1. Upload your Django project
2. Setup virtual environment
3. Install requirements
4. Point WSGI file to your project
5. Set STATIC + TEMPLATE directories
6. Include path to **wkhtmltopdf**
7. Reload the web app

---

## 👤 **Author**

**Gourav Verma** <br>
Full Stack Developer and Data Science Enthusiast

