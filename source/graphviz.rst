=========
graphviz
=========

绘制graphviz图
==============

.. graphviz::
  :alt: 继承
  :align: center
  :caption: 这是一个由graphviz绘制的图
  :name: graphviz1

  digraph UML {
      node[fontname = "LXGWWenKai-Regular", fontsize = 10, shape = record];
      edge[fontname = "LXGWWenKai-Regular", fontsize = 10, arrowhead = "empty"];

      Car[label = "{Car | v: float\nt : float | run() : float}"]

      subgraph clusterSome{
          bgcolor = "yellow";
          Bus[label = "{Bus | | carryPeople() : void}"];
          Bike[label = "{bike | | ride() : void}"];
      }
      Bus -> Car
      Bike -> Car
  }

引用graphviz文件
=================

.. graphviz:: graphviz\Sequence.dot
  :alt: 时序图
  :align: center
  :caption: 这是一个由graphviz绘制的时序图
  :name: graphviz2

无向图
=======

.. graph:: foo
  :alt: 无向图
  :align: center
  :caption: 这是一个无向图
  :name: graph

  "bar" -- "baz";

有向图
=======

.. digraph:: foo
  :alt: 无向图
  :align: center
  :caption: 这是一个有向图
  :name: digraph

  "bar" -> "baz" -> "quux";