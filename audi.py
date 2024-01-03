class AUDI:
    def __init__(self, model, year_start,year_stop):
        self.model = model
        self.year_start = year_start
        self.year_stop = year_stop
        
    def start(self):
        return f"Starting the {self.model} {self.year_start }"

    def stop(self):
        return f"Stopping the {self.model} {self.year_stop}"
