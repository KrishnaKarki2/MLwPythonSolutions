def player(prev_play, opponent_history=[], play_order={}):

    if not prev_play:
        opponent_history.clear()
        play_order.clear()

    if prev_play:
        opponent_history.append(prev_play)

        for i in range(1, 7):
            if len(opponent_history) >= i:
                seq = "".join(opponent_history[-i:])
                play_order[seq] = play_order.get(seq, 0) + 1

    prediction = 'S' 

    for i in range(6, 1, -1):
        if len(opponent_history) >= (i - 1):

            last_moves = "".join(opponent_history[-(i-1):])
            
            potential_plays = [
                last_moves + "R",
                last_moves + "P",
                last_moves + "S",
            ]
            
            sub_order = {
                k: play_order[k]
                for k in potential_plays if k in play_order
            }
            
            if sub_order:

                prediction = max(sub_order, key=sub_order.get)[-1:]
                break 

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    
    return ideal_response[prediction]