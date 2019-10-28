
**********************************
Stanley Command Line Tool
**********************************


========
SYNOPSIS
========

::
    usage: pystanley [-h] [-v] --url URL [--ca-cert CA_CERT] [--plot]
                     [--plot-markers] [--csv] [--start DATETIME]
                     [--end DATETIME]
                     PATH [PATH ...]

    Fetch data from Stanley

    positional arguments:
      PATH               Time-series path

    optional arguments:
      -h, --help         show this help message and exit
      -v, --verbose      increase output
      --url URL          Stanley archiver URL
      --ca-cert CA_CERT  Custom certification authority certificate
      --plot             plot results
      --plot-markers     show plot markers
      --csv              print results to stdout in CSV format
      --start DATETIME   initial time (default: 24h ago)
      --end DATETIME     final time (default: now)



===========
DESCRIPTION
===========

*stanley* is a command line tool to fetch data from a Stanley server.


=======
OPTIONS
=======

---------------
General options
---------------

``-h``, ``--help`` Show documentation

``-v`` Increase verbosity


-------------------------
Stanley archiver options
-------------------------

``--url`` Stanley archiver URL

``--ca-cert`` Optional certificate chain for custom certification authority


------------
Date options
------------

``--start`` Initial time [default: 24h ago]

``--end`` Final time [default: now]


--------------
Output options
--------------

``--csv`` Print results to stdout in CSV format

``--plot`` Plot results

``--plot-markers`` Show plot markers


===========
EXAMPLES
===========

The following command plots the specified time-series over the past 24h::

    pystanley --url https://localhost:8443 --plot "/some/path"
