class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
class Battery():
    """一次电瓶的简单模拟"""
    def __init__(self,battery_size=70):
        """初始化电瓶属性"""
        self.battery_size=battery_size
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a "+str(self.battery_size)+"-kWh battery.")
    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=270

        message="This car can go approximately "+str(range)
        message+='miles on a full charge.'
        print(message)
    def upgrade_battery(self):
        """检查电瓶容量"""
        if self.battery_size!=85:
            self.battery_size=85
class ElectricCar(Car):
    """Represent aspects of a car,specific to electric vehicles."""
    def __init__(self,make,model,year):
        """电动车的独特之处"""
        super().__init__(make,model,year)
        self.battery=Battery()
my_tesla=ElectricCar('tesla','model s',2016)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()