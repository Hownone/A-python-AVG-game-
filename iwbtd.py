# -*- coding:gb18030 -*-

import pgzrun
from pgzero.clock import clock
from pgzero.keyboard import keyboard

from scenes import *


def draw():
    # ���ƺ���
    # װ����Ļ���
    if scene.decorations and not scene.over:
        for dec in scene.decorations:
            screen.blit(dec.decoration, (dec.x, dec.y))
    # ʵ��Ļ���
    for i in range(len(scene.objects)):
        scene.objects[i].act.draw()
    # kid�Ļ���
    if scene.kid and scene.kid.visible:
        scene.kid.act.draw()
    # ������Ļ
    if scene.blackcurtain:
        screen.blit('blackcurtain', (0,0))
    # �ı���Ļ���
    if scene.texts:
        for text in scene.texts:
            screen.draw.text(text.text,center=text.center, align=text.align, fontname=text.fontname,
                             fontsize=text.fontsize, color=text.color)



def update():
    global scene, i
    # �ظ�����bgm
    if not music.is_playing('bgm'):
        music.play('bgm')
        music.set_volume(0.7)
    # ���³���
    scene.update()
    # ������Ҫ��j�ĵȴ��¼�
    if scene.waiting_j:
        if keyboard.j:
            scene.over = True
    # �����л������¼�
    if scene.over:
        if i == len(scenes) - 1:
            exit()
        else:
            i += 1
            scene = scenes[i]
            scene.sum_death = scenes[i - 1].death + scenes[i - 1].sum_death
            scene.difficulty = scenes[i - 1].difficulty
            scene.load()
            scene.set_difficulty(scene.difficulty)
            if scene.need_press_j:
                clock.schedule_unique(scene.set_j,1)

i = 0  # �������
scene = scenes[i]  # ��ȡ����
scene.load()
pgzrun.go()  # pycharm��������Ҫ����pgzrun.go()��������
