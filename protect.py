# protect.py
# Daniel Kogan
# 7/25/2020
import fire
from PIL import Image
import numpy as np
def main(IMG):
	mask = Image.open("mask.png")
	background = Image.open(IMG)
	background.paste(mask, (0,0), mask)
	background.save(IMG)
if __name__ == '__main__':
	fire.Fire(main)
