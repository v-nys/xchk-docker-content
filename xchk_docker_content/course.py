from xchk_core import contentviews as basecv
from xchk_core.courses import Course
from .contentviews import *

course = Course('docker',
                'Docker',
                [(DockerRunIntroView,[DockerDesktopInstallationView]),
                 (DockerDesktopInstallationView,[WhatIsDockerView]),
                 (ContainersVSVMsView,[WhatIsDockerView]),
                 (WhatIsDockerView,[WhatAreApplicationContainersView]),
                 (WhatAreApplicationContainersView,[])])
