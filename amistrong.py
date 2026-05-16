# AmIStrong?
# MIT License
# Copyright (c) 2026 Jonathan Chiu

import json
import os
from pydantic import BaseModel


DATA_DIR = 'data'

def get_external_data(path):
    """获取外部（JSON 文件）数据

    Args:
        path (str): 外部文件路径

    Returns:
        _type_: 获取的数据
    """
    with open(os.path.join(DATA_DIR, f'{path}.json'), 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

rigan_wuxing_table = get_external_data('rigan_wuxing_table')
yuezhi_wuxing_table = get_external_data('yuezhi_wuxing_table')
wuxing_interaction_table = get_external_data('wuxing_interaction_table')


def amistrong(rigan_yuezhi):
    rigan = rigan_yuezhi.get('rigan')
    yuezhi = rigan_yuezhi.get('yuezhi')

    rigan_wuxing = rigan_wuxing_table.get(rigan)
    yuezhi_wuxing = yuezhi_wuxing_table.get(yuezhi)

    if rigan_wuxing in yuezhi_wuxing:
        is_strong = 1
        favorable_wuxing = wuxing_interaction_table.get(rigan_wuxing).get('harmful')
    else:
        is_strong = 0
        favorable_wuxing = wuxing_interaction_table.get(rigan_wuxing).get('helpful')
    return { 'is_strong': is_strong, 'favorable_wuxing': favorable_wuxing }


def main():
    rigan = input('日干：')
    yuezhi = input('月支：')

    result = amistrong({ 'rigan': rigan, 'yuezhi': yuezhi })
    print(f'{'身强' if result.get('is_strong') else '身弱'}，喜用{''.join(result.get('favorable_wuxing'))}。')

    # rigan_yuezhi_favorable_wuxing_table = {}

    # for rigan in rigan_wuxing_table.keys():
    #     rigan_yuezhi_favorable_wuxing_table[rigan] = {}
    #     for yuezhi in yuezhi_wuxing_table.keys():
    #         result = amistrong({ 'rigan': rigan, 'yuezhi': yuezhi })
    #         rigan_yuezhi_favorable_wuxing_table[rigan][yuezhi] = result.get('favorable_wuxing')

    # with open(os.path.join(DATA_DIR, 'rigan_yuezhi_favorable_wuxing_table.json'), 'w', encoding='utf-8') as file:
    #     json.dump(rigan_yuezhi_favorable_wuxing_table, file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
