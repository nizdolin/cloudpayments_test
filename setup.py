from setuptools import find_packages, setup


install_requires = (
    'aiohttp==3.8.1',
    'aiohttp-basicauth==1.0.0',
    'aiosignal==1.2.0',
    'async-timeout==4.0.2',
    'attrs==21.4.0',
    'charset-normalizer==2.1.0',
    'frozenlist==1.3.0',
    'gunicorn==20.1.0',
    'idna==3.3',
    'marshmallow==3.17.0',
    'marshmallow-dataclass==8.5.8',
    'multidict==6.0.2',
    'mypy-extensions==0.4.3',
    'packaging==21.3',
    'pyparsing==3.0.9',
    'typing-inspect==0.7.1',
    'typing_extensions==4.3.0',
    'yarl==1.7.2',
)


setup(
    name='cloudpayments_client',
    version='0.0.1',
    description='Client for CloudPayments API',
    platforms=['POSIX'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,
)
