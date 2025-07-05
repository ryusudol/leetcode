class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = {}

        for product in products:
            cur = trie
            for c in product:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur['*'] = True

        ans = []
        cur = trie
        prefix = ""
        for c in searchWord:
            prefix += c
            sub_ans = []
            if cur and c in cur:
                cur = cur[c]
                self.dfs(cur, prefix, sub_ans)
            else:
                cur = None
            ans.append(sub_ans)
        return ans


    def dfs(self, node, current_word, result):
        if len(result) == 3:
            return
        if '*' in node:
            result.append(current_word)
        for char in sorted(node.keys()):
            if char == '*':
                continue
            if len(result) < 3:
                self.dfs(node[char], current_word + char, result)
            else:
                break