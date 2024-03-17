from dataypes import DataTypes
from tables import Tables
class Message:
    
    def f_r_n_key(self,Rn,Kn):
        ERn=''.join(Rn[i-1] for i in self.tb.exp_d)
        val=self.dt.XOR(ERn,Kn)
        Bn=[val[i:i+6] for i in range(0, len(val), 6)]
        val=''
        for i, b in enumerate(Bn, start=0):
            r=str(b[0]) + str(b[5])
            c=b[1:5]
            d_r=self.dt.bin2dec(r)
            d_c=self.dt.bin2dec(c)
            bin_val=self.dt.dec2bin(self.tb.sbox[i][d_r][d_c])
            bin_val=bin_val.zfill(4)
            val+=str(bin_val)
        # Now we perform straight permutation
        val=''.join(val[i-1] for i in self.tb.per)
        return val
        
        
    def calc_right_side(self,cycle,key):
        # L0 XOR f(R0, k1)
        Ln=self.L[cycle-1]
        Rn=self.f_r_n_key(self.R[cycle-1],self.subkeys[key])
        return self.dt.XOR(Ln,Rn)
    
    def encrypt(self,subkeys,plain_text):
        self.subkeys=subkeys
        for x in self.dt.split_into_chunks(plain_text):
            bin=self.dt.text2bin(x)
            ip=''
            ip+=''.join(bin[j-1] for j in self.tb.initial_perm)
            self.L[0]=ip[:32]
            self.R[0]=ip[32:]
            for y in range(1,17):
                self.L[y] = self.R[y-1]
                self.R[y] = self.calc_right_side(y,y)
            rev_order=str(self.R[16])+str(self.L[16])
            enc= ''.join(rev_order[i-1] for i in self.tb.final_perm)
            self.enc+=str(self.dt.bin2hex(enc))
        return self.enc
        
        
    def decrypt(self,subkeys,cipher_text):
        self.subkeys=subkeys
        for x in self.dt.split_hex_2_64bits(cipher_text):
            bin=self.dt.hex2bin(x)
            ip=''
            ip+=''.join(bin[j-1] for j in self.tb.initial_perm)
            self.L[0]=ip[:32]
            self.R[0]=ip[32:]
            
            for y in range(1,17):
                self.L[y] = self.R[y-1]
                self.R[y] = self.calc_right_side(y,17-y)
            rev_order=str(self.R[16])+str(self.L[16])
            dec= ''.join(rev_order[i-1] for i in self.tb.final_perm)
            self.dec+=str(self.dt.hex2text(self.dt.bin2hex(dec)))
        self.dec=self.dec.replace('~','')
        return self.dec
    
    def __init__(self):
        self.dt=DataTypes()
        self.tb=Tables()
        self.subkeys={}
        self.L={}
        self.R={}
        self.enc=''
        self.dec=''
        
        