import numpy as np
from itertools import combinations
from typing import Union, Tuple, List

def initiailize_combinations(n) -> Tuple[List, np.ndarray]:
    if n <= 0 or n >= 10:
        raise ValueError("n should be between 1 and 9, not {}".format(n))
    
    # Initializing individual pages' labels.
    pages = list(map(str, range(1, n + 1)))

    # Generating all possibles paired links between pages
    links = list(combinations(pages, 2))
    links = np.array(
        ["".join(link) for link in links]
        )
    return pages, links

def random_selection(links: np.ndarray, n: int) -> np.ndarray:
    indexes = list(range(len(links)))
    indexes_chosen = np.random.choice(indexes, n, replace=False)
    return links[indexes_chosen]

def return_pages_and_connetions(n_pages: int, n_connections: int) -> Tuple[List, np.ndarray]:
    pages, links = initiailize_combinations(n=n_pages)
    links = random_selection(links, n_connections)
    return pages, links

if __name__ == "__main__":
    pages, links = return_pages_and_connetions(n_pages=5, n_connections=5)
    print(links)