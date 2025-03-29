def get_results(session):
    return session.results[["FullName", "TeamName", "Position"]]
