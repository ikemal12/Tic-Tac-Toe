from functools import partial

from tic_tac_toe.logic.models import GameState, Mark, Move

def find_best_move(game_state: GameState) -> Move | None:
    maximizer: Mark = game_state.current_mark
    bound_minimax = partial(minimax, maximizer=maximizer)
    return max(game_state.possible_moves, key=bound_minimax)

def minimax( 
        move: Move, maximizer: Mark, alpha: int = float('-inf'), beta: int = float('inf'),
        choose_highest_score: bool = False
) -> int:
    if move.after_state.game_over:
        return move.after_state.evaluate_score(maximizer)
    
    if choose_highest_score:
        value = float('-inf')
        for next_move in move.after_state.possible_moves:
            value = max(value, minimax(next_move, maximizer, alpha, beta, not choose_highest_score))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for next_move in move.after_state.possible_moves:
            value = min(value, minimax(next_move, maximizer, alpha, beta, not choose_highest_score))
            beta = min(beta, value)
            if alpha >= beta:
                break  
        return value
