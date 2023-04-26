from setuptools import setup, find_namespace_packages

setup(
    name='clean-folder-a-chych',
    version='0.0.3',
    description='Folder cleaner',
    author='Andrii Chychur',
    author_email='a.chy-test@gmail.com',
    url='https://github.com/chychur/hw-7',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'],
    packages=find_namespace_packages(),
    include_package_data=True,
    entry_points={'console_scripts': [
        'clean-folder=clean_folder.clean:run']
        }
)