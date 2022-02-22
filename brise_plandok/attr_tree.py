# import json
import pyparsing
from collections import defaultdict
from pyparsing import nestedExpr
import logging

ALL_STRINGS = set()


class AttrTree(list):
    @staticmethod
    def from_string(raw_string):
        ALL_STRINGS.clear()
        t_string = raw_string.replace("*", "").replace(",", " ").replace("''", "")
        if not t_string:
            return AttrTree.from_list([])
        try:
            t_list = nestedExpr("(", ")").parseString(t_string).asList()
        except pyparsing.ParseException:
            print("pyparsing exception caused by:", raw_string, t_string)
            print("returning empty")
            return AttrTree.from_list([])
        return AttrTree.from_list(t_list)

    @staticmethod
    def from_list(t_list):
        # print('construncting from this list:', t_list)
        if isinstance(t_list, str):
            # print(f'ALL STRINGS: {ALL_STRINGS}')
            if t_list in ALL_STRINGS:
                s = t_list + "_"
            else:
                s = t_list
            ALL_STRINGS.add(s)
            return s
        else:
            return AttrTree(AttrTree.from_list(elem) for elem in t_list)

    def gen_attr_dfs(self):
        for elem in self:
            if isinstance(elem, str):
                yield elem
            else:
                yield from elem.gen_attr_dfs()

    def count_attr_dists(self):
        if self.d:
            return
        strings, strees = [], []
        self_dist = {}
        for selem in self:
            if isinstance(selem, str):
                strings.append(selem)
            else:
                strees.append(selem)
                selem.count_attr_dists()
                self.d.update(selem.d)
                self_dist.update(
                    {
                        attr: min(self_dist.get(attr, float("inf")), val + 1)
                        for attr, val in selem.d["self"].items()
                    }
                )
        self.d["self"] = self_dist

        for s in strings:
            for attr, dist in self.d["self"].items():
                self.d[attr][s] = dist + 1
                self.d[s][attr] = dist + 1

            self.d["self"][s] = 1
            for s2 in strings:
                if s != s2:
                    self.d[s][s2] = 1
                    self.d[s2][s] = 1

        for attr, dist in self.d["self"].items():
            for attr2, dist2 in self.d["self"].items():
                # print('checking:', attr, attr2)
                if attr == attr2 or attr2 in self.d[attr]:
                    continue
                logging.debug("new_path:", attr, attr2)
                self.d[attr][attr2] = dist + dist2
                self.d[attr2][attr] = dist + dist2

        # print('counted, d:')
        # print(json.dumps(self.d))

    def __init__(self, seq):
        super(AttrTree, self).__init__(seq)
        self.d = defaultdict(dict)
