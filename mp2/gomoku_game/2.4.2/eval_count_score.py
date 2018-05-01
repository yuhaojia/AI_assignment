from eval_train_getwbs import eval_getwbs

def eval_count(board, ident):
    oppo = 3 - ident
    mywbs = eval_getwbs(board, ident)
    oppowbs = eval_getwbs(board, oppo)
    mywbs_bool = True
    oppowbs_bool = True
    grids = board.grids
    score = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count0 = 0
    opp_4 = 0
    opp_3 = 0
        
    if not mywbs:
        mywbs_bool = False
    if mywbs_bool:
        # mwb_helper = []
        # score = 0
        for mwb in mywbs:
            mwb_v = []
            for g in mwb:
                v = grids[g[0]][g[1]]
                mwb_v.append(v)
                count = mwb_v.count(ident)
                if count == 5:
                    score = score + 10000000
                    count5 += 1
                elif count == 4:
                    count4 += 1
                    score = score + 100000
                elif count == 3:
                    count3 += 1
                    score = score + 1000
                elif count == 2:
                    count2 += 1
                    score = score + 100
                elif count == 1:
                    count1 += 1
                    score = score + 10
                elif count == 0:
                    count0 += 1
                    score = score + 1
    if not oppowbs:
        oppowbs_bool = False
    if oppowbs_bool:
            for owb in oppowbs:
                owb_v = []
                for g in owb:
                    v = grids[g[0]][g[1]]
                    owb_v.append(v)
                count = owb_v.count(oppo)
                if count == 4:
                    opp_4 += 1
                    score = score - 1000000
                elif count == 3:
                    opp_3 += 1
                    score = score - 10000
    '''if count5 > 0 or count4 > 1:
        score = 10000000
    '''
    count_arr = [count5, count4, count3, count2, count1, count0, opp_4, opp_3]
    return count_arr, score

