# flake8: noqa

import pkg_resources
import os.path as osp


__version__ = pkg_resources.get_distribution('viewer-3d').version


viewer_3d_executable = osp.join(
    osp.abspath(osp.dirname(__file__)), 'viewer_3d')
