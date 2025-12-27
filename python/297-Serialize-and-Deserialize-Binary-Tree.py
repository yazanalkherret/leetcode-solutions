# Unreadable and messy but it works

class Codec:

    def serialize(self, root):
        res = []
        def serialize_helper(curr):
            if not curr:
                res.append('_')
                return
            
            isNegative = False
            val = curr.val
            s = ''
            if val < 0:
                val *= -1
                isNegative = True

            val = str(val)
            digits = len(val)

            if isNegative: digits += 4

            res.append(str(digits) + val)

            serialize_helper(curr.left)
            serialize_helper(curr.right)

        serialize_helper(root)
        return "".join(res)

    def deserialize(self, data):
        end = 0
        def deserialize_helper(i):
            nonlocal end
            if data[i] == '_':
                end += 1 
                return


            x = int(data[i]) % 4 if (int(data[i]) % 4 != 0) else 4
            start, end = i + 1, max(end, i + x + 1)
            #print(data[start : end])
            num = int(data[start : end])
            if int(data[i]) > 4: num *= -1

            curr = TreeNode(num)
            curr.left = deserialize_helper(end)
            curr.right = deserialize_helper(end)

            return curr
        return deserialize_helper(0)