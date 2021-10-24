#Author: Deryck Ho Student Number: 101181150

import Cimpl

def flip_vertical() -> None:
    """
    Returns an image that is flipped upside down (vertically)
    """
    file= Cimpl.choose_file()
    image = Cimpl.load_image(file)
    x = Cimpl.get_width(image)
    y = Cimpl.get_height(image)

   
    
    for i in range(x):
        for j in range(y//2):
            color1= Cimpl.get_color(image,i,j)
            color2= Cimpl.get_color(image,i,y-1-j)
            r,g,b= color1
            r1,g1,b1= color2
            newcolor1=Cimpl.create_color(r,g,b)
            newcolor2=Cimpl.create_color(r1,g1,b1)
            
            Cimpl.set_color(image, i,j,newcolor2)
            Cimpl.set_color(image, i,y-1-j,newcolor1)
    Cimpl.show(image)
    return 

flip_vertical()









    