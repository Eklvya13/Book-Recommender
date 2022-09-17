
# Book-Recommender ![MIT License](https://img.shields.io/badge/License-MIT-green.svg)

This is a simple web-app which recommends books based on the user input.

Web Application : https://recommendbookapp.herokuapp.com




## Requirements

- Python (3.10 or newer)
- Streamlit
- Numpy & Pandas
- Pickle



## Files

- app.py - Main file which contains the backend as well as the front end part of the App 

- .pkl files - These files contain the required dictionaries and list which are used to fetch recommendations and book details.

- requirements.txt - contains names of libraries used

- Dataset & Manipulation
    - books.csv - contains onformation of more than 16,000 books
    - Dataset Manipulation.ipynb - Contains all the commands run on jupyter notebook to clean and filter out the dataset. It is where the 2 pickle files are generated.

- .streamlit - folder containing streamlit config (theme)

## API Reference

Uses [Google Books Public API](https://developers.google.com/books).

#### Search for a book


| Parameter    | Type     | Description                |
| :--------    | :------- | :------------------------- |
| `Book_title` | `string` | **Required**. Title of searched volume   |

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `api_key`      | `string` | **Optional**. For usage analysis |

#### Get item

```http
    GET https://www.googleapis.com/books/v1/volumes?q=<Book_title><api_key>

```



returns a json file containing volumes and thier info.



## Documentations for used libraries

- [Numpy](https://pypi.org/project/numpy/)

- [Pandas](https://pypi.org/project/pandas/)

- [Streamlit](https://linktodocumentation)

- [Nltk](https://www.nltk.org/)
    - PorterStemmer

- [ast](https://docs.python.org/3/library/ast.html)

- [Scikit Learn](https://scikit-learn.org/stable/index.html)
    - CountVectorizer (feature_extraction > text)
    - cosine_similarity (metrics > pairwise)
- [Pickle](https://pypi.org/project/pickle5/)


## Deployment

To deploy this project run

```bash
  streamlit run app.py
```

