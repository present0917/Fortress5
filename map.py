import pygame
import sys

def selectMap(screen, maps):
    font = pygame.font.Font(None, 100) #기본폰트, 크기
    screen.fill((255,255,255)) #배경색
    mapText = font.render("Choose the Map", True, (0, 0, 0)) #맵선택문구
    screen.blit(mapText, (121, 25))

    mapsel = [] #버튼 담을 빈배열
    for i, mapName in enumerate(maps.keys()): #필드명으로
        buttonText = font.render(mapName, True, (0, 0, 0))#필드명으로 텍스트
        buttonRect = pygame.Rect(125 + (i * 200), 300, 100, 100) #125부터 간격벌리면서
        pygame.draw.rect(screen, (0, 255, 0), buttonRect) 
        screen.blit(buttonText, (145 + (i * 200), 315))
        mapsel.append((buttonRect, mapName)) #만든거 배열에 넣고

    selectedMap = None
    while not selectedMap:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #끄는건 항상넣어주고
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: #누르면
                for buttoneRect, mapName in mapsel:
                    if buttoneRect.collidepoint(event.pos): #누른위치가 버튼과충들
                        selectedMap = mapName #고른맵을 담아서
                        break
        pygame.display.update()

    return selectedMap#맵숫자반환
