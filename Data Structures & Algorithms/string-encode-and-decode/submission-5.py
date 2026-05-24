class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for c in strs:
            res.append(c)
            res.append(".")
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        res = s.split(".")
        res.pop()
        return res