import sys
from setuptools import setup
import glob

NAME = 'rciam_probes'
NAGIOSPLUGINS = '/usr/libexec/argo-monitoring/probes/rciam'

def get_ver():
    try:
        for line in open(NAME + '.spec'):
            if "Version:" in line:
                return line.split()[1]
    except IOError:
        print("Make sure that %s is in directory" % (NAME + '.spec'))
        sys.exit(1)


def data_files():
    import os
    if not os.path.isdir('/usr/libexec/'):
        return []
    return [(NAGIOSPLUGINS, glob.glob('src/*'))]


setup(name=NAME,
      version=get_ver(),
      license='Apache-2.0',
      author='ioigoume@admin.grnet.gr',
      author_email='ioigoume@admin.grnet.gr',
      description='Package includes probes for RCIAM',
      platforms='noarch',
      long_description='''
      This package includes probes for RCIAM.
      Currently it supports the following components:
        - Metadata Health
        - Login Health
      ''',
      url='https://github.com/ioigoume/rciam_probes',
      data_files=data_files(),
      packages=['rciam_probes'],
      package_dir={'rciam_probes': 'modules/'},
      python_requires='~=3.5'
      )
