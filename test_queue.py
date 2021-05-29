import pytest
from queueController import Controller

queue = Controller()

def test_queue():
    assert queue.DoIHaveItems() == True
    assert queue.DoIFull() == False
    
    for _ in range(9):
        queue.AddToQueue("TEST", "TEST")
    
    assert queue.DoIHaveItems() == True
    assert queue.DoIFull() == True
