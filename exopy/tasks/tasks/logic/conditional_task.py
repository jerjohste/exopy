# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright 2015-2018 by Exopy Authors, see AUTHORS for more details.
#
# Distributed under the terms of the BSD license.
#
# The full license is in the file LICENCE, distributed with this software.
# -----------------------------------------------------------------------------
"""Task equivalent to an if statement.

"""
from atom.api import (Unicode, set_default)

from ..validators import Feval
from ..base_tasks import ComplexTask


class ConditionalTask(ComplexTask):
    """Task calling its children only if a given condition is met.

    """
    #: Condition to meet in order to perform the children tasks.
    condition = Unicode().tag(pref=True, feval=Feval())
    
    database_entries = set_default({'condition': False})

    def perform(self):
        """Call the children task if the condition evaluate to True.

        """
        
        self.write_in_database('condition', self.format_and_eval_string(self.condition))
        
        if self.format_and_eval_string(self.condition):
            for child in self.children:
                child.perform_()
