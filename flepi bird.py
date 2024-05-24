import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Warna
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Membuat layar
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")

# Load gambar
bird_img = pygame.image.load("flappy.png")
pipe_img = pygame.image.load("pipe.jpeg")
background_img = pygame.image.load("mikasa.webp")

# Mengubah ukuran gambar burung dan pipa
bird_img = pygame.transform.scale(bird_img, (50, 50))
pipe_img = pygame.transform.scale(pipe_img, (80, 500))

# Clock untuk mengatur frame rate
clock = pygame.time.Clock()

# Fungsi untuk menampilkan teks di layar
def draw_text(text, font, color, x, y):
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))

# Fungsi untuk menjalankan permainan
def game():
    bird_x = 50
    bird_y = SCREEN_HEIGHT // 2
    bird_velocity = 0
    gravity = 1

    pipe_width = 80
    pipe_height = random.randint(100, 400)
    pipe_x = SCREEN_WIDTH
    pipe_y = SCREEN_HEIGHT - pipe_height

    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_velocity = -15

        bird_velocity += gravity
        bird_y += bird_velocity

        pipe_x -= 5
        if pipe_x < -pipe_width:
            pipe_x = SCREEN_WIDTH
            pipe_height = random.randint(100, 400)
            pipe_y = SCREEN_HEIGHT - pipe_height
            score += 1

        screen.fill(WHITE)
        screen.blit(background_img, (0, 0))
        screen.blit(bird_img, (bird_x, bird_y))
        screen.blit(pipe_img, (pipe_x, pipe_y))
        draw_text(f"Score: {score}", pygame.font.Font(None, 36), GREEN, 10, 10)

        if bird_y > SCREEN_HEIGHT or bird_y < 0:
            running = False

        pygame.display.update()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    game()
