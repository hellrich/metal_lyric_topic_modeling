for x in ~/tmp/lyrics/www.darklyrics.com/lyrics/* ; do echo -n "$(basename $x) "; ( for y in $x/*; do grep "<title>.*</title>" $y | sed -n "s/.*(\([0-9][0-9][0-9][0-9]\)).*/\1/p"; done ) | sort | head -n 1 ; done > firstYearPerBand