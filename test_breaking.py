
from e5utils import LockBox, CaerfilyDesinedSurvis
from breaking import break_lockbox, break_facade


def test_break_lockbox():
    password = 'opensesame'
    contents = 'TODO: (1) take over the world'
    lockbox = LockBox(password, contents)

    found_password, found_contents = break_lockbox(lockbox)
    
    assert found_password == password
    assert found_contents == contents


def test_break_facade():
    service = CaerfilyDesinedSurvis('potatocakes')
    facade = service.create_facade()
    
    takeover = break_facade(facade)
    
    assert takeover == 'Taking over!'
