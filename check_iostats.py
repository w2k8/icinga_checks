#/usr/bin/python3
__author__ = "w2k8"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "w2k8"

import subprocess
import sys

def runcommand():
    try:
        out_bytes = subprocess.check_output(['iostat', '-x' ,'-d' ,'-k' ])
        out_text = out_bytes.decode("utf-8")
        return(out_text)
    except subprocess.CalledProcessError as e:
        print('Error: {} - {}'.format(e.returncode, e.output))
        sys.exit(1)

def generate_output(data):
    for line in data.split('\n'):
        if line != '' and not line.startswith('Linux') and not line.startswith('Device'):
            stats=line.split()
        if line.startswith('Device'):
            device=line.split()
        try:
            zip_list = zip(device,stats)
            if not len(line) == 0:
                for item in zip_list:
                    if not str(item[0]).startswith('Device') and not str(zip_list[0][1]).startswith('loop'):
                        print('iostat|{}-{}={}'.format(str(zip_list[0][1]), str(item[0]), str(item[1])))
        except:
            pass
    return(data)

if __name__ == "__main__":
    result = generate_output(runcommand())
    sys.exit(0)