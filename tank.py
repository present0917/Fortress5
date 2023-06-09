import pygame
from pygame.locals import * #방향키인식위해
import os #경로설정 위해
import random #무작위선택 위해
import bullet

class Tank(pygame.sprite.Sprite): #스프라이트화
    def __init__(self,player): #초기화
        super().__init__()
        self.images = [] #빈배열선언후
        imageNames = ["cannon.png", "carrot.png", "catapult.png", "missile.png"] #탱크폴더의 이미지이름들
        for name in imageNames:
            image_path = os.path.join("images", "tank", name) #해당경로의 파일이미지
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, (100, 60))
            self.images.append(image) #모든이미지를 올려두고
        self.index = random.randint(0, len(self.images) - 1)  #무작위 선택
        self.image = self.images[self.index] #무작위 탱크 선택
        self.rect = self.image.get_rect() #충돌설정 위한 범위설정
        if player==1:
            self.direc="R"
        else:
            self.direc="L" #플레이어에 따른 초기방향설정    

        if player == 1:
            self.rect.x = 0
        else:
            self.rect.x=700  # 탱크위치 플레이어따라 선택
        self.rect.y =0
        self.speed = 5
        self.hp=100 #체력초기설정
        self.power=0
        self.isLand=False
        self.firing = False
        self.fireTime = 0
        self.theBullet=None #발사된총알
        self.alive=True #살아있는지

    def flip(self, surface):
        image = self.image
        if self.direc == "L":
            image = pygame.transform.flip(image, True, False)
        surface.blit(image, self.rect) #방향따라서 렌더링
        
        if self.firing: #발사 게이지, 발사중이면 탱크 위에 게이지가 나온다.
            pygame.draw.rect(surface,(255,0,0), (self.rect.x, self.rect.y - 10, 100 * self.fireTime / 3, 5)) 
            

    def fire(self):
        speed = [5, -10 * self.fireTime]  # 스페이스 누르는 시간 비례
        return bullet.Bullet(self.rect.center, speed,self.direc)


    def update(self, keys,blocks,exist):
        if exist:
            return
        if self.rect.y>600:
            self.hp-=20
        if self.hp <= 0:
            self.kill()
        if keys[K_LEFT] and self.isLand:
            self.rect.x -= self.speed
            self.direc="L"
        if keys[K_RIGHT]and self.isLand:
            self.rect.x += self.speed
            self.direc="R"

        if keys[K_SPACE]:
            if not self.firing and self.isLand:
                self.firing = True
                self.fireTime = 0
            else:
                if self.fireTime < 10:
                    self.fireTime += 0.05
                else:
                    self.firing = False
                    return self.fire()
        else:
            if self.firing:
                self.firing = False
                return self.fire()
            
    def hiten(self):  # 탱크가 탄환에 맞았을 때 체력을 깎는 함수입니다.
        self.hp -= 40
        

    def kill(self):
        self.alive = False