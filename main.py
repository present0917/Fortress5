import pygame
import tank
import block
import bullet
import hpbar
import map

pygame.init()  # 초기화

maps = {
    "1": [(0, 200),(100, 300),(200, 400),(300, 500),(400, 500),(500, 400),(600, 300),(700, 200)],
    "2": [(0,300),(700,300)],
    "3": [(0, 450), (100, 500),(600, 450), (700, 400)]
}
#맵구조 설계


font = pygame.font.Font(None, 100) #기본폰트, 크기
backgroundColor = (255, 255, 255)  # 배경색 지정
background = [800, 600]  # 배경 해상도
screen = pygame.display.set_mode(background)  # screen을 지정한 해상도로
done = False  # 게임이 끝났는가?
clock = pygame.time.Clock()
tanks = [tank.Tank(1), tank.Tank(2)]  # 탱크가 두개가됐다.
hbar = [hpbar.Hpbar(10, 10, 100), hpbar.Hpbar(800 - 210, 10, 100)] #각 플레이어별 체력바

nowPlayer=0 #0번플레이어부터 시작
blocks = pygame.sprite.Group()  # 스프라이트의 묶음으로


theBullet = None  # 탄환변수

def running():

    themap = map.selectMap(screen, maps) #고른맵을 반환받아
    for i in maps[themap]: #반환받은 숫자로 맵중에골라서
        blockObj = block.Block(i)
        blocks.add(blockObj) #맵에따라 블럭배치
    
    global done, tanks, theBullet,nowPlayer  # 캐릭터와 게임오버여부,탄환 전역변수로
    while not done:
        clock.tick(30)  # 30프레임
        screen.fill(backgroundColor)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pygame.draw.circle(screen,(0, 0, 0),(tanks[nowPlayer].rect.x + 50, tanks[nowPlayer].rect.y - 10),10)
        #턴플레이어위에 점하나띄운다.

        
        for i in range(2): #두명치 체력바 다 그려준다
            hbar[i].current = tanks[i].hp
            hbar[i].draw(screen)

        for tank in tanks:
            if not tank.isLand:
                tank.rect.y+=10
                if pygame.sprite.spritecollide(tank,blocks,False):
                    tank.isLand=True
            if not pygame.sprite.spritecollide(tank,blocks,False):
                tank.isLAnd=False


        exist=theBullet is not None
        newBullet = tanks[nowPlayer].update(pygame.key.get_pressed(),blocks,exist)  # 키 입력을 받은대로 탱크에 보낸다.
        if newBullet and not exist:
            theBullet = newBullet  # 새 탄환
        

        
        
        for tank in tanks:
            tank.flip(screen)   #탱크 렌더링
              # for i,tank in enumerate(tanks):  
                #   screen.blit(tank.image, tank.rect)  #이전에는 그냥 출력했지만
                #상황에 따라 탱크의 모양을 뒤집으며 시점을 바꾸며 렌더링
        
            
            
            
            
        
        blocks.draw(screen)  # 블럭묶음 렌더링   

        if theBullet:
            theBullet.update()
            if theBullet.rect.y >= background[1]:  # 탄환이 바닥에 닿으면
                theBullet = None  # 탄환을제거
                nowPlayer = (nowPlayer + 1) % 2  # 턴넘김
            else:
                for i, tank in enumerate(tanks):  # hit체크
                    if theBullet.rect.colliderect(tank.rect) and i != nowPlayer:  # 상대에 탄맞으면
                        tank.hiten()  # 체력까기
                        theBullet = None  # 탄환제거
                        nowPlayer = (nowPlayer + 1) % 2  # 턴넘김
                        break
                if theBullet:  # 아직탄환 날라가는중이면
                    screen.blit(theBullet.image, theBullet.rect)  # 렌더링
                


        

        if not tanks[0].alive:  #죽으면
            text = font.render("Player2 Win", True, (0, 0, 0))  #승리문구
            screen.blit(text, (100, 100))  #텍스트렌더링
            pygame.display.update()  #렌더링
            pygame.time.wait(5000)  #5초동안 보여주다가
            break  #게임종료

        elif not tanks[1].alive: 
            text = font.render("Player1 Win", True, (0, 0, 0)) 
            screen.blit(text, (100, 100))
            pygame.display.update() 
            pygame.time.wait(2000) 
            break 

        pygame.display.update()

running()
pygame.quit()  # 종료
