from setuptools import setup, find_packages

setup(name='Remove Brackets',
      version='0.1',
      description='A script to remove brackets and parentheses from file names.',
      author='Derek Santos',
      license='The MIT License (MIT)',
      url='https://github.com/santosderek/Remove_Brackets',
      packages=['remove_brackets'],
      scripts=['remove_brackets/__main__.py'],
      entry_points={
          'console_scripts':
              ['remove_brackets = remove_brackets.__main__:main',
               'rb = remove_brackets.__main__:main']
      }
      )
