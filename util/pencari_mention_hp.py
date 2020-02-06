from typing import List, Dict


def cek_hp(caption): 
    hasil = []
    for hp_str in caption.split(): 
        if (len(hp_str)>10 and hp_str.isdigit()) or '08' in hp_str: 
            hasil.append(hp_str)
        else: 
            hasil.append(None)
    hasil = [h for h in hasil if h]
    if hasil: 
        return ' '.join(hasil)
    else: 
        return None

def cek_mention(caption): 
    hasil = []
    for hp_str in caption.split(): 
        if hp_str.startswith('@'):
            hasil.append(hp_str)
        else: 
            hasil.append(None)
    hasil = [h for h in hasil if h]
    if hasil: 
        return ' '.join(hasil)
    else: 
        return None




if __name__=='__main__': 
    df = pd.read_excel('caption_ig.xlsx')
    df.dropna(subset=['caption'], inplace=True)
    df['telpon'] = df['caption'].apply(cek_hp)
    df['mention'] = df['caption'].apply(cek_mention)
    df.to_csv('test_caption_ig.csv', index=False)
    df.to_csv('test_caption_ig.csv', index=False)
