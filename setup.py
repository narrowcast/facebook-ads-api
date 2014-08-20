import subprocess
import sys
from distutils.core import setup, Command


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        errno = subprocess.call([sys.executable, 'test_facebook.py'])
        raise SystemExit(errno)

setup(
    name='facebook-ads-api',
    version='0.1.39',
    author='Chee-Hyung Yoon',
    author_email='yoonchee@gmail.com',
    py_modules=['facebook', ],
    url='http://github.com/narrowcast/facebook-ads-api',
    license='LICENSE',
    description='Python client for the Facebook Ads API',
    long_description=open('README.md').read(),
    cmdclass={'test': TestCommand},
)
