==================================
Developer Install - Ubuntu (linux)
==================================

.. contents::


1. Miniconda installation
-------------------------

Follow official website instruction to install miniconda :

http://conda.pydata.org/miniconda.html

2. Create virtual environment and activate it
---------------------------------------------

.. code:: shell

    conda create --name strawberry python
    source activate strawberry


3. Install dependencies with conda
----------------------------------

.. code:: shell

    conda install --c conda-forge python=3.8 pandas k3d openalea.deploy jupyter voila voila-vuetify nodejs cufflinks-py ipyvuetify qgrid plotly
    conda -c fredboudon -c conda-forge openalea.mtg openalea.plantgl openalea.lpy

	git clone git@github.com:pomme-abricot/mtg.git
	cd mtg; python setup.py install; cd ..

	git clone git@github.com:pomme-abricot/oawidgets.git
	cd oawidgets; python setup.py install; cd ..


4. Install the strawberry package
---------------------------------

.. code:: shell

    git clone git@github.com:openalea-incubator/strawberry.git
	cd strawberry; python setup.py install; cd ..
