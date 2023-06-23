from audiocaps_download import Downloader

d = Downloader(
    root_path='/home/yincao/Workspace/SSD2/datasets/AudioCaps/',
    n_jobs=32
)
# d.format = 'wav'
# d.quality = 0
d.download(format='wav')
d.cross_check()
