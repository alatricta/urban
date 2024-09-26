from random import randint
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 7
FORSAGE = 5

BALL_SPEED = 5

PLAYER_COUNT = 2


class Player(arcade.Sprite):
    def __init__(self, path_image):
        super().__init__(path_image, 0.13)
        self.score = 0

    def update(self):
        """ Move the player """
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

class Ball(arcade.Sprite):
    def __init__(self, path_image):
        super().__init__(path_image, 0.12)
        self.score = 0

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0 or self.right > SCREEN_WIDTH - 1:
            self.change_x = -self.change_x

        if self.bottom < 0 or self.top > SCREEN_HEIGHT - 1:
            self.change_y = -self.change_y

class MenuView(arcade.View):
    def __init__(self):
        super().__init__()

        self.buttons = arcade.SpriteList()
        coord_x, coord_y = self.window.get_size()
        offset = 50
        coord_x = coord_x // 2
        coord_y = coord_y // 2 + offset
        self.set_1_player_button = arcade.create_text_sprite(
            '1 Player',
            coord_x,
            coord_y,
            arcade.color.WHITE,
            font_size=50,
            bold=True,
            anchor_x="center",
            anchor_y="center",
            background_color=arcade.color.BLACK
        )
        self.set_1_player_button.center_x = coord_x
        self.set_1_player_button.center_y = coord_y
        self.buttons.append(self.set_1_player_button)
        coord_y -= offset * 2
        self.set_2_player_button = arcade.create_text_sprite(
            '2 Player',
            coord_x,
            coord_y,
            arcade.color.WHITE,
            font_size=50,
            bold=True,
            anchor_x="center",
            anchor_y="center",
            background_color=arcade.color.BLACK
        )
        self.set_2_player_button.center_x = coord_x
        self.set_2_player_button.center_y = coord_y
        self.buttons.append(self.set_2_player_button)


    def on_show_view(self):
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        self.clear()

        self.buttons.draw()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        global PLAYER_COUNT
        hit_buttons = arcade.get_sprites_at_point((_x, _y), self.buttons)

        if hit_buttons:
            if hit_buttons[0] == self.set_1_player_button:
                PLAYER_COUNT = 1
            else:
                PLAYER_COUNT = 2

            game = GameView()
            self.window.show_view(game)

class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        arcade.set_background_color(arcade.color.BANGLADESH_GREEN)
        self.window.set_min_size(width=480, height=360)

        # Variables that will hold sprite lists
        self.player_list = None
        self.ball_list = None

        # Set up the player info
        # self.player_sprite = None

        # Track the current state of what key is pressed
        self.p1_left_pressed = False
        self.p1_right_pressed = False
        self.p2_left_pressed = False
        self.p2_right_pressed = False

        self.p1_forsage = False
        self.p2_forsage = False

        self.score_players = [0, 0]
        self.score_comp = [0, 0]

        # Don't show the mouse cursor
        if PLAYER_COUNT == 1:
            self.window.set_mouse_visible(False)

        self.setup()

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.ball_list = arcade.SpriteList()

        offset = 100 if PLAYER_COUNT > 1 else 0

        for i in range(PLAYER_COUNT):
            self.player_list.append(Player(f'module_6_pong_resource/racket{i}.png'))
            self.player_list[i].center_x = SCREEN_WIDTH // 2 + offset
            self.player_list[i].center_y = 100
            self.score_players[i] = self.player_list[i].score

            self.ball_list.append(Ball(f'module_6_pong_resource/ball{i}.png'))
            self.ball_list[i].center_x = SCREEN_WIDTH // 2 + offset
            self.ball_list[i].center_y = SCREEN_HEIGHT // 2
            self.ball_list[i].change_x = randint(1, BALL_SPEED)
            self.ball_list[i].change_y = BALL_SPEED
            self.score_comp[i] = self.ball_list[i].score

            offset = -offset

    def on_draw(self):
        # Screen and border
        self.clear()
        center_x = SCREEN_WIDTH // 2
        center_y = SCREEN_HEIGHT // 2
        arcade.draw_rectangle_outline( center_x, center_y, SCREEN_WIDTH, SCREEN_HEIGHT, arcade.color.WHITE, 20 )
        arcade.draw_rectangle_outline( center_x, center_y, SCREEN_WIDTH, SCREEN_HEIGHT, arcade.color.BLACK, 2 )

        # Show score
        step_line = 30
        font_size = 16
        coord_player_score = [
            (SCREEN_WIDTH-20, SCREEN_HEIGHT-step_line, 'right'),
            (20, SCREEN_HEIGHT-step_line, 'left')
        ]
        coord_comp_score = [
            (SCREEN_WIDTH-20, SCREEN_HEIGHT-step_line*2, 'right'),
            (20, SCREEN_HEIGHT - step_line*2, 'left')
        ]
        for i, pl in enumerate(self.player_list):
            arcade.draw_text(
                f'Score P{i+1}: {pl.score}',
                coord_player_score[i][0],
                coord_player_score[i][1],
                anchor_x=coord_player_score[i][2],
                bold=True,
                font_size = font_size
            )
        for i, bl in enumerate(self.ball_list):
            arcade.draw_text(
                f'Score COMP{i+1}: {bl.score}',
                coord_comp_score[i][0],
                coord_comp_score[i][1],
                anchor_x=coord_comp_score[i][2],
                bold = True,
                font_size = font_size
            )

        # Draw all the sprites.
        self.player_list.draw()
        self.ball_list.draw()

    def on_update(self, delta_time: float):
        self.player_list.update()
        self.ball_list.update()

        for ball in self.ball_list:
            for pl in self.player_list:
                if pl.center_y+30 >= ball.bottom >= pl.center_y and \
                        pl.left < ball.center_x < pl.right and \
                        ball.change_y < 0:
                    ball.change_y = -ball.change_y
                    pl.score += 1

            if ball.bottom < 0:
                ball.score += 1

    def on_resize(self, width, height):
        global SCREEN_WIDTH, SCREEN_HEIGHT
        super().on_resize(width, height)
        SCREEN_WIDTH, SCREEN_HEIGHT = self.window.get_size()

    def update_player_speed(self):
        for pl in self.player_list:
            pl.change_x = 0
            pl.change_y = 0

        speed_p1 = (MOVEMENT_SPEED + FORSAGE) if self.p1_forsage else MOVEMENT_SPEED
        speed_p2 = (MOVEMENT_SPEED + FORSAGE) if self.p2_forsage else MOVEMENT_SPEED

        if self.p1_left_pressed and not self.p1_right_pressed:
            self.player_list[0].change_x = -speed_p1
        elif self.p1_right_pressed and not self.p1_left_pressed:
            self.player_list[0].change_x = speed_p1

        if self.p2_left_pressed and not self.p2_right_pressed:
            self.player_list[1].change_x = -speed_p2
        elif self.p2_right_pressed and not self.p2_left_pressed:
            self.player_list[1].change_x = speed_p2

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if PLAYER_COUNT == 1:
            self.player_list[0].center_x = x

    def on_key_press(self, key, modifiers):
        match key:
            case arcade.key.RCTRL:
                self.p1_forsage = True
            case arcade.key.LSHIFT:
                self.p2_forsage = True
            case arcade.key.LEFT:
                self.p1_left_pressed = True
            case arcade.key.RIGHT:
                self.p1_right_pressed = True
            case arcade.key.A:
                self.p2_left_pressed = True
            case arcade.key.D:
                self.p2_right_pressed = True

        self.update_player_speed()

    def on_key_release(self, key, modifiers):
        match key:
            case arcade.key.RCTRL:
                self.p1_forsage = False
            case arcade.key.LSHIFT:
                self.p2_forsage = False
            case arcade.key.LEFT:
                self.p1_left_pressed = False
            case arcade.key.RIGHT:
                self.p1_right_pressed = False
            case arcade.key.A:
                self.p2_left_pressed = False
            case arcade.key.D:
                self.p2_right_pressed = False

        self.update_player_speed()

def main():
    win = arcade.Window(
        width = SCREEN_WIDTH,
        height = SCREEN_HEIGHT,
        title = 'PongPing Game',
        center_window = True,
        resizable = True
    )
    win.show_view(MenuView())
    arcade.run()

if __name__ == '__main__':
    main()