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
            print("Incorrect data format, should be YYYYMMDD")
            return False
        else:
            return True


if __name__ == '__main__':
    iters = iter(range(1, 50))
    for i in iters:
        if i == 2:
            next(iters)
        print(i)

    print(Utils.is_valid_date('20090312'))
    print(Utils.is_valid_date('200jk90312'))


