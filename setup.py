import setuptools

setuptools.setup(
    name="simplelayout-meitounao110",  # Replace with your own username
    version="0.0.1",
    author="meitounao110",
    author_email="431041317@qq.com",
    description="A simplelayout package",
    url="https://github.com/idrl-assignment/3-simplelayout-package-meitounao110",
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    install_requires=['matplotlib', 'numpy', 'scipy', 'pytest'],
    entry_points={
        'console_scripts': [  # 配置生成命令行工具及入口
            'simplelayout = simplelayout.__main__:main'
        ]
    },
)
