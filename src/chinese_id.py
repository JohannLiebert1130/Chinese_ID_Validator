from src.get_administrative_divisions_codes import AddressCode
from src.utils import Utils
import re


class ChineseID:
    address_code_url = 'http://www.mca.gov.cn/article/sj/xzqh//1980/'
    addr_code_dic = AddressCode.get_latest_addr_code(address_code_url)

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
        pass

    def is_valid_id(self):
        pass


if __name__ == '__main__':
    example = ChineseID('330225189608140005')
    print(example)
    example.is_valid_addr_code()
    print(example.is_valid_sequence_code())
