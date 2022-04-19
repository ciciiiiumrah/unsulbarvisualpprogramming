class hero:
    def __init__(self, name, armor, m_armor, pyshic_p, magic_p):
        self.name = name
        self.armor = armor
        self.m_armor = m_armor
        self.pyshic_p = pyshic_p
        self.magic_p = magic_p
    def print(self):
        print("{", self.name, " , " ,self.armor," , " ,self.m_armor," , "
              ,self.pyshic_p ," , " ,self.magic_p  ,"}")
    
helcurt = hero("helcurt", 20,20,121,9)
gusion = hero("gusion", 21, 20, 120, 100)
helcurt.print()
gusion.print()
