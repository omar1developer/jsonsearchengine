from setuptools import setup, find_packages

setup(
    name='JsonSearchEngine',
    version='1.0.0',
    packages=find_packages(),
    author='omar khattara',
    author_email='omar1developer@gmail.com',
    description='A Python class for searching within JSON data structures',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/omar1developer/jsonsearchengine',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    package_dir={'': 'src'}
)