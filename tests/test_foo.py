from pyramid_flower.foo import foo


def test_foo():
    assert foo("foo") == "foo"
