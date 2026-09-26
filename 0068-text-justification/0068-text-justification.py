class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        
        while i < len(words):
            # Find words that fit in the current line
            line_len = len(words[i])
            last = i + 1
            while last < len(words) and line_len + 1 + len(words[last]) <= maxWidth:
                line_len += 1 + len(words[last])
                last += 1
                
            # Build the line
            line = []
            num_words = last - i
            num_spaces = maxWidth - (line_len - (num_words - 1)) # total spaces to distribute
            
            # If last line or line has only one word, left-justify
            if last == len(words) or num_words == 1:
                for k in range(i, last):
                    line.append(words[k])
                    if k < last - 1:
                        line.append(" ")
                current_str = "".join(line)
                current_str += " " * (maxWidth - len(current_str))
                res.append(current_str)
            else:
                # Fully justify
                spaces_between = num_spaces // (num_words - 1)
                extra_spaces = num_spaces % (num_words - 1)
                
                for k in range(i, last):
                    line.append(words[k])
                    if k < last - 1:
                        # Add spaces, prioritizing extra spaces to the left gaps
                        s_to_add = spaces_between + (1 if k - i < extra_spaces else 0)
                        line.append(" " * s_to_add)
                res.append("".join(line))
                
            i = last
            
        return res
        