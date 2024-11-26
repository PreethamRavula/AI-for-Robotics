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

# Initialize Wall-E
wall_e = Wall_E()

# Find combined events containing 'A1'
event_name='A1'
events=wall_e.find_event(event_name)
print(f"Combined events containing {event_name} : ", events)
