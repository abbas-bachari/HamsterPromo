from setuptools import setup, find_packages

setup(
    name='HamsterPromo',
    version='1.0.4',
    author='Abbas Bachari',
    author_email='abbas-bachari@hotmail.com',
    description='Hamster Kombat Promo Code Generator',
    long_description=open('README.md',encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    packages=find_packages(),
    url='https://github.com/abbas-bachari/HamsterPromo',
    python_requires='>=3.10',
    project_urls={
    "Homepage":'https://github.com/abbas-bachari/HamsterPromo',
    'Documentation': 'https://github.com/abbas-bachari/HamsterPromo',
    'Source': 'https://github.com/abbas-bachari/HamsterPromo/',
    'Tracker': 'https://github.com/abbas-bachari/HamsterPromo/issues',
   
},
    
    install_requires=[
                    'aiohttp',
                    'aiohttp_proxy',
                    'asyncio',
                    'loguru',
                    ],
    
    keywords=['hamster', 'hamster key', 'hamster-pythom', 'HamsterPromo',  'api', 'abbas bachari'],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
        
        
        
    ],
)


