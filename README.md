# Youtube Video Auto Downloader
 download youtube videos automatically

## Introduction
 This Document is Intended for you who want to Use this Humble Repository</br>
 to Automatically Download Youtube Videos along Presetted Queries.</br>
 </br>
 The Scripts Use Youtube Data Api for Searching Videos and Getting Source URLs.</br>
 To Download Videos from URLs, a Brilliant Package Called **pytube** have been Used.</br>
 </br>

## Getting Started

### 1. Clone the Repository
 ```
 pip install -r requirements.txt
 ```
 </br>

### 2. Install All the Requirements
 ```
 pip install -r requirements.txt
 ```
 </br>

### 3. Get a Youtube Data API Key and Store it
 Follow the Instroduction of [Youtube Data API Guide](https://developers.google.com/youtube/v3/getting-started) to Get your API Key.</br>
 Create a File Named **secret.py** in the Origin Directory.</br>
 secret.py is Included in .gitignore List, so Don't Worry about Push Mistakes.</br>
 Open secret.py and Store your API Key as below.</br>
 ```
 API_KEY = "YOUR_API_KEY"
 ```

</br>

### 3. Run
 **Step 1**</br>
 ```
 python search_video.py
 ```
 You can Edit a List Variable Named **queries** before Run this Script to Preset Search Queries for Video Search.</br>

 **Step 2**</br>
 ```
 python download_video.py
 ```
 </br>