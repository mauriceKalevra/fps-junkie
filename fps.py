from ursina import *           # this will import everything we need from ursina with just one line.
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import Keys
app = Ursina()

player = FirstPersonController()
skybox = load_texture("earth_from_space.png")
Sky()
cube = Entity(model='cube', color=color.orange, scale=(2,2,2))

window.title = 'fps-junkie'                # The window title
window.borderless = False               # Show a border
window.fullscreen = False               # Do not go Fullscreen
window.exit_button.visible = False      # Do not show the in-game red X that loses the window
window.fps_counter.enabled = True       # Show the FPS (Frames per second) counter

def add_object_box(position):
    Button(
        parent=scene,
        model='sphere',
        origin=0.5,
        color=color.brown,
        position=position,
        texture='grass',
        scale=(9,9,9)
    )

for i in range(20):
    for j in range(20):
        add_object_box( (i,0,j) )
   






app.run()                     # opens a window and starts the game.