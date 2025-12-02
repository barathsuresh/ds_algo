from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        Problem: Encodes a list of strings to a single string.

        Example:
        Input: ["lint","code","love","you"]
        Output: "lint:code:love:you" (Format depends on implementation)
        """
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        """
        Problem: Decodes a single string to a list of strings.

        Example:
        Input: "lint:code:love:you"
        Output: ["lint","code","love","you"]
        """
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            i = j + 1
            end = i + length
            res.append(s[i:end])
            i = end
        return res


# --- Test Runner ---
if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ["lint", "code", "love", "you"],
        ["we", "say", ":", "yes"],
        [""],  # Single empty string
        [],  # Empty list
    ]

    for i, original_input in enumerate(test_cases):
        encoded = solver.encode(original_input)
        decoded = solver.decode(encoded)

        print(f"Test Case {i+1}:")
        print(f"  Input: {original_input}")
        print(f"  Encoded (Internal): {encoded}")
        print(f"  Output: {decoded}")
        print(f"  Expected: {original_input}")
        print("-" * 30)
