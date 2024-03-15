class DataTypes:
    @staticmethod
    def hex2bin(s):
        mp = {'0': "0000", '1': "0001", '2': "0010", '3': "0011",
              '4': "0100", '5': "0101", '6': "0110", '7': "0111",
              '8': "1000", '9': "1001", 'A': "1010", 'B': "1011",
              'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"}
        bin = ""
        for i in range(len(s)):
            bin = bin + mp[s[i]]
        return bin

    @staticmethod
    def bin2hex(s):
        mp = {"0000": '0', "0001": '1', "0010": '2', "0011": '3',
              "0100": '4', "0101": '5', "0110": '6', "0111": '7',
              "1000": '8', "1001": '9', "1010": 'A', "1011": 'B',
              "1100": 'C', "1101": 'D', "1110": 'E', "1111": 'F'}
        hex = ""
        for i in range(0, len(s), 4):
            ch = s[i:i+4]
            hex = hex + mp[ch]
        return hex

    @staticmethod
    def dec2bin(n):
        return bin(n).replace("0b", "")

    @staticmethod
    def bin2dec(b):
        return int(b, 2)

    @staticmethod
    def dec2hex(n):
        return hex(n).replace("0x", "")

    @staticmethod
    def hex2dec(h):
        return int(h, 16)