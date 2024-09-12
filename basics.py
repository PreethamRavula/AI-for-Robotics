import random
import matplotlib.pyplot as plt 

class Wall_E:
    def __init__(self):
        self.paths = ['AC1', 'ADF1', 'BEGF1', 'BEGFDAC1', 'ACF2', 'ADF2', 'BEGF2', 'BEG3', 'ACFG3', 'ADFG3', 'B4', 'ACFGEB4', 'ADFGEB4'] #wheneve class is instantiated assigns the particular instance variable to the sample space

    def find_event(self, event):
        paths_contained = []
        for path in self.paths: # parse through all paths
            contained = True    # set contained to True  
            for room in event:  # parse tthrough rooms passed in an event
                if (room in path) == False: # if any of the room is not present in the path that event doesn't occur break the loop after setting contained to False
                    contained = False
                    break
            if (contained == True): # if contained was never chnaged that means loop never broke and the current path gets added to list containing the path with certain event 
                paths_contained+=[path]
        return paths_contained # finally return all paths with certain event

    def frequentist_probability(self, num_trials=10000, seed=None):
        if seed is not None:
            random.seed(seed)
        path_counts = {path:0 for path in self.paths}

        for _ in range(num_trials):
            chosen_path = random.choice(self.paths)
            path_counts[chosen_path] += 1

        probabilities = {path: count/num_trials for path, count in path_counts.items()}

        return probabilities

    def plot_histogram(self, probabilities=None, **kwargs):

        if probabilities==None:
            probabilities=self.frequentist_probability(**kwargs)

        paths = list(probabilities.keys())
        probs = list(probabilities.values())

        plt.figure(figsize=(10, 6))
        plt.bar(paths, probs, color='skyblue')
        plt.title('Probabilities of Wall-E Path Selections')
        plt.xlabel('Path')
        plt.ylabel('Probability')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

wall_e = Wall_E() # create an instance of Wall_E class
# event_name = '14'
# events = wall_e.find_event(event_name) # call the find_event function with the instance of class 
# print(f"The paths with specified event {event_name} present are: ", events)
# Plot histogram
wall_e.plot_histogram(seed=0)