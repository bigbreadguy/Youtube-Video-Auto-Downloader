import os
import json

from html.parser import HTMLParser

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

import pytube

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options, api_key):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
        developerKey=api_key)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        publishedAfter=options.published_after,
        q=options.q,
        type=options.type,
        part="id,snippet",
        maxResults=options.max_results
    ).execute()

    search_res_dict = dict()

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            search_res_dict[search_result["snippet"]["title"]] = search_result["id"]["videoId"]

    return search_res_dict

def youtube_video(options, URLParser, api_key):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
        developerKey=api_key)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.videos().list(
        part="snippet,player,statistics",
        id=options.id
    ).execute()

    search_res_dict = dict()

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
        URLParser.feed(str(search_result["player"]["embedHtml"]))
        url = URLParser.src
        ins_dict = {"url" : url, "viewCount" : search_result["statistics"]["viewCount"]}
        search_res_dict[search_result["snippet"]["title"]] = ins_dict

    return search_res_dict

def download(url, save_dir : str):
    yt = pytube.YouTube(url)

    videos = yt.streams.filter(progressive=True, file_extension="mp4")\
                .order_by("resolution")

    videos[0].download(save_dir)

class URLParser(HTMLParser):
    def __init__(self):
        super(URLParser, self).__init__()
        self.src = ""

    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if attr[0] == "src":
                self.src = "https:" + attr[1]