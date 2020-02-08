from typing import List, Dict
import re


def cek_hp(caption):
    hasil = re.findall(
        r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', caption)

    if len(hasil) > 0:
        return ' '.join(hasil)
    else:
        return None
