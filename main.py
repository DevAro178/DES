from key import Key
from dataypes import DataTypes
from message import Message

if __name__ == "__main__":
    dt=DataTypes()
    mg=Message()
    k_ins = Key()
    
    # Step 1 - Key Generation
    User_Key=input("Enter a 64-bit Key (1uiu21i1): ") or '1uiu21i1'
    subkeys=k_ins.generate(User_Key)
    
    # Step 2 - Message Encryption
    User_Msg=input("Enter a 64-bit Message (Hello World!): ") or "Hello World!"
    mg.encrypt(subkeys,User_Msg)
    