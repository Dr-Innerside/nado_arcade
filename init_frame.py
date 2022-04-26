import pygame

# 1. 기본 초기화(반드시 해야됨)
pygame.init()
# 화면 크기 설정
screen_width = 480  # 가로
screen_height = 640  # 세로
screen = pygame.display.set_mode((screen_width, screen_height))
# 화면 타이틀
pygame.display.set_caption("Title")
# Frame Per Second
clock = pygame.time.Clock()

# 2. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 폰트, 속도)


# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    dt = clock.tick(30)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창 나가기 버튼을 누르면
            running = False  # 게임이 진행중이 아님

    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기
    
    pygame.display.update()  # 게임 화면을 다시 그리기!

# 게임 종료
pygame.quit()
