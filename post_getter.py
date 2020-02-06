import json
from pathlib import Path
import pandas as pd
from datetime import datetime
from util.pencari_mention_hp import *


def csv_jos(filename , outfile = ''):
    with open(filename) as f:
        lol = json.load(f)

    posts = []
    for i,p in enumerate(lol['posts']):
        hasil={'caption': p['caption'], 'likes':p['likes']['count'], 'sumber':lol['username'], 'url':p['url']}
        posts.append(hasil)

    df = pd.DataFrame(posts)
    df.drop_duplicates(inplace=True)
    df['telpon'] = df['caption'].apply(cek_hp)
    df['mention'] = df['caption'].apply(cek_mention)
    return df


def kumpulan_json():
    return [filename for filename in Path('./profiles').rglob('*.json')]

def di_csv_kan():
    kumpulan_df = []
    for f in kumpulan_json():
        kumpulan_df.append(csv_jos(f))
    df = pd.concat(kumpulan_df)
    df.to_csv(f'kumpulan_{datetime.now().strftime("%d_%m_%Y")}.csv', index=False)
