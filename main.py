
# Import necessary modules
from flask import Flask, render_template, request

# Create a Flask application
app = Flask(__name__)

# Sample data for articles
articles = [
    {
        "id": 1,
        "title": "Article 1",
        "author": "Author 1",
        "date_published": "2023-01-01",
        "content": "This is the content of Article 1."
    },
    {
        "id": 2,
        "title": "Article 2",
        "author": "Author 2",
        "date_published": "2023-01-02",
        "content": "This is the content of Article 2."
    },
    {
        "id": 3,
        "title": "Article 3",
        "author": "Author 3",
        "date_published": "2023-01-03",
        "content": "This is the content of Article 3."
    }
]

# Define the home page route
@app.route('/')
def home():
    """
    Renders the home page with a list of recent newspaper articles.

    Returns:
        rendered home page
    """
    return render_template('index.html', articles=articles)


# Define the article page route
@app.route('/article/<int:article_id>')
def article(article_id):
    """
    Renders the full content of a single newspaper article.

    Args:
        article_id: the id of the article to display

    Returns:
        rendered article page
    """
    article = next((article for article in articles if article["id"] == article_id), None)

    if article:
        return render_template('article.html', article=article)
    else:
        return "<h1>Article not found</h1>"


# Define the search route
@app.route('/search', methods=['GET'])
def search():
    """
    Filters the list of articles based on the search criteria entered by the user.

    Returns:
        rendered home page with filtered articles
    """
    search_term = request.args.get('search_term')

    filtered_articles = [article for article in articles if search_term in article["title"]]

    return render_template('index.html', articles=filtered_articles)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
