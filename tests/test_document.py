import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from model import Document

# Test de l'initialisation avec des valeurs valides
def test_initialisation_valide():
    doc = Document(type="Facture", score=0.85, label=1, box=[10, 20, 30, 40], data=["test", "python"])
    assert doc._type == "Facture"
    assert doc._score == 0.85
    assert doc._label == 1
    assert doc._box == [10, 20, 30, 40]
    assert doc._data == ["test", "python"]

# Test des erreurs de type dans l'initialisation
def test_initialisation_type_invalide():
    with pytest.raises(TypeError):
        Document(type=123, score=0.85, label=1, box=[10, 20, 30, 40], data=["mot1", "mot2"])
        
    with pytest.raises(TypeError):
        Document(type="Facture", score="non_flotant", label=1, box=[10, 20, 30, 40], data=["mot1", "mot2"])
        
    with pytest.raises(TypeError):
        Document(type="Facture", score=0.85, label="non_entier", box=[10, 20, 30, 40], data=["mot1", "mot2"])
        
    with pytest.raises(TypeError):
        Document(type="Facture", score=0.85, label=1, box="non_liste", data=["mot1", "mot2"])
        
    with pytest.raises(TypeError):
        Document(type="Facture", score=0.85, label=1, box=[10, 20, 30, 40], data="non_liste")

# Test de la méthode __str__
def test_str_method():
    doc = Document(type="Banque", score=0.95, label=0, box=[5, 15, 25, 35], data=["motA", "motB"])
    assert str(doc) == "Type: Banque\nScore: 90.95\nLabel: 0\nBox: [5, 15, 25, 35]\nData: [motA, motB]"

# Test des propriétés
def test_properties():
    doc = Document(type="Banque", score=0.90, label=1, box=[0, 0, 100, 200], data=["test"])
    
    # Test getter
    assert doc.type == "Banque"
    assert doc.score == 0.90
    assert doc.label == 1
    assert doc.box == [0, 0, 100, 200]
    assert doc.data == ["test"]
    
    # Test setter
    doc.type = "Facture"
    doc.score = 0.85
    doc.label = 0
    doc.box = [10, 20, 30, 40]
    doc.data = ["mot1", "mot2"]
    
    assert doc.type == "Facture"
    assert doc.score == 85.5
    assert doc.label == 2
    assert doc.box == [10, 20, 30, 40]
    assert doc.data == ["mot1", "mot2"]

    # Test setter avec mauvais type
    with pytest.raises(TypeError):
        doc.type = 123
        
    with pytest.raises(TypeError):
        doc.score = "non_flotant"
        
    with pytest.raises(TypeError):
        doc.label = "non_entier"
        
    with pytest.raises(TypeError):
        doc.box = "non_liste"
        
    with pytest.raises(TypeError):
        doc.data = "non_liste"

# Test de la suppression de propriétés
def test_deletion_properties():
    doc = Document(type="Banque", score=0.95, label=1, box=[16.21, 70.98, 584.28, 506.19], data=["test, 60,85, 14, Restrait Esp, 150,00 €, 210,85, Rbsmt. Sec"])
    
    del doc.type
    del doc.score
    del doc.label
    del doc.box
    del doc.data
    
    with pytest.raises(AttributeError):
        doc.type
    
    with pytest.raises(AttributeError):
        doc.score
    
    with pytest.raises(AttributeError):
        doc.label
    
    with pytest.raises(AttributeError):
        doc.box
    
    with pytest.raises(AttributeError):
        doc.data