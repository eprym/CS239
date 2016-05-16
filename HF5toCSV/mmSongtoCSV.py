import logging
import os
import sys

from pyspark import SparkContext
from mmsongsdbtocsvconverter import MMSongsDbToCsvConverter

# Logger
logger = logging.getLogger('')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s (%(process)d): %(message)s',
                              '%Y-%m-%d %H:%M:%S')

# Stream handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
logger.addHandler(ch)

# File handler
cwd = os.path.dirname(os.path.realpath(__file__))
log_filename = os.path.join(cwd, 'mmsongsdb.log')
fh = logging.FileHandler(log_filename)
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)
logger.addHandler(fh)

def main():
    try:
        partitions_num = sys.argv[1]
        csv_filename = sys.argv[2]
        base_dir = sys.argv[3]
        attrs_to_save = sys.argv[4:]
    except:
        logger.error("Usage: ./mmsongsdb_to_csv.py partitions_num <csv_filename> <directory> [<attrs_to_save>]")
        sys.exit(1)
        return
    sc = SparkContext(appName="mmSongtoCSV")
    sc.addPyFile("/root/mm-songs-db-tools-master2/hdf5_getters.py")
    sc.addPyFile("/root/mm-songs-db-tools-master2/mmsongsdbtocsvconverter.py")
    converter = MMSongsDbToCsvConverter(csv_filename, attrs_to_save)

    file_list = filter(lambda s: s.endswith(".h5"), ["%s%s%s" %(root, os.sep, file)
                                                    for root, dirs, files in
                                                    os.walk(base_dir)
                                                    for file in files])
    
    file_partitions = sc.parallelize(file_list, partitions_num)
    rdd = file_partitions.map(converter._handle_h5_file)
    #print rdd.count()
    rdd.saveAsTextFile(csv_filename)
    
    
if __name__ == '__main__':
    main()
