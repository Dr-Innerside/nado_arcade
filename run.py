import pygame, os

# 초기화 반드시 필요
pygame.init()

# 화면 크기 설정
screen_width = 480  # 가로
screen_height = 640  # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀
pygame.display.set_caption("나도코딩 오락실: PANG")

# Frame Per Second
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("./background.png")

# 스프라이트 불러오기
character = pygame.image.load("./character.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해옴
character_width = character_size[0]  # 캐릭터의 가로 크기
character_height = character_size[1]  # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = 0
to_y = 0

# 이동속도
character_speed = 5

# bgm
pygame.mixer.init()
pygame.mixer.music.load('bgm.mp3')
pygame.mixer.music.play()


# 에너미 캐릭터
enemy = pygame.image.load("./enemy.png")
enemy_size = enemy.get_rect().size  # 이미지의 크기를 구해옴
enemy_width = enemy_size[0]  # 에너미의 가로 크기
enemy_height = enemy_size[1]  # 에너미의 세로 크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)

# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트 객체 생성 (폰트, 크기)

WHITE = (255, 255, 255)

# 총 시간
total_time = 10

# 시간 계산
start_ticks = pygame.time.get_ticks()  # 시작 tick 을 받아옴

# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    dt = clock.tick(120)  # 게임화면의 초당 프레임 수를 설정
    # 파이게임을 쓸 때 무조건 넣는 코드
    # 입력 값을 계속 받아줌
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창 나가기 버튼을 누르면
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP:  # 캐릭터를 위쪽으로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:  # 캐릭터를 아래쪽으로
                to_y += character_speed

        if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    # 가로 경계 값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    # 세로 경계 값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print('collide')
        running = False

    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # 경과시간(ms)를 1000으로 나누어서 초(s) 단위로 표시

    #  시간, 안티알리아스(True), RGB 색상 값
    timer = game_font.render(str(int(total_time - elapsed_time)), True, WHITE)
    # print(timer)

    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # 적 그리기
    screen.blit(timer, (10, 10))


    # 시간이 0 이하면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임 아웃")
        running = False


    pygame.display.update()  # 게임 화면을 다시 그리기!

# 게임 종료
pygame.quit()
