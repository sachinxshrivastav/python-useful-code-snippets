from tqdm import tqdm
from time import sleep

for i in tqdm(range(100), total = 100 ,desc ="Progress"):
	sleep(.1)