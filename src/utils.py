class Utils:
    @staticmethod
    def represents_int(s):
        try:
            int(s)
            return True
        except:
            return False


if __name__ == '__main__':
    iters = iter(range(1, 50))
    for i in iters:
        if i == 2:
            next(iters)
        print(i)


