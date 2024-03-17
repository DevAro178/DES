from dataypes import DataTypes
from tables import Tables

class Key:
    
    def left_shift(self,table,round):
        for i in range(table[round]):
            self.C = self.C[1:] + self.C[0]
            self.D = self.D[1:] + self.D[0]
        return self.C+''+self.D
    
    def make_subkeys_16(self,table):
        for i in range(1,17):
            self.subkeys[i]=self.left_shift(table,i-1)
            
    def subkey_comp(self,table):
        for i in range(1,17):
            temp_key = self.subkeys[i]
            temp_key = ''.join(temp_key[i-1] for i in table)
            self.subkeys[i]=temp_key
    
    def __init__(self):
        self.subkeys={}
    
    def generate(self,value):
        # Initialising Variables and Objects
        dt=DataTypes()
        tb=Tables()
        self.key = dt.text2hex(value)
        # Converting Hex Key to Binary
        hex_key=dt.hex2bin(self.key)
        # Parity bit drop table
        hex_key = ''.join(hex_key[i-1] for i in tb.keyp)
        # Splitting 56bits to 28bits
        self.C = hex_key[:28]
        self.D = hex_key[28:]
        # making 16 subkeys
        self.make_subkeys_16(tb.shift_table)
        # Key Compression using PC-2 table
        self.subkey_comp(tb.key_comp)
        # print(self.subkeys)
        return self.subkeys
        
        
        
        
    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return f'Key({self.value})'