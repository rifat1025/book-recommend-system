# 📚 Book Recommender System

## 🔎 Introduction

The **Book Recommender System** is a machine learning–powered web application built using the Django framework. It recommends books to users based on similarity and popularity metrics.

The recommendation model is trained on a dataset collected from **Kaggle**.
Data cleaning, preprocessing, and model building are performed in a notebook environment. The trained model is then exported as **pickle files** and integrated into the Django backend to serve real-time recommendations.

This project demonstrates the complete workflow of:


* Saving the model
* Deploying it into a production-ready web application

---

## ✨ Features

* 📖 Search for books
* 🎯 Get instant book recommendations
* 🧩 Clean and modular Django structure
* 🌐 Deployment ready

---

## 🧠 Recommendation Method

* Data preprocessing and cleaning
* Popularity-based filtering
* Similarity-based recommendation
* Cosine similarity for finding related books

---

## 🛠 Tech Stack

**Backend:** Django
**Frontend:** HTML, CSS, Bootstrap
**Machine Learning:** Pandas, NumPy, Scikit-learn
**Model Storage:** Pickle
**Dataset Source:** Kaggle

---

## 📂 Dataset

The dataset used to train the model is collected from Kaggle.

https://www.kaggle.com/code/arkaradeniz/book-recommendation

---

## ⚙️ Project Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/book-recommender-system.git
cd book-recommender-system
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate Virtual Environment

**Linux / Mac**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 4️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 5️⃣ Apply Migrations

```bash
python manage.py migrate
```

### 6️⃣ Run the Server

```bash
python manage.py runserver
```

---

## 📦 Download Pickle Files

Download the picke files from **Google Drive** and place them inside the project root directory.

🔗 **Drive Link:**
`https://drive.google.com/drive/folders/1Y4ZKuBgrby6X7FburvaTRTYhbF0zzRCF?usp=sharing`

### Required Files

* `books.pkl`
* `similarity_scores.pkl`
* `popularity_df`
*  `pt.pkl`


---

## 📁 Project Structure

```

├── db.sqlite3
├── manage.py
├── picklefile
│   └── popularity_df
├── README.md
├── recommend
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── settings.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── wsgi.cpython-310.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
└── system
    ├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── migrations
    │   ├── __init__.py
    │   └── __pycache__
    │       └── __init__.cpython-310.pyc
    ├── models.py
    ├── __pycache__
    │   ├── admin.cpython-310.pyc
    │   ├── apps.cpython-310.pyc
    │   ├── __init__.cpython-310.pyc
    │   ├── models.cpython-310.pyc
    │   ├── urls.cpython-310.pyc
    │   └── views.cpython-310.pyc
    ├── templates
    │   └── system
    │       ├── index.html
    │       └── reommend.html
    ├── tests.py
    ├── urls.py
    └── views.py
```

---

## 📸 Screenshots

Add your project screenshots here:

* Home page
* Recommendation result page
* Popular books section

---

## 🚀 Future Improvements

* User authentication system
* Save user favorite books
* Django REST API integration
* Hybrid recommendation system
* Docker support
* Cloud deployment

---

## 👨‍💻 Author

**Rifat Sarker**
CSE Student | Django Developer | Machine Learning Enthusiast

---

## 📜 License

This project is for educational purposes only.
