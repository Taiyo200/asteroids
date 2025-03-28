from circleshape import *
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0
        self.timer = 0
        

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)
        
        
    def rotate(self, dt):
        self.rotation += PLAYER_TRUN_SPEED * dt
        
        
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
        
    def shoot(self):
        if self.timer < 0:
            bullet = Shoot(self.position.x, self.position.y, SHOT_RADIUS)
            direction = pygame.Vector2(0, -1).rotate(self.rotation - 180)
            bullet.velocity = direction * PLAYER_SHOOT_SPEED
            self.timer = PLAYER_SHOOT_COOLDOWN
    
    
    def update(self, dt):
        
        self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
            
            
class Shoot(CircleShape):
    def __init__(self, x, y, SHOT_RADIUS):
        super().__init__(x, y, SHOT_RADIUS)
        if Shoot.containers:
            for container in Shoot.containers:
                container.add(self)
        

    def draw(self, screen):
        pygame.draw.circle(screen, 
                           (255,255,255), 
                           (self.position.x, self.position.y), 
                           self.radius, 
                           width = 2) 
        
        
    def update(self, dt):
        self.position += (self.velocity * dt)