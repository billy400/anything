from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('bilal.html', )

@app.route('/recommendation')
def recommendation():
    return render_template('index.html',)

@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.form['movie']
    # Call the API to get movie recommendations
    recommendations = get_movie_recommendations(user_input)
    return render_template('index.html', movie=user_input, recommendations=recommendations)

def get_movie_recommendations(movie_name):
    api_key = '70ae3aaf'
    url = f'http://www.omdbapi.com/?apikey={api_key}&s={movie_name}'
    response = requests.get(url)
    data = response.json()  # Corrected indentation
    recommendations = []
    if 'Search' in data:
        for movie in data['Search'][:10]:  # Get top 10 recommendations
            recommendations.append(movie['Title'])
    return recommendations

if __name__ == '__main__':  # Corrected main check
    app.run(debug=True)

