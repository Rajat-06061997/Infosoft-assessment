class DataStream:
    # default constructor
    def __init__(self):
        self.sysdict = {}
    
    # returns true if input time is more than 5 for an element else returns false.
    def should_output_data_str(self,timestamp: int,data_str: str) -> bool:
        if data_str in self.sysdict.keys():
            if (timestamp - self.sysdict[data_str])>5:
                self.sysdict[data_str] = timestamp
                return True
            else:
                return False
        else:
            self.sysdict[data_str] = timestamp
            return True