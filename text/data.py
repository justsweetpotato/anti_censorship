#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


def printN(cur, row, msg):
    col = len(msg) // row
    s = ''
    for j in range(0, col + 1):  # 列
        try:
            s += msg[cur + row * j] + ' '  # [当前行 + 总行数*list间隔], 13*0, 13*1, 13*2
        except:
            pass
    return s


def sub(msg):
    msg = re.sub('0', '０', msg)
    msg = re.sub('1', '１', msg)
    msg = re.sub('2', '２', msg)
    msg = re.sub('3', '３', msg)
    msg = re.sub('4', '４', msg)
    msg = re.sub('5', '５', msg)
    msg = re.sub('6', '６', msg)
    msg = re.sub('7', '７', msg)
    msg = re.sub('8', '８', msg)
    msg = re.sub('9', '９', msg)
    msg = re.sub(' ', '㍐', msg)  # TODO
    msg = re.sub(',', '，', msg)
    msg = re.sub('[,;]', '，', msg)  # TODO
    msg = re.sub('\.', '・', msg)
    msg = re.sub(':', '：', msg)
    msg = re.sub('!', '！', msg)
    msg = re.sub('\?', '？', msg)
    msg = re.sub('"', '〃', msg)  # TODO
    msg = re.sub('\'', '゛', msg)  # TODO
    msg = re.sub('[/|]', '／', msg)
    msg = re.sub('-', '︱', msg)
    msg = re.sub('~', '～', msg)
    msg = re.sub('[\(（]', '︵', msg)
    msg = re.sub('[\)）]', '︶', msg)
    msg = re.sub('[\[「]', '﹁', msg)
    msg = re.sub('[\]」]', '﹂', msg)
    msg = re.sub('a', 'ａ', msg)
    msg = re.sub('A', 'Ａ', msg)
    msg = re.sub('b', 'ｂ', msg)
    msg = re.sub('B', 'Ｂ', msg)
    msg = re.sub('c', 'ｃ', msg)
    msg = re.sub('C', 'Ｃ', msg)
    msg = re.sub('d', 'ｄ', msg)
    msg = re.sub('D', 'Ｄ', msg)
    msg = re.sub('e', 'ｅ', msg)
    msg = re.sub('E', 'Ｅ', msg)
    msg = re.sub('f', 'ｆ', msg)
    msg = re.sub('F', 'Ｆ', msg)
    msg = re.sub('g', 'ｇ', msg)
    msg = re.sub('G', 'Ｇ', msg)
    msg = re.sub('h', 'ｈ', msg)
    msg = re.sub('H', 'Ｈ', msg)
    msg = re.sub('i', 'ｉ', msg)
    msg = re.sub('I', 'Ｉ', msg)
    msg = re.sub('j', 'ｊ', msg)
    msg = re.sub('J', 'Ｊ', msg)
    msg = re.sub('k', 'ｋ', msg)
    msg = re.sub('K', 'Ｋ', msg)
    msg = re.sub('l', 'ｌ', msg)
    msg = re.sub('L', 'Ｌ', msg)
    msg = re.sub('m', 'ｍ', msg)
    msg = re.sub('M', 'Ｍ', msg)
    msg = re.sub('n', 'ｎ', msg)
    msg = re.sub('N', 'Ｎ', msg)
    msg = re.sub('o', 'ｏ', msg)
    msg = re.sub('O', 'Ｏ', msg)
    msg = re.sub('p', 'ｐ', msg)
    msg = re.sub('P', 'Ｐ', msg)
    msg = re.sub('q', 'ｑ', msg)
    msg = re.sub('Q', 'Ｑ', msg)
    msg = re.sub('r', 'ｒ', msg)
    msg = re.sub('R', 'Ｒ', msg)
    msg = re.sub('s', 'ｓ', msg)
    msg = re.sub('S', 'Ｓ', msg)
    msg = re.sub('t', 'ｔ', msg)
    msg = re.sub('T', 'Ｔ', msg)
    msg = re.sub('u', 'ｕ', msg)
    msg = re.sub('U', 'Ｕ', msg)
    msg = re.sub('v', 'ｖ', msg)
    msg = re.sub('V', 'Ｖ', msg)
    msg = re.sub('w', 'ｗ', msg)
    msg = re.sub('W', 'Ｗ', msg)
    msg = re.sub('x', 'ｘ', msg)
    msg = re.sub('X', 'Ｘ', msg)
    msg = re.sub('y', 'ｙ', msg)
    msg = re.sub('Y', 'Ｙ', msg)
    msg = re.sub('z', 'ｚ', msg)
    msg = re.sub('Z', 'Ｚ', msg)

    return msg


def anti_censor(row, msg):
    if not msg:
        return None

    msg = sub(msg)
    word_list = ''
    for i in range(0, row):  # 行
        word_list += printN(i, row, msg) + '<br>'
    return word_list
