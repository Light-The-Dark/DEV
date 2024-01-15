class TEST():
    def __init__(self) -> None:
        self.number = 5

    def breathe(self):
        print("breathing")

class TEST2(TEST):
    def __init__(self) -> None:
        super().__init__()
    
    def breathe(self):
        super().breathe()
        print("TEST @")

a = TEST2()

a.breathe()