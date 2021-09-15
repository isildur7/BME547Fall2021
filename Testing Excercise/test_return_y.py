import pytest

@pytest.mark.parametrize("points, x_coord, expected", [
    ([(0,1),(1,0)], 2, -1),
    ([(0,0),(1,1)], 2, 2),
    ([(1,3),(2,6)], 3, 9),
    ([(0,-1),(2,0)], 4, 1)])
def test_return_y(points, x_coord, expected):
    from return_y import return_y
    answer = return_y(points, x_coord)
    assert answer == expected
