import pygame

def chess_grid():



# 초기화 반드시 필요
pygame.init()

# 화면 크기 설정
screen_width = 480  # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀
pygame.display.set_caption("나도코딩 오락실: PANG")

# 배경 이미지 불러오기
background = pygame.image.load("background.png")

# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    # 파이게임을 쓸 때 무조건 넣는 코드
    # 입력 값을 계속 받아줌
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 창 나가기 버튼을 누르면
            running = False

# 게임 종료
pygame.quit()
