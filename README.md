# 📊 Student Performance Prediction System

A Full Stack Machine Learning Web Application that predicts student final exam performance based on study hours, attendance, and previous scores.

---

## 🚀 Features

* 📈 Predict student performance in real-time
* 🔗 REST API built with Flask
* 🤖 Machine Learning model (Linear Regression)
* 💾 Model persistence using Pickle
* 🌐 Interactive and responsive web interface

---

## 🛠️ Tech Stack

**Frontend:**

* HTML5
* CSS3
* JavaScript

**Backend:**

* Python (Flask)

**Machine Learning:**

* scikit-learn (Linear Regression)
* pandas
* numpy

---

## 📂 Project Structure

```
student-performance-prediction/
│
├── app.py
├── dataset/
│   └── student_data.csv
├── model/
├── templates/
│   └── index.html
├── .gitignore
└── README.md
```

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/student-performance-prediction.git
cd student-performance-prediction
```

### 2️⃣ Install dependencies

```
pip install flask pandas scikit-learn numpy
```

### 3️⃣ Run the application

```
python app.py
```

### 4️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## 📊 Dataset

The dataset contains:

* Study Hours
* Attendance Percentage
* Previous Exam Score
* Final Score

✔️ Synthetic dataset generated to simulate real-world student performance patterns.

---

## 🔮 API Endpoint

**POST** `/api/predict`

### Request Body:

```
{
  "study": 5,
  "attendance": 85,
  "previous": 70
}
```

### Response:

```
{
  "predicted_marks": 78.5
}
```

---

## 💡 Future Improvements

* Add user authentication (login/signup)
* Use larger real-world dataset
* Improve model accuracy with advanced algorithms
* Deploy using cloud platforms (AWS/Render)

---

## 👨‍💻 Author

**Siddhant Dongre**
Developed as a Full Stack Machine Learning Project

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!

