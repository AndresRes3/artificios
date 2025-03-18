import pytest
from app.m_analyzer import contains_artifact_clue

def test_horizontal():
    manuscript = [
        "ABCDEF",
        "GHIJKL",
        "MNOPQR",
        "STUVWX",
        "AAAARF",    
        "ABCDEF"
    ]
    assert contains_artifact_clue(manuscript) == True

def test_vertical():
    manuscript = [
        "ANDRES",
        "ALEJAN",
        "ALFRED",
        "ALANAC",
        "BAAARF",    
        "ABCDEF"
    ]
    assert contains_artifact_clue(manuscript) == True

def test_diagonal_rigth():
    manuscript = [
        "ABCDEQ",
        "EABATH",
        "IRAAKL",
        "JAAAAR",  
        "RSTAAA",
        "UVWXYZ"
    ]
    assert contains_artifact_clue(manuscript) == True 

def test_diagonal_left():
    manuscript = [
        "ABCDEQ",
        "EABRTH",
        "IJKLRR",
        "MNOARR",
        "RSTARR",
        "UVWARR"  
    ]
    assert contains_artifact_clue(manuscript) == True


def test_no_manuscript():
    manuscript = [
        "ABCDEF",
        "GHIJKL",
        "MNOPQR",
        "STUVWX",
        "YZABCD",
        "EFGHIJ"
    ]
    assert contains_artifact_clue(manuscript) == False 

def test_no_input():
    assert contains_artifact_clue([]) == False

def test_small_matriz():
    manuscript = [
        "AB",
        "CD"
    ]
    assert contains_artifact_clue(manuscript) == False


def test_easy_case():
    manuscript = [
        "AAAA",  
        "BCDE",
        "FGHI",
        "JKLM"
    ]
    assert contains_artifact_clue(manuscript) == True
