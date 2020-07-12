'''Property class which represents any apartment or home'''
class Property:
    '''Method to initialize Property or any sublclass object'''
    def __init__(self,square_feet='',beds='',baths='',**kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths
    
    '''Method which displays the property details'''
    def display(self):
        print("Property Details")
        print("======================")
        print("Square footage:  {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()
    
    def prompt_init ():
        return dict(square_feet = input("Enter the square feet: "),
        beds = input("Enter number of bed rooms:"),
        baths = input("Enter number of bath rooms:"))
    prompt_init=staticmethod(prompt_init)

class Apartment(Property):
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: {}".format(self.laundry))
        print("has balcony: {}".format(self.balcony))
        print()

    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = get_valid_input("What laundry facilities does the property have",Apartment.valid_laundries)
        balcony = get_valid_input("Does the property have a balcony?",Apartment.valid_balconies)
        parent_init.update({"laundry": laundry,"balcony": balcony})
        return parent_init
        prompt_init = staticmethod(prompt_init)

def get_valid_input(input_string,valid_options):
        input_string+= "({})".format(", ".join(valid_options))
        response = ''
        while response.lower() not in valid_options:
            print(response)
            response=input(input_string)
        return response

class House(Property):
    valid_garage = ('attached','detached','none')
    valid_fenced = ('yes','no')

    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        super().__init__(**kwargs)
        self.num_stories = num_stories
        self.gagrage = garage
        self.fenced = fenced
    
    def display(self):
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("Garage: {}".format(self.gagrage))
        print("Fenced yard: {}".format(self.fenced))
        print()
    
    def prompt_init():
        parent_init = Property.prompt_init()
        garage = get_valid_input("Is there a garage?" , House.valid_garage)
        fenced = get_valid_input("Is the yard fenced?",House.valid_fenced)
        num_stories = input("How many stories?")
        parent_init.update({"garage" : garage,"fenced":fenced,"num_stories":num_stories})
        return parent_init
        prompt_init = staticmethod(prompt_init)

class Purchase:
    def __init__(self,price='',taxes='',**kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print("Purchase Details")
        print("Selling Price: {}".format(self.price))
        print("Estimated taxes: {}".format(self.taxes))
        print()
    
    def prompt_init():
        return dict (
            price=input("What is the selling price ?"),
            taxes=input("Enter the taxes ?"))
        prompt_init = staticmethod(prompt_init)

class Rental:
    def __init__(self,furnished='',utilities='',rent='',**kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.utilities = utilities
        self.rent = rent

    def display(self):
        super().display()
        print("Rental Details")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))
        print()
    
    def prompt_init():
        return dict(
            rent = input("What is monthly rent?"),
            utilities = input("What is the estimated utilities?"),
            furnished = get_valid_input("Is the property furnished",("yes","no"))
        )
        prompt_init = staticmethod(prompt_init)

class HouseRental(Rental,House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

class HousePurchase(Purchase,House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

class ApartmentRental(Rental,Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

class ApartmentRental(Purchase,Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)