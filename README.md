# Movie Suggester Based on Emotions
This Python code allows you to generate movie suggestions based on different emotions. The code uses the requests library to send HTTP requests and BeautifulSoup to parse the HTML content of an IMDb genre page. It extracts movie titles from the parsed data using regular expressions and then randomly suggests a movie title from the list.

### Emotions
The code starts by printing a list of emotions, which include "normal", "hatred", and "depressed". If the user inputs any other emotion, the code returns an "Invalid" response.

### Main Function
The main() function takes an emotion as input and suggests a movie based on that emotion. Depending on the emotion, the function sets a specific IMDb genre link to scrape movie titles from. It then sends an HTTP request to get the content of the genre page and parses the data using BeautifulSoup. The function extracts the movie titles from the parsed data using regular expressions and stores them in a list. Finally, it randomly suggests a movie title from the list.

### How to Use
To use this code, simply run the Python script and input an emotion when prompted. The code will suggest a movie title based on the given emotion. If no movies are found for the given emotion, the code will return a "No movies found for this emotion" response.
