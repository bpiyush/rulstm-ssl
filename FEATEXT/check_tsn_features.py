import lmdb

if __name__ == "__main__":
    import ipdb; ipdb.set_trace()
    path_to_lmdb = "../RULSTM/data/ek100/rgb/"
    env = lmdb.open(path_to_lmdb, readonly=True, lock=False)
    import ipdb; ipdb.set_trace()