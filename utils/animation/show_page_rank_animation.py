from manim import *
import json

class ShowPageRank(Scene):
    def construct(self):
        links, scores = self.load_logs()
        link_indexes = self.get_link_indexes(links)
        
        group_circles, group_texts, coords = self.create_circles_and_labels(n=len(scores))
        group_lines = self.create_lines(coords=coords, indexes=link_indexes)
        group_scores = self.create_score_mobjects(scores)

        self.play(group_circles, run_time=3)
        self.wait()
        self.play(group_lines, run_time=1)
        self.wait()
        self.play(group_texts, run_time=1)
        self.wait()
        self.play(group_scores, run_time=1)
        self.wait(2)
        
    def create_circles_and_labels(self, n: int):
        """Circle and their corresponding labels are initiated"""
        coords = np.array([0, 3])
        circles = []
        texts = []
        coords_list = []
        angle = 2 * np.pi / n

        for i in range(1, n + 1):
            circle = Circle(radius=0.5)
            circle.set_coord(coords[0], 0)
            circle.set_coord(coords[1], 1)
            text = Text(str(i), fill_opacity=1.0, font_size=48)
            
            coord_circle = circle.get_center()
            text.move_to(coord_circle)

            circles.append(Create(circle))
            texts.append(Create(text))
            coords_list.append(coord_circle)
            
            coords = self.estimate_coord(coords, angle)

        group_circles = AnimationGroup(*circles)
        group_texts = AnimationGroup(*texts)

        return group_circles, group_texts, coords_list
    
    def create_lines(self, coords, indexes):
        """Lines - Links are created to be drawn"""
        lines = []
        for index in indexes:
            line = Line(coords[index[0]], coords[index[1]])
            lines.append(Create(line))
        group = AnimationGroup(*lines)
        return group

    def create_score_mobjects(self, scores):
        """Group of moobjecs are created to exhibit scores"""
        n = len(scores)
        step = 6 / n

        labeled_scores = self.get_scores_with_labels(scores)
        texts = []
        coord = [-6, 3]
        for label, score in labeled_scores:
            text = Text("{}: {}".format(label, score), fill_opacity=1.0, font_size=24)
            text.set_coord(coord[0], 0)
            text.set_coord(coord[1], 1)
            texts.append(Create(text))

            coord[1] -= step

        group = AnimationGroup(*texts)
        return group
    
    def estimate_coord(self, init_coord: np.ndarray, angle: float):
        """Estimating the next coordinate with the transformation by a certain angle"""
        # rotation matrix
        R = np.array(
            [[np.cos(angle), -np.sin(angle)], 
            [np.sin(angle), np.cos(angle)]
            ]
            )
        next_coord = R.dot(init_coord)
        return next_coord

    def get_link_indexes(self, links):
        """original link notations are converted to subscriptable objects - lists"""
        indexes = [[int(link[0]) - 1, int(link[1]) - 1] for link in links]
        return indexes
    
    def get_scores_with_labels(self, scores):
        labeled_scores = list(
            zip(
                list(range(1, len(scores) + 1)), 
                scores
                )
                )
        labeled_scores.sort(key=lambda x: x[1], reverse=True)
        return labeled_scores
    
    def load_logs(self):
        """Loading the logs saved by PageRank algorithm."""
        with open("./logs/logs.json", "r") as f:
            data = json.load(f)
            scores = data["scores"]
            links = data["links"]
        return links, scores
    