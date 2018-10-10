"""
# 
# 05/09/2018
# Oladotun Rominiyi - Copyright © 2018. all rights reserved.
"""
__author__ = 'dotun rominiyi'

# IMPORTS
from cosine.core.args import CosineCmdLineArgs
from cosine.core.algo import CosineAlgo


def main():
    args = CosineCmdLineArgs(appdesc='Cosine Algo')

    args.print_help()
    args.parse()

    app = CosineAlgo(cmdline_args=args.asdict())
    app.run()


if __name__ == "__main__":
    main()