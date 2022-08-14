class FuelStation:
    def __init__(self,diesel: int,petrol: int,electric: int):
        self.diesel: int = diesel
        self.petrol: int = petrol
        self.electric: int = electric
		# copy variables to compare the values when releasing slots
        self.diesel_copy: int = diesel
        self.petrol_copy: int = petrol
        self.electric_copy: int = electric
    
    def fuel_vehicle(self,fuel_type: int) -> bool:
        #allot vehicle a slot if slot is available else return False
        if fuel_type == "diesel":
            if self.diesel > 0:
                self.diesel-=1
                return True
            else:
                return False
        elif fuel_type == "petrol":
            if self.petrol > 0:
                self.petrol-=1
                return True
            else:
                return False
        elif fuel_type == "electric":
            if self.electric > 0:
                self.electric-=1
                return True
            else:
                return False
        
    def open_fuel_slot(self,fuel_type: int) -> bool:
        #empties a slot when a vehicle is removed
        if fuel_type == "diesel":
            if self.diesel < self.diesel_copy:
                self.diesel+=1
                return True
            else:
                return False
        if fuel_type == "petrol":
            if self.petrol < self.petrol_copy:
                self.petrol+=1
                return True
            else:
                return False
        if fuel_type == "electric":
            if self.electric < self.electric_copy:
                self.electric+=1
                return True
            else:
                return False