==========
test page
==========

hhhhhhhhsdjfijsdfijfkdjlfxcjklhvklcjvsiodjfgsdiohfgsdiofh
=========================================================

.. tags:: tag1, tag2

.. seealso::

  saidaosfhjfh



kkkk lorem :hoverxref:`example-ref` 

.. figure:: .png
	:figwidth: 600 px
	:align: center

	General view



.. list-table:: 
   :widths: 5 95
   :header-rows: 1
   :class: instruction-table
  
   * - Step
     - Description
   * - **1**
     - 
   * - **2**
     - 

The :mechpart:`worm wheel` is single-helix.

I have footnoted a first item [#f1]_ and second item [#f2]_.
This also references the second item [#f2]_.

.. rubric:: Footnotes
.. [#f1] My first footnote.
.. [#f2] My second footnote.

.. note:: 
	kafkaesque!

.. list-table:: --
   :widths: 5 95
   :header-rows: 1
   :class: instruction-table
  
   * - Step
     - Description
   * - **1**
     - Switch off the supply of the MotoSuiveur® cabinet or all the circuit breaker inside.
   * - **2**
     - 


.. list-table::
  :widths: 30 10 30
  :header-rows: 1
  
  * - Number
    - Image
    - Description
  * - 1
    - 
    - Prior to removing the existing plummer block, make one rotation and find by comparator the 2 points on the barrel side flange that are on the same axial plane on the diameter of the future pin and bolts diameter. These two points will receive the bolt holes.
  * - 2
    - 
    - Remove the existing plummer block.
  * - 3
    - 
    - Put the transmission flange on the barrel shaft (fitted assembly) and use the holes to counter-drill holes on the barrel side flange.
  * - 4
    - 
    - Mount the transmission flange on the MS wheel (bolts, pins).
  * - 5
    - 
    - Assemble the flanged MS to the side flange of the barrel. The washers create a gap which allows the MS to be strictly aligned with the barrel (shaft) axis. The MS wheel and flange are fitted to the existing barrel shaft so the MS is strictly concentric to the barrel.



+-----+------+-----+-----+------+-----+
| sd  | fsd  | fs  | df  | fsd  |     |
+=====+======+=====+=====+======+=====+
| dfs | d    | s   | fsd | fsd  |     |
+-----+------+-----+-----+------+-----+
| dfs | d    | f   | sd  | sd   | df  |
+-----+------+-----+-----+------+-----+
| s   | sd   | f         | d    |     |
+-----+------+           +------+-----+
| d   | d    |           | d    |     |
+-----+------+-----+-----+------+-----+
|     | dd   | d   |     |      |     |
+-----+------+-----+-----+------+-----+
|     | d    |     |     | d    |     |
+-----+------+-----+-----+------+-----+

.. rubric:: "rubric" directive

The "rubric" directive inserts a "rubric" element into the document tree. A rubric is like an informal heading that doesn't correspond to the document's structure.


+--------------------------+----------------------------+
| **Navigation to screen** | Main screen ➔ Menu screen |
+--------------------------+----------------------------+


Some text that requires a footnote [#f1]_ .

Title
=======

.. raw:: html

   <hr>

Some other thext.







.. rubric:: Footnotes

.. [#f1] Text of the first footnote.




.. figure:: docs/source/_img/Backup/backup-mode-off-on.PNG
    :target: https://siguren-documentation.readthedocs.io/en/0.1.1/99-test.html



.. figure:: ../../_img/Backup/backup-down-up-control-off.png
	:figwidth: 300 px
	:align: center

	End of lowering

:doc:`../../operation/regular/index`
  An introduction to Blender's window system, widgets and tools.


Sections
========

.. only:: builder_html and (not singlehtml)

   .. container:: toc-cards

      .. container:: card

         .. figure:: /_img/electricalConnections.png
            :target: interface/index.html

         :doc:`/about/features`
            An introduction to Blender's window system, widgets and tools.

      .. container:: card

         .. figure:: /images/index_editors.jpg
            :target: editors/index.html

         :doc:`/editors/index`
            Overview of the interface and functionality of all editors.

      .. container:: card

         .. figure:: /images/index_scene.jpg
            :target: scene_layout/index.html

         :doc:`/scene_layout/index`
            Objects and their organization into scenes, view layers and collections.

      .. container:: card


.. grid:: 2 3 3 4

    .. grid-item::

        .. card:: Title
            :img-background: /_img/electricalConnections.png
            :class-card: sd-text-black
            :img-alt: my text

            Text

    .. grid-item-card:: Title
        :img-top: /_img/electricalConnections.png
        :img-alt:

        Header
        ^^^
        Content
        +++
        Footer

    .. grid-item-card:: Title
        :img-bottom: /_img/electricalConnections.png

        Header
        ^^^
        Content
        +++
        Footer

.. _cards-clickable:

Cards Clickable
...............

.. card:: Clickable Card (external)
    :link: https://example.com

    The entire card can be clicked to navigate to https://example.com.

.. card:: Clickable Card (internal)
    :link: cards-clickable
    :link-type: ref

    The entire card can be clicked to navigate to the ``cards`` reference target.
