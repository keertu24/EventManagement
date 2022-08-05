from user.models import Cart,Order
from organiser.models import Package

def usercart(owner):
    """Function that returns the ordered product package id like[1,3,4,none,2]"""
    user_cart=Cart.objects.filter(user_name=owner)# getting list of the selected items in cart
    user_cart_items=[]# it saves the id of each cart item and also to get only some value 
    select_pack_to_template=[]# it send the selected item information that store in the package table 
    for i in user_cart:
        user_cart_items=i.food_choice,i.music_choice,i.stage_choice,i.decor_choice,i.light_choice #selecting only 5 items and avoiding rest of details 
    return user_cart_items


def usercartproduct(owner):
    """function that returns package table info for package id that user have booked like query set that contain particular info of select product in cart """
    user_cart=Cart.objects.filter(user_name=owner)# getting list of the selected items in cart
    user_cart_items=[]# it saves the id of each cart item and also to get only some value 
    select_pack_to_template=[]# it send the selected item information that store in the package table 
    for i in user_cart:
        user_cart_items=i.food_choice,i.music_choice,i.stage_choice,i.decor_choice,i.light_choice #selecting only 5 items and avoiding rest of details 
    for i in user_cart_items:
            user_cart_items_selected=Package.objects.filter(package_id=i)
            select_pack_to_template.append(user_cart_items_selected)#appending to list of item 
    return select_pack_to_template