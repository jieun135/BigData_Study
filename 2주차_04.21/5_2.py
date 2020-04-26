class MaxLinitCalculator(Calculator):
    def add(self,val):
        self.value +=val
        if self.value>100:
            self.value = 100
