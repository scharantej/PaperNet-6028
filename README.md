## Flask Application Design for Recent Newspaper Article Website

### HTML Files

- **`index.html`** - This will be the home page of the website, displaying a list of recent newspaper articles. It will include an HTML table with columns for the article title, author, date published, and a link to the full article. It may also include a search bar for filtering the articles.

- **`article.html`** - This HTML file will display the full content of a single newspaper article. It will include the article's title, author, date published, and the article's text.

### Routes

- **`@app.route('/')`** - This route will handle the home page of the website and will render the `index.html` file.

- **`@app.route('/article/<int:article_id>')`** - This route will handle requests for individual newspaper articles and will render the `article.html` file, passing in the `article_id` as a parameter to retrieve the corresponding article from the database.

- **`/search`** - This route will handle search requests and will filter the list of articles based on the search criteria entered by the user. It will render the `index.html` file with the filtered list of articles.