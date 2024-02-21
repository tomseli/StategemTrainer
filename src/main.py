import pygame
from arrow import drawKey
from enums import Code, Center
import strategem
import time

pygame.init()
(WIDTH, HEIGHT) = (720, 520)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont('calibri', 20)
pygame.display.set_caption('Strategem Trainer')
icon = pygame.image.load('img/icon.png')
pygame.display.set_icon(icon)

buttons = []
texts = []

pad = 20
button_width = 300
button_height = 50
button_PAC = pygame.Rect(
    WIDTH-pad-button_width, 20, button_width, button_height)
buttons.append(button_PAC)
texts.append('Patriotic Administration Center')

button_orbital = pygame.Rect(
    WIDTH-pad-button_width, 90, button_width, button_height)
buttons.append(button_orbital)
texts.append('Orbital Cannons')

button_hangar = pygame.Rect(
    WIDTH-pad-button_width, 160, button_width, button_height)
buttons.append(button_hangar)
texts.append('Hangar')

button_bridge = pygame.Rect(
    WIDTH-pad-button_width, 230, button_width, button_height)
buttons.append(button_bridge)
texts.append('Bridge')

button_engineering = pygame.Rect(
    WIDTH-pad-button_width, 300, button_width, button_height)
buttons.append(button_engineering)
texts.append('Engineering Bay')

button_robotics = pygame.Rect(
    WIDTH-pad-button_width, 370, button_width, button_height)
buttons.append(button_robotics)
texts.append('Robotics Workshop')

button_next = pygame.Rect(WIDTH-pad-140, 440, 140, button_height)
buttons.append(button_next)

button_prev = pygame.Rect(WIDTH-pad-button_width, 440, 140, button_height)
buttons.append(button_prev)

active_stategem = strategem.EagleNapalmAirstrike
active_center = Center.hangar

running = True
key = None
idx_check = 0
idx_strategem = 0
correct_codes = []
start_time = 0
finished_time = 0
while running:
    screen.fill(pygame.Color('white'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Get the pressed key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                key = Code.UP
            if event.key == pygame.K_a:
                key = Code.LEFT
            if event.key == pygame.K_s:
                key = Code.DOWN
            if event.key == pygame.K_d:
                key = Code.RIGHT
        # Clickey
        if event.type == pygame.MOUSEBUTTONDOWN:
            for idx, button in enumerate(buttons):
                if button.collidepoint(event.pos) and idx < len(Center):
                    active_center = Center(idx)
                    active_stategem = strategem.CenterList[idx][0][1]
                    idx_strategem = 0
                if button.collidepoint(event.pos) and idx == 6:
                    if idx_strategem + 1 > len(strategem.CenterList[active_center.value]) - 1:
                        pass
                    else:
                        idx_strategem += 1
                    active_stategem = strategem.CenterList[active_center.value][idx_strategem][1]
                if button.collidepoint(event.pos) and idx == 7:
                    if idx_strategem - 1 < 0:
                        pass
                    else:
                        idx_strategem -= 1
                    active_stategem = strategem.CenterList[active_center.value][idx_strategem][1]
    
    # Draw buttons
    for button in buttons:
        pygame.draw.rect(screen, pygame.Color('blue'), button)
    offset = button_height // 3 + pad
    for text in texts:
        surface = font.render(text, True, pygame.Color('white'))
        screen.blit(surface, (WIDTH-pad+10-button_width, offset))
        offset += 70
    surface = font.render('Previous', True, pygame.Color('white'))
    screen.blit(surface, (WIDTH-pad+10-button_width, offset))
    surface = font.render('Next', True, pygame.Color('white'))
    screen.blit(surface, (WIDTH-pad+10-140, offset))

    surface = font.render(
        strategem.CenterList[active_center.value][idx_strategem][0], 
        True, 
        pygame.Color('black'))
    screen.blit(surface, (40, 80))
    surface = font.render(
        'Time: {:.3f}'.format(finished_time), 
        True,
        pygame.Color('black'))
    screen.blit(surface, (40, 100))

    # Draw the code on display
    spacing = 30
    initial = pygame.Vector2(50, 50)
    coordinate = initial
    for code in active_stategem:
        drawKey(screen, code, coordinate, pygame.Color('black'))
        coordinate = pygame.Vector2(coordinate[0] + spacing, 50)

    coordinate = initial
    for code in correct_codes:
        drawKey(screen, code, coordinate, pygame.Color('gray'))
        coordinate = pygame.Vector2(coordinate[0] + spacing, 50)
    
    # If a key is pressed, handle it
    if key is not None:
        # Correct key
        if key == active_stategem[idx_check]:
            if idx_check == 0:
                start_time = time.time()
            
            idx_check += 1
            coordinate = pygame.Vector2(initial[0] + spacing*idx_check, initial[1])
            correct_codes.append(key)
            
            # Completed
            if idx_check == len(active_stategem):
                finished_time = time.time() - start_time
                idx_check = 0
                correct_codes = []
        
        # Incorrect key
        else:
            correct_codes = []
            idx_check = 0
        key = None

    # end of the frame
    pygame.display.flip()
        
    