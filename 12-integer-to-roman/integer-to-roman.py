class Solution(object):
    def intToRoman(self, num):
        temp = num
        count = ""
        while temp != 0:
            if temp >=1000:
                count += "M"
                temp = temp - 1000

            elif temp >=900:
                count += "CM"
                temp = temp - 900

            elif temp >=500:
                count += "D"
                temp = temp - 500

            elif temp >=400:
                count += "CD"
                temp = temp - 400


            elif temp >=100:
                count += "C"
                temp = temp - 100
            
            elif temp >=90:
                count += "XC"
                temp = temp - 90

            elif temp >=50:
                count += "L"
                temp = temp - 50

            elif temp >=40:
                count += "XL"
                temp = temp - 40


            elif temp >=10:
                count += "X"
                temp = temp - 10
            
            elif temp >=9:
                count += "IX"
                temp = temp - 9
            
            elif temp >=5:
                count += "V"
                temp = temp - 5
            
            elif temp >=4:
                count += "IV"
                temp = temp - 4
                
            elif temp >=1:
                count += "I"
                temp = temp - 1
        
        return count
            