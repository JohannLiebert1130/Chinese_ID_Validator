from src.get_administrative_divisions_codes import AddressCode
from src.utils import Utils
import re


class ChineseID:
    address_code_url = 'http://www.mca.gov.cn/article/sj/xzqh//1980/'
    addr_code_dic = AddressCode.read_addr_code_from_local()

    def __init__(self, id_str):
        self.id_str = id_str

        if not self.is_valid_length():
            raise Exception("invalid ID length!")

        self.address_code = id_str[:6]
        self.birth_date_code = id_str[6:14]
        self.sequence_code = id_str[14:17]
        self.check_code = id_str[17]

    def __str__(self):
        return f"Address code:{self.address_code}\nBirth date code:{self.birth_date_code}\nsequence code:" \
               f"{self.sequence_code}\ncheck code:{self.check_code}"

    def is_valid_length(self):
        if len(self.id_str) == 18:
            return True
        else:
            return False

    def is_valid_addr_code(self):

        if self.address_code in ChineseID.addr_code_dic:
            return True
        else:
            return False

    def is_valid_birth_date(self):
        return Utils.is_valid_date(self.birth_date_code)

    def is_valid_sequence_code(self):
        p = re.compile(r'\d\d\d$')
        if p.match(self.sequence_code) is not None:
            return True
        else:
            return False

    def is_valid_check_code(self):
        sum = 0
        for i in range(17):
            sum += ((1 << (17 - i)) % 11) * int(self.id_str[i])
        print(sum)
        n = (12 - (sum % 11)) % 11
        print(n)
        if n < 10:
            return n == int(self.id_str[17])
        else:
            return self.id_str[17] == 'X'

    def is_valid_id(self):
        print(f'is valid length: {self.is_valid_length()}\n'
              f'is valid addr: {self.is_valid_addr_code()}\n'
              f'is valid birth: {self.is_valid_birth_date()}\n'
              f'is valid sequence code: {self.is_valid_sequence_code()}\n'
              f'is valid check code: {self.is_valid_check_code()}')
        if self.is_valid_length() and self.is_valid_addr_code() and self.is_valid_birth_date() \
                and self.is_valid_sequence_code() and self.is_valid_check_code():

            return True
        else:
            return False


if __name__ == '__main__':
    example = ChineseID('530121198904253359')
    # print(example)
    # example.is_valid_addr_code()
    # print(example.is_valid_sequence_code())

    print(example.is_valid_id())

    example2 = ChineseID('330183199611305027')
    print(example2.is_valid_id())

    print(ChineseID.addr_code_dic)
