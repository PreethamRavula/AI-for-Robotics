class Wall_E:
    def __init__(self):
        self.paths = ['AC1', 'ACF2', 'ADF1', 'ADF2', 'ADFG3', 'ADFG3', 'BEGFDAC1', 'BEGF2', 'BEGF1', 'BEG3', 'B4', 'ADFGEB4', 'ACFGEB4']
    
    def find_event(self, event):
        paths_contained = []
        for path in self.paths:
            contained = True
            for room in event:
                if (room in path) == False:
                    contained = False
                    break

            if (contained == True):
                paths_contained += [path]
        return paths_contained

wall_e = Wall_E()

event_name = '14'
events = wall_e.find_event(event_name)
print(f"Events containing {event_name}", events) 