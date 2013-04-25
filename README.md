maelstrom
---------
The plan is to write a program for media collecting, browsing and sharing with
the following features:

* Extremely simple command-line interface.
    * Initialize a collection with one command.
    * Serve media over LAN or other networks with one command.
    * Intuitive commands to list, find, create and edit items.
    * Configure the program.
* Generate a beautiful interface for displaying and browsing your media
  collection.
* Serve the content online (with password protection).
* Customize the appearance of the web-based interface.

Possible libraries to build on include:

* Django or Flask as a web framework.
* Twitter Bootstrap for the base layout and appearance.
* IMDbPy to scrape movie data.
* PostgreSQL or SQLite to store the data.
* Docopt or argparse for the command-line interface.
* The command-line interface can build on [mov](https://github.com/hph/mov) and
  improve it.
