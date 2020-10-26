from setuptools import setup

setup(
		name='ugit',
		version='1.0',
		packages=['ugits'],
		entry_points={
						'console_scripts':['ugit = ugits.cli:main']
						}
		)
