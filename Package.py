class Package(): 
    W_GR_100 = 10 
    def __init__(self,
                 id:int=  0, 
                 weight: float= 1.0 , 
                 description: str= 'description', 
                 cost:float=1.0): 
        
        self.__id = id
        self.__weight = weight
        self.__description = description
        self.__cost = cost
    
    def set_id(self):
        self.__id=0 

    def get_id(self):
        return self.__id
    
    def set_weight(self):
        self.__weight = 1

    def get_weight(self):
        return self.__weight 

    def set_description(self):
        self.__description='description'

    def get_description(self):
        return self.__description

    def set_cost(self):
        self.__cost = 1.0 

    def get_cost(self):
        return self.__cost
    
    def _str_(self):
        print("*Id(Code)= ", self._id, "\n*Weight= ", self.weight, "\n*W_GR_100= ", 
              W_GR_100, "\n*Description= ", self._description, "\n*Cost= ", self._cost)

    def calculate(self):
        print("COSTO TOTAL ENVIO: $ ", (self.__cost * self.__weight))

class StandardPackage(Package):
    def __init__(self, 
                 id=0, 
                 weigth=1, 
                 cost=0, 
                 description='Description.', 
                 fixedfee=0):
        
        self.__id=id
        self.__weight=weigth
        self.__cost=cost
        self.__description=description
        self.__fixedfee=fixedfee

    def get_id(self):
        return self.__id

    def set_id(self):
        self.__id=0

    def get_weight(self):
        return self.__weight

    def set_weight(self):
        self.__weight=1

    def get_description(self):
        return self.__description
        
    def set_description(self):
        self.__description='Description'

    def get_cost(self):
        return self.__cost
        
    def set_cost(self):
        self.__cost=1.0

    def get_fixedfee(self):
        return self.__fixedfee

    def set_fixedfee(self):
        self.__fixedfee=0 
    
    def _str_(self):
        super()._str_()
        print("\n*FIXED FEE", self.__fixedfee)
    
    def calculate(self):
        print("COSTO TOTAL DE ENVIO-> $ ", ((self.__cost*self.__fixedfee) + self.__weight))


class OverweightPackage(Package):
    def __init__(self, 
                 id, 
                 weigth=1, 
                 cost=0, 
                 description='Description.', 
                 overweight=0):
        
        self.__id=id
        self.__weight=weigth
        self.__cost=cost
        self.__description=description
        self.__overweigth=overweight

    def get_id(self):
        return self.__id

    def set_id(self):
        self.__id=0

    def get_weight(self):
        return self.__weight

    def set_weight(self):
        self.__weight=1

    def get_description(self):
        return self.__description
        
    def set_description(self):
        self.__description='Description'

    def get_cost(self):
        return self.__cost

    def set_cost(self):
        self.__cost=1.0
        
    def get_overweight(self):
        return self.__overweigth

    def set_overweight(self):
        self.__overweigth=0 
    
    def _str_(self):
        super()._Str_()
        print("\n*OVERWEIGHT", self.__overweight)
        
    def calculate(self):
        print("COSTO DE ENVIO CON SOBREPESO->$ ",((self.__cost*self.__weight) + self.__overweigth))

class Person():
    def __init__(self, 
                 name= 'name', 
                 lastname= 'lastname', 
                 iduser=0, 
                 telnumber=0):
        
        self .__name= name
        self .__lastname= lastname
        self .__iduser= iduser
        self .__telnumber= telnumber

    def set_name (self, name):
        self.__name= "name"

    def get_name (self):
        return self.__name
    
    def set_lastname (self, lastname):
        self.__name= "lastname"
    
    def get_lastname(self):
        return self.__lastname
    
    def set_iduser (self,iduser):
        self.__iduser=0 if iduser==None else iduser
    
    def get_iduser(self):
        return self.__iduser
    
    def set_telnumber (self, telnumber):
        self.__telnumber=0 if telnumber == None else telnumber
    
    def get_telnumber (self):
        return self.__telnumber
    
    def _str_(self):
        print("*NAME: ", self._name, "\n*LAST NAME: ", 
              self._lastname, "\n*ID USER : ", self.__iduser,
              "\n*CELLPHONE: ", self.__telnumber)

class Address():
    def __init__(self, streetnumber=0, housenumber=0, district= 'district'):
        self.__streetnumber= streetnumber
        self.__housenumber =housenumber 
        self.__district = district
    
    def set_streetnumber(self,streetnumber):
        self.__streetnumber
    
    def get_streetnumber (self):
        return self.__streetnumber

    def set_house_number(self, housenumber):
        self.__housenumber = 0 if housenumber == None else housenumber

    def get_housenumber(self):
        return self.__housenumber
    
    def set_district (self, district):
        self.__district= 'district'
    
    def get_district (self):
        return self.__district
    
    def _str_(self):
        print("*STREET NUMBER: ", self.streetnumber, "\nHOUSE NUMBER: ",self.__housenumber, 
              "\n*DISTRICT: ", self.__district)

class Delivor(Person):
    def _init_(self,
                 name: str= " ", 
                 lastname: str="",
                 dnicard: int = 0,
                 birthdate: str="",
                 phone: int = 0,
                 id: str="",
                 date: str ="",
                 time: str ="",
                 sender=Person(),
                 receiver=Person(),
                 sender_add=Address(),
                 receiver_add=Address(),
                 contact=Person(),
                 items=[Package()]):
        
        self.__id = id
        self.__date = date
        self.__time = time
        self.__sender = Person() 
        if (sender != Person):
            print ("\nVALOR INCORRECTO")
        else:
            self.__sender = Person()
            
        self.__receiver = Person() 
        if (receiver != Person):
            print ("\nVALOR INCORRECTO")
        else:
            self.__receiver = Person() 
            
        self.__sender_add = Address() 
        if (sender_add!= Address()):
            print ("\nVALOR INCORRECTO")
        else:
            self.__sender_add = Address()
            
        self.__receiver_add = Address() 
        if (receiver_add!= Address()):
            print ("\nVALOR INCORRECTO")
        else:
            self.__receiver_add = Address()
            
        self.__contact = Person() 
        if (contact != Person):
            print ("\nVALOR INCORRECTO")
        else:
            self.__contact = Person() 
            
        self.__items = [Package()] 
        if (items != Package()):
            print ("\nNULL")
        else:
            self.__items = Package()

    def get_idpersona(self):
        return self.__idpersona
    
    def set_idpersona(self, idpersona):
        self.__idpersona = idpersona
        
    def get_date(self):
        return self.__date

    def set_date(self, date):
        self.__date = date

    def get_time(self):
        return self.__time
    
    def set_time(self, time):
        self.__time = time
        
    def get_sender(self):
        return self.__sender
    
    def set_sender(self, sender):
        if type (sender) != Person:
            print ("\n¡¡DATO INGRESADO INVALIDO!!, por favor ingrese nuevo dato")
        else:
            self.__sender = Person( ) 
        
    def get_receiver(self):
        return self.__receiver
    
    def set_receiver(self, receiver): 
        if type (receiver) != Person:
            print ("\n¡¡DATO INGRESADO INVALIDO!!, por favor ingrese nuevo dato")
        else:
            self.__receiver = Person() 
        
    def get_sender_add(self):
        return self.__sender_add

    def set_sender_add(self, sender_add):
         if type (sender_add) != Address:
            print ("\n¡¡DATO INGRESADO INVALIDO!!, por favor ingrese nuevo dato")
         else:
            self.__sender_add = Address()
        
    def get_receiver_add(self):
        return self.__receiver_add
    
    def set_receiver_add(self, receiver_add):
        if type (receiver_add) != Address:
            print ("\n¡¡DATO INGRESADO INVALIDO!!, por favor ingrese nuevo dato")
        else:
            self.__receiver_add = Address()

    def get_contact(self):
        return self.__contact
    
    def set_contact(self, contact):
        if type (contact) != Person:
            print ("\n¡¡DATO INGRESADO INVALIDO!!, por favor ingrese nuevo dato")
        else:
            self.__contact = Person() 
    
    def get_items(self):
        return self.__items
    
    def set_items(self, items):
        if (items != Package()):
            print ("\n¡¡DATO INGRESADO INVALIDO!!, por favor ingrese nuevo dato")
        else:
            self.__items = [Package()]
            
    def _str_(self):
        print("*ID= ", self.__id, "\n*FECHA= ", self.__date, "\n*TIEMPO DE ENTREGA= ", self.__date, "\N*INFORMACION DEL QUE ENVIA= " ,self.__sender, "\n*INFORMACION DEL QUE LO RECIBE= ", self.__receiver)
        
        