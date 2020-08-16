from xchk_core.contentviews import ContentView
from xchk_core.strats import *

# iets over hub?
# iets over play with docker?
# https://www.docker.com/resources/what-container

class DockerRunIntroView(ContentView):
     
    uid = 'docker_run_intro_1'
    template = 'xchk_docker_content/docker_run_intro.html'
    title = 'Je eerste container opstarten: docker run'
    strat = Strategy(refusing_check=TrueCheck(),
                     accepting_check=Negation(TrueCheck()))


class ContainersVSVMsView(ContentView):
     
    uid = 'containers_vs_vms_1'
    template = 'xchk_docker_content/containers_vs_vms.html'
    title = 'Containers vergeleken met virtuele machines'
    strat = Strategy(refusing_check=TrueCheck(),
                     accepting_check=Negation(TrueCheck()))

class WhatAreApplicationContainersView(ContentView):
     
    uid = 'what_are_application_containers_1'
    template = 'xchk_docker_content/what_are_application_containers.html'
    title = 'Wat zijn applicatiecontainers?'
    strat = Strategy(refusing_check=TrueCheck(),
                     accepting_check=Negation(TrueCheck()))

class WhatIsDockerView(ContentView):
     
    uid = 'what_is_docker_1'
    template = 'xchk_docker_content/what_is_docker.html'
    title = 'Wat is Docker?'
    strat = Strategy(refusing_check=Negation(TrueCheck()),
                     accepting_check=TrueCheck())

class DockerDesktopInstallationView(ContentView):
     
    uid = 'docker_desktop_installation_1'
    template = 'xchk_docker_content/docker_desktop_installation.html'
    title = 'Docker Desktop installeren'
    # TODO: testen dat installatie gelukt is via bv. `docker --version`,...
    strat = Strategy(refusing_check=TrueCheck(),
                     accepting_check=Negation(TrueCheck()))
