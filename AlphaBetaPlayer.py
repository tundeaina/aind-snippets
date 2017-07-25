import random

class SearchTimeout(Exception):
    pass

class AlphaBetaPlayer(IsolationPlayer):

    def get_move(self, game, time_left):

        self.time_left = time_left

        best_move = (-1, -1)
        
        depth = 1
        while True:
        
            try:
                best_move = self.alphabeta(game, depth)
            except SearchTimeout:
                break
           
            depth += 1
            
            if depth >= 2147483648:
                break
            
        return best_move

        
    def max_value(self, game, depth, alpha, beta):
        
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
            
        if depth == 0:
            return self.score(game, self)
        
        value = float("-inf")
        
        legal_moves = game.get_legal_moves()
        
        for move in legal_moves:
            score = self.min_value(game.forecast_move(move), depth-1, alpha, beta)
            value = max(value, score)
            
            if value >= beta:
                return value
            
            alpha = max(alpha, value)
         
        return value 
    
    
    def min_value(self, game, depth, alpha, beta):
        
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
            
        if depth == 0:
            return self.score(game, self)
        
        value = float("inf")
        
        legal_moves = game.get_legal_moves()
        
        for move in legal_moves:
            score = self.max_value(game.forecast_move(move), depth-1, alpha, beta)
            value = min(value, score)
            
            if value <= alpha:
                return value
            
            beta = min(beta, value)
         
        return value        
        
    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        best_move = (-1,-1)
            
        legal_moves = game.get_legal_moves()
        
        if not legal_moves:
            return best_move
        
        value = float("-inf") 
        
        for move in legal_moves:
            score = self.max_value(game.forecast_move(move), depth, alpha, beta)
            
            if score >= value:
                best_move = move
                value = score
            
            alpha = max(alpha, value)
        
        return best_move
