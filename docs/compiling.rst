Compiling
=========

Langrinder provides two convenient ways to compile your locale files into a usable format:

**CLI (Command Line Interface)** - Quick and simple compilation using terminal commands[2]

**Programmatically** - Full control over the compilation process from your Python code[2]

CLI Compilation
---------------------

Getting Help
~~~~~~~~~~~~

To see all available options and commands:

.. code-block:: shell

    langrinder --help

Basic Usage
~~~~~~~~~~~~

Compile your locale files with a single command:

.. code-block:: shell

    langrinder locales/ locales/output.json

This command will:
- Scan the ``locales/`` directory for all ``.mako`` template files
- Parse and compile them into a single JSON output file
- Generate optimized translations ready for production use

Programmatic Compilation
-------------------------

For advanced users who need more control over the compilation process, Langrinder offers a comprehensive Python API[2][3].

Step 1: Parse Template Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import langrinder

    # Initialize parser with content and parameters
    parser = langrinder.ABCParser(
        content=template_content, 
        params=langrinder.ParserParameters(...)
    )
    
    # Parse all templates
    parsed = parser.parse_all()


**Built-in implementations:**

- ``langrinder.SyntaxParser`` - Default parser for Mako template syntax

Step 2: Compile Parsed Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Compile parsed templates into final format
    compiled = langrinder.ABCCompiler.compile(parsed)


**Built-in implementations:**

- ``langrinder.JSONCompiler`` - Generates optimized JSON output for production

Step 3: Save Compiled Output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import pathlib

    # Write compiled data to file
    with pathlib.Path("output.json").open("w", encoding="utf-8") as file:
        file.write(compiled)

Why Use Each Method?
---------------------

**Choose CLI when:**

- Quick compilation during development
- Integrating with build scripts or CI/CD pipelines
- Simple project structure

**Choose Programmatic when:**

- Custom compilation logic required
- Integration with existing Python applications  
- Advanced error handling and validation needed
- Working with dynamic template content

Both methods produce the same high-quality compiled output optimized for runtime performance.
