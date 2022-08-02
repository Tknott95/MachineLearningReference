#!/bin/bash

_fileLoc=$1
_fileOut=$2

ffmpeg -framerate 10 -pattern_type glob -i "$fileLoc/*.png"   -c:v libx264 -r 30 -pix_fmt yuv420p $_fileOut
