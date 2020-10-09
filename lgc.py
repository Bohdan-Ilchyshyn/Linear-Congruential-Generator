class LCG:

    def __init__(self, m=2 ** 17 - 1, a=4 ** 3, c=21, seed=256):
        self.m = m
        self.a = a
        self.c = c
        self.seed = seed
        self.numbers_list = [seed]

    def _lcg(self, x):
        return (self.a * x + self.c) % self.m

    def get_current(self):
        return self.numbers_list[-1]

    def get_next(self):
        x = self._lcg(self.numbers_list[-1])
        self.numbers_list.append(x)
        return self.numbers_list[-1]

    def generate_n_numbers(self, n: int):
        for i in range(n-1):
            self.get_next()
        return self.numbers_list

    def get_period(self) -> int:
        try:
            x = self.seed
            count = 0
            while x != self.seed:
                x = self._lcg(x)
                count += 1
            return count
        except:
            return -1

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for num in self.numbers_list:
                file.write(str(num) + '\n')
