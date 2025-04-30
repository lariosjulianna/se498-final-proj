import pygame
import sys
import mysql.connector


# Initialize pygame
pygame.init()

# Set screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Striking Vipers - Login")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 50, 255)
GREEN = (50, 255, 50)

# Fonts
font = pygame.font.SysFont("Arial", 30)
button_font = pygame.font.SysFont("Arial", 24)

# Game state
current_screen = "login"  # 'login' or 'level'

# Function to draw the login screen
def draw_login_screen(username, password, classcode, username_box, password_box, classcode_box):
    screen.fill(WHITE)

    # Title
    login_text = font.render("Login Page", True, BLACK)
    screen.blit(login_text, (WIDTH // 2 - login_text.get_width() // 2, HEIGHT // 6))

    # Draw input boxes
    pygame.draw.rect(screen, BLUE, classcode_box, 2)
    pygame.draw.rect(screen, BLUE, username_box, 2)
    pygame.draw.rect(screen, BLUE, password_box, 2)

    # Render and draw text inside input boxes
    classcode_text = font.render(classcode if classcode else "Class Code", True, BLACK)
    username_text = font.render(username if username else "Username", True, BLACK)
    hidden_pw = "*" * len(password)
    password_text = font.render(hidden_pw if password else "Password", True, BLACK)

    screen.blit(classcode_text, (classcode_box.x + 10, classcode_box.y + 5))
    screen.blit(username_text, (username_box.x + 10, username_box.y + 5))
    screen.blit(password_text, (password_box.x + 10, password_box.y + 5))

    # Draw login button
    login_button = pygame.draw.rect(screen, GREEN, (WIDTH // 2 - 100, HEIGHT // 2 + 100, 200, 50))
    button_text = button_font.render("Login", True, WHITE)
    screen.blit(button_text, (WIDTH // 2 - button_text.get_width() // 2, HEIGHT // 2 + 110))

    return login_button

# Draw level selection screen
def draw_level_screen():
    screen.fill(WHITE)
    level_text = font.render("Select Level", True, BLACK)
    screen.blit(level_text, (WIDTH // 2 - level_text.get_width() // 2, HEIGHT // 4))

    level_1_button = pygame.draw.rect(screen, GREEN, (WIDTH // 2 - 100, HEIGHT // 2 - 20, 200, 50))
    level_2_button = pygame.draw.rect(screen, GREEN, (WIDTH // 2 - 100, HEIGHT // 2 + 60, 200, 50))

    screen.blit(button_font.render("Level 1", True, WHITE), (WIDTH // 2 - 40, HEIGHT // 2 - 10))
    screen.blit(button_font.render("Level 2", True, WHITE), (WIDTH // 2 - 40, HEIGHT // 2 + 70))

    return level_1_button, level_2_button

# Draw level screen
def draw_level1_screen():
    screen.fill(BLACK)
    level_text = font.render("Level 1", True, WHITE)
    screen.blit(level_text, (WIDTH//2-level_text.get_width()//2,HEIGHT//4))

    begin_button = pygame.draw.rect(screen, GREEN, (WIDTH // 2 - 100, HEIGHT // 2 - 20, 200, 50))

    screen.blit(button_font.render("Begin", True, WHITE), (WIDTH // 2 - 40, HEIGHT // 2 - 10))

#login verification 
def handle_login_event(username, password, classcode):
    try:
        conn = mysql.connector.connect(
            host="localhost",   
            user="root",
            password="CPSC408!",
            database="StrikingVipers"
        )

        cursor = conn.cursor()

        query = """
            SELECT * FROM Students 
            WHERE StudentUserName = %s AND StudentPassWord = %s AND ClassCode = %s
        """
        cursor.execute(query, (username, password, classcode))
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        return result is not None

    except mysql.connector.Error as err:
        print("Database error:", err)
        return False
# Main game loop
def main():
    global current_screen
    username = ""
    password = ""
    classcode = ""
    selected_box = None

    print("Main loop starting...")

    # Centered input boxes
    box_width = 300
    box_height = 40
    box_x = WIDTH // 2 - box_width // 2
    spacing = 20  # Space between boxes

    # Stack boxes vertically
    classcode_box = pygame.Rect(box_x, HEIGHT // 2 - box_height - spacing*2, box_width, box_height)
    username_box = pygame.Rect(box_x, HEIGHT // 2 - box_height//2, box_width, box_height)
    password_box = pygame.Rect(box_x, HEIGHT // 2 + box_height + spacing, box_width, box_height)

    while True:
        screen.fill(WHITE)

        if current_screen == "login":
            login_button = draw_login_screen(username, password, classcode, username_box, password_box, classcode_box)
            #print("Drawing login screen...")

        elif current_screen == "level":
            level_1_button, level_2_button = draw_level_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if current_screen == "login":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("Mouse click detected at:", event.pos)

                    if classcode_box.collidepoint(event.pos):
                        selected_box = "classcode"
                        print("Classcode box selected")

                    elif username_box.collidepoint(event.pos):
                        selected_box = "username"
                        print("Username box selected")

                    elif password_box.collidepoint(event.pos):
                        selected_box = "password"
                        print("Password box selected")

                    elif login_button.collidepoint(event.pos):
                        print("Login button clicked!")
                        print("Classcode entered:", classcode)
                        print("Username entered:", username)
                        print("Password entered:", password)

                        if handle_login_event(username, password, classcode):
                            print("Login successful!")
                            current_screen = "level"
                        else:
                            print("Login failed.")

                elif event.type == pygame.KEYDOWN:
                    print("Key pressed:", event.unicode)

                    if selected_box == "classcode":
                        if event.key == pygame.K_BACKSPACE:
                            classcode = classcode[:-1]
                        else:
                            classcode += event.unicode
                        print("Updated classcode:", classcode)

                    elif selected_box == "username":
                        if event.key == pygame.K_BACKSPACE:
                            username = username[:-1]
                        else:
                            username += event.unicode
                        print("Updated username:", username)

                    elif selected_box == "password":
                        if event.key == pygame.K_BACKSPACE:
                            password = password[:-1]
                        else:
                            password += event.unicode
                        print("Updated password:", password)

            elif current_screen == "level":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("Mouse click on level screen at:", event.pos)
                    if level_1_button.collidepoint(event.pos):
                        print("Level 1 clicked")
                    elif level_2_button.collidepoint(event.pos):
                        print("Level 2 clicked")

        pygame.display.update()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("CRASHED WITH ERROR:", e)
        pygame.quit()
        sys.exit()

