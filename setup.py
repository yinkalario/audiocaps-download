from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='audiocaps-download',
    version='1.0',
    description='This package aims at simplifying the download of the AudioCaps dataset.',
    py_modules=["Downloader"],
    packages=find_packages(include=['audiocaps_download', 'audiocaps_download.*']),
    classifiers={
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    },
    long_description = long_description,
    long_description_content_type = "text/markdown",
    install_requires = [
        "joblib",
        "pandas",
        "yt-dlp",
        "pandas",
        "torchaudio",
        "tqdm"
    ],
    extras_require = {
        "dev" : [
            "pytest>=3.7",
        ],
    },
    url="https://github.com/MorenoLaQuatra/audiocaps-download",
    author="Moreno La Quatra",
    author_email="moreno.laquatra@gmail.com",
)