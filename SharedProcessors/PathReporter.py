#!/usr/bin/python
#
# Copyright 2019 Mario Panighetti
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Reports environment paths for current process context."""

import os
import sys

from autopkglib import Processor


__all__ = ["PathReporter"]


class PathReporter(Processor):
    """Reports environment paths for current process context. This processor is for troubleshooting purposes only and should not be used by anyone."""
    input_variables = {
    }
    output_variables = {
        "path_report": {
            "description": "Contents of $PATH."
        }
    }
    description = __doc__


    def main(self):
        # clear any pre-exising summary result
        if 'path_report' in self.env:
            del self.env['path_report']

        self.env['path_report'] = os.environ["PATH"]


if __name__ == '__main__':
    PROCESSOR = PathReporter()
    PROCESSOR.execute_shell()
