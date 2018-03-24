from distutils.core import setup 

setup(
  name = 'GlucTool',
  version='0.1.0',
  packages = ['GlucTool'], 
  description = 'Utility for converting plasma glucose ("blood sugar") units.',
  author = 'Marshall J. Krinitz',
  author_email = 'mjk235@nyu.edu',
  url = 'https://github.com/marshki/GlucTool',
  download_url = 'https://github.com/marshki/GlucTool/archive/0.1.tar.gz',
  license = 'MIT',
  keywords = ['blood sugar', 'glucose', 'conversion', 'utility' 'mg' 'mmol'], 
  install_requires=['argparse'],
)
