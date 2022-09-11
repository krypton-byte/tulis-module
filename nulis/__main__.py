import argparse
from . import tulis
cmd = argparse.ArgumentParser(prog='nulis')
cmd.add_argument('--worker', type=str, default='5')
cmd.add_argument('--name', type=str, required=True, help='filename result')
src = cmd.add_argument_group('Source')
text = src.add_mutually_exclusive_group(required=True)
text.add_argument('--text', type=str)
text.add_argument('--file', type=argparse.FileType('r'))
parser = cmd.parse_args()
for n, i in enumerate(tulis(parser.text if parser.text else parser.file.read(), parser.worker if parser.worker == 'auto' else int(parser.worker))):
    i.save(parser.name + '.'+n.__str__()+'.jpg')
    print('filename: '+parser.name + '.'+n.__str__()+'.jpg')