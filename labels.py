from pygame import font


def Label(window, size, text, color, x, y, f = 'freesansbold.ttf'):
    fnt = font.Font(f,size)
    l = fnt.render(text, True, color)
    lRect = l.get_rect()
    lRect.topleft = (x,y)
    window.blit(l,lRect)