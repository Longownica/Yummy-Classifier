# YummyClassifier
Classifies an image of food as yummy / not yummy,
along with the probability of yumminess.

Trained on r/foodporn and r/shittyfoodporn subreddits.

Images were scraped using https://github.com/impshum/Multithreaded-Reddit-Image-Downloader.

## Setup
```buildoutcfg
pip install fastbook
pip install torch
pip install graphviz
pip install tk
```

## Usage
Run main.py and use basic GUI: choose .jpg/.png file.

Here you can see an exemple where I tested pierogi.jpg - and well, they really do look yummy!

![output](https://user-images.githubusercontent.com/50869539/224735416-f63f66dc-3685-4bda-b72c-4089ff39dcaa.PNG)

