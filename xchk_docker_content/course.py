from xchk_core import contentviews as basecv
from xchk_core.courses import Course
from .contentviews import *

course = Course('docker',
                'Docker',
                [(WhatIsDockerView,[])],
                "git@github.com:v-nys/docker-modeloplossingen.git")