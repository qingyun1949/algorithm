# algorithm
Given a valid sentence without any spaces between the words and a dictionary of valid
English words, find all possible ways to break the sentence in individual dictionary words.
Example:
Consider the following dictionary
{ i, like, sam, sung, samsung, mobile, ice, cream, man go}
Input: "ilikesamsungmobile"
Output: i like sam sung mobile
i like samsung mobile
Input: "ilikeicecreamandmango"
Output: i like ice cream and man go
#Stage 2 - new requirement to be implemented:
If user provide a customized dictionary of valid English words as additional input, and the
program will only find in the user customized dictionary
E.g.: the user customized dictionary
{ i, like, sam, sung, mobile, icecream, man go, mango}
#Stage 3 - new requirement to be implemented:
If user provide a customized dictionary of valid English words as additional input, and the
program will find all the valid words in the both dictionaries
E.g.: the user customized dictionary
{ i, like, sam, sung, mobile, icecream, man go, mango}

思路:
利用递归方式解决,假如某个中间状态为 res=[i, like],此时剩余的字符串还有samsungmobile.此时进入下一层递归,判断以's'开头的是否list中;
为了查找效率,在一开始对输入的list做了一个hash,这样每层递归内部只有遍历slot_list的时间复杂度:O(k), 这样总体的时间复杂度:O(klogn),其中k可以认为是list重复开头的最大值.
