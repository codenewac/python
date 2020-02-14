def make_sandwich(*toppings):
    """制作三明治，顾客点食材"""
    print("\nI want:")
    for topping in toppings:
        print(topping)
def car_info(maker,type,**other_info):
    """车辆的信息"""
    car_infofile={}
    car_infofile['maker']=maker
    car_infofile['type']=type
    for key,value in other_info.items():
        car_infofile[key]=value
    return car_infofile