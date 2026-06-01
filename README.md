# Movie Recommendation System

A content-based movie recommender built on the [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata). Pick a movie you like and get five similar titles based on genres, keywords, plot, cast, and director.

## Features

- **Content-based filtering** — recommendations from movie metadata, not user ratings
- **Rich feature tags** — combines overview, genres, keywords, top cast, and director into a single text profile per film
- **Streamlit web UI** — search by title and view top 5 recommendations
- **Precomputed similarity** — fast lookups via pickled model artifacts

## How it works

1. **Data prep** (`model.ipynb`): Merge TMDB movies and credits, clean JSON fields (genres, keywords, cast, crew), and build a `tags` string per movie.
2. **Text processing**: Lowercase tokens, Porter stemming (NLTK), and join into one document per movie.
3. **Vectorization**: `CountVectorizer` (max 5,000 features, English stop words) turns tags into sparse vectors.
4. **Similarity**: Cosine similarity between all movie vectors is stored in `similarity.pkl`.
5. **Inference** (`app.py`): For the selected title, rank movies by similarity and return the top 5 (excluding the query movie).

## Project structure

```
Movie-Recommendation-System/
├── app.py              # Streamlit recommendation UI
├── model.ipynb         # Data processing and model training
├── main.py             # Placeholder entry point
├── movies.pkl          # Processed movie dataframe (generated)
├── similarity.pkl      # Cosine similarity matrix (generated)
├── pyproject.toml      # Dependencies (uv/pip)
└── .python-version     # Python 3.13
```

> `*.pkl` files are gitignored. Generate them by running `model.ipynb`, or obtain them from a teammate/release.

## Requirements

- Python **3.13+**
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/itsanaskhanz/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

### 2. Install dependencies

With **uv**:

```bash
uv sync
```

With **pip**:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e .
```

### 3. Download the dataset

Place these CSV files in the project root (from [Kaggle — TMDB 5000](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) or equivalent):

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

### 4. Train the model (if you don't have `.pkl` files)

Open and run all cells in `model.ipynb`. This creates:

- `movies.pkl` — dataframe with `movie_id`, `title`, and processed `tags`
- `similarity.pkl` — pairwise cosine similarity matrix (~180 MB)

### 5. Run the app

```bash
uv run streamlit run app.py
```

Or with an activated venv:

```bash
streamlit run app.py
```

Open the URL shown in the terminal (usually `http://localhost:8501`), choose a movie, and click **Recommend**.

## Tech stack

| Component       | Library               |
| --------------- | --------------------- |
| UI              | Streamlit             |
| Data / ML       | pandas, scikit-learn  |
| NLP             | NLTK (Porter stemmer) |
| Notebook        | Jupyter               |
| Package manager | uv                    |

## Example

Selecting **Avatar** might suggest other sci-fi / adventure films with overlapping cast, themes, and plot keywords—because similarity is driven by the combined tag text, not collaborative filtering.

## Author

[itsanaskhanz](https://github.com/itsanaskhanz)
