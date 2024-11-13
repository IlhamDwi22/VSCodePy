from setuptools import setup, find_packages # type: ignore

setup(
    name='paket_js_13',
    version='0.1.0',
    author='IlhamDwi22',
    author_email='ilhamdwiganteng@gmail.com',
    description='A short description of my package',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    
    python_requires='>=3.6',
)