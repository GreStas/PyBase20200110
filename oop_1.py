class Shop:
    open_at = '08:00'
    close_at = '22:00'

    def __init__(self, name, open_at=None, close_at=None):
        self.name = name
        if open_at:
            self.open_at = open_at
        if close_at:
            self.close_at = close_at

    def printing(self):
        print(f"{self.name} открыт с {self.open_at} по {self.close_at}")

aushan = Shop('Ашан', close_at='24:00')

result = aushan.printing()

print(result)