from paver.tasks import task, BuildFailure, needs
from paver.easy import sh

''' paver allows to define a global built '''

@task
def unit_tests():
    sh('nosetests --rednose --with-coverage -v tests/unit')
    
@task
def acceptance_tests():
    sh('lettuce tests/bdd')
    
@task
def run_pylint():
    try:
        sh('pylint --msg-template= "{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" peakfinderalgorithms > pylint.txt')
    except BuildFailure:
        pass

@needs('unit_tests','acceptance_tests','run_pylint')
@task
def default():
    pass