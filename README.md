# Movie_Recommendation_System

This is a movie recommender system built with Streamlit. It uses the TMDB 5000 movies dataset and the cosine similarity algorithm to recommend movies that are similar to the selected movie.

To run the app, clone the repository and install the dependencies. Then, run the following command:

```
streamlit run app.py
```

The app will open in your browser. You can then select a movie from the dropdown and click the "Show Recommendations" button to see a list of recommended films.

The app also uses Streamlit's custom CSS styling to add a background image to the report view.

Here is a step-by-step explanation of the code:

1. The `fetch_poster()` function fetches the poster image for a given movie.
2. The `recommend()` function recommends movies that are similar to the selected movie. It does this by first finding the index of the selected film in the `movies` data frame. Then, it sorts the similarity scores for the selected movie and returns the names and posters of the top 5 movies.
3. The `main()` function loads the `movies` and `similarity` data frames from pickle files. It then displays the app title and description, and a dropdown menu for selecting a movie. When the user clicks the "Show Recommendations" button, the `recommend()` function is called and the results are displayed.
4. The `st.markdown()` function is used to add text and HTML to the app. The `st.selectbox()` function is used to create a dropdown menu. The `st.image()` function is used to display an image.
5. The `st.columns()` function is used to create a layout with five columns.
6. The `st.background()` function is used to add a background image to the report view.

I hope this helps!
