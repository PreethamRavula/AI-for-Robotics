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

class Event:
    def __init__(self, event_list):
        self.event_list = event_list

    def intersection(self,other_event):
        intersection_event = [element for element in self.event_list if element in other_event.event_list]
        return Event(intersection_event)  

    def union(self,other_event):
        union_event = list(set(self.event_list) | set(other_event.event_list))   
        return Event(union_event)

    def complement(self, sample_space):
        complement_event = [element for element in sample_space if element not in self.event_list]
        return Event(complement_event)

wall_e = Wall_E()

event_1_name='A1'
event_1=wall_e.find_event(event_1_name)

print(f"Combined events containing {event_1_name}: ", event_1)

event_2_name = 'BEGF1'
event_2 = wall_e.find_event(event_2_name)

print(f"Combined events containing {event_2_name}: ", event_2)

event1 = Event(event_1)
event2 = Event(event_2)

# Intersection of events
intersection = event1.intersection(event2)
print("Intersection of events: ", intersection.event_list)

# Union of events
union = event1.union(event2)
print("Union of events: ", union.event_list)

# Complement of event1 with respect sample space
complement = event1.complement(wall_e.paths)
print("Complement of event1: ", complement.event_list)