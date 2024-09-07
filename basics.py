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

wall_e = Wall_E() # create an instance of Wall_E class
event_name = '14'
events = wall_e.find_event(event_name) # call the find_event function with the instance of class 
print(f"The paths with specified event {event_name} present are: ", events)