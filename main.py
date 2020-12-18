import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Building of the Canadian Pacific Railway")

train_imgs = []
train_change = 0
checkpoint = 1

for i in range(10):
    train_imgs.append(
        pygame.transform.scale(pygame.image.load("images/frame_0" + str(i) + "_delay-0.07s.png"), (400, 180)))

for i in range(10, 16):
    train_imgs.append(
        pygame.transform.scale(pygame.image.load("images/frame_" + str(i) + "_delay-0.07s.png").convert_alpha(),
                               (400, 180)))
anim_count = 0
bg_x1 = 0
bg_x2 = 800
bg_vel = 2
bg_count = 0
bg_x1_change = 0
bg_x2_change = 0
dis = 1

checkpoint_x = 580
reached_checkpoint = False

lobby_img = pygame.image.load("images/lobby_bg.png").convert_alpha()
guide_img = pygame.transform.scale(pygame.image.load("images/guide.png").convert_alpha(), (300, 300))
bg_img = pygame.image.load("images/cpr_bg.png").convert_alpha()
citations_img = pygame.transform.scale(pygame.image.load("images/citations.png"), (600, 300))
g1_img = pygame.transform.scale(pygame.image.load("images/g1.png").convert_alpha(), (300, 190))
g2_img = pygame.transform.scale(pygame.image.load("images/g2.png").convert_alpha(), (300, 190))
g3_img = pygame.transform.scale(pygame.image.load("images/g3.png").convert_alpha(), (300, 190))
g4_img = pygame.transform.scale(pygame.image.load("images/g4.png").convert_alpha(), (300, 190))
g5_img = pygame.transform.scale(pygame.image.load("images/g5.png").convert_alpha(), (300, 190))
g6_img = pygame.transform.scale(pygame.image.load("images/g6.png").convert_alpha(), (300, 190))
g7_1_img = pygame.transform.scale(pygame.image.load("images/g7_1.png").convert_alpha(), (300, 190))
g7_2_img = pygame.transform.scale(pygame.image.load("images/g7_2.png").convert_alpha(), (300, 190))

pygame.mixer.music.load("images/cpr_bgsound.mp3")
pygame.mixer.music.play(-1)

text_font = pygame.font.Font("freesansbold.ttf", 25)
title_font = pygame.font.Font("freesansbold.ttf", 38)
info_font = pygame.font.Font("freesansbold.ttf", 18)
guide_message = [["Hello, my name is Soham, I will be your guide for today.",
                  "Welcome to the CPR Game",
                  "Use your Right Arrow Key to navigate the train to checkpoints",
                  "I will share my historical knowledge about the CPR at each checkpoint",
                  "Big Question: Did the Construction of CPR outweigh the harms?",
                  "Think about the big question and enjoy the game :)"],
                 ["Congratulations on reaching the first checkpoint",
                  "Purpose of Construction",
                  "CPR would reassure British Columbia upon joining Confederation of 1867,",
                  "CPR would also help keep the nation together,",
                  "Not to mention the profits which would be gained from transport, trade, and more.",
                  ""],
                 ["Great Job, you have reached Checkpoint 2",
                  "Expansion and Development",
                  "In 1883, CPR started developing their own steamed locomotives and ships,",
                  "In 1889, CPR increased their trackage by 17.6km to compete with other railways,",
                  "and in 1889, diverse businesses like Japanese tea stalls opened to serve customers.",
                  ""],
                 ["Incredible, you have reached Checkpoint 3.",
                  "Tourism and Immigration",
                  "CPR advertised the Banff Springs Hotel in 1881 which attracted many tourists.",
                  "Since then, many tourists come to enjoy the recreational activities and resorts.",
                  "CPR attracted immigrants by showing them “ready made farms” and prairies.",
                  ""],
                 ["Congrats, you reached Checkpoint 4.",
                  "War Efforts",
                  "During WWI, CPR gave resources to British Empire: trains, ships, telegraphs, etc.",
                  "11 340 employees enlisted in the army and unfortunately many died.",
                  "CPR took the same initiatives in WWII as well.",
                  ""],
                 ["Mad skills, you reached Checkpoint 5.",
                  "Impacts on First Nations",
                  "In 1870, the government took some of first nations’ land to build the railway,",
                  "There were 7 treaties made assuring first nations resources such as:",
                  "land, cash, hunting and fishing tools, farming supplies, and more.",
                  "However some of these promises have not yet been fulfilled ..."],
                 ["You reached Checkpoint 6, keep it up.",
                  "Who was involved in the construction of CPR",
                  "Cheap labour workers from China helped develop the railway.",
                  "Chinese workers developed the railway in harsh conditions and many died.",
                  "They only received $2 a day, which was nothing compared to their expenses.",
                  "Due to the racism and Chinese Immigration Act, many chinese workers left Canada."],
                 ["Congratulations, you reached the last Checkpoint",
                  "Past to Present links",
                  "Differences: technology in CPR trains are more advanced and efficient now.",
                  "Also, CPR is much more safer due to modern engineers upgrading the tracks.",
                  "Similarities:",
                  "The purpose of CPR still remains the same: Transport and Trade."],
                 ["Thank you for playing the game",
                  "Did the Construction of CPR outweigh the harms?",
                  "", "", "", ""],
                 ]
lobby_clicks = []
guide_intro_clicks = []
guide1_clicks = []
guide2_clicks = []
guide3_clicks = []
guide4_clicks = []
guide5_clicks = []
guide6_clicks = []
guide7_clicks = []
guide8_clicks = []


def button(text, btn_color, txt_color, x, y):
    pygame.draw.rect(win, btn_color, (x, y, 100, 30))
    button_text = text_font.render(str(text), True, txt_color)
    win.blit(button_text, (x + 15, y + 5))
    mouse_pos = pygame.mouse.get_pos()
    mouse_press = pygame.mouse.get_pressed()
    if x <= mouse_pos[0] <= x + 100 and y <= mouse_pos[1] <= y + 30 and mouse_press[0] == 1:
        return True


def guide(message, message1, message2, message3, message4, message5):
    win.fill((0, 0, 0))
    win.blit(guide_img, (20, 20))
    guide_text = info_font.render(str(message), True, (255, 255, 255))
    guide_text1 = info_font.render(str(message1), True, (255, 255, 255))
    guide_text2 = info_font.render(str(message2), True, (255, 165, 0))
    guide_text3 = info_font.render(str(message3), True, (255, 165, 0))
    guide_text4 = info_font.render(str(message4), True, (255, 165, 0))
    guide_text5 = info_font.render(str(message5), True, (255, 165, 0))
    win.blit(guide_text, (300, 120))
    win.blit(guide_text1, (300, 170))
    win.blit(guide_text2, (25, 300))
    win.blit(guide_text3, (25, 340))
    win.blit(guide_text4, (25, 380))
    win.blit(guide_text5, (25, 420))


def guide_intro():
    guide(guide_message[0][0], guide_message[0][1], guide_message[0][2], guide_message[0][3],
          guide_message[0][4], guide_message[0][5])
    btn_guide = button("NEXT", (255, 0, 0), (255, 255, 255), 650, 500)
    if btn_guide:
        guide_intro_clicks.append(btn_guide)


def guide1():
    guide(guide_message[1][0], guide_message[1][1], guide_message[1][2], guide_message[1][3],
          guide_message[1][4], guide_message[1][5])
    win.blit(g1_img, (100, 410))
    btn_guide = button("NEXT", (255, 0, 0), (255, 255, 255), 650, 500)
    if btn_guide:
        guide1_clicks.append(btn_guide)


def guide2():
    guide(guide_message[2][0], guide_message[2][1], guide_message[2][2], guide_message[2][3],
          guide_message[2][4], guide_message[2][5])
    win.blit(g2_img, (100, 410))
    btn_guide = button("NEXT", (255, 0, 0), (255, 255, 255), 650, 500)
    if btn_guide:
        guide2_clicks.append(btn_guide)


def guide3():
    guide(guide_message[3][0], guide_message[3][1], guide_message[3][2], guide_message[3][3],
          guide_message[3][4], guide_message[3][5])
    win.blit(g3_img, (100, 410))
    btn_guide = button("NEXT", (255, 0, 0), (255, 255, 255), 650, 500)
    if btn_guide:
        guide3_clicks.append(btn_guide)


def guide4():
    guide(guide_message[4][0], guide_message[4][1], guide_message[4][2], guide_message[4][3],
          guide_message[4][4], guide_message[4][5])
    win.blit(g4_img, (100, 410))
    btn_guide = button("NEXT", (255, 0, 0), (255, 255, 255), 650, 500)
    if btn_guide:
        guide4_clicks.append(btn_guide)


def guide5():
    guide(guide_message[5][0], guide_message[5][1], guide_message[5][2], guide_message[5][3],
          guide_message[5][4], guide_message[5][5])
    win.blit(g5_img, (100, 440))
    btn_guide = button("NEXT", (255, 0, 0), (255, 255, 255), 650, 500)
    if btn_guide:
        guide5_clicks.append(btn_guide)


def guide6():
    guide(guide_message[6][0], guide_message[6][1], guide_message[6][2], guide_message[6][3],
          guide_message[6][4], guide_message[6][5])
    win.blit(g6_img, (100, 440))
    btn_guide = button("NEXT", (255, 0, 0), (255, 255, 255), 650, 500)
    if btn_guide:
        guide6_clicks.append(btn_guide)


def guide7():
    guide(guide_message[7][0], guide_message[7][1], guide_message[7][2], guide_message[7][3],
          guide_message[7][4], guide_message[7][5])
    win.blit(g7_1_img, (70, 440))
    win.blit(g7_2_img, (390, 440))
    btn_guide = button("NEXT", (255, 0, 0), (255, 255, 255), 650, 500)
    if btn_guide:
        guide7_clicks.append(btn_guide)


def guide8():
    guide(guide_message[8][0], guide_message[8][1], guide_message[8][2], guide_message[8][3],
          guide_message[8][4], guide_message[8][5])
    win.blit(citations_img, (70, 280))
    btn_guide = button("EXIT", (255, 0, 0), (255, 255, 255), 650, 500)
    if btn_guide:
        guide8_clicks.append(btn_guide)


def lobby():
    win.blit(lobby_img, (0, 0))
    title_text = title_font.render("Building of the Canadian Pacific Railway", True, (255, 255, 255))
    question_text = text_font.render("Did the Construction of the CPR Outweigh the harms?", True, (255, 255, 255))
    win.blit(title_text, (10, 150))
    win.blit(question_text, (10, 200))
    btn = button("PLAY", (255, 0, 0), (255, 255, 255), 400, 300)
    if btn:
        lobby_clicks.append(btn)


def show_score():
    score_text = text_font.render("Score: " + str(bg_count * 10), True, (255, 255, 255))
    win.blit(score_text, (20, 20))
    dist_text = text_font.render("Next Checkpoint: " + str(2 - (bg_count % dis)) + " km -->", True, (255, 255, 255))
    win.blit(dist_text, (20, 60))
    check_text = text_font.render("Checkpoint: " + str(checkpoint) + " /7", True, (255, 255, 255))
    win.blit(check_text, (20, 100))


def draw_bg():
    win.blit(bg_img, (bg_x1, 0))
    win.blit(bg_img, (bg_x2, 0))
    show_score()


def draw_train():
    win.blit(train_imgs[(anim_count - 1) // 10], (50, 320))


def move_train():
    global bg_x1, bg_x2, bg_vel, anim_count, bg_x1_change, bg_x2_change, train_change, bg_count, checkpoint
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                train_change = 1
                bg_x1_change = -bg_vel
                bg_x2_change = -bg_vel
        if event.type == pygame.KEYUP:
            train_change = 0
            bg_x1_change = 0
            bg_x2_change = 0
    if anim_count >= len(train_imgs):
        anim_count = 0
    if bg_x1 + WIDTH < 0:
        bg_x1 = bg_x2 + WIDTH
        bg_count += 1
        checkpoint += 1
    if bg_x2 + WIDTH < 0:
        bg_x2 = bg_x1 + WIDTH
        bg_count += 1
        checkpoint += 1
    bg_x1 += bg_x1_change
    bg_x2 += bg_x2_change
    anim_count += train_change


def position1_checkpoint():
    global checkpoint_x, bg_count
    if bg_count == dis:
        guide1()


def position2_checkpoint():
    global checkpoint_x, bg_count
    if bg_count == 2 * dis:
        guide2()


def position3_checkpoint():
    global checkpoint_x, bg_count
    if bg_count == 3 * dis:
        guide3()


def position4_checkpoint():
    if bg_count == 4 * dis:
        guide4()


def position5_checkpoint():
    global checkpoint_x, bg_count
    if bg_count == 5 * dis:
        guide5()


def position6_checkpoint():
    global checkpoint_x, bg_count
    if bg_count == 6 * dis:
        guide6()


def position7_checkpoint():
    global checkpoint_x, bg_count
    if bg_count == 7 * dis:
        guide7()


def play():
    draw_bg()
    draw_train()
    move_train()


def game():
    play()
    position1_checkpoint()


def game1():
    global bg_img
    bg_img = pygame.transform.scale(pygame.image.load("images/cpr_bg1.png").convert_alpha(), (WIDTH, HEIGHT))
    play()
    position2_checkpoint()


def game2():
    global bg_img
    bg_img = pygame.transform.scale(pygame.image.load("images/cpr_bg2.png").convert_alpha(), (WIDTH, HEIGHT))
    play()
    position3_checkpoint()


def game3():
    global bg_img
    bg_img = pygame.transform.scale(pygame.image.load("images/cpr_bg.png"), (WIDTH, HEIGHT))
    play()
    position4_checkpoint()


def game4():
    global bg_img
    bg_img = pygame.transform.scale(pygame.image.load("images/cpr_bg1.png"), (WIDTH, HEIGHT))
    play()
    position5_checkpoint()


def game5():
    global bg_img
    bg_img = pygame.transform.scale(pygame.image.load("images/cpr_bg2.png"), (WIDTH, HEIGHT))
    play()
    position6_checkpoint()


def game6():
    global bg_img
    bg_img = pygame.transform.scale(pygame.image.load("images/cpr_bg1.png"), (WIDTH, HEIGHT))
    play()
    position7_checkpoint()


def game7():
    guide8()


def main():
    lobby()
    if True in lobby_clicks:
        guide_intro()
    if True in guide_intro_clicks:
        game()
    if True in guide1_clicks:
        game1()
    if True in guide2_clicks:
        game2()
    if True in guide3_clicks:
        game3()
    if True in guide4_clicks:
        game4()
    if True in guide5_clicks:
        game5()
    if True in guide6_clicks:
        game6()
    if True in guide7_clicks:
        game7()


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    main()
    pygame.display.update()
pygame.quit()
quit()
