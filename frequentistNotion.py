import random
import matplotlib.pyplot as plt 

class Wall_E:
    def __init__(self):
        self.paths = ['AC1', 'ADF1', 'BEGF1', 'BEGFDAC1', 'ACF2', 'ADF2', 'BEGF2', 'BEG3', 'ACFG3', 'ADFG3', 'B4', 'ACFGEB4', 'ADFGEB4']

    def find_event(self, event):
        paths_contained=[]
        for path in self.paths:
            contained = True
            for room in event:
                if (room in path) == False:
                    contained=False
                    break
            
            if contained==True:
                paths_contained+=[path]
        return paths_contained

    def frequentist_probability(self, num_trials=10000, seed=None):
        if seed is not None:
            random.seed(seed)
        path_counts = {path: 0 for path in self.paths}

        for _ in range(num_trials):
            chosen_path = random.choice(self.paths)
            path_counts[chosen_path] += 1

        probabilities = {path: count/num_trials for path, count in path_counts.items()}
        return probabilities

    def plot_histogram(self, probabilities=None, **kwargs):
        if probabilities == None:
            probabilities = self.frequentist_probability(**kwargs)

        paths = list(probabilities.keys())
        probs = list(probabilities.values())

        plt.figure(figsize=(10, 6))
        plt.bar(paths, probs, color='skyblue')
        plt.title('Probabilities of Wall-E Path Selection')
        plt.xlabel('Path')
        plt.ylabel('Probability')
        plt.xticks(rotation=45,ha='right')
        plt.tight_layout()
        plt.show()

wall_e = Wall_E()

wall_e.plot_histogram(seed=0)

