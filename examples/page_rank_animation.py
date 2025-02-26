from applications.PageRank import PageRank
from utils.animation import ShowPageRank
from manim import *

pagerank = PageRank(n_pages=7, n_fraction=0.6, filepath="./logs/logs.json")
links, scores = pagerank.run()
print("Algorithm run")

ShowPageRank().render(True)
