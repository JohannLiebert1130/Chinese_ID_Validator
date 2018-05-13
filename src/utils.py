import datetime


class Utils:
    @staticmethod
    def represents_int(s):
        try:
            int(s)
            return True
        except:
            return False

    @staticmethod
    def is_valid_date(date_text):
        try:
            datetime.datetime.strptime(date_text, '%Y%m%d')
        except:
            raise ValueError("Incorrect data format, should be YYYYMMDD")


if __name__ == '__main__':
    iters = iter(range(1, 50))
    for i in iters:
        if i == 2:
            next(iters)
        print(i)

    Utils.is_valid_date('20090312')


