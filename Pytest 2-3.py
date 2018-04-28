#  2-3 序列（字符串）乘法运算

# 在位于屏幕中央且宽度合适的方框内打印一个句子

sentence = input('Sentence: ')

screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
Left_margin = (screen_width - box_width)//2

print()
print(' ' * Left_margin + '+' + '-' * (box_width-2) + '+')
print(' ' * Left_margin + '|' + ' ' * (text_width+2)  + '|')
print(' ' * Left_margin + '|' + ' ' + sentence + ' '  + '|')
print(' ' * Left_margin + '|' + ' ' * (text_width + 2)  + '|')
print(' ' * Left_margin + '+' + '-' * (box_width-2) + '+')
print()

print()
print(' ' * Left_margin + '+' + '-' * (box_width-2) + '+')
print(' ' * Left_margin + '|' + ' ' * (box_width-2)  + '|')
print(' ' * Left_margin + '|' + '  ' + sentence + '  '  + '|')
print(' ' * Left_margin + '|' + ' ' * (box_width-2)  + '|')
print(' ' * Left_margin + '+' + '-' * (box_width-2) + '+')
print()