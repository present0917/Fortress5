import pygame
import random #랜덤한 위치에 렌더링하기위해

screenW = 800
screenH = 600
blockColor= (255, 0, 0) #red

class Block(pygame.sprite.Sprite):
    def __init__(self,posi):
        super().__init__()
        self.image = pygame.Surface((random.randint(70, 120), 20)) #가로 길이 변화폭을 작게
        self.image.fill(blockColor)
        self.rect = self.image.get_rect() #탱크와 충돌설정 위해
        # self.rect.x = random.randint(0, screenW - self.rect.width)
        # self.rect.y = random.randint(300, 600)
        self.rect.x = (posi[0]) 
        self.rect.y = (posi[1]) #블럭배치위치를 지정한 맵 데이터로
