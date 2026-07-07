class Solution:
  def getRow(self, rowIndex):
    row = [1]
    for i in range(1, rowIndex + 1):
      val = row[-1] * (rowIndex - i + 1) // i
      row.append(val)
    return row