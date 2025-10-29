import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import user
from main import play_game
from unittest.mock import patch


# Test avec une entrée valide
def test_user_valid_choice():
    with patch('builtins.input', side_effect=['pierre']):
        assert user() == 'pierre'

# Test avec une entrée invalide (check du message d'erreur) ensuite une entrée valide
def test_user_invalid_message(capsys):
    with patch('builtins.input', side_effect=['banane', 'pierre']):
        user()
        out = capsys.readouterr().out
        assert "Veuillez entrer un choix valide !" in out

# Test égalité
def test_egalite(capsys):
    # 3 égalités, puis une victoire pour sortir de la boucle
    with patch('builtins.input', side_effect=['pierre', 'pierre', 'pierre', 'ciseaux', 'ciseaux', 'ciseaux']), \
         patch('main.computer', side_effect=['pierre', 'pierre', 'pierre', 'feuille', 'feuille', 'feuille']):
        play_game()
        out = capsys.readouterr().out
        assert out.count("-- Match nul !") == 3

# Test Victoire
def test_victoire_joueur(capsys):
    with patch('builtins.input', side_effect=['pierre', 'pierre', 'pierre', 'ciseaux', 'ciseaux', 'ciseaux']), \
         patch('main.computer', side_effect=['ciseaux', 'ciseaux', 'ciseaux', 'feuille', 'feuille', 'feuille']):
        play_game()
        out = capsys.readouterr().out
        assert "-- Vous avez gagnez ! --" in out