# ctrl+d = 해당 줄 복사, ctrl+/ = 주석처리, shift + d / = 여러줄, ctrl shift alt j = 전체변환

import os

# from IPython.display import HTML as html_print
from pyNastran.bdf.bdf import BDF, CaseControlDeck
model = BDF()

bdf_filename_out = os.path.join('sol145_OUT.bdf')
model.write_bdf(bdf_filename_out, enddata=True)
print(bdf_filename_out)

print('----------------------------------------------------------------------------------------------------')