
import sys
from pathlib import Path

def gen_new_md(accepted, papers):
    id2data = dict()
    for l in papers:
        l = l.strip()
        if l == "":
            continue
        l = l.split('\t')
        id = l[0]
        name = l[1]
        paper = l[2]
        print(f'{id}: name = "{name}". paper = "{paper}"')
        id2data[int(id)] = (paper, name)
    accepted_ids = set(int(x) for l in accepted for x in l.split())
    print(accepted_ids)
    to_print = []
    for x in id2data.items():
        num, data = x
        paper, name = data
        if num not in accepted_ids:
            continue
        to_print.append((num, paper, name))
    to_print = sorted(to_print, key=lambda x: (x[2], x[1]))
    if False: # Copying file
        print()
        print('Copy to sent')
        print()
        for new_id, x in enumerate(to_print, start=1):
            num, paper, name = x
            print(f'cp prl2021/posters/PRL2021_poster_{num}.pdf prl2021/PRL-posters-gather/{new_id:02}-PRL.pdf')
    print()
    print('Markdown')
    print()
    for new_id, x in enumerate(to_print, start=1):
        num, paper, name = x
        #print(f'* #{new_id}: {paper} ({name}) ([PDF](prl2021/papers/PRL2021_paper_{num}.pdf))')
        print(f'* #{new_id}: {paper} ({name}) ([Paper PDF](prl2021/papers/PRL2021_paper_{num}.pdf))', end='')
        poster = f'posters/PRL2021_poster_{num}.pdf'
        if Path(poster).exists():
            print(f' ([Poster PDF](prl2021/{poster}))', end='')
        slides = f'slides/PRL2021_slides_{num}.pdf'
        if Path(slides).exists():
            print(f' ([Slides PDF](prl2021/{slides}))', end='')
        print()

# Main
with open('code/accepted-num.txt') as accepted:
    with open('code/papers-easychair.txt') as papers:
        gen_new_md(accepted, papers)
