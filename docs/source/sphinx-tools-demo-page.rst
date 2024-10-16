============================
Sphinx Tools Demo Page (Dev)
============================

Heading 1
=========

Content

Heading 2
---------

➔ test➔ test➔ test➔ test➔ test➔ test


.. tags:: tag1, tag2

.. seealso::

  seealso content



:hoverxref:`example-ref` 

.. figure:: /_img/Backup/backup-down-up-control-off.png
	:figwidth: 600 px
	:class: instructionimg

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
| **Navigation to screen** | Main screen ➔ Menu screen  |
+--------------------------+----------------------------+


Some text that requires a footnote [#f1]_ .

Title
=======

.. raw:: html

   <hr>

Some other thext.







.. figure:: /_img/Backup/backup-mode-off-on.PNG
    :target: https://siguren-documentation.readthedocs.io/en/0.1.1/99-test.html

    figure comment


.. figure:: /_img/Backup/backup-down-up-control-off.png
    :figwidth: 300 px
    :align: center

    End of lowering


:doc:`../../operation/regular/index`
  An introduction to Blender's window system, widgets and tools.


Heading 2
^^^^^^^^^^

Curve Preset
   :Custom:
      You can choose how the strength of the falloff is determined from the center of the brush
      to the borders by manually manipulating the control points within the curve widget.
      There are also a couple of preset custom curves displayed at the bottom of the curve widget
      that can be used on their own or as a starting point for tweaking.

      .. list-table:: Custom Preset types.

         * - .. figure:: _img/Regular-operations/MS-block-diagram-color_1.PNG

                Smooth.

           - .. figure:: _img/Regular-operations/MS-block-diagram-color_1.PNG

                Sphere.

           - .. figure:: _img/Regular-operations/MS-block-diagram-color_1.PNG

                Root.

         * - .. figure:: _img/Regular-operations/MS-block-diagram-color_1.PNG

                Sharp.

           - .. figure:: _img/Regular-operations/MS-block-diagram-color_1.PNG

                Linear.

           - .. figure:: _img/Regular-operations/MS-block-diagram-color_1.PNG

                Constant.

The following standard selection operations are supported:

- :kbd:`Reset` -- Single faces
- :kbd:`Shift-Alt-LMB` -- Select more or remove them from the selection.
- :kbd:`A` -- All faces, :kbd:`A A` to deselect.
- :kbd:`B` -- Box selection.
- :kbd:`C` -- Circle select with brush.
- :kbd:`Ctrl-I` -- Invert selection.
- :kbd:`L` -- Pick linked (under the mouse cursor).
- :kbd:`Ctrl-L` -- Select linked.
- :kbd:`Ctrl-NumpadPlus` -- Extend Selection
- :kbd:`Ctrl-NumpadMinus` -- Shrink Selection

.. figure:: _img/Regular-operations/MS-block-diagram-color_1.PNG

   Vertex Selection masking.


.. the following is from "Dimitar-test.rst"

.. card:: 
    :width: auto
    :img-top: _img/Peter/MSwarningNumber10.png
    :link: https://siguren-documentation.readthedocs.io/en/0.1.1/equipment/ms-solution/ms-unit.html

    MotoSuiveour Unit

Original size
-------------

.. grid:: 3
    :gutter: 4
    
    .. grid-item-card::
        :img-top: _img/Index/Original/Control-cabinet-overview.png
        :link: ../ms-solution/ms-unit

        MotoSuiveur Unit
 
        

    .. grid-item-card::
        :img-top: _img/Index/Original/hydraulic-ms.PNG
        :link: ../diagnostics/controller-errors.rst

        MS Controller Faults and Warnings


resized
-------

.. grid:: 3
    :gutter: 4
    
    .. grid-item-card::
        :width: auto
        :img-top: _img/Index/control-cabinet.jpg
        :link: ../ms-solution/ms-unit

        MotoSuiveur Unit
 
        

    .. grid-item-card::
        :width: auto
        :img-top: _img/Index/ms-unit.jpg
        :link: ../diagnostics/controller-errors.rst

        MS Controller Faults and Warnings