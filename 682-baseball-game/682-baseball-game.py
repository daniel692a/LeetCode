class Solution:
    def calPoints(self, ops: List[str]) -> int:
        new_records = []
        for value in ops:
            if value == "C":
                new_records.pop()
            elif value == "D":
                new_records.append(new_records[len(new_records)-1]*2)
            elif value == "+":
                new_records.append(new_records[len(new_records)-1]+new_records[len(new_records)-2])
            else:
                new_records.append(int(value))
        return sum(new_records)