import pygame
import sys

pygame.init()

screen_width=480
screen_height=600
screen=pygame.display.set_mode((screen_width,screen_height))

clock=pygame.time.Clock()

pygame.display.set_caption("살려줘 혈관!")

background=pygame.image.load("D:\헬스케어2회차_YJI\Python_BloodstreamGame\살려줘혈관!.png")
character=pygame.image.load("D:\헬스케어2회차_YJI\Python_BloodstreamGame\Adobe Express - file.png")
character_size=character.get_rect().size
character_width=character_size[0]
character_height=character_size[1]
character_x_pos=(screen_width/2)-(character_width/2)
character_y_pos=screen_height-character_height
character_speed=2

to_x=0
to_y=0

# 색상 정의
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# font 정의
font = pygame.font.Font(None, 74)
button_font = pygame.font.Font(None, 36)

# 게임 상태
game_started = False

# 버튼 클래스 정의
class Button:
    def __init__(self, x, y, width, height, color, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = button_font.render(self.text, True, (255, 255, 255))
        screen.blit(text_surface, (self.rect.x + (self.rect.width - text_surface.get_width()) // 2,
                                   self.rect.y + (self.rect.height - text_surface.get_height()) // 2))

    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

# 버튼 생성
start_button = Button(170, 200, 150, 60, RED, "Game Start!")


running=True
while running:
    dt=clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.is_hovered(pygame.mouse.get_pos()):
                game_started = True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                to_x-=character_speed
            elif event.key==pygame.K_RIGHT:
                to_x+=character_speed
            elif event.key==pygame.K_DOWN:
                to_y+=character_speed
            elif event.key==pygame.K_UP:
                to_y-=character_speed

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                to_x=0
            if event.key==pygame.K_DOWN or event.key==pygame.K_UP:
                to_y=0

    if not game_started:
        start_button.draw(screen)

    else:
        # 게임 시작 후 화면
        screen.blit(background,(0,0))
        screen.blit(character,(character_x_pos,character_y_pos))
       
    pygame.display.update()

    character_x_pos += to_x
    character_y_pos += to_y

    if character_x_pos<0:
        character_x_pos=0
        
    elif character_x_pos>screen_width-character_width:
        character_x_pos=screen_width-character_width

    if character_y_pos<0:
        character_y_pos=0
        
    elif character_y_pos>screen_height-character_height:
        character_y_pos=screen_height-character_height

    

pygame.quit()
