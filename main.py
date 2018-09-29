"""
# 
# 05/09/2018
# Oladotun Rominiyi - Copyright © 2018. all rights reserved.
"""
__author__ = 'dotun rominiyi'

# IMPORTS
import argparse
from cosine.core.algo import CosineAlgo


def main():
    parser = argparse.ArgumentParser(description='Cosine Algo')
    parser.add_argument("-c", "--config",
                        help="Config YAML file required to setup the algo.")
    parser.add_argument("-e", "--env", choices=['DEV', 'TST', 'PRD'],
                        help="The execution environment.")
    parser.add_argument("-a", "--appname", default='Cosine Algo',
                        help="The name of the application.")
    parser.add_argument("-lf", "--logfile",
                        help="The name of the log file. Do not change this unless you know what you're doing.")
    parser.add_argument("-lv", "--loglevel",
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'FATAL', 'CRITICAL'],
                        help="Log level.")
    parser.add_argument("-nl", "--nologfile",
                        const=True, default=False, nargs='?',
                        help="Disable log file generation.")

    parser.print_help()
    args = parser.parse_args()

    # filter out None value fields...
    args = args.__class__(**({arg: args.__dict__[arg] for arg in args.__dict__ if args.__dict__[arg] is not None}))

    app = CosineAlgo(cmdline_args=args.__dict__)
    app.run()


if __name__ == "__main__":
    main()