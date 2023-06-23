from audiocaps_download import Downloader

d = Downloader(
    root_path='./AudioCaps/',
    n_jobs=16
)
# d.format = 'wav'
# d.quality = 0
d.download(format='wav')
d.cross_check()
