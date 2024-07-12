from src.decorators import log

def test_decorators(capsys):
    @log
    captured = capsys.readouterr()
    assert captured.out == ''

