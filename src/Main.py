'''
Created on 4 juni 2018

@author: arvidbjurklint
'''
import GameModel
import View

def main():
    view = View()
    gameModel = GameModel()
    gameModel.view = view

if __name__ == '__main__':
    main()