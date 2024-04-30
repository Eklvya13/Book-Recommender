
# Book-Recommender (v1.1) ![MIT License](https://img.shields.io/badge/License-MIT-green.svg)

This is a simple web-app which recommends books based on the user input.

Web Application : https://recommendbookapp.herokuapp.com (Disabled)

Video URL : not present



## Requirements

- Python (3.10 or newer)
- Streamlit
- Numpy & Pandas
- Pickle

## Alternatively (using a Docker container)

- Docker Engine
- Docker CLI

## Files

- app.py - Main file which contains the backend as well as the front end part of the App 

- .pkl files - These files contain the required dictionaries and list which are used to fetch recommendations and book details.

- requirements.txt - contains names of libraries used

- Dataset & Manipulation
    - books.csv - contains onformation of more than 16,000 books
    - Dataset Manipulation.ipynb - Contains all the commands run on jupyter notebook to clean and filter out the dataset. It is where the 2 pickle files are generated.

- .streamlit - folder containing streamlit config (theme)

- Dockerfile - Useful for building own Docker image

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

- [Docker](https://www.docker.com/)

- [Docker-Hub](https://hub.docker.com/)

## Working Principal

To make Good recommendations I needed more Information about the book than just its title , author & genre.
I specefically looked for a dataset which contains description,sample etc. of the books which would allow the software to make a more educated recommendation as more data is present which can diffrentiate on book from another.
now that I have a good dataset . I can perform the following tasks:

- Filtering out incomplete/ NULL entries : using numpy's and pandas' functions i cleaned out the data to make it workable and ready for the next step. (please look up the .ipynb file for code and detailed explanations.
- Using Stem function to look for words with similar meaning. for ex: ['Love', 'Loved', 'loving'].stem() returns ['Love', 'Love', 'Love']
- Now that the data is cleaned 5000 most common word from thier description are taken and all the books are plotted on a 5000 dimentional space with each of thier coordinates the frequence of those 5000 words.
- After plotting the nearest 5 points to the selected point are the recommendations. These are found via the function cosine_similarity.
- Top 5 sorted similarities of each of the books are converted into a picle file for use in the app.py.
- app.py simply takes input title , gets its index and fetches recommendations.
- Each of the titles of these recommendations are used in GET request to give thies Thumbnail src link which is displayed along with name and title.
- The frontend is via Streamlit 


## Deployment

To deploy this project run

Manually:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Using Docker:
    Build Own image:
```bash
docker build -t image_name .
docker run -p 8501:8501 image_name
```

Pull Docker Image from public repo:
```bash
docker pull <>
docker run -p 8501:8501 image_name
```
App hosted on : http://localhost:8501
