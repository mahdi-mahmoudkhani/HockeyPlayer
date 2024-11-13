finalState = aStarSearch(object)
    print("A* Search answer:\nsteps: {}\ntotal_cost: {}\ntotal_depth: {}".format(
        reconstruct_path(finalState)[:50], finalState.cost, finalState.depth))
    print("\n-----------------------------\n")