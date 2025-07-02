import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN
from constants import PLAYER_TURN_SPEED, PLAYER_SPEED
from shot import Shot
from constants import PLAYER_SHOOT_SPEED






class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.angle = 0  # Default facing upward
        self.shoot_timer = 0  # player can shoot immediately at game start


        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)  # turn left = negative rotation
        if keys[pygame.K_d]:
          self.rotate(dt)   # turn right = positive rotation
        if keys[pygame.K_w]:
            self.move(dt)     # move forward
        if keys[pygame.K_s]:
            self.move(-dt)    # move backward (reverse direction)
        if keys[pygame.K_SPACE] and self.shoot_timer == 0:
            self.shoot()
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN

        self.shoot_timer -= dt
        if self.shoot_timer < 0:
            self.shoot_timer = 0  # keep it non-negative




    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        direction = pygame.Vector2(0, 1).rotate(self.rotation)  # match movement
        velocity = direction * PLAYER_SHOOT_SPEED
        Shot(self.position.x, self.position.y, velocity)
