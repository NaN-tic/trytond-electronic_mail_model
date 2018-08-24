# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields

__all__ = ['IMAPServer']


class IMAPServer(metaclass=PoolMeta):
    __name__ = 'imap.server'

    model = fields.Many2One('ir.model', 'Model')
