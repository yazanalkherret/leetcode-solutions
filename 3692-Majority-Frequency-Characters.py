class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        charFreq = Counter(s)
        # char - > number
        freqChars = defaultdict(list)
        for char, freq in charFreq.items():
            freqChars[freq].append(char)
        print(freqChars)
        # number -> char
        maxSize = 0
        res = None # Edge case 
        for key in sorted(freqChars.keys()):
            if len(freqChars[key]) >= maxSize:
                maxSize = len(freqChars[key])
                res = freqChars[key]

        # Convert to string
        return "".join(res)
        
            
            