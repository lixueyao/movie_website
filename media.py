# coding=UTF-8
import webbrowser

class Movies():
    def __init__(self, title, movie_storyline, poster_image_url, trailer_youtube_url):
        """初始化电影

        keyword arguments:
        title -- 电影名称
        movie_storyline -- 电影简介
        poster_image_url -- 海报播放路径
        trailer_youtube_url -- 预告路径
        """
        self.title = title
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """播放电影预告"""
        webbrowser.open(self.trailer_youtube_url)
