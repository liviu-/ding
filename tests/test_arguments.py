from subprocess import Popen, PIPE


TOOL = 'ding'

def run_tool(args=[]):
    p = Popen([TOOL] + args, stdout=PIPE, stderr=PIPE)
    stdout, stderr = (out.decode('utf-8') for out in p.communicate())
    return p, stdout, stderr

def test_tool_no_arguments():
    p, stdout, stderr = run_tool()
    assert p.returncode == 1
    assert stderr
    assert not stdout

def test_tool_insufficient_arguments_in():
    p, stdout, stderr = run_tool(['in'])
    assert p.returncode == 1
    assert stderr
    assert not stdout

def test_tool_insufficient_arguments_at():
    p, stdout, stderr = run_tool(['at'])
    assert p.returncode == 1
    assert stderr
    assert not stdout

def test_tool_in_wrong_suffix():
    p, stdout, stderr = run_tool(['in 1x'])
    assert p.returncode == 1
    assert stderr
    assert not stdout

def test_tool_in_partly_wrong_suffix():
    p, stdout, stderr = run_tool(['in 1s 1x'])
    assert p.returncode == 1
    assert stderr
    assert not stdout

def test_tool_at_invalid_separator():
    p, stdout, stderr = run_tool(['at 15 30'])
    assert p.returncode == 1
    assert stderr
    assert not stdout

def test_tool_at_invalid_hour():
    p, stdout, stderr = run_tool(['at 25'])
    assert p.returncode == 1
    assert stderr
    assert not stdout

def test_tool_at_invalid_minute():
    p, stdout, stderr = run_tool(['at 22:71'])
    assert p.returncode == 1
    assert stderr
    assert not stdout
