from hello import main

def test_output(capfd):
    main()
    out, _ = capfd.readouterr()
    assert "Hello, world!" in out
