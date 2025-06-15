Langrinder
==========

Langrinder is a flexible **internationalization (i18n) engine** based on **Mako** templates

Why Langrinder?
---------------

- Based on mako templates. Maximum flexibility and comfort
- Compiles directly into Python classes
- Variety of built-in functions and integrations

Installation
------------

.. code-block:: shell

    pip install "langrinder @ git+https://github.com/tirch/langrinder.git"
    pip install "langrinder[telegrinder] @ git+..."
    pip install "langrinder[cli] @ git+..." # Recommended

Usage
-----

- Create locales files (``locales/<locale>/<smth>.mako``)
    - ``locales/en/main.mako``:
        
        .. code-block:: mako

            @start: Hello from ${html.bold('Langrinder')}!

    - ``locales/ru/main.mako``:
        
        .. code-block:: mako

            @start: Привет от ${html.bold('Langrinder')}!

- Compile translations

.. code-block:: shell

    langrinder locales/ locales/compiled.json

- Enjoy! See our main example and bot example!

Latest update
-------------

v3.0.0 - Big update!
~~~~~~~~~~~~~~~~~~~~

- Free of Telegrinder
- Free of Pendulum (removed time formatter. Use custom (humanize, babel, etc.)
- New compiling style
- Code rewriting and refactoring
- CLI interface (``pip install langrinder[cli]``)

License
-------

Langrinder licensed under MIT license. Free and open-source!


.. toctree::
   :hidden:

   compiling
