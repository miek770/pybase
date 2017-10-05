# -*- coding: utf-8 -*-

import argparse, logging, sys

# If global variables are required
import config

def main():
    """Arguments parsing, logger setup and keyboard interrupt handling."""

    parser = argparse.ArgumentParser(description="Python project template")

    parser.add_argument('-v',
                        '--verbose',
                        action='store_true',
                        help="Increase program verbosity.")

    parser.add_argument('-l',
                        '--logfile',
                        action='store',
                        default=None,
                        help="Specify logfile name and location.")

    args = parser.parse_args()

    # Logging configuration
    log_frmt = "%(asctime)s[%(levelname)s] %(message)s"
    date_frmt = "%Y-%m-%d %H:%M:%S "
    if args.verbose:
        log_lvl = logging.DEBUG
    else:
        log_lvl = logging.INFO

    logging.basicConfig(filename=self.args.logfile,
                        format=log_frmt,
                        datefmt=date_frmt,
                        level=log_lvl)

    logging.info("Log initiated: {}".format(args.logfile))

    try:
        pass

    # On CTRL-C...
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()
