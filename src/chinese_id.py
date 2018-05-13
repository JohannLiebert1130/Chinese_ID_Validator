class ChineseID:
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
        pass

    def is_valid_birth_date(self):
        pass

    def is_valid_sequence_code(self):
        pass

    def is_valid_check_code(self):
        pass

    def is_valid_id(self):
        pass


if __name__ == '__main__':
    example = ChineseID('305020189608140115')
    print(example)

    example2 = ChineseID('1111111111111111111')
    print(example2)