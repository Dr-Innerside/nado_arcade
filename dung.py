import pygame, random


# 1. 기본 초기화(반드시 해야됨)
pygame.init()
# 화면 크기 설정
screen_width = 480  # 가로
screen_height = 640  # 세로
screen = pygame.display.set_mode((screen_width, screen_height))
# 화면 타이틀
pygame.display.set_caption("똥피하기")
# Frame Per Second
clock = pygame.time.Clock()
# Speed
character_speed = 15
enemy_speed = 10

# 2. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 폰트, 속도)

# background
background = pygame.image.load('background.png')
# character
character = pygame.image.load('character.png')
character_size = character.get_size()
character_width = character_size[0]
character_height = character_size[1]
character_x = screen_width/2 - character_width/2
character_y = screen_height - character_height
# enemy
enemy = pygame.image.load('enemy.png')
enemy_size = enemy.get_size()
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x = random.randint(0, screen_width-enemy_width)
enemy_y = 0


# location
to_x = 0
to_y = 0


# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    dt = clock.tick(30)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창 나가기 버튼을 누르면
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                to_x += character_speed

        if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의
    # character
    character_x += to_x

    if character_x < 0:
        character_x = 0
    elif character_x > screen_width - character_width:
        character_x = screen_width - character_width

    # enemy
    enemy_y += enemy_speed

    if enemy_y > screen_height:
        enemy_y = 0
        enemy_x = random.randint(0, screen_width-enemy_width)


    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x
    character_rect.top = character_y

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x
    enemy_rect.top = enemy_y

    if character_rect.colliderect(enemy_rect):
        print("collide")
        running=False

    # 5. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(character, (character_x,character_y))
    screen.blit(enemy, (enemy_x,enemy_y))

    pygame.display.update()  # 게임 화면을 다시 그리기!

# 게임 종료
pygame.quit()
