from pico2d import * 
from gfw import *
import main_scene

world = World(['bg', 'title'])

canvas_width = main_scene.canvas_width
canvas_height = main_scene.canvas_height

class Title(Sprite):
    def __init__(self, filename, x, y):
          super().__init__(filename, x, y)
          self.selected = False
          self.x = x
          self.y = y
    
    def draw(self):
        if self.selected == True:
             self.image.draw_to_origin(0, 0, self.x, self.y)
    def update(self):
        pass
    

def enter():
    world.append(HorzFillBackground('resource/Background/Layer_0011_0.png', speed = 100 // 4), world.layer.bg)
    world.append(HorzFillBackground('resource/Background/Layer_0010_1.png', speed = 100 // 4), world.layer.bg)
    world.append(HorzFillBackground('resource/Background/Layer_0009_2.png', speed = 100 // 4), world.layer.bg)
    world.append(HorzFillBackground('resource/Background/Layer_0008_3.png', speed = 100 // 4), world.layer.bg)
    world.append(HorzFillBackground('resource/Background/Layer_0007_Lights.png', speed = 100 // 3.5), world.layer.bg)
    world.append(HorzFillBackground('resource/Background/Layer_0006_4.png', speed = 100 // 3.5), world.layer.bg)
    world.append(HorzFillBackground('resource/Background/Layer_0005_5.png', speed = 100 // 3), world.layer.bg)
    world.append(HorzFillBackground('resource/Background/Layer_0004_Lights.png', speed = 100 // 3), world.layer.bg)
    world.append(HorzFillBackground('resource/Background/Layer_0003_6.png', speed = 100 // 2.5), world.layer.bg)
    world.append(HorzFillBackground('resource/Background/Layer_0002_7.png', speed = 100 // 2), world.layer.bg)
    world.append(HorzFillBackground('resource/Background/Layer_0001_8.png', speed = 100 // 1.5), world.layer.bg)
    world.append(HorzFillBackground('resource/Background/Layer_0000_9.png', speed = 100 // 1.5), world.layer.bg)

    global titles
    titles = []
    global title_idx
    title_idx = 0

    title = Title('resource/Title/New Game.png', canvas_width, canvas_height)
    world.append(title, world.layer.title)
    titles.append(title)
    title = Title('resource/Title/Load.png', canvas_width, canvas_height)
    world.append(title, world.layer.title)
    titles.append(title)
    title = Title('resource/Title/Option.png', canvas_width, canvas_height)
    world.append(title, world.layer.title)
    titles.append(title)
    title = Title('resource/Title/Quit.png', canvas_width, canvas_height)
    world.append(title, world.layer.title)
    titles.append(title)

    titles[title_idx].selected = True

def exit():
    world.clear()

def pause():
    print('[main.pause()]')

def resume():
    print('[main.resume()]')

def handle_event(e):
    global title_idx
    global titles
    if e.type == SDL_MOUSEBUTTONDOWN:
            pass
    
    if e.type == SDL_KEYDOWN:
        if e.key == SDLK_RETURN:
            if title_idx == 0:
                gfw.change(main_scene)
            elif title_idx == 1:
                pass
            elif title_idx == 2:
                pass
            elif title_idx == 3:
                quit()
             
        elif e.key == SDLK_UP or e.key == SDLK_w:
             if title_idx == 0:
                  pass
             else:
                  titles[title_idx].selected = False
                  title_idx -= 1
                  titles[title_idx].selected = True
        elif e.key == SDLK_DOWN or e.key == SDLK_s:
             if title_idx == 3:
                  pass
             else:
                  titles[title_idx].selected = False
                  title_idx += 1
                  titles[title_idx].selected = True

if __name__ == '__main__':
    gfw.start_main_module()

