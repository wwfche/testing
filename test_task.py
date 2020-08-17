from .task import Triangle

def test_task_fail():
    trig = Triangle(0,0,0,0,3,3)
    res = trig.exist()
    assert res!=0, 'треугольника не существует'

def test_task_pass_1():
    trig = Triangle(0,0,3,0,3,3)
    res = trig.exist()
    assert res!=0, 'треугольника не существует'

def test_task_pass_2():
    trig = Triangle(-1,0,6,0,3,3)
    res = trig.exist()
    assert res!=0, 'треугольника не существует'