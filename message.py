from dataypes import DataTypes
from tables import Tables
class Message:
    
    def f_r_n_key(self,Rn,Kn):
        ERn=''.join(Rn[i-1] for i in self.tb.exp_d)
        # print('Kn = '+Kn)
        # print('E(Rn) = '+ERn)
        val=self.dt.XOR(ERn,Kn)
        # print('E(Rn) XOR Kn = '+val)
        Bn=[val[i:i+6] for i in range(0, len(val), 6)]
        val=''
        for i, b in enumerate(Bn, start=0):
            r=str(b[0]) + str(b[5])
            c=b[1:5]
            d_r=self.dt.bin2dec(r)
            d_c=self.dt.bin2dec(c)
            bin_val=self.dt.dec2bin(self.tb.sbox[i][d_r][d_c])
            bin_val=bin_val.zfill(4)
            # print('-')
            # print('S'+str(i+1)+'(B'+str(i+1)+') = '+str(d_r)+' '+str(d_c)+' =>'+bin_val+' '+str(self.dt.bin2dec(bin_val)))
            # print('S'+str(i+1)+'(B'+str(i+1)+') = '+r+' '+c+' =>'+bin_val)
            val+=str(bin_val)
        # Now we perform straight permutation
        val=''.join(val[i-1] for i in self.tb.per)
        return val
        
        
    def calc_right_side(self,cycle):
        # L0 XOR f(R0, k1)
        Ln=self.L[cycle-1]
        Rn=self.f_r_n_key(self.R[cycle-1],self.subkeys[cycle])
        # print('f() = '+Rn)
        return self.dt.XOR(Ln,Rn)
    
    def encrypt(self,subkeys,plain_text):
        self.subkeys=subkeys
        # this for loop is on each 64 bit block of text
        for i,x in enumerate(self.dt.split_into_chunks(plain_text),start=0):
            print('M = '+x)
            bin=self.dt.text2bin(x)
            # this binary is a testing string
            # bin='0000000100100011010001010110011110001001101010111100110111101111'
            
            # print('M =  '+bin)
            ip=''
            ip+=''.join(bin[j-1] for j in self.tb.initial_perm)
            # print('IP = '+ip)
            self.L[i]=ip[:32]
            self.R[i]=ip[32:]
            print(f'L{i} = '+self.L[i])
            print(f'R{i} = '+self.R[i])
            
            for y in range(1,17):
                # print('--------------------------------')
                # print('Round '+str(y))
                self.L[y] = self.R[y-1]
                self.R[y] = self.calc_right_side(y)
                # print('Rn = '+self.R[y])
                # break
            rev_order=str(self.R[16])+str(self.L[16])
            # print('R16L16 = '+rev_order)
            # final permutation is remaining
            enc= ''.join(rev_order[i-1] for i in self.tb.final_perm)
            # print('Encrypted Text = '+enc)
            self.enc+=str(self.dt.bin2hex(enc))
            # break
        print('Encrypted Text = '+self.enc)
    
    def __init__(self):
        self.dt=DataTypes()
        self.tb=Tables()
        self.subkeys={}
        self.L={}
        self.R={}
        self.enc=''
        
        