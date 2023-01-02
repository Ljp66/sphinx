=============
reST语法学习
=============

基本语法
=========
段落
---------

.. sidebar:: 这是一个侧边栏

    这是一个侧边栏, 可以放入代码, 也可以放入图像代码等等, 它下面可以是文字, 图像, 代码等等, 如本例中下面是一段文字.

这是一个段落，里面包含 **强调字** 、``code block`` 和 *斜体字*。

这是另一个段落，不包含\**强调字\**、\``code\`` 和\*斜体字\*。

本段学习使用注脚 [1]_，注脚有很多种格式 [2]_。

本段学习使用链接，有多种链接表达方式，例如单独一个链接：https://python.org ;

例如外部链接 `python <https://python.org>`_。
还有另一种表达方式 `python website`_。

::

  原意表达区块，在这里仅仅表达原意。
  **强调** ， *斜体* ，都无法使用。
  列表也无法使用

  - 列表一
  - 列表二 

来一个区块引用：

春江潮水连海平，
  
  海上明月共潮生；

    滟滟随波千万里，

      何处春江无月明。

>>> print("hello world")
hello world


-----

| 本段学习换行。
| 这是新的一行。
| 这又是新的一行。

.. _python website: https://python.org

当然，也可以使用内部链接，`表格`_ ;
另一种内部链接 :ref:`list`。

还可以链接图片 :ref:`image1`,可以链接python 代码 :ref:`python code`。

..  [1] 这是注脚一。
..  [2] 这是注脚二。

代码
=====
代码高亮
--------

..  code:: python

  import os
  print("你好，世界")

.. sourcecode::

  import matplotlib.pyplot as plt

.. code-block:: python
  :caption: python代码
  :emphasize-lines: 2,3
  :linenos:
  :name: python code

  print("hello world!")
  print("hello world!")
  print("hello world!")
  print("hello world!")
  print("hello world!")

嵌入文件
--------

.. literalinclude:: code/calculator.py
  :language: python
  :emphasize-lines: 2,3
  :caption: this is a python file
  :name: python file
  :linenos:

图片
=====


.. image:: images/logo.png
  :height: 100
  :width: 100
  :scale: 25%
  :align: center
  :alt: logo
  :target: https://google.com

.. _image1:

.. figure:: images/logo.png
  :scale: 20%
  :align: center
  :alt: logo

  这是图像说明

.. _list:

列表
=====

再来一些无序列表：

- 无序序列一
- 无序序列二
- 无序序列三

接下来是有序列表：

1. 有序列表一
#. 有序列表二
#. 有序列表三

试试序列杂糅：

a. 有序序列

 - 无序序列一
 - 无序序列二

b. 有序序列二

c. 有序序列三

 - 序列一
 - 序列二

:Something: single item
:Someitem: single item

Term
    Definition for term
Term2
    Definition for term 2

.. note:: 这是一个注解！

.. _表格:

下面是表格：

表格
=====

列表式表格
----------

.. list-table:: 列表式表格
    :widths: 15 10 30
    :header-rows: 1

    * - 名称
      - 质量
      - 描述
    * - vs code
      - 10
      - 轻量级文本编辑器
    * - pycharm
      - 10
      - 专业python IDE
    * - notepad++
      - 5
      - 微型记事本

栅栏式表格
----------

+--------+--------+--------+
| Time   | Number | Value  |
+========+========+========+
| 12:00  | 42     | 2      |
+--------+--------+--------+
| 23:00  | 23     | 4      |
+--------+--------+--------+

+-------+-------+--------+
| name  | value |  rate  |
+=======+=======+========+
| vscode| 10    |        |
+-------+-------+--------+
| pycha | 11    |        |
+-------+-------+--------+

简单表格
--------

========   ========
名称         排名
--------   --------
vscode       2
========   ========
pycharm      1
========   ========

csv表格
--------

.. csv-table:: Frozen Delights!
  :header: "Treat", "Quantity", "Description"
  :widths: 15, 10, 30

  "Albatross", 2.99, "On a stick!"
  "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
   crunchy, now would it?"
  "Gannet Ripple", 1.99, "On a stick!"

数学
=====

| 行内公式 :math:`\alpha > \beta` :
| 居中公式：

.. math::

  n_{\mathrm{offset}} = \sum_{k=0}^{N-1} s_k n_k

  a^2 + b^2 = c^2

提示警告
=========

.. tip:: 这是小技巧

.. note:: 这是备注

.. hint:: 这是提示

.. danger:: This is a danger

.. error:: 这是错误

.. warning:: This is a warning

.. caution:: This is a caution

.. attention:: This is an attention

.. important:: This is an important

.. seealso:: This is seealso

小技巧
======
评论
-----

.. 这是一个不显示的评论。
.. 
  
  这是一个评论，不知道如何显示。

引用
-----

Sphinx支持标准的 reST 引文, 此外, 在Sphinx里, 所有的 [引文]_ 都是全局的,
所有文件都能引用任意的文献, 像下面这样使用引文:

.. [引文] 引文所引用的内容。

替换
-----

你看到了吗? 第二个单词 word |word| !

.. |word| replace:: 替换成我了


"大唐芙蓉园-婚纱照"本来是个短语, 使用 |图片| 会被替换成图像!

.. |图片| image:: images/logo.png
          :alt: logo
          :scale: 25%