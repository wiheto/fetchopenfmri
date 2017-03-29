from setuptools import setup,find_packages
setup(name='fetchopenfmri',
      version='1.0.3',
      description='Fetches files for the latest version of an openfMRI dataset',
      packages=find_packages(),
      author='William Hedley Thompson',
      author_email='hedley@startmail.com',
      url='https://www.github.com/wiheto/fetchopenfmri',
      entry_points={
        'console_scripts': ['fetchopenfmri=fetchopenfmri.fetch:main'],
      },
      download_url = 'https://github.com/wiheto/fetchopenfmri/archive/v1.0.1.tar.gz',
      keywords=['openfmri','open data','fmri']
      )
