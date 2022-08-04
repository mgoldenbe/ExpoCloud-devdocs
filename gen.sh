#!/usr/bin/sh
sphinx-apidoc -f -M -P -o source ..
make html
