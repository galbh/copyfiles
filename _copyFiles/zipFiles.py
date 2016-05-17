import os
import zipfile


def compress_to_zip(src, dst, file_name):

    zf = zipfile.ZipFile(file_name+".tar", "w", zipfile.ZIP_DEFLATED)
    abs_src = os.path.abspath(src)

    for dirname, subdirs, files in os.walk(src):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1:]
            print(arcname)
            # print 'zipping %s as %s' % (os.path.join(dirname, filename),
            #                             arcname)
            zf.write(absname, arcname)
    zf.close()

