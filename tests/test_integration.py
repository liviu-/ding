from subprocess import Popen, PIPE

def run_tool(args):
    p = Popen(['ding'] + args, stdout=PIPE, stderr=PIPE)
    stdout, stderr = (out.decode('utf-8') for out in p.communicate())
    return p, stdout, stderr

def test_integration_in_1_second():
    run_tool(['in', '1s'])

def test_integration_with_silent():
    p, stdout, stderr = run_tool(['in', '1s', '--silent'])
    assert(stderr == '')
    assert(stdout == "\07" * 4) # these are the beeps
