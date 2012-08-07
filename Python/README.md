Project-Euler
=============

 Introduction
-------------
http://projecteuler.net/

Project Euler is a website dedicated to a series of computational problems intended to be solved with computer programs. The project attracts adults and students interested in mathematics and computer programming. Here we will solve them using Python with purely functional programming style. 

Some people have expressed their concerns about making the solutions of the Euler Project public. While the risk of having people using them unjustly certainly exists (shame on them), the benefits of sharing knowledge should exceed this petty inconvenient.

Project Euler Python
=======================

简介
---------
用Python 3.x计算Project Euler 开发环境是Win7/Eclipse Juno/Pydev


文件简介
------------
* [.euler.py](https://github.com/ifooth/ProjectEuler-Python/blob/master/src/_euler.py) -- 运行主入口
* [.euler_pdb.py](https://github.com/ifooth/ProjectEuler-Python/blob/master/src/_euler.py) -- 动态调试模块
* [.euler_profiling.py](https://github.com/ifooth/ProjectEuler-Python/blob/master/src/_euler.py) -- profiling测试模块
* [.euler_unitest.py](https://github.com/ifooth/ProjectEuler-Python/blob/master/src/_euler.py) -- unitest测试模块
* [.euler.lib](https://github.com/ifooth/ProjectEuler-Python/blob/master/src/_euler.py) -- 算法库
* [.euler.lib.ext](https://github.com/ifooth/ProjectEuler-Python/blob/master/src/_euler.py) -- 标准数据类型扩展库
* [.euler.lib.data](https://github.com/ifooth/ProjectEuler-Python/blob/master/src/_euler.py) -- 数据文件处理模块
* [.euler.lib.utilities](https://github.com/ifooth/ProjectEuler-Python/blob/master/src/_euler.py) -- 小实用库
* [.euler.problem](https://github.com/ifooth/ProjectEuler-Python/blob/master/src/_euler.py) -- 问题代码库
* [.euler.problem.problem](https://github.com/ifooth/ProjectEuler-Python/blob/master/src/_euler.py) -- 问题入口类
* [.euler.problem.problem_x_x](https://github.com/ifooth/ProjectEuler-Python/blob/master/src/_euler.py) -- 问题代码库
* [euler.data](https://github.com/ifooth/ProjectEuler-Python/blob/master/src/_euler.py) -- 问题需要的数据文件


开发编码规范
==========

代码的布局
-------------
Eclipse Juno+PyDev 默认编码

命名约定
----------

1. 包名与的总是全部小写的ASCII字母 lowcaselowcase
2. 模块名全部是小写的ASCII字母,运行下划线
3. 类名是个一名词，采用大小写混合的方式，每个单词的首字母大写
4. 函数名方法名是一个动词，采用大小写混合的方式，第一个单词的首字母小写，其后单词的首字母大写
5. 变量名 除了变量名外，所有实例，包括类，类常量，均采用大小写混合的方式，第一个单词的首字母小写，其后单词的首字母大写
6. 常量名 常量的声明，应该全部大写，单词间用下划线隔开
9. 方法与变量名 参见函数名与全局变量名

继承的设计
----------
1. _表示内部变量与函数 可以认为protected
2. __表示私有变量与函数 可以认为private
