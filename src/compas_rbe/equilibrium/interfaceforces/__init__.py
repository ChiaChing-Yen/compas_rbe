from __future__ import absolute_import, division, print_function

from .interfaceforces_cvx import *
from .interfaceforces_cvxopt import *


def compute_iforces_xfunc(data, backend='cvx', **kwargs):
    from compas_rbe.datastructures import Assembly
    from compas_rbe.datastructures import Block

    assembly = Assembly.from_data(data['assembly'])
    assembly.blocks = {int(key): Block.from_data(data['blocks'][key]) for key in data['blocks']}

    if backend == 'cvx':
        compute_iforces_cvx(assembly, **kwargs)

    if backend == 'cvxopt':
        compute_iforces_cvxopt(assembly, **kwargs)

    return {
        'assembly': assembly.to_data(),
        'blocks': {str(key): assembly.blocks[key].to_data() for key in assembly.blocks}
    }


__all__ = [name for name in dir() if not name.startswith('_')]
