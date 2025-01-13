<h1 align="center">🎥 Movie Recommender System 🎥</h1>

---

<h2 align="left">➡️ Visit the Application</h2>

[![Click Me](https://img.shields.io/badge/Click-Me-blue?style=for-the-badge)](https://movie-recommender-system-oki4.onrender.com)

---

<h2 align="left">➡️ Description</h2>

A simple **`Movie Recommender System`** built with Streamlit. It suggests movies based on a selected movie using pre-trained similarity data and fetches movie posters from the TMDB API.

---

<h2 align="left">🚀 Features</h2>

- Recommends **5 similar movies** based on your selected movie.
- Fetches **movie posters** dynamically from the TMDB API.
- Interactive and user-friendly **web interface** powered by Streamlit.
- **`Technologies Used`**: Python, Scikit-learn, Pandas, Matplotlib/Seaborn for visualization

---

<h2 align="left">📂 Project Structure</h2>

```plaintext
.
├── app.py                  # Main Streamlit app
├── movies_dict.pkl         # Pre-trained movie data
├── similarity.pkl          # Pre-trained similarity matrix
└── README.md               # Project documentation
```

---

<h2 align="left">🛠️ Setup Instructions</h2>

### `Prerequisites`

- Python 3.7 or later
- Required libraries:
  ```bash
  pip install -r requirements.txt
  ```
- A `TMDB API Key`. Sign up at [The Movie Database](https://www.themoviedb.org/) to get one.

### `Installation`

1. Clone the repository:
   ```bash
   git clone https://github.com/MrGenius18/Movie_Recommender_System.git
   cd Movie_Recommender_System
   ```

2. Add your TMDB API key to the code:
   Open `app.py` and replace `YOUR_TMDB_API_KEY` with your actual API key.

3. Run the application:
   ```bash
   streamlit run app.py
   ```

4. Access the app in your browser at `http://localhost:8501`.

---

<h2 align="left">✨ Demo</h2>

![Movie Recommender System Screenshot](https://github.com/MrGenius18/Movie_Recommender_System/blob/99c474f9472bfbf5ed405f7b063aa7360c633446/app%20demo.png)

---

<h2 align="left">📊 Data</h2>

- The movie data (`movies_dict.pkl`) and similarity matrix (`similarity.pkl`) were pre-trained using a dataset.
- Ensure these files are included in your project directory for the app to work.

---

<h2 align="left">🤝 Contributing</h2>

Contributions are welcome! Feel free to submit a pull request or open an issue to improve the project.

---

<h2 align="left">⭐ Acknowledgments</h2>

- [Streamlit](https://streamlit.io/) for providing an amazing framework.
- [TMDB API](https://www.themoviedb.org/documentation/api) for movie data and posters.

---
