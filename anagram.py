class anagram:

    def __init__(self,x):
        self.new=x

    def arm_num(self):
        new_num = ''
        while self.new<0:
            n = self.new % 10
            new_num += str(n)
            self.new = self.new // 10
        return new_num

if __name__=="__main__":
    k=anagram(int(input('enter the number:- ')))
    test=k.arm_num()
    if test==k:
        print('its anagram')
    else:
        print('its not anagram')



