from xchk_core.contentviews import ContentView
from xchk_core.strats import *

class WhatIsDockerView(ContentView):
     
    uid = 'what_is_docker'
    template = 'xchk_docker_content/what_is_docker.html'
    strat = Strategy(refusing_check=TrueCheck()),
                     accepting_check=Negation(TrueCheck()))
