from os.path import isfile, isdir, getsize
from tqdm import tqdm
import zipfile

class DLProgress(tqdm):
    last_block = 0

    def hook(self, block_num=1, block_size=1, total_size=None):
        self.total = total_size
        self.update((block_num - self.last_block) * block_size)
        self.last_block = block_num

def downloadData(file, url):        
    if not isfile(file):
        with DLProgress(unit='B', unit_scale=True, miniters=1, desc='Fake News Dataset') as pbar:
            urlretrieve(url, file, pbar.hook)

    with zipfile.ZipFile(file) as f:
        f.extractall('./data/')
