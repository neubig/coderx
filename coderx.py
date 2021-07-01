import sys, os, re, shutil

def seq2seq(input_filename, output_filename):
  '''
  A highly sophisticated sequence-to-sequence model.

  :param input_filename: An input source file
  :param output_filename: An output source file
  '''
  if re.search(r'(LICENSE|COPYING)', input_filename):
    pass
  else:
    shutil.copy(input_filename, output_filename)

m = re.search(r'/([^/]*)\.git$', sys.argv[1])
if not m:
  raise ValueError('Illegal git repository name')
topname = m.group(1)
topname_coderx = f'{topname}_coderx'
os.system(f'git clone {sys.argv[1]}')
topname_regex = re.compile(f'^{topname}')
for dir_name, subdir_list, file_list in os.walk(topname):
  new_dir_name = re.sub(topname_regex, topname_coderx, dir_name)
  os.mkdir(new_dir_name)
  for f in file_list:
    seq2seq(f'{dir_name}/{f}', f'{new_dir_name}/{f}')

