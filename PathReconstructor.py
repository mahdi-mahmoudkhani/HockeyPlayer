def reconstruct_path(state):
    path = []
    while state.parent is not None:
        path.append(state.move[0].capitalize())
        state = state.parent
    return path[::-1]