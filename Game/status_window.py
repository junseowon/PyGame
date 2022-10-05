import pygame
from load_fonts import *
from button_UI import *
#hamzzizzi 대화 상태창
def hamzzizzi_dialog(input_screen, font_color, input_line):
    dialog = pygame.image.load("E:/PyGame/Game/images/UIs/Dialog.png")
    input_screen.blit(dialog, (0, 0))

    if input_line == 1:
        pixel_font(input_screen, "???", font_color, 295, 490, 30)
        pixel_font(input_screen, "동물 친구와 멀어져서 대화를 종료하거나 SPACE를 누르면 말을", font_color, 200, 550, 30)
        pixel_font(input_screen, " 걸 수 있습니다.", font_color, 200, 580, 30) 
    elif input_line == 2:
        pixel_font(input_screen, "햄찌", font_color, 295, 490, 30)
        pixel_font(input_screen, "해바라기씨를 잃어버렸어요...", font_color, 200, 550, 30)
    elif input_line == 3:
        pixel_font(input_screen, "햄찌", font_color, 295, 490, 30)
        pixel_font(input_screen, "동생 생일선물이었는데...ㅠ", font_color, 200, 550, 30)
    elif input_line == 4:
        pixel_font(input_screen, "햄찌", font_color, 295, 490, 30)
        pixel_font(input_screen, "혹시 찾아주시는 걸 도와주실 수 있나요?", font_color, 200, 550, 30)
    elif input_line == 5:
        pixel_font(input_screen, "???", font_color, 295, 490, 30)
        pixel_font(input_screen, "햄찌찌씨를 도와 잃어버린 선물을 찾아주세요.", font_color, 200, 550, 30)

def hamzzizzi_dialog_clear(input_screen, font_color, input_line):
    dialog = pygame.image.load("E:/PyGame/Game/images/UIs/Dialog.png")
    input_screen.blit(dialog, (0, 0))

    if input_line == 1:
        pixel_font(input_screen, "???", font_color, 295, 490, 30)
        pixel_font(input_screen, "동물 친구와 멀어져서 대화를 종료하거나 SPACE를 누르면 말을", font_color, 200, 550, 30)
        pixel_font(input_screen, " 걸 수 있습니다.", font_color, 200, 580, 30) 
    elif input_line == 2:
        pixel_font(input_screen, "햄찌", font_color, 295, 490, 30)
        pixel_font(input_screen, "ㅠㅠ 다시 오셨네요...ㅠㅠ", font_color, 200, 550, 30)
    elif input_line == 3:
        pixel_font(input_screen, "햄찌", font_color, 295, 490, 30)
        pixel_font(input_screen, "아직도 못 찾았어요....ㅠㅠ", font_color, 200, 550, 30)
    elif input_line == 4:
        pixel_font(input_screen, "햄찌", font_color, 295, 490, 30)
        pixel_font(input_screen, "뭐 말 하고 싶은거 있으신가요....?", font_color, 200, 550, 30)
    elif input_line == 5:
        pixel_font(input_screen, "나", font_color, 295, 490, 30)
        pixel_font(input_screen, "여기....", font_color, 200, 550, 30)
    elif input_line == 6:
        pixel_font(input_screen, "햄찌", font_color, 295, 490, 30)
        pixel_font(input_screen, "와! 이거 제가 잃어버렸던 씨앗 맞아요!", font_color, 200, 550, 30)
    elif input_line == 7:
        pixel_font(input_screen, "햄찌", font_color, 295, 490, 30)
        pixel_font(input_screen, "정말 감사합니다!!!", font_color, 200, 550, 30)
    elif input_line == 8:
        pixel_font(input_screen, "햄찌", font_color, 295, 490, 30)
        pixel_font(input_screen, "아 혹시 이름이 뭐에요?", font_color, 200, 550, 30)
    elif input_line == 9:
        pixel_font(input_screen, "나", font_color, 295, 490, 30)
        pixel_font(input_screen, "박진철...", font_color, 200, 550, 30)
    elif input_line == 10:
        pixel_font(input_screen, "햄찌", font_color, 295, 490, 30)
        pixel_font(input_screen, "진철님 정말 감사합니다!!!", font_color, 200, 550, 30)
    elif input_line == 11:
        pixel_font(input_screen, "햄찌", font_color, 295, 490, 30)
        pixel_font(input_screen, "덕분에 동생 선물을 줄 수 있을 것 같아요!!", font_color, 200, 550, 30)
    elif input_line == 12:
        pixel_font(input_screen, "???", font_color, 295, 490, 30)
        pixel_font(input_screen, "당신은 행복한 모습으로 가는 햄찌찌씨의 모습을 보며 약간의", font_color, 200, 550, 30)
        pixel_font(input_screen, "따스함을 느꼈습니다...", font_color, 200, 580, 30)
    elif input_line == 13:
        pixel_font(input_screen, "햄찌", font_color, 295, 490, 30)
        pixel_font(input_screen, "찾아주셔서 감사합니다!! 그럼 저는 선물을 주러갈게요!!~~", font_color, 200, 550, 30)

def seed_dialog(input_screen, font_color, input_line):
    dialog = pygame.image.load("E:/PyGame/Game/images/UIs/Dialog.png")
    input_screen.blit(dialog, (0, 0))

    if input_line == 1:
        pixel_font(input_screen, "???", font_color, 295, 490, 30)
        pixel_font(input_screen, "씨앗이 떨어져 있습니다. 이 씨앗의 주인은 누굴까요?", font_color, 200, 550, 30) 
        pixel_font(input_screen, "씨앗을 주으려면 E를 눌러주세요.", font_color, 200, 600, 30)
#hamzzizzi 대화 상태창 끝

def pengiun_dialog(input_screen, font_color, input_line):
    dialog = pygame.image.load("E:/PyGame/Game/images/UIs/Dialog.png")
    input_screen.blit(dialog, (0, 0))

    if input_line == 1:
        pixel_font(input_screen, "???", font_color, 295, 490, 30)
        pixel_font(input_screen, "동물 친구와 멀어져서 대화를 종료하거나 SPACE를 누르면 말을", font_color, 200, 550, 30)
        pixel_font(input_screen, " 걸 수 있습니다.", font_color, 200, 580, 30) 
    elif input_line == 2:
        pixel_font(input_screen, "팽돌이", font_color, 295, 490, 30)
        pixel_font(input_screen, "후에에에엥ㅠㅠㅠㅠ", font_color, 200, 550, 30)
    elif input_line == 3:
        pixel_font(input_screen, "팽돌이", font_color, 295, 490, 30)
        pixel_font(input_screen, "아저씨 저 좀 도와주세요ㅠㅠㅠㅠ", font_color, 200, 550, 30)
    elif input_line == 4:
        pixel_font(input_screen, "팽돌이", font_color, 295, 490, 30)
        pixel_font(input_screen, "장난감이 연못에 빠져서 못 찾겠어요ㅠㅠㅠㅠㅠ", font_color, 200, 550, 30)
    elif input_line == 5:
        pixel_font(input_screen, "???", font_color, 295, 490, 30)
        pixel_font(input_screen, "팽돌이를 도와 팽돌이의 장난감을 찾아주세요.", font_color, 200, 550, 30)

def pengiun_dialog_clear(input_screen, font_color, input_line):

    dialog = pygame.image.load("E:/PyGame/Game/images/UIs/Dialog.png")
    input_screen.blit(dialog, (0, 0))

    if input_line == 1:
        pixel_font(input_screen, "???", font_color, 295, 490, 30)
        pixel_font(input_screen, "동물 친구와 멀어져서 대화를 종료하거나 SPACE를 누르면 말을", font_color, 200, 550, 30)
        pixel_font(input_screen, " 걸 수 있습니다.", font_color, 200, 580, 30) 
    elif input_line == 2:
        pixel_font(input_screen, "팽돌이", font_color, 295, 490, 30)
        pixel_font(input_screen, "ㅠㅠ 다시 오셨네요...ㅠㅠ", font_color, 200, 550, 30)
    elif input_line == 3:
        pixel_font(input_screen, "팽돌이", font_color, 295, 490, 30)
        pixel_font(input_screen, "아직도 못 찾았어요....ㅠㅠ", font_color, 200, 550, 30)
    elif input_line == 4:
        pixel_font(input_screen, "팽돌이", font_color, 295, 490, 30)
        pixel_font(input_screen, "뭐 말 하고 싶은거 있으신가요....?", font_color, 200, 550, 30)
    elif input_line == 5:
        pixel_font(input_screen, "???", font_color, 295, 490, 30)
        pixel_font(input_screen, "주운 인형을 줄까요?", font_color, 200, 550, 30)

    ok_button = pygame.image.load("images/UIs/ok_select_button.png")
    ok_button_act = pygame.image.load("images/UIs/ok_select_button_act.png")
    Button(input_screen, ok_button, 512, 550, 128, 128, ok_button_act, 512, 550, pengiun_dialog_clear_choice1(input_screen, font_color, input_line))

    cancel_button = pygame.image.load("images/UIs/cancel_select_button.png")
    cancel_button_act = pygame.image.load("images/UIs/cancel_select_button_act.png")
    Button(input_screen, cancel_button, 712, 550, 128, 128, cancel_button_act, 712, 550, pengiun_dialog_clear_choice2(input_screen, font_color, input_line))

def pengiun_dialog_clear_choice1(input_screen, font_color, input_line):
    dialog = pygame.image.load("E:/PyGame/Game/images/UIs/Dialog.png")
    input_screen.blit(dialog, (0, 0))

    if input_line == 6:
        pixel_font(input_screen, "팽돌이", font_color, 295, 490, 30)
        pixel_font(input_screen, "하지만 이건 제게 아닌걸요...", font_color, 200, 550, 30)
    elif input_line == 7:
        pixel_font(input_screen, "나", font_color, 295, 490, 30)
        pixel_font(input_screen, "넌..정말..착한....아..아이구나...!", font_color, 200, 550, 30)
    elif input_line == 8:
        pixel_font(input_screen, "나", font_color, 295, 490, 30)
        pixel_font(input_screen, "이.. 이거... 그냥 너 줄게 가져...!", font_color, 200, 550, 30)
    elif input_line == 9:
        pixel_font(input_screen, "팽돌이", font_color, 295, 490, 30)
        pixel_font(input_screen, "정말 저 주시는건가요..?", font_color, 200, 550, 30)
    elif input_line == 10:
        pixel_font(input_screen, "나", font_color, 295, 490, 30)
        pixel_font(input_screen, "물론이지..!!", font_color, 200, 550, 30)
    elif input_line == 11:
        pixel_font(input_screen, "팽돌이", font_color, 295, 490, 30)
        pixel_font(input_screen, "제건 아니지만 정말 감사합니다...!!", font_color, 200, 550, 30)
    elif input_line == 12:
        pixel_font(input_screen, "???", font_color, 295, 490, 30)
        pixel_font(input_screen, "당신은 행복한 모습으로 가는 팽돌이의 모습을 보며 약간의", font_color, 200, 550, 30)
        pixel_font(input_screen, "따스함을 느꼈습니다...", font_color, 200, 580, 30)
    elif input_line == 13:
        pixel_font(input_screen, "팽돌이", font_color, 295, 490, 30)
        pixel_font(input_screen, "아저씨 감사합니다~!!", font_color, 200, 550, 30)

def pengiun_dialog_clear_choice2(input_screen, font_color, input_line):
    if input_line == 6:
        pixel_font(input_screen, "팽돌이", font_color, 295, 490, 30)
        pixel_font(input_screen, "아쉽네요....ㅠ", font_color, 200, 550, 30)
    elif input_line == 7:
        pixel_font(input_screen, "나", font_color, 295, 490, 30)
        pixel_font(input_screen, "미안하구나...", font_color, 200, 550, 30)
    elif input_line == 8:
        pixel_font(input_screen, "나", font_color, 295, 490, 30)
        pixel_font(input_screen, "나도 노력은 해봤어...", font_color, 200, 550, 30)
    elif input_line == 9:
        pixel_font(input_screen, "팽돌이", font_color, 295, 490, 30)
        pixel_font(input_screen, "도와주시려고 하셔서 감사합니다....ㅠㅠ", font_color, 200, 550, 30)
    elif input_line == 10:
        pixel_font(input_screen, "나", font_color, 295, 490, 30)
        pixel_font(input_screen, "...", font_color, 200, 550, 30)
    elif input_line == 11:
        pixel_font(input_screen, "팽돌이", font_color, 295, 490, 30)
        pixel_font(input_screen, "그냥 집에 돌아가면서 찾아볼게요...ㅠㅠㅠ", font_color, 200, 550, 30)
    elif input_line == 12:
        pixel_font(input_screen, "???", font_color, 295, 490, 30)
        pixel_font(input_screen, "당신은 슬픈 모습으로 가는 팽돌이의 모습을 보며 약간의", font_color, 200, 550, 30)
        pixel_font(input_screen, "미안함을 느꼈습니다...", font_color, 200, 580, 30)
    elif input_line == 13:
        pixel_font(input_screen, "팽돌이", font_color, 295, 490, 30)
        pixel_font(input_screen, "저 먼저 가볼게요...ㅠㅠㅠ", font_color, 200, 550, 30)

def duck_doll_dialog(input_screen, font_color, input_line):
    dialog = pygame.image.load("E:/PyGame/Game/images/UIs/Dialog.png")
    input_screen.blit(dialog, (0, 0))

    if input_line == 1:
        pixel_font(input_screen, "???", font_color, 295, 490, 30)
        pixel_font(input_screen, "인형이 있네요... 누구의 인형일까요?", font_color, 200, 550, 30) 
        pixel_font(input_screen, "인형을 주으려면 E를 눌러주세요.", font_color, 200, 600, 30)          

def obstacle_dialog(input_screen, font_color, input_line):
    dialog = pygame.image.load("E:/PyGame/Game/images/UIs/Dialog.png")
    input_screen.blit(dialog, (0, 0))

    if input_line == 1:
        pixel_font(input_screen, "???", font_color, 295, 490, 30)
        pixel_font(input_screen, "연못이 깊어 보입니다...", font_color, 200, 550, 30) 
        pixel_font(input_screen, "뭔가 많아 보이지만 찾기는 힘들어 보입니다...", font_color, 200, 600, 30)