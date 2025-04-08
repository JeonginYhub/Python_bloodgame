import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 400, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("방향키로 움직이기")

# 색깔
DARK_RED = (139, 0, 0)
WHITE = (255, 255, 255)

# 플레이어 설정
player_width = 40   # 가로
player_height = 25   # 세로
player_x = WIDTH // 2
player_y = HEIGHT // 2
speed = 10

# 게임 루프
running = True
while running:
    screen.fill(DARK_RED)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키보드 입력 처리 + 경계 제한
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x - player_width // 2 > 0:
        player_x -= speed
    if keys[pygame.K_RIGHT] and player_x + player_width // 2 < WIDTH:
        player_x += speed
    if keys[pygame.K_UP] and player_y - player_height // 2 > 0:
        player_y -= speed
    if keys[pygame.K_DOWN] and player_y + player_height // 2 < HEIGHT:
        player_y += speed

    # 플레이어 그리기 (중앙 기준)
    pygame.draw.ellipse(screen, WHITE, (
        player_x - player_width // 2,
        player_y - player_height // 2,
        player_width,
        player_height
    ))

    pygame.display.update()
    pygame.time.Clock().tick(60)

# 종료
pygame.quit()
sys.exit()