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

#pengiun 대화 상태창
def pengiun_dialog(input_screen, font_color, input_line):
    dialog = pygame.image.load("E:/PyGame/Game/images/UIs/Dialog.png")
    input_screen.blit(dialog, (0, 0))

    if input_line == 1:
        pixel_font(input_screen, "???", font_color, 295, 490, 30)
        pixel_font(input_screen, "동물 친구와 멀어져서 대화를 종료하거나 SPACE를 누르면 말을", font_color, 200, 550, 30)
        pixel_font(input_screen, " 걸 수 있습니다.", font_color, 200, 580, 30) 
    elif input_line == 2:
        pixel_font(input_screen, "팽돌이", font_color, 280, 490, 30)
        pixel_font(input_screen, "후에에에엥ㅠㅠㅠㅠ", font_color, 200, 550, 30)
    elif input_line == 3:
        pixel_font(input_screen, "팽돌이", font_color, 280, 490, 30)
        pixel_font(input_screen, "아저씨 저 좀 도와주세요ㅠㅠㅠㅠ", font_color, 200, 550, 30)
    elif input_line == 4:
        pixel_font(input_screen, "팽돌이", font_color, 280, 490, 30)
        pixel_font(input_screen, "제 장난감 좀 찾아주세요ㅠㅠㅠ", font_color, 200, 550, 30)
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
        pixel_font(input_screen, "팽돌이", font_color, 280, 490, 30)
        pixel_font(input_screen, "ㅠㅠ 다시 오셨네요...ㅠㅠ", font_color, 200, 550, 30)
    elif input_line == 3:
        pixel_font(input_screen, "팽돌이", font_color, 280, 490, 30)
        pixel_font(input_screen, "아직도 못 찾았어요....ㅠㅠ", font_color, 200, 550, 30)
    elif input_line == 4:
        pixel_font(input_screen, "팽돌이", font_color, 280, 490, 30)
        pixel_font(input_screen, "뭐 말 하고 싶은거 있으신가요....?", font_color, 200, 550, 30)
    elif input_line == 5:
        pixel_font(input_screen, "나", font_color, 295, 490, 30)
        pixel_font(input_screen, "이 인형은 어때...?", font_color, 200, 550, 30)
    elif input_line == 6:
        pixel_font(input_screen, "팽돌이", font_color, 280, 490, 30)
        pixel_font(input_screen, "하지만 이건 제게 아닌걸요...", font_color, 200, 550, 30)
    elif input_line == 7:
        pixel_font(input_screen, "나", font_color, 295, 490, 30)
        pixel_font(input_screen, "그냥 떨어졌던 인형이긴 해...", font_color, 200, 550, 30)
    elif input_line == 8:
        pixel_font(input_screen, "팽돌이", font_color, 280, 490, 30)
        pixel_font(input_screen, "네? 설마 빨간 집 앞에 떨어져 있었나요?", font_color, 200, 550, 30)
    elif input_line == 9:
        pixel_font(input_screen, "나", font_color, 295, 490, 30)
        pixel_font(input_screen, "어?! 그랬던 것 같은데...", font_color, 200, 550, 30)
    elif input_line == 10:
        pixel_font(input_screen, "팽돌이", font_color, 280, 490, 30)
        pixel_font(input_screen, "오! 그럼 이거 제 거 맞는 것 같아요..!!", font_color, 200, 550, 30)
    elif input_line == 11:
        pixel_font(input_screen, "팽돌이", font_color, 280, 490, 30)
        pixel_font(input_screen, "정말 감사합니다...!!", font_color, 200, 550, 30)
    elif input_line == 12:
        pixel_font(input_screen, "???", font_color, 295, 490, 30)
        pixel_font(input_screen, "당신은 웃는 팽돌이의 모습을 보며 기분이 좋아졌습니다.", font_color, 200, 550, 30)
    elif input_line == 13:
        pixel_font(input_screen, "팽돌이", font_color, 280, 490, 30)
        pixel_font(input_screen, "아저씨 감사합니다~!!", font_color, 200, 550, 30)

def duck_doll_dialog(input_screen, font_color, input_line):
    dialog = pygame.image.load("E:/PyGame/Game/images/UIs/Dialog.png")
    input_screen.blit(dialog, (0, 0))

    if input_line == 1:
        pixel_font(input_screen, "???", font_color, 295, 490, 30)
        pixel_font(input_screen, "인형이 있네요... 누구의 인형일까요?", font_color, 200, 550, 30) 
        pixel_font(input_screen, "인형을 주으려면 E를 눌러주세요.", font_color, 200, 600, 30)          
#pengiun 대화 상태창 끝

#bear_grandfa 대화 상태창
def bear_grandfa_dialog(input_screen, font_color, input_line):
    dialog = pygame.image.load("E:/PyGame/Game/images/UIs/Dialog.png")
    input_screen.blit(dialog, (0, 0))

    if input_line == 1:
        pixel_font(input_screen, "???", font_color, 295, 490, 30)
        pixel_font(input_screen, "동물 친구와 멀어져서 대화를 종료하거나 SPACE를 누르면 말을", font_color, 200, 550, 30)
        pixel_font(input_screen, " 걸 수 있습니다.", font_color, 200, 580, 30) 
    elif input_line == 2:
        pixel_font(input_screen, "곰 할배", font_color, 280, 490, 30)
        pixel_font(input_screen, "아이고... 힘들구만 나도 이제 나이를 먹었다 이건가...?", font_color, 200, 550, 30)
        pixel_font(input_screen, "내가 10년만 더 젊었으면 이 정도는 충분히 들고 갈텐데...", font_color, 200, 600, 30)
        pixel_font(input_screen, "어이구... 누가 나 좀 도와줬으면 좋겠구만...(눈치)", font_color, 200, 650, 30)
    elif input_line == 3:
        pixel_font(input_screen, "나", font_color, 295, 490, 30)
        pixel_font(input_screen, "하..할아버지... 제가 좀 도와드릴까요..?", font_color, 200, 550, 30)
    elif input_line == 4:
        pixel_font(input_screen, "곰 할배", font_color, 280, 490, 30)
        pixel_font(input_screen, "아이고~! 우리 동네에 이렇게 건장한 청년이 있었나~? 자네", font_color, 200, 550, 30)
        pixel_font(input_screen, "힘 좀 쓰겠구만~!! 여기 와서 이 상자 좀 내 집에 옮겨줄 수", font_color, 200, 600, 30)
        pixel_font(input_screen, "있겠나? 우리집은 그냥 빨간집이야~ 그럼 나 먼저 가겠네 ^^", font_color, 200, 650, 30)
    elif input_line == 5:
        pixel_font(input_screen, "???", font_color, 295, 490, 30)
        pixel_font(input_screen, "곰 할아버지를 도와 할아버지의 집까지 상자를 옮겨주세요.", font_color, 200, 550, 30)

def bear_grandfa_dialog_clear(input_screen, font_color, input_line):
    dialog = pygame.image.load("E:/PyGame/Game/images/UIs/Dialog.png")
    input_screen.blit(dialog, (0, 0))

    if input_line == 1:
        pixel_font(input_screen, "???", font_color, 295, 490, 30)
        pixel_font(input_screen, "동물 친구와 멀어져서 대화를 종료하거나 SPACE를 누르면 말을", font_color, 200, 550, 30)
        pixel_font(input_screen, " 걸 수 있습니다.", font_color, 200, 580, 30) 
    elif input_line == 2:
        pixel_font(input_screen, "곰 할배", font_color, 280, 490, 30)
        pixel_font(input_screen, "아이고 자네 왔구만~ 내가 여기서 얼마나 기다린 줄 아는가?", font_color, 200, 550, 30)
        pixel_font(input_screen, "내가 이렇게 나이가 들었지만 왕년에 이 마을에서 최고에 ", font_color, 200, 600, 30)
        pixel_font(input_screen, "달리기 선수였다고~~ 아 물론 1등은 다른 놈이었지만...", font_color, 200, 650, 30)
    elif input_line == 3:
        pixel_font(input_screen, "곰 할배", font_color, 280, 490, 30)
        pixel_font(input_screen, "그래도 나 정도면 어디서 알아주는 달리기 선수였지 크~", font_color, 200, 550, 30)
        pixel_font(input_screen, "추억이구만 그래... 나도 한 때는 자네 같은 몸을 같고", font_color, 200, 600, 30)
        pixel_font(input_screen, "있었지 하지만 나이가 들면서 근육이 빠지더라고 허허...", font_color, 200, 650, 30)
    elif input_line == 4:
        pixel_font(input_screen, "곰 할배", font_color, 280, 490, 30)
        pixel_font(input_screen, "그래서 요즘 다시 근육 운동을 하고 있다네~ 그치만 옛날 힘은", font_color, 200, 550, 30)
        pixel_font(input_screen, "안 나더라고... 만약 신이 나의 소원을 들어주신다면 난", font_color, 200, 600, 30)
        pixel_font(input_screen, "젊음을 달라고 할 것 같네... 물론 과거의 나를 그리워하는", font_color, 200, 650, 30)
    elif input_line == 5:
        pixel_font(input_screen, "나", font_color, 295, 490, 30)
        pixel_font(input_screen, "할아버지...", font_color, 200, 550, 30)
    elif input_line == 6:
        pixel_font(input_screen, "곰 할배", font_color, 280, 490, 30)
        pixel_font(input_screen, "뭐야 갑자기 왜 말을 끊고 그래.", font_color, 200, 550, 30)
    elif input_line == 7:
        pixel_font(input_screen, "나", font_color, 295, 490, 30)
        pixel_font(input_screen, "이것만 내려놓고 들으면 안 될까요...? 너무 무거워요...", font_color, 200, 550, 30)
        pixel_font(input_screen, "(뭐가 들어있는지 상당히 무겁다...)", font_color, 200, 600, 30)
    elif input_line == 8:
        pixel_font(input_screen, "곰 할배", font_color, 280, 490, 30)
        pixel_font(input_screen, "아 그래! 그거 그냥 문 앞에 놔 어차피 여기서부터는 내가", font_color, 200, 550, 30)
        pixel_font(input_screen, "들면 되거든~", font_color, 200, 600, 30)
    elif input_line == 9:
        pixel_font(input_screen, "나", font_color, 295, 490, 30)
        pixel_font(input_screen, "넵...", font_color, 200, 550, 30)
    elif input_line == 10:
        pixel_font(input_screen, "곰 할배", font_color, 280, 490, 30)
        pixel_font(input_screen, "그래서 어디까지 말을 했더라...? 아 맞아! 내가 그래서 젊음을", font_color, 200, 550, 30)
        pixel_font(input_screen, "얻고 싶어... 하지만 난 지금의 나도 많이 좋다네 젊은이~~!", font_color, 200, 600, 30)
        pixel_font(input_screen, "아 그리고 내가 LA에 있을 때......$!#$!#$!%#@$#%@#$@#$@%@", font_color, 200, 650, 30)
    elif input_line == 11:
        pixel_font(input_screen, "나", font_color, 295, 490, 30)
        pixel_font(input_screen, "(할아버지가 말이 너무 많으시다...)", font_color, 200, 550, 30)
    elif input_line == 12:
        pixel_font(input_screen, "???", font_color, 295, 490, 30)
        pixel_font(input_screen, "당신은 신나서 말하시는 할아버지의 모습을 보고 이야기를 끝", font_color, 200, 550, 30)
        pixel_font(input_screen, "까지 듣고 있습니다...", font_color, 200, 580, 30)
    elif input_line == 13:
        pixel_font(input_screen, "곰 할배", font_color, 280, 490, 30)
        pixel_font(input_screen, "아이고~ 내 이야기 들어줘서 고맙고~^^ 오랜만에 재밌었구만", font_color, 200, 550, 30)
        pixel_font(input_screen, "도와줘서 고맙구만~ 다음에 시간되면 마을 회관에서 보자고~", font_color, 200, 600, 30)

def box_dialog(input_screen, font_color, input_line):
    dialog = pygame.image.load("E:/PyGame/Game/images/UIs/Dialog.png")
    input_screen.blit(dialog, (0, 0))

    if input_line == 1:
        pixel_font(input_screen, "???", font_color, 295, 490, 30)
        pixel_font(input_screen, "곰 할아버지의 상자인가 봅니다.", font_color, 200, 550, 30) 
        pixel_font(input_screen, "상자를 주으려면 E를 눌러주세요.", font_color, 200, 600, 30)
#bear_grandfa 대화 상태창 끝

#연못 대화 창
def pond_dialog(input_screen, font_color, input_line):
    dialog = pygame.image.load("E:/PyGame/Game/images/UIs/Dialog.png")
    input_screen.blit(dialog, (0, 0))

    if input_line == 1:
        pixel_font(input_screen, "???", font_color, 295, 490, 30)
        pixel_font(input_screen, "연못이 깊어 보입니다...", font_color, 200, 550, 30) 
        pixel_font(input_screen, "뭔가 많아 보이지만 찾기는 힘들어 보입니다...", font_color, 200, 600, 30)

#집 대화 창
def house_dialog(input_screen, font_color, input_line):
    dialog = pygame.image.load("E:/PyGame/Game/images/UIs/Dialog.png")
    input_screen.blit(dialog, (0, 0))

    if input_line == 1:
        pixel_font(input_screen, "???", font_color, 295, 490, 30)
        pixel_font(input_screen, "누구의 집일까요?...", font_color, 200, 550, 30) 
        pixel_font(input_screen, "분명히 집주인이 있겠죠...?", font_color, 200, 600, 30)