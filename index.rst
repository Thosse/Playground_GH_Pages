Intersphinx Minimal Example
===========================

Links to Headders added via autosectionlabels work inconsistently with intersphinx.
The following header names contain either "Works" if the can be linked to via intersphinx
or "Fails" if they cannot be linked to.

Any direct referencing (not using inersphinx) works fine.
All corresponding link objects exist, as seen in :download:`the converted objects.inv file <media/sphobjinv.txt>`.

However, only some headers can be linked to via intersphinx.
This seems to be an error related to the decryption of the objects.inv file,
since calling

    ``python -m sphinx.ext.intersphinx https://thosse.github.io/Playground_GH_Pages/``

returns only :download:`a subset of the link targers <media/intersphinx.txt>`.


Headers without Digits work
---------------------------

:ref:`index:Headers without Digits work`

1 Works
-------
:ref:`index:1 Works`

Works 1
-------
:ref:`index:Works 1`

Works 1 Works
-------------
:ref:`index:Works 1 Works`

123 Works
---------
:ref:`index:123 Works`

1 2 3 Fails
-----------
:ref:`index:1 2 3 Fails`

Fails Fails 1
-------------
:ref:`index:Fails Fails 1`

Fails Fails 2 Fails Fails
-------------------------
:ref:`index:Fails Fails 2 Fails Fails`

Fails 1 2 Fails
---------------
:ref:`index:Fails 1 2 Fails`

Fails 1 Fails 2
---------------
:ref:`index:Fails 1 Fails 2`

Fails 1 2 3
------------
:ref:`index:Fails 1 2 3`

1 Fails 1
---------
:ref:`index:1 Fails 1`
