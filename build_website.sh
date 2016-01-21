#!/bin/bash
pandoc --from markdown_github --to html5 README --standalone -o cpmerge.html
