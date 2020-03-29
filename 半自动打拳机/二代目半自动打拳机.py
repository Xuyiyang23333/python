#半自动打拳机

import os
import pygame
import sys

print('by：吴帷,徐艺扬,以及某位40岁大叔')
print('pygame相关的代码我是抄的，源代码在https://bbs.nga.cn/read.php?tid=19561185&page=e&rand=508能看到。')

print('图中女性居多吗？')
print('a=女多于男或全为女性')
print('b=男多于女或全为男性')
选择1 = input('请输入：')
if 选择1 == 'a' :
    输出结果1 = '可怕，在这种情况都要女性来担当重任，男人们都死绝了？父系社会的本质就是在压榨和剥削女性。'
if 选择1 == 'b' :
    输出结果1 = '明明女性也同样在工作，为何只彰显男人的功绩、对女性的付出避而不谈？媒体使用春秋笔法，居心叵测。'

print('图中的女性好看吗？')
print('a=好看')
print('b=谈不上好看')
选择2 = input('请输入：')
if 选择2 == 'a' :
    输出结果2 = '物化女性的行径简直令人发指，女性不是男性的泄欲工具，而是独立的人。请不要用你们的眼神强奸别人。'
if 选择2 == 'b' :
    输出结果2 = '难道所有的女性都像图中那样不堪？用以偏概全的方式故意丑化女性，我只能感受到对女性的迫害和侮辱。'

print('是歌颂女性的吗？')
print('a=是')
print('b=不是')
选择3 = input('请输入：')
if 选择3 == 'a' :
    输出结果3 = '呵呵，中国女人承担了分内分外的所有事情，稍微歌功颂德就能打发了？目的还是为了更好的培养女人的奴性、让她们心甘情愿付出。'
if 选择3 == 'b' :
    输出结果3 = '中国女性明明承担了那么多，在这里连一点体现都没有？是我们不配吗？'

text = str(输出结果1+输出结果2+输出结果3+'地狱空荡荡，恶魔在人间。中国女性何时才能站起来？')



textList = []


class Message:
    size = 28

    def __init__(self, text):
        self.text = text
        self.size = Message.size
        self.color = (255, 255, 255)
        self.bg = None
        self.font = pygame.font.SysFont('wqyzenhei', self.size)
        self.surface = self.font.render(self.text, True, self.color, self.bg)
        self.rect = self.surface.get_rect()

    def show_me(self, screen):
        screen.blit(self.surface, self.rect)


def check_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def cut_text(text):
    global lineSpacing  # 行距
    lineSpacing = Message.size * 0.6
    for i in range(0, len(text) + 1):
        m = Message(text[0:i])
        if m.rect.width > 780:
            textList.append(text[0:i - 1])
            # if (Message.size + lineSpacing) * len(textList) > 580: textList.remove(textList[0])
            # 上边一行主要解决超过窗口高度
            text = text[i - 1:len(text)]
            cut_text(text)
            break
        if i == len(text) and m.rect.width <= 780:
            textList.append(text[0:i])
            # if (Message.size + lineSpacing) * len(textList) > 580: textList.remove(textList[0])
            print(m.rect.height, m.size)


def messageShow(screen):
    for i in range(0, len(textList)):
        m = Message(textList[i])
        m.rect.left = 10
        m.rect.top = 10 + i * (Message.size + lineSpacing)
        m.show_me(screen)


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    cut_text(text)

    while True:
        screen.fill((0, 0, 0))
        messageShow(screen)
        check_event()
        pygame.display.flip()
        pygame.time.Clock().tick(60)


run_game()

'''
from pygame. locals import*
pygame.init()
font = pygame.font.SysFont('wqyzenhei',64)
ftext = font.render(text, True, (65, 83, 130), (255, 255, 255))
pygame.image.save(ftext,"/home/david/打拳.jpg")
'''

'''
#coding: UTF-8
#载入必要的模块
import os
import pygame

from pygame. locals import*
#pygame初始化
pygame.init()
text = u"PythonTab中文网"
#设置字体和字号
font = pygame.font.SysFont('wqyzenhei',64)
#渲染图片,设置背景颜色和字体样式前面的颜色是字体颜色
ftext = font.render(text, True, (65, 83, 130), (255, 255, 255))
#保存图片
pygame.image.save(ftext,"~/结果.jpg")
#图片保存地址
'''

'''
print('')
print('a=')
print('b=')
选择* = input('请输入：')
if 选择* == a :
    输出结果* = ''
if 选择* == b :
    输出结果2* = ''
'''
