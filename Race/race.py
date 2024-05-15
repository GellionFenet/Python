import pygame
from pygame.locals import *
import random

pygame.init()

# Создание окна
width = 500
height = 500
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Car Game')

# Звуки
pygame.mixer.music.load('sound/engine.wav')
pygame.mixer.music.play(-1, 0.0)
gameOverSound = pygame.mixer.Sound('../Race/sound/crash.wav')

# Цвета
gray = (100, 100, 100)
kor = (150, 75, 0)
green = (76, 208, 56)
red = (200, 0, 0)
white = (255, 255, 255)
yellow = (255, 232, 0)
black = (0, 0, 0)

# Размеры дорог и указателей
road_width = 300
marker_width = 10
marker_height = 50

# координаты полосы движения
left_lane = 150
center_lane = 250
right_lane = 350
lanes = [left_lane, center_lane, right_lane]

# дорожные указатели и бордюры
road = (100, 0, road_width, height)
left_edge_marker = (95, 0, marker_width, height)
right_edge_marker = (395, 0, marker_width, height)

# для анимации перемещения маркеров полосы движения
lane_marker_move_y = 0

# Стартовые координаты игрока
player_x = 250
player_y = 400

# Настройки кадра
clock = pygame.time.Clock()
fps = 120

# Настройки игры
gameover = False
speed = 2
score = 0

class Vehicle(pygame.sprite.Sprite):
    
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        # scale the image down so it's not wider than the lane
        image_scale = 45 / image.get_rect().width
        new_width = image.get_rect().width * image_scale
        new_height = image.get_rect().height * image_scale
        self.image = pygame.transform.scale(image, (new_width, new_height))
        
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        
class PlayerVehicle(Vehicle):
    
    def __init__(self, x, y):
        image = pygame.image.load('images/usercar.png')
        super().__init__(image, x, y)
        
# Группы машин
player_group = pygame.sprite.Group()
vehicle_group = pygame.sprite.Group()

# Создание авто игрока
player = PlayerVehicle(player_x, player_y)
player_group.add(player)

# Загрузка изображений ТС
image_filenames = ['police.png', 'semi_trailer.png', 'taxi.png', 'van.png']
vehicle_images = []
for image_filename in image_filenames:
    image = pygame.image.load('images/' + image_filename)
    vehicle_images.append(image)

    
# Загрузка изображения взрыва
crash = pygame.image.load('images/crash.png')
crash_rect = crash.get_rect()


# цикл игры
running = True
while running:

    clock.tick(fps)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
        # Перемещение авто игрока с помощью клавиш Налево и Направо
        if event.type == KEYDOWN:
            
            if event.key == K_LEFT and player.rect.center[0] > left_lane:
                player.rect.x -= 100
            elif event.key == K_RIGHT and player.rect.center[0] < right_lane:
                player.rect.x += 100
                
            # Проверка столкновения после перестроения
            for vehicle in vehicle_group:
                if pygame.sprite.collide_rect(player, vehicle):
                    
                    gameover = True
                    
                    # Размещение авто игрока рядом с другими ТС
                    # и определение размещения изображения аварии
                    if event.key == K_LEFT:
                        player.rect.left = vehicle.rect.right
                        crash_rect.center = [player.rect.left, (player.rect.center[1] + vehicle.rect.center[1]) / 2]
                    elif event.key == K_RIGHT:
                        player.rect.right = vehicle.rect.left
                        crash_rect.center = [player.rect.right, (player.rect.center[1] + vehicle.rect.center[1]) / 2]
            
            
    # Прорисовка травы
    screen.fill(kor)
    
    # Прорисовка дороги
    pygame.draw.rect(screen, gray, road)
    
    # Прорисовка маркеровки по краям
    pygame.draw.rect(screen, black, left_edge_marker)
    pygame.draw.rect(screen, black, right_edge_marker)
    
    # Прорисовка маркеров полос движения
    lane_marker_move_y += speed * 2
    if lane_marker_move_y >= marker_height * 2:
        lane_marker_move_y = 0
    for y in range(marker_height * -2, height, marker_height * 2):
        pygame.draw.rect(screen, white, (left_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
        pygame.draw.rect(screen, white, (center_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
        
    # Прорисовка авто игрока
    player_group.draw(screen)
    
    # Добавление ТС
    if len(vehicle_group) < 2:
        
        # Расстояние между ТС
        add_vehicle = True
        for vehicle in vehicle_group:
            if vehicle.rect.top < vehicle.rect.height * 1.5:
                add_vehicle = False
                
        if add_vehicle:
            
            # Выбор случайно полосы движения
            lane = random.choice(lanes)
            
            # Выбор случайного изображения ТС
            image = random.choice(vehicle_images)
            vehicle = Vehicle(image, lane, height / -2)
            vehicle_group.add(vehicle)
    
    # Передвижение ТС
    for vehicle in vehicle_group:
        vehicle.rect.y += speed
        
        # Удаление авто после исчезнавения с экрана
        if vehicle.rect.top >= height:
            vehicle.kill()
            
            # Добавление счётчика
            score += 1
            
            # Увеличение скорости движения после каждых 5 очков
            if score > 0 and score % 5 == 0:
                speed += 1
    
    # Прорисовка траффика
    vehicle_group.draw(screen)
    
    # Вывод счёта на экран
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render('Счёт: ' + str(score), True, white)
    text_rect = text.get_rect()
    text_rect.center = (250, 50)
    screen.blit(text, text_rect)
    
    # Проверка лобового столкновения
    if pygame.sprite.spritecollide(player, vehicle_group, True):
        gameover = True
        crash_rect.center = [player.rect.center[0], player.rect.top]
            
    # Экран завершения игры
    if gameover:
        screen.blit(crash, crash_rect)

        pygame.mixer.music.stop()
        gameOverSound.play()
        pygame.draw.rect(screen, red, (0, 50, width, 100))
        
        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render('Игра окончена. Хотите продолжить (Y-да, N-нет)?', True, white)
        text_rect = text.get_rect()
        text_rect.center = (width / 2, 100)
        screen.blit(text, text_rect)
            
    pygame.display.update()

    # Ожидание выбора пользователя
    while gameover:
        
        clock.tick(fps)

        for event in pygame.event.get():

            if event.type == QUIT:
                gameover = False
                running = False
                
            # Получение выбора пользователя
            if event.type == KEYDOWN:
                if event.key == K_y:
                    # Перезапуск игры
                    gameover = False
                    speed = 2
                    score = 0
                    vehicle_group.empty()
                    player.rect.center = [player_x, player_y]
                    pygame.mixer.music.play(-1, 0.0)
                elif event.key == K_n:
                    # Выход из цикла
                    gameover = False
                    running = False

pygame.quit()