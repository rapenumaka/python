class Students:
    # define properties of class

    def __init__(self,name, contact):
        self.name = name
        self.contact = contact

    def getdata(self):
        print('Acceptng Data')
        self.name = input('Enter name')
        self.contact = input('Enter contact')

    def putdata(self):
        print('the name is '+self.name,'this is the contact :'+self.contact)