import sys
sys.path.append("../../")
import numpy as np
import json
from scipy.special import comb
from collections import Counter
from utils.random_pages import return_pages_and_connetions
from utils.eigen import eig

class PageRank:
    def __init__(self, n_pages: int, n_fraction: float, filepath: str):
        links_total = comb(n_pages, 2)
        links_required = int(links_total * n_fraction)
        pages, links = return_pages_and_connetions(n_pages=n_pages, n_connections=links_required)
        self.pages = pages
        self.links = links
        self.filepath = filepath

    def get_probability_map(self, index_map):
        """Generating Markov matrix"""
        probs_map = np.zeros((len(self.pages), len(self.pages)))
        for page, index_arr in index_map.items():
            if (index_arr.sum()) == 0:
                continue
            probs_map[index_arr == 1, int(page) - 1] = 1 / index_arr.sum()
        return probs_map
    
    def __get_index_map(self):
        index_map = {page: np.array([0.0] * len(self.pages)) for page in self.pages}
        return index_map

    def get_counted_links_and_map(self):
        _counter = dict(zip(self.pages, len(self.pages) * [0]))

        # the variable will be removed in the next update
        links_counted = Counter(_counter)
        index_map = self.__get_index_map()
        
        for link in self.links:
            page_1, page_2 = link
            links_counted[page_1] = links_counted[page_1] + 1
            links_counted[page_2] = links_counted[page_2] + 1
            
            # Changing the index value of the corresponding page
            row = index_map[page_1]
            row[int(page_2) - 1] = 1
            row = index_map[page_2]
            row[int(page_1) - 1] = 1

        return index_map
    
    def run(self):
        index_map = self.get_counted_links_and_map()
        probs_map = self.get_probability_map(index_map)
        _, eigen_vectors = eig(probs_map)
        
        scores = np.abs(eigen_vectors[:, 0])
        scores = (scores - scores.min()) / (scores.max() - scores.min()) * 95 + 5
        scores = scores.astype(np.int16)
        self.save(scores)
        return self.links, scores
    
    def save(self, scores):
        log = {
            "scores": scores.tolist(),
            "links": self.links.tolist()
        }
        with open(self.filepath, "w") as f:
            json.dump(log, f)

if __name__ == "__main__":
    pagerank = PageRank(n_pages=9, n_fraction=0.3, filepath="./logs.json")
    links, scores = pagerank.run()
    print(scores)
    print(links)

