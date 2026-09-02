from common.paths import get_data_path

data_file = get_data_path("0054_poker.txt")
with data_file.open(encoding="utf-8") as file:
    hands = [line.split() for line in file if line.strip()]

hand_types = { "High": 0, "One": 1, "Two": 2, "Three": 3,
                "Straight": 4, "Flush": 5, "Full": 6,
                 "Four": 7, "SFlush": 8, "RFlush": 9 }
suites_dict = { 'H':0, 'C':1, 'S':2, 'D':3 }
values_dict = {  "T":10, "J":11, "Q":12, "K":13, "A":14 }
for d in range(2,10):
    values_dict[str(d)] = d

class Hand:
    def __init__(self, cards: list):
        self.cards = cards
        self.card_tuples = [Hand.card_to_tuple(card) for card in cards]
        self.vset = dict()
        self.sset = dict()
        self.process_card_tuples()

    @staticmethod
    def card_to_tuple(card):
        s = suites_dict[card[-1]]
        v = values_dict[card[0:len(card)-1]]
        return [v,s]

    def process_card_tuples(self):
        for i, ctuple in enumerate(self.card_tuples):
            if ctuple[0] not in self.vset:
                self.vset[ctuple[0]] = []
            self.vset[ctuple[0]].append(i)
            if ctuple[1] not in self.sset:
                self.sset[ctuple[1]] = []
            self.sset[ctuple[1]].append(i)

    def is_royal_flush(self):
        _is_straight_flush, _ = self.is_straight_flush()
        return _is_straight_flush and min(self.vset.keys()) == 10, []

    def is_straight_flush(self):
        _is_flush, _ = self.is_flush()
        _is_straight, _ = self.is_straight()
        return _is_flush and _is_straight, [max(self.vset.keys())]

    def is_flush(self):
        if len(self.sset) == 1:
            return True, sorted(self.vset.keys(), reverse = True)
        return False, []

    def is_straight(self):
        if len(self.vset) == 5:
            vlist = sorted(self.vset.keys())
            for i in range(4):
                if vlist[i+1]-vlist[i] != 1:
                    return False, []
            return True, [max(self.vset.keys())]
        return False, []

    def is_full_house(self):
        if len(self.vset) == 2:
            vlist = sorted([len(v) for v in self.vset.values()])
            if vlist[0] == 2 and vlist[1] == 3:
                lst = [0, 0]
                for k, v in self.vset.items():
                    if len(v) == 2:
                        lst[1] = k
                    else:
                        lst[0] = k
                return True, lst
        return False, []

    def is_four_kind(self):
        if len(self.vset) == 2:
            vlist = sorted([len(v) for v in self.vset.values()])
            if vlist[0] == 1 and vlist[1] == 4:
                lst = [0, 0]
                for k, v in self.vset.items():
                    if len(v) == 1:
                        lst[1] = k
                    else:
                        lst[0] = k
                return True, lst
        return False, []

    def is_three_kind(self):
        if len(self.vset) == 3:
            if max([len(v) for v in self.vset.values()]) == 3:
                lst = []
                tk = -1
                for k,v in self.vset.items():
                    if len(v) == 1:
                        lst.append(k)
                    else:
                        tk = k
                lst.sort(reverse=True)
                lst.insert(0, tk)
                return True, lst
        return False, []

    def is_two_pair(self):
        if len(self.vset) == 3:
            if max([len(v) for v in self.vset.values()]) == 2:
                lst = []
                tk = -1
                for k,v in self.vset.items():
                    if len(v) == 2:
                        lst.append(k)
                    else:
                        tk = k
                lst.sort(reverse=True)
                lst.append(tk)
                return True, lst
        return False, []

    def is_one_pair(self):
        if len(self.vset) == 4:
            if max([len(v) for v in self.vset.values()]) == 2:
                lst = []
                tk = -1
                for k,v in self.vset.items():
                    if len(v) == 1:
                        lst.append(k)
                    else:
                        tk = k
                lst.sort(reverse=True)
                lst.insert(0, tk)
                return True, lst
        return False, []

    def is_high_card(self):
        return True, sorted(self.vset.keys(), reverse=True)

    def get_hand_type(self):
        flag, lst = self.is_royal_flush()
        if flag:
            return [9] + lst
        flag, lst = self.is_straight_flush()
        if flag:
            return [8] + lst
        flag, lst = self.is_four_kind()
        if flag:
            return [7] + lst
        flag, lst = self.is_full_house()
        if flag:
            return [6] + lst
        flag, lst = self.is_flush()
        if flag:
            return [5] + lst
        flag, lst = self.is_straight()
        if flag:
            return [4] + lst
        flag, lst = self.is_three_kind()
        if flag:
            return [3] + lst
        flag, lst = self.is_two_pair()
        if flag:
            return [2] + lst
        flag, lst = self.is_one_pair()
        if flag:
            return [1] + lst
        flag, lst = self.is_high_card()
        return [0] + lst

cnt = 0
for hand in hands:
    p1 = Hand(hand[0:5])
    p2 = Hand(hand[5:])

    p1_type = p1.get_hand_type()
    p2_type = p2.get_hand_type()

    p1_wins = False
    for x,y in zip(p1_type, p2_type):
        if x == y:
            continue
        p1_wins = x > y
        break       
    if p1_wins:
        cnt += 1

print(cnt) 