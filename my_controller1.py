from controller import Robot
from controller import Keyboard

robot = Robot()
keyboard = Keyboard()

timestep=64

w_1=robot.getDevice("w_1")
w_1.setPosition(float('inf'))
w_1.setVelocity(0.0)

w_2=robot.getDevice("w_2")
w_2.setPosition(float('inf'))
w_2.setVelocity(0.0)

w_3=robot.getDevice("w_3")
w_3.setPosition(float('inf'))
w_3.setVelocity(0.0)

w_4=robot.getDevice("w_4")
w_4.setPosition(float('inf'))
w_4.setVelocity(0.0)

speed=4
 
keyboard.enable(timestep)

w_hile (robot.step(timestep) !=-1):
   
    key_pressed= keyboard.getKey()
    print(key_pressed)
    
    # front movement - press up arrow_ key
    if(key_pressed== 315):
        w_1.setVelocity(speed)
        w_2.setVelocity(speed)
        w_3.setVelocity(speed)
        w_4.setVelocity(speed)
        
    # back movement - press dow_n arrow_ key   
    if(key_pressed== 317):
        w_1.setVelocity(-speed)
        w_2.setVelocity(-speed)
        w_3.setVelocity(-speed)
        w_4.setVelocity(-speed)
    
    # left movement - press left arrow_ key      
    if(key_pressed== 314):
        w_1.setVelocity(-speed)
        w_2.setVelocity(speed)
        w_3.setVelocity(-speed)
        w_4.setVelocity(speed)
    
    # right movement - press right arrow_ key     
    if(key_pressed== 316):
        w_1.setVelocity(speed)
        w_2.setVelocity(-speed)
        w_3.setVelocity(speed)
        w_4.setVelocity(-speed)
    
    # if no key is pressed   
    if(key_pressed== -1):
        w_1.setVelocity(0)
        w_2.setVelocity(0)
        w_3.setVelocity(0)
        w_4.setVelocity(0)