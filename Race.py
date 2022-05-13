import arcade
import random


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Race"



# class with the game
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background=arcade.load_texture("/Users/abdulazizsuleymanov/Desktop/Python/Arcade/Car Race/background.png")
        self.ferrari=Car("/Users/abdulazizsuleymanov/Desktop/Python/Arcade/Car Race/Audi.png",0.6)
        self.barrier=Barrier("/Users/abdulazizsuleymanov/Desktop/Python/Arcade/Car Race/wall.png",0.7)
        self.red_line=Red_line("/Users/abdulazizsuleymanov/Desktop/Python/Arcade/Car Race/red_line_v2.png",0.9)
        
        '''if self.ferrari.center_x == 750 or self.ferrari.center_x == 0:
            self.lives-=1
            print(self.lives)'''

    # initial values
    def setup(self):
        self.ferrari.center_x=300
        self.ferrari.center_y=300
        self.ferrari.change_x=5
        self.ferrari.change_y=5

        self.barrier.center_x=SCREEN_WIDTH/2
        self.barrier.center_y=SCREEN_HEIGHT
        #barrier speed
        self.barrier.change_y=5

        self.red_line.center_x=410
        self.red_line.center_y=360
        self.red_line.change_x=0
        self.red_line.change_y=0

        self.score=0
        self.lives=99
        self.hit_barrier=0

        self.move=True

    # rendering
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.AMAZON)
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,self.background)
        self.ferrari.draw()
        self.barrier.draw()
        text_score=f"Score: {self.score}"
        arcade.draw_text(text_score,80,560,arcade.color.BLUE,20)
        text_lives=f"Lives: {self.lives}"
        arcade.draw_text(text_lives,80,530,arcade.color.BLUE,20)
        if self.score == 5:
            self.ferrari.stop()
            self.barrier.stop()
            self.move=False
            self.red_line.draw()
            text_win=f"Congratulations!You won the game by having,the score of {self.score} points"
            arcade.draw_text(text_win,35,345,arcade.color.BLUE,20)


    # game logic
    def update(self, delta_time):
        self.ferrari.update()
        self.barrier.update()
        self.red_line.update()
        
        #if ferrari goes into barrier then lives ----1
        if arcade.check_for_collision(self.ferrari, self.barrier):
            self.barrier.stop()
            self.ferrari.stop()
            self.ferrari.change_x=0
            self.move=False
            self.lives-=1
            if self.lives <= 0:
                self.move=True
                self.ferrari.update()
                self.barrier.update()
        
        if self.barrier.center_y <= 0:
            self.score+=1
        
        #if ferrari goes into wall then lives ----1
        if self.ferrari.right >= SCREEN_WIDTH-50:
            self.lives-=1
            self.move=False
        
        #if lives == 0 then the game continues
            if self.lives < 0:
                self.move=True
                self.ferrari.update()
                self.barrier.update()

        
        if self.ferrari.left <= 50:
            self.lives-=1
        
        if self.lives <=0:
            self.barrier.stop()
            self.ferrari.stop()
            self.move=False

    # pressing on keys
    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT and self.move == True:
            self.ferrari.change_x=5
            #self.ferrari.angle=-20
        if key == arcade.key.LEFT and self.move == True:
            self.ferrari.change_x = -5
            #self.ferrari.angle=20

    # not pressing on keys
    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.ferrari.change_x=0
            self.ferrari.angle=0

class Car(arcade.Sprite):
    def update(self):
        if self.left < 50 :
            self.left=50
        if self.right > SCREEN_WIDTH-50:
            self.right=SCREEN_WIDTH-50
        self.center_x += self.change_x 

class Barrier(arcade.Sprite):
    def update(self):
        if self.center_y <= 0:
            self.center_y=SCREEN_HEIGHT
            self.center_x=random.randint(130,SCREEN_WIDTH-130)
        self.center_y -= self.change_y  

class Red_line(arcade.Sprite):
    def update(self):
        pass

window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
