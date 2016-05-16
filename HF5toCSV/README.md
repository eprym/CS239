# mm-songs-db-tools
Million Songs DB Tools

Tools based on the Million Songs DB: [http://labrosa.ee.columbia.edu/millionsong/](http://labrosa.ee.columbia.edu/millionsong/)

## Usage:

### MMSongsDbToCsvConverter

Helper object for reading hdf5 files and writing the results to a csv

Sample usage:

    from mmsongsdbtools.mmsongsdbtocsvconverter import MMSongsDbToCsvConverter
    converter = MMSongsDbToCsvConverter('mmsongsdb.csv', ['artist_name', 'tempo'])
    converter.convert_directory('.')

The second parameter for the constructor of `MMSongsDbToCsvConverter` is an optional list of attributes to fetch for your csv. Available options are listed here:

[http://labrosa.ee.columbia.edu/millionsong/pages/example-track-description](http://labrosa.ee.columbia.edu/millionsong/pages/example-track-description)

Helper command line script: `mmsongsdb_to_csv.py`.

Sample usage:

    $ ./mmsongsdb_to_csv.py <csv_filename> <directory> [<attr_to_save> <attr_to_save> ...]

Parameters:

- `<csv_filename>` the filename of the output csv file
- `<directory>` the name of the directory that has the `.h5` files in it
- `<attr_to_save>` optional attributes to save in the csv file (if not specified, all attributes will be used)

Example:

    $ ./mmsongsdb_to_csv.py /path/to/file.csv /path/to/input/directory artist_name title tempo

Will create the file `/path/to/file.csv` that has data like this:

    artist_name,title,tempo
    Sticky Fingaz,Oh My God,80.149000000000001
    Dame Joan Sutherland / New Philharmonia Orchestra / Richard Bonynge,Joy To The World,82.421999999999997
    The Jeff Healey Band,Hoochie Coochie Man,107.197
    Angela Dimitriou,Ftei O Erotas,124.17700000000001
    Danny Wilson,The Second Summer Of Love,196.03399999999999
    Lionel Rogg,Prelude And Fugue In C Major BWV 531 : Fugue,64.400999999999996
    Java,Don't Phunk With My Heart,130.86099999999999
    SWAMI featuring Asuivre,Give It What U Got,90.007999999999996
    The Black Velvet Band,Dancing To A Standstill,122.17400000000001
    Lisa Lynne,Isla del Luna,95.980999999999995
    Pe'z,Spirit,75.954999999999998
    Shawn Colvin,Another Long One,210.87100000000001
    Stephy Tang,Leng Jing,105.196


## Requirements:

- [pytables](http://pytables.github.io/)


## Resources:

- http://labrosa.ee.columbia.edu/millionsong/
- https://github.com/tbertinmahieux/MSongsDB/tree/master/PythonSrc
    - hdf5\_getters.py is a direct copy straight from [https://github.com/tbertinmahieux/MSongsDB/blob/408393766dfa449da90faaf8a65aed9cc420849a/PythonSrc/hdf5_getters.py](https://github.com/tbertinmahieux/MSongsDB/blob/408393766dfa449da90faaf8a65aed9cc420849a/PythonSrc/hdf5_getters.py)
