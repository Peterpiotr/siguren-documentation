==========================
Controller internal check
==========================

.. include:: ../../_img/_image-substitutions.rst

After initial power up or after reset is performed, MS Controller start internal check.
All steps and actions from initialization are displayed on integrated 7 segment display.
Internal initialization sequences is as follows:

1. Initial initialization check
2. MS Controller OS version
3. Fieldbus addres

Initial initialization check
----------------------------

1. |start| - start of internal check
2. |driver| - communication initialization
3. |communication| - communication initialization OK
4. |init-app-done| - initialization of loaded software OK
5. |init-done| - initialization done