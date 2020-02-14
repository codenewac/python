class Restaurant():
    """一个餐馆"""
    def __init__(self,restaurant_name,cuisine_type):
        """初始化"""
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        """描述餐馆"""
        print('The restaurant called '+self.restaurant_name.title())
        print('The restaurant has '+self.cuisine_type.title())
    def open_restaurant(self):
        """餐馆开业"""
        print("The resaurant is open!Welcome you!")
    def set_number_served(self,number_set):
        """设置就餐人数"""
        self.number_served=number_set
    def increment_number_served(self,incr_num):
        """增加就餐人数"""
        self.number_served+=incr_num

"""resaurant=Restaurant('hotel','beef chicken')
print(resaurant.restaurant_name.title())
print(resaurant.cuisine_type)
resaurant.describe_restaurant()
resaurant.open_restaurant()
resaurant_1=Restaurant('beijing hotel','duck')
resaurant_2=Restaurant('peace hotel','rest')
resaurant_1.describe_restaurant()
resaurant_2.describe_restaurant()
restaurant=Restaurant('beijing restaurant','hot')
restaurant.set_number_served(88)
nm=restaurant.number_served
print(nm)
restaurant.increment_number_served(9)
nm=restaurant.number_served
print(nm)"""
class IceCreamStand(Restaurant):
    """冰淇淋饭店"""
    def __init__(self,restaurant_name,cuisine_type,*flavors):
        """初始化"""
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=flavors
    def show_IceCream(self):
        print(self.flavors)
icecreamstand=IceCreamStand('beijing','ice','red','beef','hot')
icecreamstand.describe_restaurant()
icecreamstand.show_IceCream()