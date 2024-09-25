
# Video Game Rating Predictor

This project was made to help a fictional game development studio to maximize the customer satisfaction of their next game, by creating a video game rating predictor, that could help the studio make a better decision. The model got a 0.21 r2-score, which taught me the importance of feature engineering.


## Background

In the rapidly evolving world of video games, the ability to predict a game's rating can be invaluable for developers, marketers, and gamers alike. This project aims to leverage machine learning techniques to create a predictor that can estimate the ratings of video games based on various features such as genre, player count, and price.

The primary objective of this project is to build a predictive model that can assess the potential success of a video game prior to its release. By analyzing past data, we can identify trends and factors that contribute to high ratings, providing insights that can guide development and marketing strategies.


## Acknowledgements

- [Main Dataset, game_data_all.csv](https://www.kaggle.com/datasets/whigmalwhim/steam-releases?select=game_data_all.csv)
- [Supporting Dataset, merged_data.csv](https://www.kaggle.com/datasets/nikatomashvili/steam-games-dataset)


## Methods & Tech Stack

- **Data Pre-Processing & Exploration:** Python, Pandas, Numpy, Matplotlib, Seaborn

- **Machine Learning:** Sklearn, Scipy, Pickle

- **Deployment:** Streamlit


## Workflow

Problem Identification -> Data Understanding -> Data Preparation -> EDA -> Feature Engineering -> Model Training -> Model Evaluation -> Model Deployment -> Conclusion


## Screenshots

![Deployment Screenshot](https://github.com/weewoo2636/video_game_rating_predictor/blob/main/screenshot_1.png?raw=true)


## Output/Deployment

To see the deployed model, visit here: [link_to_deployed_model](https://huggingface.co/spaces/weewoo2636/P1M2_wilson_deployment)


## Files Overview

Here are brief descriptions of the key files in the "video_game_rating_predictor" repository:

1. **README.md**: Overview of the project, explaining its purpose to predict video game ratings using machine learning, along with a brief description of tools used.
2. **cleaned.csv**: Preprocessed dataset ready for model training.
3. **game_data_all.csv**: Original dataset containing various features of video games.
4. **main_notebook.ipynb**: Jupyter notebook detailing the steps for data exploration, feature engineering, and model training.
5. **inference_notebook.ipynb**: Notebook for testing the trained model on new data.
6. **regressor_pipeline.pkl**: Serialized machine learning model ready for deployment.
7. **deployment folder**: Contains code and configurations for deploying the model using Streamlit.
8. **url.txt**: Contains relevant URLs for resources or references.

### `/deployment` Folder

9. **`app.py`**: The main application file that contains code for the web interface where users can input game info and get the predicted rating from the trained model.
10. **`requirements.txt`**: Lists the Python dependencies and packages required to run the application and model. It ensures the deployment environment installs the correct libraries.


## Authors

- [@weewoo2636](https://www.github.com/weewoo2636)

