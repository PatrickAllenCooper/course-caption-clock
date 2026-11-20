from app import retime
from candidate import ends

def check():
    assert ends([(0,500,'a'*17),(1300,1900,'ok')],2400)==[1000,1900]
    assert ends([(0,500,'x'*30),(510,800,'y')],800)==[500,800]
    assert retime("1\n00:00:00,000 --> 00:00:00,500\n" + "a"*17 + "\n", 1100).splitlines()[1].endswith("00:00:01,000")
