from setuptools import setup, find_packages

setup(
  name = 'voicebox-pytorch',
  packages = find_packages(exclude=[]),
  version = '0.0.28',
  license='MIT',
  description = 'Voicebox - Pytorch',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/lucidrains/voicebox-pytorch',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'text to speech'
  ],
  install_requires=[
    'audiolm-pytorch>=1.2.28',
    'naturalspeech2-pytorch>=0.0.41',
    'beartype',
    'einops>=0.6.1',
    'lightning>=2.0.7',
    'torch>=2.0',
    'torchdiffeq',
    'torchode',
    'vocos'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
