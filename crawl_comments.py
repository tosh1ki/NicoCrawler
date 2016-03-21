#!/usr/bin/env python
# -*- coding: utf-8 -*-


__doc__ = '''
Crawl comment from nicovideo.jp

Usage:
    crawl_comments.py [--sqlite <sqlite>] [--csv <csv>]

Options:
    --sqlite <sqlite>  (optional) path of comment DB [default: comments.sqlite3]
    --csv <csv>        (optional) path of csv file contains urls of videos [default: crawled.csv]
'''


from docopt import docopt

from nicocrawler.nicocrawler import NicoCrawler


if __name__ == '__main__':

    # コマンドライン引数の取得
    args = docopt(__doc__)
    path_sqlite = args['--sqlite']
    path_csv = args['--csv']

    ncrawler = NicoCrawler()
    ncrawler.connect_sqlite(path_sqlite)

    url = 'http://ch.nicovideo.jp/2016winter_anime'
    df = ncrawler.get_all_video_url_of_season(url)
    ncrawler.initialize_csv_from_db(path_csv)

    # # デイリーランキング1~300位の動画を取得する
    # url = 'http://www.nicovideo.jp/ranking/fav/daily/all'
    # ncrawler.initialize_csv_from_url(url, path_csv, max_page=3)

    # ncrawler.get_all_comments_of_csv(path_csv, max_n_iter=1)
