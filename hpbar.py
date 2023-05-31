import pygame

class Hpbar:
    def __init__(self, x, y, total):
        self.x = x
        self.y = y#체력바위치
        self.total = total#최대값
        self.current = total
        self.barLength = 200
        self.barHeight = 20# 체력바 크ㄱㅣ



    def draw(self, surface):
        currentLength = self.barLength * (self.current / self.total)
        borderRect = pygame.Rect(self.x, self.y, self.barLength, self.barHeight)
        innerRect = pygame.Rect(self.x, self.y, currentLength, self.barHeight)
        pygame.draw.rect(surface, (255, 0, 0), borderRect, 2)  # 테두리렌더링
        pygame.draw.rect(surface, (0, 255, 0), innerRect)  #현재체력으로다시렌더링
