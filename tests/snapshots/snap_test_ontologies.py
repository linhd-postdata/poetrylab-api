# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_join_tokens 1'] = 'Jamás , encontraré'

snapshots['test_join_syllables 1'] = 'Jamás'

snapshots['test_join_syllables_symbol 1'] = ','
