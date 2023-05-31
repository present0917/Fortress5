import pygame
from pygame.locals import * #방향키인식위해
import os #경로설정 위해
import random #무작위선택 위해


class Tank(pygame.sprite.Sprite): #스프라이트화
    def __init__(self): #초기화
        self.images = [] #빈배열선언후
        image_names = ["cannon.png", "carrot.png", "catapult.png", "missile.png"] #탱크폴더의 이미지이름들
        for name in image_names:
            image_path = os.path.join("images", "tank", name) #해당경로의 파일이미지
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, (100, 60))
            self.images.append(image) #모든이미지를 올려두고
        self.index = random.randint(0, len(self.images) - 1)  #무작위 선택
        self.image = self.images[self.index] #무작위 탱크 선택
        self.rect = self.image.get_rect() #충돌설정 위한 범위설정
        self.speed = 5

    def update(self, keys):
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed
        if keys[K_UP]:
            self.rect.y -= self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed