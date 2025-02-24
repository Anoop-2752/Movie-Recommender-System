# 🎬 Movie Recommender System

![Image](https://github.com/user-attachments/assets/3d9828e7-1fda-4cd8-b119-db783a8b7e18)



## 📌 Project Overview
The **Movie Recommender System** is a machine learning-based web application built using **Streamlit**. It provides personalized movie recommendations based on similarity scores between movies. The system uses **content-based filtering** and fetches movie posters via the **TMDB API**.

## ⚡ Features
- ✅ **Movie Recommendation** – Get top 5 similar movies based on user selection.  
- ✅ **Poster Display** – Fetches and displays posters from **TMDB API**.  
- ✅ **User-Friendly UI** – Built using **Streamlit** for an interactive experience.  
- ✅ **Content-Based Filtering** – Uses movie similarities for recommendations.  

---

## 🛠️ Tech Stack
- **Python** 🐍  
- **Pandas** – Data handling  
- **Scikit-Learn** – Machine learning  
- **Streamlit** – Web UI  
- **TMDB API** – Fetching movie posters  
- **Pickle** – Model serialization  
- **dotenv** – Securing API keys  

---

## 🎯 Dataset & Exploratory Data Analysis (EDA)
- The dataset contains **movie titles, descriptions, genres, cast, and crew details**.
- EDA was performed using **Jupyter Notebook (`EDA.ipynb`)** to:
  - Clean and preprocess movie data  
  - Generate similarity scores  
  - Analyze distributions of genres, ratings, and keywords  

---

## 📂 Project Structure

```

│── 📂 data                  
│   ├── tmdb_5000_credits.csv
    ├─   tmdb_5000_movies.csv
│── 📂 notebook              
│   ├── eda.ipynb
    ├── preprocessed.ipynb
│── 📂 models              
│   ├── movie.pkl
    ├── similarity.pkl              
│── 📜 .gitignore             
│── 📜 README.md              
│── 📜 app.py                 
│── 📜 requirements.txt      

```


---

## 🚀 How to Run the Project

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/Movie-Recommender-System.git
cd Movie-Recommender-System
```
### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```
### Step 3 :Set Up API Key
```
Create a .env file in the project root and add:
```
### Step 4: Run the Application

```bash
streamlit run app.py
```

## 📈 Future Enhancements 

- 🚀 Add collaborative filtering for better recommendations.
- 🎭 Introduce genre-based filtering for more control.
- 🌎 Support multi-language movie recommendations.
- 📊 Improve UI with Netflix-like layout.

## 🤝 Contribution  
Contributions are welcome! Please follow these steps: 

1️⃣ **Fork the repository**

2️⃣ **Create a new branch** ```(feature-branch)```

3️⃣ **Commit your changes**  ```(git commit -m "Added new feature")```

4️⃣ **Push to GitHub and submit a Pull Request**

## 📜 License
This project is licensed under **MIT License**.
