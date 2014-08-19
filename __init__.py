# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .imap import *

def register():
    Pool.register(
        IMAPServer,
        module='electronic_mail_model', type_='model')
