from setuptools import setup

setup(
    name="vlanchange",
    version='0.1',
    py_modules=['cli'],
    install_requires=[
        'click',
        'python-dotenv',
        'netmiko'
    ],
    entry_points='''
        [console_scripts]
        vlanchange=cli:main
    '''
)

