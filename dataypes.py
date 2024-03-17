class DataTypes:
    def hex2bin(self,s):
        mp = {'0': "0000", '1': "0001", '2': "0010", '3': "0011",
              '4': "0100", '5': "0101", '6': "0110", '7': "0111",
              '8': "1000", '9': "1001", 'A': "1010", 'B': "1011",
              'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"}
        bin = ""
        for i in range(len(s)):
            bin = bin + mp[s[i]]
        return bin

    def bin2hex(self,s):
        mp = {"0000": '0', "0001": '1', "0010": '2', "0011": '3',
              "0100": '4', "0101": '5', "0110": '6', "0111": '7',
              "1000": '8', "1001": '9', "1010": 'A', "1011": 'B',
              "1100": 'C', "1101": 'D', "1110": 'E', "1111": 'F'}
        hex = ""
        for i in range(0, len(s), 4):
            ch = s[i:i+4]
            hex = hex + mp[ch]
        return hex

    def dec2bin(self,n):
        return bin(n).replace("0b", "")

    def bin2dec(self,b):
        return int(b, 2)

    def dec2hex(self,n):
        return hex(n).replace("0x", "")

    def hex2dec(self,h):
        return int(h, 16)
    
    def text2hex(self,s):
        return (''.join([hex(ord(c)).replace("0x", "") for c in s])).upper()

    def hex2text(self,h):
        return ''.join([chr(int(h[i:i+2], 16)) for i in range(0, len(h), 2)])
    
    def text2bin(self,s):
        str= s.encode('utf-8')
        return ''.join(['{0:04b}'.format(int(d, 16)) for d in str.hex()])
    
    def split_into_chunks(self, s):
        chunks = [s[i:i+8] for i in range(0, len(s), 8)]
        chunks[-1] = chunks[-1].ljust(8, 'x')
        return chunks
    
    def split_hex_2_64bits(self,s):
        chunks = [s[i:i+18] for i in range(0, len(s), 18)]
        return chunks
    
    def XOR(self,a, b):
        y = int(a, 2)^int(b,2)
        return bin(y)[2:].zfill(len(a))