import random
import pygame
import time
import threading

pygame.init()

# Initialize the counters
full_light_count = 0
mid_light_count = 0
stra2_count = 0

total_vehicle_count = 0

def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)

road = pygame.image.load("road.png")
truck = pygame.image.load("truck.png")
grass = scale_image(pygame.image.load("grass.png"), 0.45)
bike = pygame.image.load("bike.png")
car = pygame.image.load("car.png")
stra = pygame.image.load("off-7.png")
stra2 = pygame.image.load("off-7.png")
mid_light = pygame.image.load("on-mid1.png")
full_light = pygame.image.load("on-f.png")
ca = pygame.image.load("car.png")

width, height = 1000, 590
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Real Time Traffic Simulation")

car_positions = []
bike_positions = []
truck_positions = []

car_count = 0
truck_count = 0
bike_count = 0

pixel_positions = [255, 570, 870]  

def handle_image_change(car_positions):
    global stra2, full_light, mid_light, full_light_count, mid_light_count, stra2_count

    lights_positions = [(0, 80), (270, 80), (570, 80), (870, 80)]
    default_lights = [stra2, stra2, stra2, stra2]

    for car_pos in car_positions:
        if 0 < car_pos[0] < 255:
            default_lights[0] = full_light
            default_lights[1] = mid_light
            full_light_count += 1
            mid_light_count += 1
        elif 255 < car_pos[0] < 570:
            default_lights[1] = full_light
            default_lights[2] = mid_light
            full_light_count += 1
            mid_light_count += 1
        elif 570 < car_pos[0] < 870:
            default_lights[2] = full_light
            default_lights[3] = mid_light
            full_light_count += 1
            mid_light_count += 1
        elif 870 < car_pos[0] < width:
            default_lights[3] = full_light
            full_light_count += 1

    for light, position in zip(default_lights, lights_positions):
        screen.blit(light, position)
        if light == stra2:
            stra2_count += 1

def swap_images():
    global stra, stra2, full_light, mid_light
    while True:
        if car_count or bike_count or truck_count >= 1:
            stra = pygame.image.load("on.png")
        else:
            stra2 = pygame.image.load("off-7.png")
        time.sleep(0.1)

lock = threading.Lock()

t0 = threading.Thread(target=swap_images)
t0.daemon = True
t0.start()

t3 = threading.Thread(target=handle_image_change, args=(car_positions,))
t3.daemon=True
t3.start()

run = True
clock = pygame.time.Clock()

while run:
    # Define the positions for road and grass
    road_positions = [(0, 70), (200, 70), (400, 70), (600, 70)]
    grass_positions = [
        (0, 0), (150, 0), (300, 0), (400, 0), (500, 0), (600, 0), (700, 0), (830, 0),
        (830, 400), (700, 400), (600, 400), (500, 400), (400, 400), (300, 400), (150, 400), (0, 400)
    ]

    # Blit road tiles
    for pos in road_positions:
        screen.blit(road, pos)

    # Blit grass tiles
    for pos in grass_positions:
        screen.blit(grass, pos)

    if random.randint(1, 200) == 1:
        car_positions.append([-50, random.randint(200, 380)])

    for i in range(len(car_positions)):
        car_position = car_positions[i]
        car_position[0] += 5

        handle_image_change(car_positions)

        screen.blit(car, car_position)

        if car_position[0] > 0 :
           car_count = 1
        if car_position[0] > width:
            car_positions.pop(i)
            car_count = car_count + 1
            break

    font = pygame.font.Font(None, 36)
    total_vehicle_count = len(car_positions) 

    def get_traffic_level(total_vehicle_count):
        if total_vehicle_count <= 3:
            return "Low Traffic"
        elif 4 <= total_vehicle_count <= 6:
            return "Moderate Traffic"
        else:
            return "Heavy Traffic"

    if total_vehicle_count >= 1 :
        camera_text = font.render("Camera On",True,(0, 0, 0))
    else:
        screen.blit(stra2, (0, 80))
        screen.blit(stra2, (270, 80))
        screen.blit(stra2, (570, 80))
        screen.blit(stra2, (870, 80))
        camera_text = font.render("Camera Off",True,(245,19,2))

    clock.tick(160)    
    car_count_text = font.render("Real Vehicle Count: " + str(total_vehicle_count), True, (0,0,0))
    screen.blit(car_count_text, (10, 10))
    screen.blit(camera_text, (850, 10))
    traffic_level = get_traffic_level(total_vehicle_count)
    traffic_text = font.render("Traffic Level: " + traffic_level, True, (0,0,0))
    screen.blit(traffic_text, (10, 40))

    pygame.display.flip() 
    pygame.display.flip()  # update the display

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # check if user clicked the window
            run = False

# Print the counts to the console after the simulation is closed
print("Full light intensity count: ", full_light_count)
print("Mid light intensity count: ", mid_light_count)
print("Zero light intensity count", stra2_count)
