class Solution:
    def isValid(self, s: str) -> bool:
        open = s.count("(")
        closed = s.count(")")
        if open != closed: return False
        open = s.count("[")
        closed = s.count("]")
        if open != closed: return False
        open = s.count("{")
        closed = s.count("}")
        if open != closed: return False

        stack = []
        closed = [')', ']', '}']
        opened = ['(', '[', '{']
        for ch in s:
            if ch not in closed and ch not in opened: continue
            if ch in opened: 
                stack.append(ch)
                continue
            if len(stack) == 0: return False #closed par but there is no open par

            #le parentesi più piccole possono venire prima di quelle più grandi
            if closed.index(ch) <= opened.index(stack[-1]):
                stack.pop(-1)
            else: return False
        return True

            


        return True

        
